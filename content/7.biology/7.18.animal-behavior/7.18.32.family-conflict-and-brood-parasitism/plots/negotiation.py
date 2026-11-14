"""Sexual conflict over how much care to give: best-response curves (Houston and Davies 1985).

A: brood success depends on the total effort T = x + y of the female (x) and male (y), B(T) = 1 - exp(-T),
with diminishing returns; each parent pays its own cost, k x^2 / 2 (k = 0.6 for the female, 0.9 for the male).
A parent's best response to its partner's effort solves exp(-(x + y)) = k x; its slope lies between 0 and -1,
so a parent compensates only partly for a reduction in its partner's effort. The curves cross at a stable
equilibrium of biparental care; the staircase shows successive best responses converging on it from an
initial female effort of 0.05.
B: if each parent's best response had a slope steeper than -1 (overcompensation), shown with linear best
responses x = 1.2 - 1.6 y and y = 1.2 - 1.6 x, the crossing point is unstable and successive responses diverge
until one parent does all the work (uniparental care).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT


def best(other, k):
    lo, hi = 0.0, 5.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if np.exp(-(mid + other)) > k * mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


kf, km = 0.6, 0.9
e = np.linspace(0, 1.6, 200)
fig, ax = bio.canvas(30.0, 11.0)
pa = Ch.axes_at(ax, (2.6, 1.9, 9.0, 8.0))
fx = [best(y, kf) for y in e]
my = [best(x, km) for x in e]
pa.plot(fx, e, color=Ch.line("rna"), lw=1.9, label="female's best response to male")
pa.plot(e, my, color=Ch.line("dna"), lw=1.9, label="male's best response to female")
x = 0.05
pts = [(x, 0)]
for _ in range(8):
    y = best(x, km)
    pts.append((x, y))
    x = best(y, kf)
    pts.append((x, y))
pts = np.array(pts)
pa.plot(pts[:, 0], pts[:, 1], color=P.ink(), lw=0.9, ls=(0, (2, 1.5)))
pa.plot([pts[-1, 0]], [pts[-1, 1]], "o", color=P.ink(), ms=6)
pa.text(pts[-1, 0] + 0.05, pts[-1, 1] + 0.05, "stable biparental care", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 1.6)
pa.set_ylim(0, 1.6)
pa.set_aspect("equal")
Ch.style_axes(pa, "female effort $x$", "male effort $y$")
Ch.title(pa, "Partial compensation: stable")
leg = pa.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "A", (0.3, 10.8))

pb = Ch.axes_at(ax, (18.6, 1.9, 9.0, 8.0))
a, b = 1.2, 1.6
xx = np.linspace(0, 1.2 / 1.6, 50)
pb.plot(np.clip(a - b * xx, 0, None), xx, color=Ch.line("rna"), lw=1.9)
pb.plot(xx, np.clip(a - b * xx, 0, None), color=Ch.line("dna"), lw=1.9)
xs = a / (1 + b)
x = xs + 0.03
pts = [(x, 0.0)]
for _ in range(6):
    y = max(a - b * x, 0)
    pts.append((x, y))
    x = max(a - b * y, 0)
    pts.append((x, y))
pts = np.array(pts)
pb.plot(pts[:, 0], pts[:, 1], color=P.ink(), lw=0.9, ls=(0, (2, 1.5)))
pb.plot([xs], [xs], "o", color=P.ink(), ms=6, mfc=P.surface())
pb.text(xs + 0.06, xs + 0.04, "unstable", fontsize=FS["tiny"], color=P.ink())
pb.plot([a], [0], "o", color=Ch.line("rna"), ms=6)
pb.text(a - 0.02, 0.07, "female cares alone", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right")
pb.plot([0], [a], "o", color=Ch.line("dna"), ms=6, clip_on=False)
pb.text(0.05, a + 0.05, "male cares alone", fontsize=FS["tiny"], color=Ch.line("dna"))
pb.set_xlim(0, 1.6)
pb.set_ylim(0, 1.6)
pb.set_aspect("equal")
Ch.style_axes(pb, "female effort $x$", "male effort $y$")
Ch.title(pb, "Overcompensation: unstable")
bio.panel(ax, "B", (16.3, 10.8))
