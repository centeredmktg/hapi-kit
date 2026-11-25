# Associations — Does X Move With Y?

> Source: Industry standard.

## Forms
| Situation | Form |
|---|---|
| Two quantitative variables | Scatter plot; add color for one categorical split; add a trend line (linear or LOESS) |
| Three quantitative variables | Scatterplot matrix → two scatters sharing the response → bubble chart (weakest) |
| Four or more | Correlogram (circle size by abs(r)), paired with raw views or PCA (loadings arrows + scores scatter) |
| Paired measurements (before/after) | Many pairs or a systematic shift: scatter with an x = y diagonal. Few pairs, identities matter, or 3+ time points: slopegraph |

## Rules
- Color by a categorical split to expose confounding, where the overall trend is driven by a subgroup.
- Bubble charts encode one kind of variable two ways (position vs. size), and size is hard to judge. Prefer a scatterplot matrix or separate panels.
- Past 3–4 variables a scatterplot matrix gets unwieldy, so use a correlogram.
- Correlogram: diverging color from −1 to 1, with circle size by abs(r) so weak correlations fade. Correlograms hide the raw data; always pair them with a raw view.
- PCA: show what each component is made of (loading arrows) and where the data sits (PC1/PC2 scatter colored by group). Usually 2–3 components carry the story.
- Paired data: use the x = y diagonal *instead of* a grid, never both. Use log axes if magnitudes vary widely.
- Same units on x and y means a square grid (1:1 aspect).
- Trend lines: state the method. When smoothing (LOESS/spline), try more than one setting before trusting it.
- Scatter symbols are solid and filled, differing in color *and* shape across groups.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| BAD | 3D scatter on a static image | Scatterplot matrix or color/size for the third variable |
| BAD | Paired scatter with a grid but no diagonal | Diagonal only |
| BAD | Groups separated by color only, with similar hues side by side | Distinct hues + distinct shapes |
| UGLY | Grid and diagonal together | Diagonal only |
| UGLY | Open, outline-only symbols | Solid symbols |
