# Chart QA Checklist

> Source: Industry standard. Default grade in brackets. Raise the grade when a failure changes what a reader would conclude.

## Honesty and encoding
1. [WRONG] Can every plotted value be recovered from an axis, a gridline, or a printed label? (Floating marks with no scale fail.)
2. [WRONG] Do bars and filled areas on a linear axis start at 0?
3. [WRONG] On a log axis, are there no bars, or do bars represent ratios starting at 1?
4. [WRONG] Is every shaded area proportional to its value (no truncated fills, no rescaled regions or insets)?
5. [WRONG] Do parts drawn as a whole sum to 100% with no double counting?
6. [WRONG] Is every scale one-to-one, with one shared scale where values are compared?
7. [WRONG] Are error bars or bands labeled with what they represent (SD, SE, CI level)?
8. [WRONG] Is a log axis titled with the variable (not "log(x)"), with the base clear?
9. [WRONG] Does a density or smoothed curve avoid implying impossible values (negative counts, over 100%)?
10. [BAD] Does the chart form match the question (amount, distribution, proportion, relationship, trend, geo, uncertainty)?
11. [BAD] Is the most important variable on position, with size and color for secondary ones?
12. [BAD] Are unordered categories sorted by value and ordered categories in natural order?
13. [BAD] Are stacks limited to quantities whose total means something (no stacked rates, medians, or means)?
14. [BAD] Is spread shown as a distribution (box, violin, points), not mean ± error bars?
15. [BAD] Is overplotting handled so no data is hidden?
16. [BAD] For histograms and densities: does the bin width or bandwidth look deliberately chosen, not a spiky or washed-out default?
17. [BAD] No 3D effects, and no 3D position axes on a static image?
18. [BAD] Ratios or multi-magnitude data on a log scale?
19. [UGLY] Shapes filled rather than outlined (bars and boxes lightly filled, points solid)?

## Color
20. [BAD] Does color have a job (distinguish, encode value, highlight)? If it's decorative, remove it.
21. [BAD] Categorical colors: 8 or fewer (3–5 ideal)? Past that, use direct labels or coarser groups.
22. [BAD] Continuous data on a monotonic light-to-dark scale, never rainbow?
23. [BAD] Diverging scale used only with a meaningful midpoint, with balanced arms?
24. [BAD] Does it survive colorblind simulation and grayscale (no red/green-only or blue/green-only distinctions)?
25. [BAD] Key distinctions redundantly coded (shape, position, label), not color alone, especially on thin lines and small points?
26. [BAD] Same variable, same color across every panel and figure in the set?
27. [UGLY] Highlight charts: are non-focal elements gray so the accent wins?
28. [UGLY] No large areas of heavily saturated color?

## Axes, labels, text
29. [BAD] Every axis titled with units, unless self-evident (years, names)?
30. [BAD] Small multiples share axis ranges (or the caption says why not)?
31. [BAD] Text legible at final size on the target canvas?
32. [BAD] Legend order matches the visual order of the data?
33. [UGLY] Tick labels horizontal (horizontal bars instead of rotated text)?
34. [UGLY] Same units on x and y means a square grid?
35. [UGLY] Aspect ratio shows the real differences without inflating them?
36. [UGLY] Text and marks balanced (no big text with tiny points, or the reverse)?
37. [UGLY] Not over-labeled (no redundant legend titles or obvious units)?
38. [UGLY] Could the legend be replaced by direct labels? If it stays, one legend per variable?

## Ink and layout
39. [BAD] Enough context that nothing floats (a grid, an axis, or a reference line)?
40. [BAD] Paired data uses an x = y diagonal (not a grid)?
41. [BAD] Small multiples ordered logically (magnitude, time, rank), not alphabetically by default?
42. [UGLY] Frames, borders, and minor gridlines removed; major gridlines light?
43. [UGLY] Gridlines perpendicular to the variable of interest?
44. [UGLY] Compound panels aligned, with consistent colors and order and small consistent a/b/c labels?
45. [UGLY] Value labels don't visually lengthen bars?

## Story and annotation
46. [BAD] Does the chart make one clear point a busy reader gets in seconds (does the cold read match the intended point)?
47. [BAD] Does the title state the point as a sentence, with exactly one title (image or caption, not both)?
48. [BAD] Are dimensions that don't serve the point removed?
49. [UGLY] Actual numbers printed where area or angle is hard to judge?
50. [UGLY] Data source credited (caption, or in the image for standalone use)?
51. [UGLY] In a figure set: raw data before derived, and chart types varied across analyses?

## Export (check when files are provided)
52. [BAD] No JPEG for charts. Vector (SVG/PDF) master, PNG for web and social?
53. [UGLY] Fonts embedded in vector output? Dense point layers rasterized?
54. [UGLY] Randomness (jitter, draws) seeded so the figure is repeatable?
