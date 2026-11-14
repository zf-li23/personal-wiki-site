"""Negative frequency-dependent selection on foraging alleles: w_R = 1 + s (p_hat - p), w_S = 1."""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
s, ph = 0.5, 0.7
fig, ax = bio.canvas(26.0, 10.0)
p = np.linspace(0, 1, 200)
pa = C.axes_at(ax, (2.4, 1.6, 9.6, 7.2))
pa.plot(p, 1 + s * (ph - p), color=C.line("negative"), lw=1.9)
pa.plot(p, np.ones_like(p), color=C.line("dna"), lw=1.9)
pa.axvline(ph, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(0.05, 1 + s * (ph - 0.05) + 0.02, "rover", color=C.line("negative"), fontsize=FS["tiny"], va="bottom")
pa.text(0.05, 0.98, "sitter", color=C.line("dna"), fontsize=FS["tiny"], va="top")
pa.text(ph + 0.02, 1.33, "p̂ = 0.7", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(0, 1)
pa.set_ylim(0.8, 1.4)
C.style_axes(pa, "frequency of rovers p", "relative fitness")
bio.panel(ax, "A", (0.4, 9.7))
pb = C.axes_at(ax, (15.4, 1.6, 9.6, 7.2))
for p0 in [0.02, 0.2, 0.5, 0.9, 0.99]:
    x = [p0]
    for g in range(40):
        q = x[-1]
        wr = 1 + s * (ph - q)
        wbar = q * wr + (1 - q)
        x.append(q * wr / wbar)
    pb.plot(range(41), x, color=C.line("negative"), lw=1.4)
pb.axhline(ph, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, 40)
pb.set_ylim(0, 1)
C.style_axes(pb, "generation", "frequency of rovers p")
bio.panel(ax, "B", (13.6, 9.7))
