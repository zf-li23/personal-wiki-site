"""Sizer, adder and timer: three rules for coordinating growth and division (simulations).

Cells grow exponentially and divide into two daughters that each receive a fraction 0.5 +- 0.03 (s.d.) of the
mother's volume. The volume at division Vd follows the linear rule Vd = a Vb + b + noise, with
    sizer:  a = 0, b = 2   (divide at a set size),
    adder:  a = 1, b = 1   (add a set volume between birth and division),
    timer:  a = 2, b = 0   (grow for a set time, so the volume doubles whatever the size at birth),
in units of the mean birth volume, and Gaussian noise of s.d. 0.1 in Vd (for the timer, an equivalent noise in
the growth time).
(A) Added volume Vd - Vb against volume at birth Vb for 600 cells of each rule: slopes a - 1 = -1, 0 and +1.
Measurements in Escherichia coli, Bacillus subtilis, Caulobacter, budding yeast daughters and many animal cell
lines give slopes near 0 (adder-like), fission yeast near -1 (sizer-like).
(B) Correction of a size deviation: the deviation of the birth volume from its mean, delta, after a cell is
born at twice the normal size; per generation delta changes by the factor a/2 (sizer 0, adder 1/2, timer 1).
(C) Coefficient of variation of the birth volume in 200 lineages over 60 generations: sizer and adder keep it
constant, whereas under a pure timer the noise accumulates and the size distribution spreads without limit.
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
RULES = [("sizer", 0.0, 2.0, "channel"), ("adder", 1.0, 1.0, "positive"), ("timer", 2.0, 0.0, "negative")]


def divide(vb, a, b, sd=0.1):
    if a == 2.0:  # timer: noise in the growth time, multiplicative
        vd = 2 * vb * np.exp(sd / 2 * rng.standard_normal(np.shape(vb)))
    else:
        vd = a * vb + b + sd * rng.standard_normal(np.shape(vb))
    f = np.clip(0.5 + 0.03 * rng.standard_normal(np.shape(vb)), 0.3, 0.7)
    return vd, f * vd


fig, ax = bio.canvas(27.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a1 = charts.axes_at(ax, (1.8, 1.5, 7.4, 6.6))
for name, a, b, tok in RULES:
    vb = np.ones(600)
    for _ in range(12 if a < 2 else 3):
        vd, vb_next = divide(vb, a, b)
        vb = vb_next
    vd, _ = divide(vb, a, b)
    a1.scatter(vb, vd - vb, s=4, color=charts.line(tok), alpha=0.5, lw=0)
    x = np.linspace(0.6, 1.4, 10)
    k, c = np.polyfit(vb, vd - vb, 1)
    a1.plot(x, k * x + c, color=charts.line(tok), lw=1.8, label=f"{name}: slope {k:+.2f}")
a1.set_xlim(0.6, 1.4)
a1.set_ylim(0.4, 1.6)
a1.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a1, "volume at birth Vb", "added volume Vd − Vb")

bio.panel(ax, "B", (10.2, 8.8))
b1 = charts.axes_at(ax, (11.8, 1.5, 6.0, 6.6))
g = np.arange(0, 7)
for name, a, b, tok in RULES:
    b1.plot(g, 1.0 * (a / 2) ** g, "o-", color=charts.line(tok), lw=1.6, ms=4, label=name)
b1.set_ylim(-0.05, 1.1)
b1.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(b1, "generation", "size deviation at birth δ / δ0")

bio.panel(ax, "C", (18.8, 8.8))
c1 = charts.axes_at(ax, (20.4, 1.5, 6.0, 6.6))
for name, a, b, tok in RULES:
    vb = np.ones(200)
    cv = []
    for _ in range(60):
        cv.append(vb.std() / vb.mean())
        _, vb = divide(vb, a, b)
    c1.plot(np.arange(60), cv, color=charts.line(tok), lw=1.6, label=name)
c1.set_ylim(0, 0.6)
c1.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(c1, "generation", "CV of birth volume")
