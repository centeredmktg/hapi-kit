# Geospatial — Where Is It?

> Source: Industry standard.

## Forms
| Situation | Form |
|---|---|
| Point locations | Layered map (base, data layer, labels) + scale bar + north arrow |
| Value per region, regions similar in size or small vs. the map | Choropleth with 4–6 binned colors (or continuous) |
| Value per region, regions very unequal in size (US states, countries) | Equal-tile cartogram heatmap → population cartogram → geofacet small multiples |
| Whole world | Equal-area projection when area matters; a compromise projection (Robinson, Winkel tripel) for general display |

## Rules
- Every flat map trades off angles vs. areas. Choose the projection by which one matters.
- **No Mercator for world maps.** It inflates high latitudes (Greenland looks bigger than Africa, which is ~14× larger). Transverse Mercator is fine for small zoomed areas.
- Never plot raw longitude/latitude as Cartesian x/y. Use a projection.
- Moving insets (Alaska, Hawaii) to save space is fine. **Rescaling them is not.**
- Build in layers and drop any layer that doesn't serve the question.
- Choropleths work best for densities (quantity per area or per capita). Raw totals are only OK if regions are similar in size, or small relative to the map.
- Bin continuous choropleth values into 4–6 classes so readers can match colors to the legend.
- Light background with dark = high for print. Dark background with bright = high can work on screens.
- Missing regions: neutral gray, explained in the legend.
- Local market maps (Reno metro, service areas): don't crop to a few ZIPs unless the brief says so. Show the full market and highlight the focus.

## Anti-patterns
| Grade | Pattern | Fix |
|---|---|---|
| BAD | Alaska shrunk under the lower 48 | Move without rescaling |
| BAD | State choropleth dominated by huge, sparse regions | Tile cartogram or geofacet |
| BAD | Rainbow choropleth | Monotonic sequential, or diverging with a real midpoint |
| BAD | Mercator world map | Equal-area or compromise projection |
