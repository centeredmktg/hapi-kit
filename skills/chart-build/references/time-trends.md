# Time & Trends — How Did It Change?

> Source: Industry standard. Also applies to any strictly ordered x (dose, step number, funnel stage order).

## Forms
| Situation | Form |
|---|---|
| One series | Line (drop dots when dense) → line + dots (sparse or uneven spacing) → filled area only if y starts at 0 |
| Few series | Lines with direct labels at the line ends, no legend |
| Two response variables over time | Two stacked line panels (easiest) → connected scatter with time cues (exposes cycles) |
| Trend in noisy data | Fitted model with an interpretable form → straight line on transformed axes → LOESS/spline (state it, test alternatives) |
| Long-run trend + deviations or seasonality | Detrended series (divide by trend) → decomposition panels (trend / seasonal / remainder) |
| Truly periodic x (hour of day, day of year) | Polar coordinates, and only then |

## Rules
- Use lines whenever x is ordered. Connecting lines guide the eye; when points are sparse, say so in the caption.
- **Fill under a line only when the y-axis starts at 0.** An area fill on a truncated axis exaggerates moves.
- Multiple series: lines, not unconnected dots (dots from different series interleave into noise). Label each line at its end in its own color.
- Indexed series (start = 100) need a reference line at 100 or a horizontal grid.
- Grid lines are horizontal for time series.
- Connected scatter must show direction and time: a color gradient darkening toward recent, date labels at key points, or arrows.
- Moving averages: window length decides which fluctuations survive. Center the window to avoid lag. Note the series gets shorter.
- Smoothers (LOESS, splines) are sensitive to settings, especially at the edges. Try two or three before trusting one, and state the method.
- To check a functional form, transform axes until it looks straight: log-y for exponential growth, log-log for power laws. Fit a straight line to the transformed data rather than an exponential curve to raw data (raw fits are dominated by the biggest values).
- Detrend by dividing by the long-run trend to expose deviations (bubbles, dips).
- Seasonal series: decompose into trend, seasonal, and remainder panels; the remainder shows one-off events.
- Aspect ratio matters: wide flattens change, tall exaggerates it. Pick the ratio that makes the real change visible without inflating it.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| BAD | Multiple series as unconnected dots | Lines + direct labels |
| BAD | Connected scatter with no direction or date cues | Color gradient + date markers or arrows |
| BAD | Area fill on a truncated y-axis | Start at 0 or drop the fill |
| BAD | Indexed lines with no grid or reference line | Reference line at the index value |
| BAD | Alphabetical legend that contradicts line order | Direct labels, or legend in line order |
| BAD | Polar coordinates for non-periodic data | Cartesian |
