# Proportions — What Share of the Whole?

> Source: Industry standard.

## Which form for which story
| Need | Pie | Stacked bars | Side-by-side bars |
|---|---|---|---|
| Shows part-of-whole clearly | ✓ | ✓ | ✗ |
| Compare individual parts | ✗ | ✗ | ✓ |
| Emphasize simple fractions (½, ⅓, ¼) or a combined majority | ✓ | ✗ | ✗ |
| Fine with very small datasets | ✓ | ✗ | ✓ |
| Many parts | ✗ | ✗ | ✓ |
| Many sets or a time series of proportions | ✗ | ✓ | ✗ |

Choose by the story. No form wins universally.

## Forms beyond the basics
- **Stacked area/density along a continuous x.** Up to about 4 categories when the trend is the message. If one category swings wildly, use one panel per category against the total in gray instead.
- **Proportion lines with a 50% reference line.** When crossing a majority is the story.
- **Mosaic plot.** Two categorical variables that fully cross (every level appears with every level). Widths encode one variable, heights the other.
- **Treemap.** Nested hierarchy that doesn't cross (state within region). Keep nesting shallow and put labels inside.
- **Nested-color pie.** Slice by the primary variable, subdivide by the secondary, with hue for primary and lightness for secondary. A treemap is usually better.
- **Parallel sets.** Three or more categorical variables. Put the variable that drives band color at the far left, and order axes to minimize crossings.

## Rules
- Slices and segments sum to 100% with **no double counting.** Overlapping categories never go in one pie.
- Don't show overlapping categories as plain side-by-side bars either; readers assume they're disjoint.
- Stacked bars: two segments is safe. Middle segments of 3+ float on a shifting baseline and can't be compared.
- Stacked percentages hide changes in the total. When the base population varies, show counts against the total.
- Mosaics and treemaps share stacked-bar weaknesses, so print counts or percentages inside the rectangles.
- Pie: few slices. Label slices directly; no legend.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| WRONG | One pie mixing overlapping categories (sums past 100%) | Mosaic or treemap |
| BAD | Row of pies (one per year or segment) | Side-by-side bars or stacked bars over time |
| BAD | Stacked bars with 3+ segments where parts must be compared | Side-by-side bars |
| BAD | Side-by-side bars of overlapping groups | Mosaic or treemap |
| BAD | Stacked density where one category swamps the rest | Partial densities per category |
| UGLY | Two-ring nested pie | Treemap or nested-color pie |
| UGLY | Parallel sets colored by the rightmost variable with tangled bands | Coloring variable leftmost, minimize crossings |
