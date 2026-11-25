# Chart Chooser

> Source: Industry standard.

Pick by the **question the reader is asking** first, then by data shape. Picks are ranked best-first. The "Avoid" column matters as much as the picks: it's where most bad charts come from.

**Family key** (the `family:` value passed to `/chart-build`): Amounts → `amounts` · Distribution → `distributions` · Proportions → `proportions` · x-y relationship → `associations` · Time / ordered x → `time-trends` · Geospatial → `geospatial` · Uncertainty → `uncertainty`. Overplotting rows add `overlap: true`.

| Question | Data shape | Ranked picks | Avoid / notes |
|---|---|---|---|
| **Amounts**: how big is each? | One numeric value per category, few to ~25 categories | 1. Bar chart (horizontal if labels are long) 2. Dot plot (Cleveland) 3. Bars with values printed + no y-axis (very few values) | Rotated labels; alphabetical sort of unordered categories; 3D bars |
| | Values large and close together, zero baseline hides differences | 1. Dot plot with restricted axis range | Bars that don't start at zero |
| | Values span orders of magnitude | 1. Dot plot on a log axis, labels beside dots | Bars on a log axis (bar start is arbitrary) |
| | Two categorical variables x one numeric | 1. Small multiples of bars (one panel per group) 2. Grouped (dodged) bars, variable of main comparison on x 3. Heatmap if large | Stacking values whose sum is meaningless (medians, rates) |
| | Many groups x many values (e.g. 20x20, or time x entity) | 1. Heatmap (ordered rows by a meaningful metric) | Grouped bars (7 groups x 4 bars is already hard) |
| **Distribution**: how are values spread? | One variable | 1. Histogram (try several bin widths) 2. Density plot (check tails) 3. ECDF when you need exact quantiles/cutoffs or no tuning parameters | Defaults for bin width/bandwidth; density on tiny n |
| | Heavily right-skewed | 1. Histogram/density/ECDF on log scale 2. Descending ECDF on log-log to test power law | Raw linear-scale density (spike at zero, no structure) |
| | Check fit to a theoretical distribution | 1. q-q plot with x=y reference line | |
| | Two groups | 1. Overlapping semi-transparent densities 2. Group density as share of overall (gray total behind) 3. Age-pyramid style mirrored histograms (exactly two groups only) | Stacked histograms; overlapping histograms |
| | Many groups (3-20) | 1. Boxplots (compact, show skew) 2. Violins (only if n per group is large enough; shows multimodality) 3. Jittered strip / sina (sparse data) | Mean ± error bar as a stand-in for spread; un-jittered strip chart |
| | Very many groups or distribution over time (20-100+) | 1. Ridgeline of densities | Ridgeline of histograms |
| **Proportions**: parts of a whole | One set, few parts, story is simple fractions (1/2, 1/3, 1/4) or a coalition/majority | 1. Pie 2. Stacked bar (horizontal) | Pie with many slices |
| | One set, many parts, compare parts to each other | 1. Side-by-side bars | Pie, single stacked bar |
| | Several sets or a time series of proportions | 1. Side-by-side bars (small multiples) 2. Stacked bars only if 2 segments 3. Stacked area/density with ≤4 categories along a continuous x | Rows of pies; stacked bars with 3+ segments (middle segments float) |
| | Proportions shifting with a continuous variable | 1. Stacked density (≤~4 categories) 2. Partial densities, one panel per category vs. total in gray 3. Proportion lines with a 50% reference line | Stacked density when one category swamps others |
| | Nested proportions, 2 categorical variables that fully cross | 1. Mosaic plot | Combined pie (double-counts, WRONG); side-by-side bars of overlapping categories (BAD) |
| | Nested hierarchy that doesn't cross (region > state) | 1. Treemap (labels inside) 2. Nested-color pie | Two-ring nested pie (double-counts visually, UGLY) |
| | 3+ categorical variables | 1. Parallel sets (coloring variable at far left, order axes to minimize crossings) | |
| **x-y relationship** | Two quantitative variables | 1. Scatter plot 2. Add color for one categorical variable 3. Add trend line (linear or LOESS) | |
| | Three quantitative variables | 1. Scatterplot matrix 2. Two scatter plots sharing the response 3. Bubble chart (weakest; size is hard to judge) | 3D scatter |
| | 4+ quantitative variables | 1. Correlogram (circles sized by abs(r)) 2. PCA: loadings arrows + scores scatter | Raw-only views; correlogram alone (too abstract, pair with raw data) |
| | Paired measurements (before/after, left/right) | 1. Scatter with x=y diagonal (many pairs, systematic shift) 2. Slopegraph (few pairs, identity of each case matters, or 3+ time points) | Background grid without diagonal |
| | Too many points (overplotting) | 1. Transparency + slight jitter (moderate n, rounded data) 2. 2D bins / hex bins (very large n) 3. Density contours (smooth density; 2-3 well separated groups) 4. Contours faceted by group (many overlapping groups) | Solid opaque points; heavy jitter; 5 colored contour sets in one panel |
| **Time / ordered x** | One series | 1. Line (drop dots when dense) 2. Line + dots (sparse/uneven) 3. Filled area only if y starts at 0 | Area fill on truncated y |
| | Few series | 1. Lines with direct labels at line ends | Unconnected dots for multiple series; alphabetic legend |
| | Two response variables over time | 1. Two stacked line panels (easier to read) 2. Connected scatter with direction/time cues (engaging, cycles) | Connected scatter with no time markers |
| | Trend in noisy data | 1. Fitted model with interpretable form 2. Straight line on transformed axes 3. LOESS / spline (state method, test alternatives) | Exponential curve fit on raw data |
| | Long-run trend + deviations / seasonality | 1. Detrended series (divide by trend) 2. Decomposition panels (trend / seasonal / remainder) | |
| | Periodic data (day of year, hour of day) | 1. Polar coordinates | Polar for non-periodic data |
| **Geospatial** | Point locations | 1. Layered map (base terrain/roads, data layer, labels) + scale bar + north arrow | |
| | Value per region, region sizes similar or small vs. map | 1. Choropleth, 4-6 binned colors 2. Continuous choropleth | Choropleth of non-density values with very unequal region sizes |
| | Value per region, regions very unequal (US states) | 1. Cartogram heatmap (equal tiles) 2. Population-scaled cartogram 3. Geofacet small multiples (one mini chart per region in geographic layout) | State-level choropleth dominated by large, sparse regions; shrinking Alaska |
| | Whole world | 1. Equal-area (Goode homolosine) when area matters 2. Compromise (Robinson, Winkel tripel) for general display | Mercator for world maps; raw lon/lat as x/y |
| **Uncertainty** | Single probability, lay audience | 1. Waffle/discrete-outcome grid (e.g. 100 squares, randomized) | Single bar or dot for a probability |
| | Distribution of outcomes, lay audience | 1. Quantile dot plot with ~10-20 dots 2. Hypothetical outcome plot (animation) | 50+ dot quantile plots; bare density |
| | Many point estimates, expert audience | 1. Point + error bars (state what bars mean) 2. Graded error bars (e.g. 80/95/99%) | Unlabeled error bars; judging significance from bar overlap |
| | Comparing estimates vs. a reference | 1. Plot the differences with their CIs vs. zero | Overlap rules of thumb |
| | Full posterior / distribution per group | 1. Ridgeline with shaded credible regions 2. Half-eye / eye plots | Confidence strips when precise reading needed |
| | Uncertainty of a fitted line | 1. Confidence band 2. Graded bands 3. Spaghetti of fitted draws (~15) | |

## Audience and medium adjustments

- **Lay / executive audience:** prefer the simplest form that lands the point. A plain bar chart beats an impressive multi-encoded chart. Uncertainty becomes discrete outcomes (100-square grids, ~10–20 quantile dots), not error bars.
- **Expert audience:** ECDFs, q-q plots, graded error bars, and correlograms are fair game.
- **LinkedIn / social:** one figure, one point, title inside the image, holds both the problem and the answer.
- **Deck / story:** 3–6 figures per storyline, raw data first and derived numbers after, with different chart types for different analyses. If the final figure is complex, show a simplified version of one panel first.
- **Too many encodings:** default budget is x, y, plus one. Each extra channel (size, shape, second color) costs comprehension. Facet instead.
