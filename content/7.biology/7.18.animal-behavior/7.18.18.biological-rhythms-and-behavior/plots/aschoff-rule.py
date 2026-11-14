"""Aschoff's rule (schematic, after Aschoff 1960). In constant light (LL), the free-running period tau of
nocturnal animals lengthens with the logarithm of light intensity, and that of diurnal animals shortens; the
ratio of activity to rest time (alpha : rho) falls in nocturnal and rises in diurnal animals. A
'velocity' interpretation: light slows the clock of a nocturnal animal and speeds that of a diurnal one. Slopes
are typical, about 0.3-0.5 h per decade of intensity; exceptions are common, especially among diurnal birds
that are not passerines and among mammals."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23, 9.6)
I = np.logspace(-1, 3, 50)
bio.panel(ax, "A", (0.3, 9.3))
p = quant.Plot(ax, (2.0, 1.7, 8.8, 6.8), xlim=(0.1, 1000), ylim=(22.5, 26.0), xlog=True,
               xlabel="Constant light intensity / lx", ylabel="Free-running period tau / h",
               xticks=[(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")], yticks=[23, 24, 25, 26])
p.line(I, 24.2 + 0.4 * np.log10(I / 0.1), "dna", text="nocturnal (mouse, hamster)", at=0.45, dy=0.45)
p.line(I, 24.9 - 0.45 * np.log10(I / 0.1), "rna", text="diurnal (finch, squirrel)", at=0.45, dy=-0.55)
p.hline(24.0, text="24 h", side="left")
bio.panel(ax, "B", (12.3, 9.3))
q = quant.Plot(ax, (14.0, 1.7, 8.4, 6.8), xlim=(0.1, 1000), ylim=(0, 2.5), xlog=True,
               xlabel="Constant light intensity / lx", ylabel="Activity : rest ratio",
               xticks=[(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")], yticks=[0, 1, 2])
q.line(I, 1.4 / (1 + 0.35 * np.log10(I / 0.1) ** 1.4), "dna", text="nocturnal", at=0.75, dy=0.18)
q.line(I, 0.5 + 0.35 * np.log10(I / 0.1), "rna", text="diurnal", at=0.75, dy=0.18)
ax.set_ylim(0.3, 9.6)
