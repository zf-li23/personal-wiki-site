"""Discrete-time logistic growth with a one-step delay in density dependence.

Model: N_{t+1} = N_t [1 + r (1 - N_{t-1} / K)], with N in units of K and N_0 = N_1 = 0.1.
A: trajectories for r = 0.2 (monotone), 0.6 (damped oscillation) and 1.05 (sustained, quasi-periodic
oscillation on an invariant closed curve). B: modulus of the dominant root of the linearized
characteristic equation z^2 - z + r = 0 (Proposition 13.1.2): the roots are real for r < 1/4 and a complex
pair of modulus sqrt(r) for r > 1/4, which leaves the unit circle at r = 1. The delayed Beverton-Holt model
N_{t+1} = R N_t / (1 + a N_{t-1}) has the characteristic equation z^2 - z + c = 0 with c = (R - 1)/R,
which always lies in the shaded range 0 < c < 1: it can oscillate (R > 4/3) but is always stable.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 15.5, 6.8))
for r, tok in [(0.2, "enzyme"), (0.6, "dna"), (1.05, "negative")]:
    N = [0.1, 0.1]
    for _ in range(80):
        N.append(N[-1] * (1 + r * (1 - N[-2])))
    pa.plot(np.arange(len(N)), N, "-o", ms=2.0, lw=0.9, color=Q.line_color(tok), label=f"r = {r}")
pa.axhline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.set_xlim(0, 81)
C.style_axes(pa, "generation t", "N / K")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=3)
pa.set_ylim(0, 2.0)
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Delayed discrete logistic", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (21.5, 1.6, 7.0, 6.8))
r = np.linspace(0.001, 1.4, 400)
mod = np.where(r < 0.25, (1 + np.sqrt(np.clip(1 - 4 * r, 0, None))) / 2, np.sqrt(r))
pb.axvspan(0, 1, color=P.mix(P.fill("atp"), P.surface(), 0.55), lw=0, zorder=0)
pb.text(0.5, 1.18, "range of c = (R - 1)/R\n(delayed Beverton-Holt)", fontsize=FS["tiny"], color=P.ink(),
        ha="center", va="top")
pb.plot(r, mod, color=Q.line_color("protein"), lw=1.7)
pb.axhline(1, color=P.muted(), lw=0.8)
for xv, txt in [(0.25, "1/4"), (1.0, "1")]:
    pb.axvline(xv, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    pb.text(xv + 0.02, 0.43, txt, fontsize=FS["tiny"], color=P.muted())
pb.text(1.38, 1.03, "unstable", fontsize=FS["tiny"], color=P.muted(), ha="right")
pb.text(0.05, 0.55, "real roots:\nmonotone", fontsize=FS["tiny"], color=P.muted())
pb.text(0.62, 0.55, "complex:\ndamped", fontsize=FS["tiny"], color=P.muted())
pb.set_xlim(0, 1.4)
pb.set_ylim(0.4, 1.25)
C.style_axes(pb, "r  (or c)", "|dominant root|")
bio.panel(ax, "B", (19.8, 9.6))
bio.label(ax, (21.5, 9.2), "Linear stability", size="small", bold=True, ha="left")
