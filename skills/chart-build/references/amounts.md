# Amounts — How Big Is Each One?

> Source: Industry standard.

## Forms
- **Bar chart.** Magnitude across categories. Horizontal when labels are long or there are many categories.
- **Dot plot.** When values are large and close together (a zero baseline would make bars look identical), or span orders of magnitude (dots on a log axis).
- **Grouped bars.** Two categorical variables × one value. Primary comparison on the x positions, secondary in color.
- **Small multiples of bars.** Preferred over grouped bars when matching colors across groups gets taxing.
- **Heatmap.** When the grid of values is too large for bars or dots (20 × 20, or time × entity). Trend over exact value.
- **Bars with printed values and no value axis.** Only for a handful of values.

## Rules
- Bars start at zero. Always. If zero hides the difference, switch to dots on a trimmed axis. Never use a trimmed bar.
- To show small changes, plot the change itself (difference from baseline) with negative bars below zero.
- On a log axis, bars mean ratios and start at 1. For raw amounts across magnitudes, use dots with labels beside the dots.
- Sort unordered categories by value. Keep ordered categories (age bands, stages, income brackets) in natural order even if the bars then go up and down.
- Stack only quantities whose total means something (counts, sums). Never stack medians, means, or rates.
- Order heatmap rows by a metric that serves the story (latest value, or when a threshold was crossed), never alphabetically.
- Value labels inside or at the end of bars must not visually lengthen the bar. Put them close and plain.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| WRONG | No value axis and no printed values | Show the axis or label values |
| BAD | Bars on a truncated axis | Dots, or plot the change |
| BAD | Bars ordered by something irrelevant, or alphabetically | Sort by value |
| BAD | Ordered categories re-sorted by height | Natural order |
| BAD | Long nearly-equal bars (60–81) | Dot plot, restricted range |
| BAD | Bars on a log axis from an arbitrary start | Dots on log axis |
| UGLY | Rotated tick labels | Horizontal bars |

## Thresholds
- Grouped bars strain at about 7 groups × 4 bars. Past that, use small multiples or a heatmap.
