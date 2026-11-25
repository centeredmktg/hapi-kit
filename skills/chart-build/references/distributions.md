# Distributions — How Are Values Spread?

> Source: Industry standard.

## Forms
| Situation | Form |
|---|---|
| One variable | Histogram (try several bin widths) → density plot → ECDF when exact quantiles or cutoffs matter |
| Heavily right-skewed | Histogram/density/ECDF on a log scale |
| Fit to a theoretical distribution | q-q plot with an x = y reference line |
| Two groups | Overlapping semi-transparent densities; group density vs. overall in gray; mirrored histograms (exactly two groups only) |
| 3–20 groups | Boxplots (default) → violins (only with enough n per group) → jittered strip / sina (sparse) |
| 20–100+ groups, or distribution over time | Ridgeline of densities |

## Rules
- **Never accept the default bin width or bandwidth.** Render at least three (narrow / medium / wide) and keep the one that shows real structure without noise. Say which you chose.
- Histogram bins are equal width.
- Check density tails for impossible values (negative ages or counts, over 100%). Bound or truncate the estimate.
- Density y-values depend on x units, so don't put analytical weight on the y numbers.
- For two or more distributions, densities beat histograms.
- **Never use mean ± error bars to show spread.** It throws away the distribution, hides whether it's a mean or a median, and forces symmetry on skewed data.
- Boxplot: median line, box = middle 50%, whiskers to the last point within 1.5 × IQR, outliers drawn individually. Lightly shade the box.
- Violins need enough points per group to justify a smooth shape. Otherwise show raw points.
- Strip charts need horizontal jitter, or points stack invisibly. Seed the jitter.
- Ridgelines: build from densities, never histograms; omit the density axis.
- ECDF for cutoffs: place tier boundaries at the start of a steep rise, not in the flat stretch just below it, so tied clusters aren't split.
- Power-law check: descending ECDF on log-log. A straight line means power law; a curved tail means not.
- q-q reference is x = y, not a regression line. Deviations at the extremes may be ceilings or floors (a 100-point max), not misfit.
- Lay audiences: histograms, boxplots, and points. ECDF and q-q are for experts.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| WRONG | Density curve running into impossible values | Bound the estimate |
| BAD | Stacked histogram (upper groups have no baseline) | Proportion-of-total densities or side-by-side panels |
| BAD | Overlapping semi-transparent histograms (overlap reads as a third group) | Densities |
| BAD | Mean ± error bars standing in for spread | Box, violin, or jittered points |
| BAD | Un-jittered strip chart | Jitter or sina |
| BAD | Linear-scale density of very skewed data | Log scale |
| UGLY | Ridgeline of histograms | Density ridgeline |
| UGLY | Empty outline histogram bars | Light fill |
