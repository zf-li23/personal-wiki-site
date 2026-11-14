"""Leong (1969): heterogeneous summation of an eye bar and orange spots in Astatotilapia burtoni dummies."""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
labels = ["eye bar\nalone", "orange spots\nalone", "sum of\nsingle effects", "both features\n(observed)"]
vals = [2.81, -1.77, 1.04, 1.12]
tokens = ["neutral", "rna", "protein", "negative"]
fig, ax = bio.canvas(16.0, 10.0)
pa = C.axes_at(ax, (3.0, 2.2, 12.0, 7.0))
x = np.arange(4)
bars = pa.bar(x, vals, width=0.6, color=[P.fill(t) for t in tokens], edgecolor=[P.edge(t) for t in tokens], lw=1.0)
bars[2].set_hatch("//")
pa.axhline(0, color=P.muted(), lw=0.8)
for i, v in enumerate(vals):
    pa.text(i, v + (0.12 if v > 0 else -0.12), f"{v:+.2f}".replace("-", "−"), ha="center",
            va="bottom" if v > 0 else "top", fontsize=FS["tiny"], color=P.ink())
pa.set_xticks(x)
pa.set_xticklabels(labels)
pa.set_ylim(-2.6, 3.6)
C.style_axes(pa, None, "change in attack rate / (attacks per min)")
