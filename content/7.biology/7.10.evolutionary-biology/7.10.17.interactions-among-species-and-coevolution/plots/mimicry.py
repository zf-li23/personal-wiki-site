"""Mimicry and frequency dependence.

A: Muller (1879): predators kill k = 50 individuals per warning pattern per season. Per capita mortality
of species 1 with abundance n1: alone k / n1; sharing the pattern with a co-mimic of abundance 1000,
k / (n1 + 1000). B: Batesian mimicry: probability that an attack on the shared pattern is rewarded (the
predator gets a palatable mimic) = m / (m + M) for mimic abundance m and model abundance M.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
k = 50
n1 = np.logspace(1.7, 3.5, 200)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.loglog(n1, k / n1, color=C.line("negative"), lw=1.9, label="own pattern")
pa.loglog(n1, k / (n1 + 1000), color=C.line("protein"), lw=1.9, label="shared with co-mimic (n₂ = 1000)")
pa.set_xlim(n1[0], n1[-1])
C.style_axes(pa, "abundance of species 1, n₁", "per capita mortality")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Müllerian mimicry: sharing the cost of learning", size="small", bold=True, ha="left")
ratio = np.logspace(-2, 2, 200)
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
pb.semilogx(ratio, ratio / (1 + ratio), color=C.line("rna"), lw=1.9)
pb.axvline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_ylim(0, 1)
pb.set_xlim(0.01, 100)
C.style_axes(pb, "ratio of mimics to models, m/M", "probability an attack is rewarded")
pb.text(0.012, 0.85, "rare mimics:\npattern protects", fontsize=FS["tiny"], color=P.ink(), va="top")
pb.text(8, 0.35, "common mimics:\nprotection lost", fontsize=FS["tiny"], color=P.ink(), va="top")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Batesian mimicry: negative frequency dependence", size="small", bold=True, ha="left")
