"""Projection of the stage-classified killer whale model (Brault and Caswell 1993).

Females of the resident killer whales (Orcinus orca) of coastal British Columbia and Washington, censused
1973-1987, in four stages: yearling (calf), juvenile, reproductive adult, post-reproductive adult. Projection
matrix as published by Brault and Caswell (1993) and reproduced in Caswell (2001):
    [[0,      0.0043, 0.1132, 0     ],
     [0.9775, 0.9111, 0,      0     ],
     [0,      0.0736, 0.9534, 0     ],
     [0,      0,      0.0452, 0.9804]].
Initial vector x0 = (10, 60, 110, 70). A: numbers in each stage and in total over 50 years (log scale).
B: the annual growth rate N(t+1)/N(t) approaches the dominant eigenvalue lambda1 = 1.0254. C: stage
proportions over 200 years approach the stable stage distribution w (dashed lines); convergence is slow
because the second eigenvalue (0.9804, the survival of post-reproductive females) is close to lambda1.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
A = np.array([[0, 0.0043, 0.1132, 0],
              [0.9775, 0.9111, 0, 0],
              [0, 0.0736, 0.9534, 0],
              [0, 0, 0.0452, 0.9804]])
names = ["yearling", "juvenile", "reproductive", "post-reproductive"]
toks = ["atp", "enzyme", "dna", "protein"]
ev, W = np.linalg.eig(A)
i = np.argmax(ev.real)
lam = ev[i].real
w = np.abs(W[:, i].real)
w /= w.sum()

T = 200
x = np.zeros((T + 1, 4))
x[0] = [10, 60, 110, 70]
for t in range(T):
    x[t + 1] = A @ x[t]
N = x.sum(axis=1)

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
for k in range(4):
    pa.plot(np.arange(51), x[:51, k], color=Q.line_color(toks[k]), lw=1.5, label=names[k])
pa.plot(np.arange(51), N[:51], color=P.ink(), lw=1.8, label="total")
pa.set_yscale("log")
pa.set_ylim(8, 8000)
pa.set_xlim(0, 50)
C.style_axes(pa, "year", "females")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left", ncol=2)
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "50-year projection", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
pb.plot(np.arange(T), N[1:] / N[:-1], color=Q.line_color("negative"), lw=1.6)
pb.axhline(lam, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(195, lam + 0.002, f"lambda1 = {lam:.4f}", fontsize=FS["tiny"], color=P.muted(), ha="right")
pb.set_xlim(0, T)
C.style_axes(pb, "year", "N(t+1) / N(t)")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Annual growth rate", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.0, 1.6, 7.0, 6.8))
for k in range(4):
    pc.plot(np.arange(T + 1), x[:, k] / N, color=Q.line_color(toks[k]), lw=1.5)
    pc.axhline(w[k], color=Q.line_color(toks[k]), lw=0.8, ls=(0, (3, 2)))
pc.set_xlim(0, T)
pc.set_ylim(0, 0.5)
C.style_axes(pc, "year", "proportion of females")
bio.panel(ax, "C", (20.5, 9.6))
bio.label(ax, (22.0, 9.2), "Convergence to w", size="small", bold=True, ha="left")
