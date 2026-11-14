# wikibehav sample (7.18): orientation. Rendered with render_plot.py like any plot script.
import numpy as np
import wikibio as bio
import wikibehav as wb

P = bio.P
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8))
bio.label(ax, (1.2, 8.5), "Emlen funnel (top view)", size="small", bold=True, ha="left")
scr = wb.vonmises(200, 2.0, 160, seed=2)
wb.emlen_funnel(ax, (4.6, 4.2), 3.0, scr, sectors=24)
bio.panel(ax, "B", (8.8, 8.8))
bio.label(ax, (9.8, 8.5), "Spring, local sky", size="small", bold=True, ha="left")
a = wb.vonmises(20, 2.5, 22, seed=1)
st = wb.circular_plot(ax, (12.6, 4.4), 2.8, a, token="dna", expected=0, expected_text="expected")
bio.panel(ax, "C", (16.6, 8.8))
bio.label(ax, (17.6, 8.5), "Disoriented", size="small", bold=True, ha="left")
b = wb.vonmises(0, 0.0, 18, seed=4)
wb.circular_plot(ax, (20.6, 4.4), 2.8, b, token="rna")
