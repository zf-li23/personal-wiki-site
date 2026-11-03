"""The hawk-dove game (Theorem 16.2.2), V = 2, C = 3.

A: payoff matrix. B: replicator dynamics dp/dt = p (1 - p) (W_H - W_D) from p0 = 0.02, 0.2, 0.5, 0.9,
0.99. C: W_H - W_D = V/2 - C p / 2 against p.
"""

import numpy as np
import wikibio as bio
from wikibio import behaviour as bh
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
V, Cc = 2.0, 3.0
M = bh.hawk_dove(V, Cc)
fig, ax = bio.canvas(34.0, 10.0)
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (1.2, 9.4), "Payoff to focal player", size="small", bold=True, ha="left")
bh.payoff_matrix(ax, (5.6, 5.0), ["Hawk", "Dove"], [["(V − C)/2 = −0.5", "V = 2"], ["0", "V/2 = 1"]],
                 w=2.9, h=1.4, tokens=["negative", "protein"])
bio.label(ax, (5.6, 2.2), "V = 2, C = 3", size="small", color=P.muted())
t = np.linspace(0, 30, 600)
pb = C.axes_at(ax, (12.6, 1.6, 9.0, 6.8))
for p0 in (0.02, 0.2, 0.5, 0.9, 0.99):
    pb.plot(t, bh.replicator(M, p0, t), color=C.line("negative"), lw=1.6)
pb.axhline(V / Cc, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.text(29, V / Cc + 0.03, "p* = V/C", color=P.muted(), fontsize=FS["tiny"], ha="right", va="bottom")
pb.set_xlim(0, 30)
pb.set_ylim(0, 1)
C.style_axes(pb, "time", "frequency of hawks p")
bio.panel(ax, "B", (11.0, 9.8))
bio.label(ax, (12.6, 9.4), "Replicator dynamics", size="small", bold=True, ha="left")
pc = C.axes_at(ax, (24.6, 1.6, 8.6, 6.8))
p = np.linspace(0, 1, 200)
pc.plot(p, V / 2 - Cc * p / 2, color=C.line("negative"), lw=1.9)
pc.axhline(0, color=P.muted(), lw=0.8)
pc.plot([V / Cc], [0], "o", ms=5, color=P.ink())
pc.set_xlim(0, 1)
C.style_axes(pc, "frequency of hawks p", "W_H − W_D")
bio.panel(ax, "C", (23.0, 9.8))
bio.label(ax, (24.6, 9.4), "Negative frequency dependence", size="small", bold=True, ha="left")
