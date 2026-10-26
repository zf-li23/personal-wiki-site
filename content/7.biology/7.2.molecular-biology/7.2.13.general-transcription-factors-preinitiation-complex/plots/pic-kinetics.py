# Kinetics of multistep preinitiation complex assembly, Eq. (13.1).
# m consecutive irreversible steps with equal rate k; the completion time is Erlang(m, k) with mean m/k.
# All curves have the same mean (10 s), so k = m / 10 s. A: cumulative fraction of promoters with a complete PIC;
# B: probability density of the completion time; the relative width is 1/sqrt(m).
import numpy as np
from scipy.stats import gamma
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19.0, 7.6)
t = np.linspace(0, 40, 500)
mean = 10.0
cases = [(1, "neutral", "1 step"), (2, "receptor", "2 steps (holoenzyme)"), (5, "enzyme", "5 steps (stepwise)")]

a = C.axes_at(ax, (1.4, 1.3, 7.2, 5.2))
b = C.axes_at(ax, (11.2, 1.3, 7.2, 5.2))
for m, tok, name in cases:
    k = m / mean
    a.plot(t, gamma.cdf(t, m, scale=1 / k), color=C.line(tok), lw=2.0, label=name)
    b.plot(t, gamma.pdf(t, m, scale=1 / k), color=C.line(tok), lw=2.0, label=f"{name}: CV = {1 / np.sqrt(m):.2f}")
for p in (a, b):
    p.axvline(mean, color=P.muted(), lw=0.7, ls=(0, (2, 2)))
    p.set_xlim(0, 40)
a.set_ylim(0, 1.02)
b.set_ylim(0, 0.135)
C.style_axes(a, "time / s", "fraction of promoters with a complete PIC")
C.style_axes(b, "completion time / s", "probability density / s$^{-1}$")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower right")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
a.text(mean + 0.6, 0.06, "mean = 10 s", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "A", (0.1, 7.5))
bio.label(ax, (0.6, 7.15), "Fraction assembled", size="normal", bold=True, ha="left")
bio.panel(ax, "B", (9.9, 7.5))
bio.label(ax, (10.4, 7.15), "Distribution of assembly times", size="normal", bold=True, ha="left")
