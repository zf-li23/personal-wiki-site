"""Hill (1991): plumage manipulation of male house finches. Proportion paired and days to pair."""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
groups = ["brightened\n(n = 40)", "sham control\n(n = 20)", "lightened\n(n = 40)"]
paired = [1.0, 0.60, 0.27]
days = [12.1, 20.2, 27.8]
tokens = ["negative", "neutral", "lipid_tail"]
fig, ax = bio.canvas(24.0, 10.0)
x = np.arange(3)
pa = C.axes_at(ax, (2.6, 2.0, 8.6, 6.6))
pa.bar(x, paired, width=0.6, color=[P.fill(t) for t in tokens], edgecolor=[P.edge(t) for t in tokens], lw=1.0)
for i, v in enumerate(paired):
    pa.text(i, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=FS["tiny"], color=P.ink())
pa.set_xticks(x)
pa.set_xticklabels(groups)
pa.set_ylim(0, 1.1)
C.style_axes(pa, None, "proportion of males paired")
bio.panel(ax, "A", (0.4, 9.7))
pb = C.axes_at(ax, (14.8, 2.0, 8.6, 6.6))
pb.bar(x, days, width=0.6, color=[P.fill(t) for t in tokens], edgecolor=[P.edge(t) for t in tokens], lw=1.0)
for i, v in enumerate(days):
    pb.text(i, v + 0.4, f"{v:.1f}", ha="center", va="bottom", fontsize=FS["tiny"], color=P.ink())
pb.set_xticks(x)
pb.set_xticklabels(groups)
pb.set_ylim(0, 32)
C.style_axes(pb, None, "time to pair / days")
bio.panel(ax, "B", (12.6, 9.7))
