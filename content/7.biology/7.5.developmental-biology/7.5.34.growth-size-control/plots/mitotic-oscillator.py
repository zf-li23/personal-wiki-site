"""A limit-cycle mitotic oscillator and the phase resetting of Physarum by heat shock (Section 34.2).

The oscillator in polar form, dr/dt = a r (1 - r^2), dphi/dt = w (a = 4, w = 2 pi so the period is 1), around
the equilibrium (X, Y) = (1, 1); mitosis occurs when y = Y - 1 rises through the threshold y0 = 0.85. A heat shock at
phase 0.75 of the cycle (shortly before mitosis) degrades the enzymes and moves the state towards the equilibrium,
r -> (1 - s) r (for s > 1 to the opposite side). A: trajectories after shocks of increasing strength: a weak shock
(1) delays the next mitosis a little, a stronger one (2) more; still stronger (3) leaves the orbit inside the
threshold for one turn, skipping a mitosis; beyond the centre (4) the phase is shifted by about half a cycle.
B: delay of the next mitosis (in periods) against the shock strength s.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
a, w, y0 = 4.0, 2 * np.pi, 0.85
phi_shock = 2 * np.pi * 0.75 + np.arcsin(y0) - 2 * np.pi * 0.99   # place the shock about a quarter period before mitosis
dt = 0.0005


def after_shock(s, tmax=4.0):
    r, ph = 1.0 * (1 - s), phi_shock
    if r < 0:
        r, ph = -r, ph + np.pi
    xs, ys = [], []
    t = 0.0
    prev = r * np.sin(ph)
    while t < tmax:
        r += dt * a * r * (1 - r * r)
        ph += dt * w
        t += dt
        y = r * np.sin(ph)
        xs.append(r * np.cos(ph))
        ys.append(y)
        if prev < y0 <= y and np.cos(ph) > 0:
            return t, np.array(xs), np.array(ys)
        prev = y
    return np.nan, np.array(xs), np.array(ys)


# unperturbed time to next mitosis from the shock phase
t_ref, _, _ = after_shock(0.0)
fig, ax = bio.canvas(24.0, 9.6)
pa = C.axes_at(ax, (1.6, 1.3, 7.6, 7.6))
th = np.linspace(0, 2 * np.pi, 200)
pa.plot(np.cos(th), np.sin(th), color=P.muted(), lw=1.0, ls=(0, (4, 2)))
pa.axhline(y0, color=P.ink(), lw=0.8)
pa.text(-1.25, y0 + 0.04, "mitosis threshold", fontsize=bio.core.FONT["tiny"], color=P.ink())
for k, (s, tk) in enumerate(((0.3, "channel"), (0.6, "positive"), (0.85, "drug"), (1.4, "protein"))):
    _, xs, ys = after_shock(s)
    pa.plot(xs, ys, color=Q.line_color(tk), lw=1.3)
    pa.plot(xs[0], ys[0], "o", ms=4, color=Q.line_color(tk))
    pa.text(xs[0] * 1.08, ys[0] * 1.08 - 0.05, str(k + 1), fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.plot(np.cos(phi_shock), np.sin(phi_shock), "s", ms=5, color=P.ink())
pa.set_aspect("equal")
pa.set_xlim(-1.3, 1.3)
pa.set_ylim(-1.3, 1.3)
C.style_axes(pa, "x = X − 1", "y = Y − 1")
bio.panel(ax, "A", (0.3, 9.4))
bio.label(ax, (1.6, 9.2), "Trajectories after a heat shock", size="small", bold=True, ha="left", va="top")

pb = C.axes_at(ax, (13.4, 1.5, 9.6, 7.0))
ss = np.linspace(0, 2.0, 161)
dl = []
for s in ss:
    tm, _, _ = after_shock(s)
    dl.append(tm - t_ref)
pb.plot(ss, dl, color=Q.line_color("protein"), lw=1.6)
pb.axvline(1.0, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.set_xlim(0, 2.0)
pb.set_ylim(0, max(np.nanmax(dl), 1.2) * 1.05)
C.style_axes(pb, "shock strength s", "delay of next mitosis / period")
bio.panel(ax, "B", (12.0, 9.4))
bio.label(ax, (13.4, 9.2), "Delay against strength", size="small", bold=True, ha="left", va="top")
