---
name: multi-channel-sequencing
description: Generates a complete cross-channel outreach sequence where each channel activates on non-response from the previous, with message content, timing, and cascade logic included.
---

## Purpose

Builds a full outreach sequence that moves across channels — LinkedIn DM, email, InMail — where each step only fires if the prior step went unanswered. Every touch uses a new angle. The sequence ends hard at 6 touches or when the prospect replies, whichever comes first. No stalking. No repetition. A clean system a human operator can actually run.

## Trigger

`/multi-channel` or when the user needs a cross-platform outreach sequence rather than a single-channel one.

## Process

1. **Get inputs:**
   - Offer (what are you selling or proposing?)
   - ICP (who is this going to — role, company type, context?)
   - Primary pain (the problem this offer solves)
   - Expected objection (what will make them hesitate?)
   - Desired outcome (what does a win look like — reply, call, demo, referral?)

2. **Get channel availability.** Ask which channels the operator has access to and can realistically execute: LinkedIn DM, email, LinkedIn InMail, phone. Build the cascade only from confirmed available channels.

3. **Choose the primary channel.** Default: LinkedIn DM first if the operator has it — warmer, lower friction for cold outreach. Email first if LinkedIn is unavailable or if the ICP is not active on LinkedIn.

4. **Build the cascade with timing:**
   - Touch 1: Primary channel, Day 1
   - Touch 2: Same or secondary channel, Day 3–5 (no reply trigger)
   - Touch 3: Channel switch, Day 7–10
   - Touch 4: Second channel follow-up, Day 13–16
   - Touch 5: Final value touch, Day 18–22
   - Touch 6: Breakup message on the most personal-feeling channel. Hard stop after this.

5. **Write each touch with:**
   - Channel and day
   - Trigger condition ("No reply on Touch [N] after [X] days")
   - Message content following channel rules:
     - **LinkedIn DM:** 3 sentences max, conversational, no subject line, no formal opener
     - **Email:** 80 words max on Touch 1, 50 words max on follow-ups, subject line required
     - **InMail:** 100 words max, must justify why InMail — acknowledge you're using a paid channel
   - Angle (must be distinct from every prior touch)
   - Single CTA per touch

6. **If a new angle cannot be found for a touch, the sequence ends there.** Do not pad.

## Output Format

```
MULTI-CHANNEL SEQUENCE
────────────────────────────────────────────────
Offer:       [stated]
ICP:         [stated]
Primary:     [channel 1]
Cascade:     [channel 1] → [channel 2] → [channel 3]
Total touches: [N]

────────────────────────────────────────────────
TOUCH 1 — [Channel] | Day 1
Trigger: Initial outreach
Angle: [one-line description]
CTA: [stated]

[Message]

────────────────────────────────────────────────
TOUCH 2 — [Channel] | Day [N]
Trigger: No reply on Touch 1 after [N] days
Angle: [one-line description]
CTA: [stated]

[Message]

[repeat through final touch]

────────────────────────────────────────────────
CASCADE NOTES
[2–4 sentences: overall strategy across channels, what signals to watch for mid-sequence, when to stop early]
```

## Rules

- Maximum 6 touches total across all channels.
- Every touch must use a new angle. Restating the same value prop in different words is not a new angle.
- If a prospect replies on any channel, the sequence stops — do not continue firing on other channels.
- Channel switching must feel natural. If it would feel like being followed, it's too aggressive.
- InMail is a last resort. Only include it if LinkedIn DM and email have both been exhausted. Acknowledge the channel explicitly in the InMail copy.
- Touch 6 is always a breakup. It is not a final pitch. Prospect moves to nurture after Touch 6, not to more outreach.
- Do not assume channel availability — confirm with the user before building the cascade.
