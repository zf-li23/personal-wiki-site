"""Clones in a critical branching process: homeostasis with neutral drift (Theorem 36.4.4).

Each stem cell, per generation, gives two stem cells or two differentiated cells with probability 1/2 each
(f(x) = (1 + x^2) / 2, m = 1, offspring variance sigma^2 = 1). 200 000 clones are followed for 60 generations
(seed 0). A: the fraction of clones still containing stem cells falls as 2 / (sigma^2 t). B: the mean size of
the surviving clones grows linearly, as sigma^2 t / 2, while the mean over all clones stays 1. C: sizes of the
surviving clones at t = 50, divided by their mean, follow an exponential law (Yaglom's theorem), the signature of
neutral drift measured in labeled epidermis and intestinal crypts.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
n0, T = 200_000, 60
z = np.ones(n0, dtype=np.int64)
surv, msize, snap = [], [], None
for t in range(1, T + 1):
    z = 2 * rng.binomial(z, 0.5)
    alive = z > 0
    surv.append(alive.mean())
    msize.append(z[alive].mean())
    if t == 50:
        snap = z[alive].astype(float)
tt = np.arange(1, T + 1)
fig, ax = bio.canvas(30.0, 9.0)

pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.2))
pa.loglog(tt, surv, "o", ms=2.6, color=Q.line_color("protein"), label="simulation")
pa.loglog(tt[1:], 2 / tt[1:], color=Q.line_color("negative"), lw=1.4, label="2 / t")
C.style_axes(pa, "generation t", "fraction of clones surviving")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.2, 8.8))
bio.label(ax, (2.0, 8.5), "Most clones are lost", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.2))
pb.plot(tt, msize, "o", ms=2.6, color=Q.line_color("protein"), label="surviving clones")
pb.plot(tt, tt / 2 + 1, color=Q.line_color("negative"), lw=1.4, label="t / 2 + 1")
pb.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(40, 2.2, "all clones: mean 1", fontsize=FS["tiny"], color=P.muted())
C.style_axes(pb, "generation t", "mean stem cells per clone")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.6, 8.8))
bio.label(ax, (12.0, 8.5), "Survivors grow linearly", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.0, 1.6, 7.0, 6.2))
w = snap / snap.mean()
pc.hist(w, bins=np.linspace(0, 5, 26), density=True, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.4,
        label="t = 50")
ww = np.linspace(0, 5, 200)
pc.semilogy(ww, np.exp(-ww), color=Q.line_color("negative"), lw=1.5, label="exp(-w)")
C.style_axes(pc, "size / mean size", "density")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (20.6, 8.8))
bio.label(ax, (22.0, 8.5), "Scaled sizes: exponential", size="small", bold=True, ha="left")
