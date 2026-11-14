"""Emlen funnel and circular statistics (simulated data in the style of Emlen's planetarium experiments with
indigo buntings, autumn). A: the funnel seen from above, with the scratch marks of one night on the paper lining;
the scratches are counted in 24 sectors. B: mean directions of 20 birds tested under a planetarium sky matching
the natural sky: oriented south (Rayleigh test, n, r, p below). C: the same birds when the planetarium sky is
rotated by 180 deg about the vertical axis, so that the stars of the north appear in the south: the birds reverse
their heading, showing that they use the stars as a compass. Dashed line: the seasonally appropriate direction
relative to the projected sky."""
import wikibio as bio
import wikibehav as wb

P = bio.P
fig, ax = bio.canvas(25, 9.4)
bio.panel(ax, "A", (0.2, 9.1))
bio.label(ax, (1.2, 8.8), "Emlen funnel (top view)", size="small", bold=True, ha="left")
wb.emlen_funnel(ax, (4.6, 4.4), 3.1, wb.vonmises(185, 2.2, 140, seed=7), sectors=24)
bio.panel(ax, "B", (9.0, 9.1))
bio.label(ax, (10.0, 8.8), "Planetarium sky as natural", size="small", bold=True, ha="left")
wb.circular_plot(ax, (12.9, 4.6), 2.8, wb.vonmises(178, 2.4, 20, seed=3), token="dna", expected=180)
bio.panel(ax, "C", (17.0, 9.1))
bio.label(ax, (18.0, 8.8), "Sky rotated by 180°", size="small", bold=True, ha="left")
wb.circular_plot(ax, (21.0, 4.6), 2.8, wb.vonmises(352, 2.0, 20, seed=5), token="rna", expected=0)
