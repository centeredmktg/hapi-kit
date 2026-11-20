#!/usr/bin/env python3
"""Deterministic content QA for a CMS-driven site. Rules only, no LLM.

Two modes:

  sitemap   Crawl the public sitemap and check what search engines see.
            python3 cms_qa.py sitemap https://www.example.com --include /blog/ --include /integrations/

  webflow   Check CMS items before they go live, via the Webflow Data API v2.
            WEBFLOW_TOKEN=... python3 cms_qa.py webflow --config context/content-qa.json

Both write a markdown report and a JSON file (default: outputs/YYYY-MM-DD-content-qa.{md,json}).
Exit code 1 if any check at severity "block" fails, so it can gate a scheduled job.
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

UA = "cms-content-qa/1.0 (+content quality check)"


def _ssl_context():
    """macOS python.org builds ship without a CA bundle; fall back to certifi or the system bundle."""
    for cafile in (os.environ.get("SSL_CERT_FILE"), "/etc/ssl/cert.pem"):
        if cafile and os.path.exists(cafile):
            return ssl.create_default_context(cafile=cafile)
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


SSL_CTX = _ssl_context()
BAD_SLUG = re.compile(r"(-\d+$|-[0-9a-f]{5}$|---|draft|copy|test)", re.I)
PLACEHOLDER = re.compile(r"(lorem ipsum|bibendum|consectetur adipiscing|meta title:|author 1\b|\bTBD\b|\bTODO\b|\[insert)", re.I)

# Each check: id -> (severity, description). "block" = must not be live.
CHECKS = {
    "fetch_failed": ("warn", "Page did not load after retries"),
    "title_empty": ("block", "Empty <title>"),
    "title_long": ("warn", "Title over 60 characters"),
    "desc_empty": ("block", "Empty meta description"),
    "desc_long": ("warn", "Meta description over 160 characters"),
    "body_thin": ("block", "Body text under the minimum word count"),
    "h1_count": ("warn", "Not exactly one non-empty <h1>"),
    "placeholder": ("block", "Placeholder or template text in the page"),
    "slug_suspect": ("warn", "Slug looks like a duplicate or working copy"),
    "dup_title": ("block", "Same title as another page"),
    "author_missing": ("warn", "Required author field is empty"),
    "field_missing": ("block", "Required CMS field is empty"),
    "img_alt_empty": ("warn", "Images with empty alt text"),
}


def fetch(url, headers=None, retries=3, timeout=25):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                last = e.code
                time.sleep(2 * (i + 1))
                continue
            return e.code, ""
        except Exception as e:  # timeouts, resets
            last = f"{type(e).__name__}: {getattr(e, 'reason', e)}"
            time.sleep(2 * (i + 1))
    return last, ""


def text_of(fragment):
    fragment = re.sub(r"(?is)<(script|style|noscript|svg|nav|header|footer)[^>]*>.*?</\1>", " ", fragment)
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()


def main_text(page, selector_hint):
    """Body text: <main>/<article> or a class hint, minus nav/header/footer."""
    if selector_hint:
        m = re.search(r'(?is)<[a-z]+[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>(.*)' % re.escape(selector_hint), page)
        if m:
            return text_of(m.group(1)[:200000])
    for tag in ("article", "main"):
        m = re.search(r"(?is)<%s[^>]*>(.*?)</%s>" % (tag, tag), page)
        if m:
            return text_of(m.group(1))
    m = re.search(r"(?is)<body[^>]*>(.*)</body>", page)
    return text_of(m.group(1) if m else page)


def check_page(url, page, cfg):
    issues = []
    title = html.unescape((re.search(r"(?is)<title[^>]*>(.*?)</title>", page) or [None, ""])[1]).strip()
    desc_m = re.search(r'(?is)<meta[^>]+name=["\']description["\'][^>]*>', page)
    desc = ""
    if desc_m:
        c = re.search(r'content=["\']([^"\']*)', desc_m.group(0))
        desc = html.unescape(c.group(1)).strip() if c else ""
    h1s = [text_of(h) for h in re.findall(r"(?is)<h1[^>]*>(.*?)</h1>", page)]
    h1s = [h for h in h1s if h]
    body = main_text(page, cfg.get("body_selector"))
    words = len(body.split())
    imgs = re.findall(r"(?is)<img\b[^>]*>", page)
    empty_alt = sum(1 for i in imgs if not re.search(r'alt=["\'][^"\']+["\']', i))
    slug = url.rstrip("/").rsplit("/", 1)[-1]

    if not title: issues.append("title_empty")
    elif len(title) > 60: issues.append("title_long")
    if not desc: issues.append("desc_empty")
    elif len(desc) > 160: issues.append("desc_long")
    if words < cfg.get("min_words", 300): issues.append("body_thin")
    if len(h1s) != 1: issues.append("h1_count")
    if PLACEHOLDER.search(body) or PLACEHOLDER.search(title): issues.append("placeholder")
    if BAD_SLUG.search(slug): issues.append("slug_suspect")
    if imgs and empty_alt: issues.append("img_alt_empty")
    return {"url": url, "title": title, "words": words, "empty_alt": empty_alt, "issues": issues}


def run_sitemap(args, cfg):
    status, xml = fetch(args.base.rstrip("/") + "/sitemap.xml")
    if not xml:
        sys.exit(f"Could not read sitemap ({status})")
    urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    if args.include:
        urls = [u for u in urls if any(p in u for p in args.include)]
    if args.limit:
        urls = urls[: args.limit]

    def one(u):
        code, page = fetch(u)
        if not page:
            return {"url": u, "title": "", "words": 0, "empty_alt": 0, "issues": ["fetch_failed"], "status": code}
        return check_page(u, page, cfg)

    # Gentle concurrency: many CMS hosts rate-limit bursts.
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        rows = list(ex.map(one, urls))
    return rows


def wf_get(path, token):
    status, body = fetch("https://api.webflow.com/v2" + path,
                         headers={"Authorization": f"Bearer {token}", "accept": "application/json"})
    if status != 200:
        sys.exit(f"Webflow API {path} returned {status}. Check the token's CMS read scope.")
    return json.loads(body)


def run_webflow(args, cfg):
    token = os.environ.get("WEBFLOW_TOKEN")
    if not token:
        sys.exit("Set WEBFLOW_TOKEN (a Webflow API token with CMS read scope).")
    rows = []
    for coll in cfg["collections"]:
        offset = 0
        while True:
            data = wf_get(f"/collections/{coll['id']}/items?offset={offset}&limit=100", token)
            for item in data.get("items", []):
                f = item.get("fieldData", {})
                url = coll.get("url_prefix", "/") + f.get("slug", "")
                issues = []
                for field in coll.get("required", []):
                    if not str(f.get(field, "") or "").strip():
                        issues.append("author_missing" if field == coll.get("author_field") else "field_missing")
                body = text_of(str(f.get(coll.get("body_field", ""), "") or ""))
                if coll.get("body_field") and len(body.split()) < coll.get("min_words", cfg.get("min_words", 300)):
                    issues.append("body_thin")
                if PLACEHOLDER.search(body) or PLACEHOLDER.search(str(f.get("name", ""))):
                    issues.append("placeholder")
                if BAD_SLUG.search(f.get("slug", "")):
                    issues.append("slug_suspect")
                rows.append({
                    "url": url, "title": str(f.get(coll.get("title_field", "name"), "")),
                    "words": len(body.split()), "issues": sorted(set(issues)),
                    "collection": coll.get("label", coll["id"]),
                    "state": "draft" if item.get("isDraft") else ("archived" if item.get("isArchived") else "live"),
                    "missing_fields": [x for x in coll.get("required", []) if not str(f.get(x, "") or "").strip()],
                })
            offset += 100
            if offset >= data.get("pagination", {}).get("total", 0):
                break
    return rows


def add_duplicate_titles(rows):
    seen = defaultdict(list)
    for r in rows:
        if r.get("title"):
            seen[r["title"].strip().lower()].append(r)
    for group in seen.values():
        if len(group) > 1:
            for r in group:
                r["issues"].append("dup_title")
                r["dup_of"] = [g["url"] for g in group if g is not r]


def report(rows, mode, source):
    today = dt.date.today().isoformat()
    counts = defaultdict(int)
    for r in rows:
        for i in set(r["issues"]):
            counts[i] += 1
    blocking = [r for r in rows if any(CHECKS[i][0] == "block" for i in r["issues"])]
    lines = [f"# Content QA, {today}", "",
             f"Mode: {mode}. Source: {source}. Pages checked: {len(rows)}. "
             f"Pages with a blocking issue: **{len(blocking)}**.", "",
             "| Check | Severity | Pages |", "|---|---|---|"]
    for cid, (sev, desc) in CHECKS.items():
        if counts[cid]:
            lines.append(f"| {desc} | {sev} | {counts[cid]} |")
    lines += ["", "## Pages to fix (blocking first)", ""]
    order = sorted(rows, key=lambda r: (-sum(CHECKS[i][0] == "block" for i in r["issues"]), -len(r["issues"])))
    for r in order:
        if not r["issues"]:
            continue
        names = ", ".join(CHECKS[i][1] for i in sorted(set(r["issues"])))
        extra = f" (missing: {', '.join(r['missing_fields'])})" if r.get("missing_fields") else ""
        lines.append(f"- {r['url']}: {names}{extra}")
    return "\n".join(lines) + "\n", len(blocking)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)
    s = sub.add_parser("sitemap")
    s.add_argument("base")
    s.add_argument("--include", action="append", help="Only URLs containing this path (repeatable)")
    s.add_argument("--limit", type=int, default=0)
    s.add_argument("--workers", type=int, default=3)
    w = sub.add_parser("webflow")
    for p in (s, w):
        p.add_argument("--config", help="JSON config (min_words, body_selector, collections)")
        p.add_argument("--out", default="outputs")
    args = ap.parse_args()
    cfg = json.load(open(args.config)) if args.config else {}

    rows = run_sitemap(args, cfg) if args.mode == "sitemap" else run_webflow(args, cfg)
    add_duplicate_titles(rows)
    source = args.base if args.mode == "sitemap" else "Webflow CMS"
    md, blocking = report(rows, args.mode, source)
    os.makedirs(args.out, exist_ok=True)
    stem = os.path.join(args.out, f"{dt.date.today().isoformat()}-content-qa")
    open(stem + ".md", "w").write(md)
    json.dump(rows, open(stem + ".json", "w"), indent=1)
    print(md.split("## Pages to fix")[0])
    print(f"Wrote {stem}.md and {stem}.json")
    sys.exit(1 if blocking else 0)


if __name__ == "__main__":
    main()
