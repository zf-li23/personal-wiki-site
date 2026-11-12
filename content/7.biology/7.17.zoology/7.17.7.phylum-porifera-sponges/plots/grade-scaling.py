"""Scaling of pumping capacity with size in the three grades of the sponge aquiferous system (schematic).
Asconoid: choanocytes line the wall of a tube of diameter d, so the choanocyte area per unit volume,
and the pumping capacity per unit volume, scale as 1/d. Syconoid: folding multiplies the area by a
constant factor (here 10). Leuconoid: chambers fill the mesohyl at a constant density, so the capacity
per unit volume is independent of size. The dashed line is the requirement of the tissue per unit volume.
All constants are illustrative.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(16.0, 9.0)
d = np.logspace(-1, 3, 300)          # body diameter in mm
need = 1.0
ascon = 2.0 / d
sycon = 20.0 / d
leucon = 5.0 * np.ones_like(d)
pl = quant.Plot(ax, (2.4, 1.6, 11.4, 6.4), xlim=(0.1, 1000), ylim=(0.05, 50), xlog=True, ylog=True,
                xlabel="body diameter d / mm (log scale)", ylabel="pumping capacity per volume (relative)",
                xticks=[(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")],
                yticks=[(0.1, "0.1"), (1, "1"), (10, "10")], grid=True)
pl.hline(need, token="ink", dashed=True, lw=1.2, text="requirement", x=150)
pl.line(d, ascon, "dna", lw=2.0, text="asconoid ∝ 1/d", at=0.12, dy=0.35)
pl.line(d, sycon, "rna", lw=2.0, text="syconoid ∝ 10/d", at=0.38, dy=0.35)
pl.line(d, leucon, "plant", lw=2.0, text="leuconoid: constant", at=0.75, dy=0.3)
pl.points([2.0, 20.0], [1.0, 1.0], "negative", r=0.12)
pl.text(1.25, 0.5, "max. size\nasconoid", size="tiny", color=quant.line_color("negative"))
pl.text(12.5, 0.5, "max. size\nsyconoid", size="tiny", color=quant.line_color("negative"))
bio.label(ax, (8.1, 8.6), "Why large sponges are leuconoid", size="small", bold=True)
bio.label(ax, (8.1, 0.3), "schematic: illustrative constants", size="tiny", color=P.muted())
