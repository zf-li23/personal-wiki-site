"""Komarova model of a bone remodelling unit: one cycle, bone mass, repeated cycles, and oscillation above Hopf."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
a1, a2, b1, b2 = 3.0, 4.0, 0.2, 0.02
g12, g21, g22 = 1.0, -0.5, 0.0
k1, k2 = 0.24, 0.0017


def steady(g11):
    G = g12 * g21 - (1 - g11) * (1 - g22)
    Cb = (b1 / a1) ** ((1 - g22) / G) * (b2 / a2) ** (g21 / G)
    Bb = (b1 / a1) ** (g12 / G) * (b2 / a2) ** ((1 - g11) / G)
    return Cb, Bb


def rhs(g11, kf, Cb, Bb):
    def f(t, y):
        C, B, z = y
        C, B = max(C, 1e-9), max(B, 1e-9)
        return [a1 * C ** g11 * B ** g21 - b1 * C, a2 * C ** g12 * B ** g22 - b2 * B,
                -k1 * max(C - Cb, 0) + kf * max(B - Bb, 0)]
    return f


fig, axs = plt.subplots(1, 4, figsize=(13.6, 3.5))
fig.subplots_adjust(left=0.05, right=0.985, bottom=0.17, top=0.86, wspace=0.45)
Cb, Bb = steady(0.5)
s = solve_ivp(rhs(0.5, k2, Cb, Bb), [0, 300], [Cb + 10, Bb, 100.0], max_step=0.5, rtol=1e-8)
a = axs[0]
a.plot(s.t, s.y[0], color=charts.line("drug"), lw=1.6)
charts.style_axes(a, "days", "osteoclasts C")
a2_ = a.twinx()
a2_.plot(s.t, s.y[1], color=charts.line("dna"), lw=1.6)
for sp in ("top", "left", "bottom"):
    a2_.spines[sp].set_visible(False)
a2_.spines["right"].set_color(P_.muted())
a2_.tick_params(colors=P_.ink(), labelsize=FT["tiny"])
a2_.set_ylabel("osteoblasts B", fontsize=FT["small"], color=P_.ink())
charts.title(a, "A  One cycle")
b = axs[1]
b.plot(s.t, s.y[2], color=charts.line("bone"), lw=1.8)
charts.style_axes(b, "days", "local bone mass (%)")
charts.title(b, "B  Resorption and refilling")
c = axs[2]
for kf, ls, lab in ((k2, "-", "balanced"), (0.9 * k2, "--", "formation -10%")):
    y = [Cb + 10, Bb, 100.0]
    T, Z = [], []
    for k in range(5):
        s2 = solve_ivp(rhs(0.5, kf, Cb, Bb), [0, 150], y, max_step=0.5, rtol=1e-8)
        T.append(s2.t + 150 * k)
        Z.append(s2.y[2])
        y = [Cb + 10, Bb, s2.y[2][-1]]
    c.plot(np.concatenate(T), np.concatenate(Z), color=charts.line("bone"), lw=1.5, ls=ls, label=lab)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower left")
charts.style_axes(c, "days", "local bone mass (%)")
charts.title(c, "C  Repeated cycles")
d = axs[3]
Cb2, Bb2 = steady(1.12)
s3 = solve_ivp(rhs(1.12, k2, Cb2, Bb2), [0, 2000], [Cb2 * 1.05, Bb2, 100.0], max_step=1.0, rtol=1e-8)
d.semilogy(s3.t, s3.y[0] / Cb2, color=charts.line("drug"), lw=1.3, label="C / steady")
d.semilogy(s3.t, s3.y[1] / Bb2, color=charts.line("dna"), lw=1.3, label="B / steady")
d.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower left")
d.set_ylim(1e-3, 1e2)
charts.style_axes(d, "days", "relative cell number")
charts.title(d, "D  g11 = 1.12: oscillation")
