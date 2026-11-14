# wikibehav sample (7.18): sdt. Rendered with render_plot.py like any plot script.
import wikibio as bio
import wikibehav as wb
from wikibio import quant

fig, ax = bio.canvas(24, 8)
bio.panel(ax, "A", (0.2, 7.8))
p = quant.Plot(ax, (1.4, 1.4, 12.0, 5.2), xlim=(-3.5, 5), ylim=(0, 0.5), xlabel="internal response", ylabel="density",
               xticks=[-2, 0, 2, 4], yticks=[0, 0.2, 0.4])
H, F = wb.sdt_panel(p, d=1.5, xc=0.75)
bio.panel(ax, "B", (15.0, 7.8))
q = quant.Plot(ax, (16.8, 1.4, 5.4, 5.4), xlim=(0, 1), ylim=(0, 1), xlabel="false-alarm rate", ylabel="hit rate",
               xticks=[0, 0.5, 1], yticks=[0, 0.5, 1], frame="box")
wb.roc_panel(q, dprimes=(0.5, 1.5, 3.0), points=[(F, H, "dna")])
