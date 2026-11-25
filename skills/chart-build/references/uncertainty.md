# Uncertainty — How Sure Are We?

> Source: Industry standard.

## Forms by audience
| Situation | Lay / executive | Expert |
|---|---|---|
| A single probability | Grid of outcomes (100 squares, randomized placement) | Same, or point estimate + interval |
| Distribution of outcomes | Quantile dot plot (~10–20 dots); hypothetical-outcome animation | Density or interval |
| Many point estimates | Few estimates with plain-language ranges | Point + error bars, or graded bars (80/95/99%) |
| Comparing estimates vs. a reference | Plot the differences with their CIs against zero | Same |
| Full distribution per group | Ridgeline with shaded 80/95/99% regions | Half-eye / eye plots |
| Fitted line | Confidence band | Graded bands, or ~15 sampled fits drawn thin |

## Rules
- Point estimates read as exact. Show uncertainty on purpose.
- **Always state what an error bar or band is** (SD, SE, which CI level), in the caption or a direct label.
- Don't confuse SD (spread of the data) with SE (precision of the estimate). SE ≈ SD / √n. A 95% CI ≈ ±2 SE.
- **Never judge significance from overlapping error bars.** Plot the difference and its CI and check whether it excludes zero.
- Lay audiences read intervals as hard min/max. Use frequency framing (discrete outcomes) or graded bars to break that.
- Quantile dot plots: fewer dots read better. Around 10 beats 50.
- Bar + SE "dynamite plots" show neither spread nor uncertainty well. Show the distribution, or point + interval.
- Drop error-bar caps when there are many bars.
- Hypothetical-outcome animations: hard cuts or fast fades, not smooth morphing. Make sure the shown draws are representative.
- Forecasts and projections (pipeline, revenue models, financial scenarios): show a range or scenarios, never a single confident line.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| WRONG | Error bars with no stated meaning | Label SD / SE / CI level |
| BAD | Significance inferred from bar overlap | Plot differences with CIs |
| BAD | A single bar or dot for a probability, shown to a lay audience | Outcome grid |
| BAD | Projection drawn as one exact line | Band or scenarios |
| UGLY | 50+ dot quantile plot | ~10–20 dots |
