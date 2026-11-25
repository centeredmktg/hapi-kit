# Overlapping Points — Nothing Hidden

> Source: Industry standard. Load alongside the family reference when n is large or values are rounded.

## Pick by situation
| Situation | Fix |
|---|---|
| Moderate n, rounded or low-precision values (points stack exactly) | Partial transparency + slight jitter (seeded) |
| Very large n (100K+) | 2D bins or hex bins colored by count (hexagons represent their points slightly better) |
| Density varies smoothly | Contour lines (optionally shaded denser = darker) over small transparent points |
| 2–3 well-separated groups | Colored contour sets in one panel |
| Many overlapping groups | Facet one group per panel against a shared grid |

## Rules
- Transparency alone can't fix very large n: dense regions go solid while sparse ones vanish. Bin instead.
- Jitter only slightly. Heavy jitter moves data to places it isn't.
- Seed all jitter so the figure is repeatable.
- Very dense point clouds in a vector export make huge, slow files. Rasterize that layer or export PNG.

## Anti-patterns (all BAD)
- Opaque overplotted scatter hiding whole subgroups
- Over-jittered scatter
- 100K transparent points forming a black band
- 5+ colored groups overplotted in one panel
- 5 overlapping colored contour sets
