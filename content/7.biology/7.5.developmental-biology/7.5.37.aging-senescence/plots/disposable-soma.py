"""A disposable-soma model of optimal investment in maintenance (Formula 37.2.2).

An organizm matures at age 1 and then allocates a fraction u of its resources to somatic maintenance and 1 - u to
reproduction (fecundity b (1 - u) per unit time). Maintenance slows intrinsic aging: the hazard is
mu(x) = A + B exp(gamma(u) x), with gamma(u) = gamma0 exp(-k u), gamma0 = 1.5, k = 3, B = 0.01. Fitness is lifetime
reproduction R0(u) = b (1 - u) integral from 1 to infinity of S(x) dx (a stationary population). A: R0(u),
normalized by its maximum, for extrinsic mortality A = 0.02, 0.1 and 0.5; dots mark the optimum u*. B: the
optimal investment u* and the resulting median lifespan as functions of A: where extrinsic mortality is high,
selection favors little maintenance and fast aging (Williams' prediction).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
B, g0, k = 0.01, 1.5, 3.0
x = np.linspace(0, 60, 6001)
dx = x[1] - x[0]


def S(u, A):
    g = g0 * np.exp(-k * u)
    return np.exp(-A * x - B / g * (np.exp(np.minimum(g * x, 50)) - 1))


def R0(u, A):
    s = S(u, A)
    return (1 - u) * s[x >= 1].sum() * dx


us = np.linspace(0, 0.98, 197)
fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
for A, tok in ((0.02, "protein"), (0.1, "enzyme"), (0.5, "negative")):
    r = np.array([R0(u, A) for u in us])
    pa.plot(us, r / r.max(), color=Q.line_color(tok), lw=1.7, label=f"A = {A:g}")
    i = int(np.argmax(r))
    pa.plot([us[i]], [1.0], "o", ms=4, color=Q.line_color(tok))
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.08)
C.style_axes(pa, "investment in maintenance u", "lifetime reproduction R0 / max")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "An optimal investment in repair", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
As = np.logspace(-2.3, 0, 30)
ust, med = [], []
for A in As:
    r = np.array([R0(u, A) for u in us])
    u = us[int(np.argmax(r))]
    ust.append(u)
    s = S(u, A)
    med.append(x[np.argmin(np.abs(s - 0.5))])
pb.semilogx(As, ust, color=Q.line_color("protein"), lw=1.7, label="optimal u*")
pb.set_ylim(0, 1)
C.style_axes(pb, "extrinsic mortality A", "optimal u*")
pb2 = pb.twinx()
pb2.semilogx(As, med, color=Q.line_color("negative"), lw=1.5, ls=(0, (4, 2)), label="median lifespan")
C.style_axes(pb2, None, None)
pb2.spines["right"].set_visible(True)
pb2.spines["right"].set_color(P.muted())
pb2.tick_params(colors=P.muted(), labelsize=FS["tiny"])
pb2.set_ylabel("median lifespan (time units)", color=P.ink(), fontsize=FS["small"])
h1, l1 = pb.get_legend_handles_labels()
h2, l2 = pb2.get_legend_handles_labels()
pb.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Dangerous worlds favor fast aging", size="small", bold=True, ha="left")
