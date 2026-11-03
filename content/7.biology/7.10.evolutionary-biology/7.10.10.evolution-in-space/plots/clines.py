"""Clines maintained by selection against gene flow, from numerical steady states of
dp/dt = (sigma^2/2) d^2p/dx^2 + f(p, x).
A: a step environment: allele A2 has relative advantage s to the east of x = 0 and disadvantage s to the
west (genic selection, f = s sgn(x) p (1 - p)). Clines for four values of the ratio sigma^2/s (distance in
arbitrary units); the width measured from p = 0.1 to p = 0.9 is 2.50 sqrt(sigma^2/s) in every case.
B: a tension zone maintained by selection against heterozygotes (fitnesses 1 : 1 - s* : 1, so that
f = s* p q (2p - 1) approximately) in a uniform environment, distance in units of sigma / sqrt(s*); the
numerical solution (line) agrees with the exact front p = 1 / (1 + exp(-x sqrt(2 s*) / sigma)) (dots), whose
width, the inverse of the maximum slope, is sqrt(8 sigma^2 / s*) = 2.83 sigma / sqrt(s*). Dashed: a neutral
cline formed when two populations fixed for different alleles meet, after a time t with sigma^2 t equal to
the same width squared over 2 pi; without selection it keeps widening as sqrt(2 pi sigma^2 t)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def steady(f, x, p0, D, dt, steps):
    dx = x[1] - x[0]
    p = p0.copy()
    for _ in range(steps):
        lap = np.zeros_like(p)
        lap[1:-1] = (p[2:] - 2 * p[1:-1] + p[:-2]) / dx**2
        lap[0], lap[-1] = lap[1], lap[-2]
        p = np.clip(p + dt * (D * lap + f(p)), 0, 1)
    return p


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9, wspace=0.28)
a = axs[0]
x = np.arange(-6, 6.0001, 0.04)
for ratio, tok in ((0.01, "negative"), (0.25, "rna"), (1.0, "plant"), (4.0, "dna")):
    D = ratio / 2  # s = 1, sigma^2 = ratio
    dt = min(0.4 * 0.04**2 / D, 0.01)
    steps = int(60 / dt)
    p = steady(lambda p: np.sign(x) * p * (1 - p), x, 0.5 + 0.45 * np.tanh(x), D, dt, steps)
    w = np.interp(0.9, p, x) - np.interp(0.1, p, x)
    a.plot(x, p, color=charts.line(tok), lw=2, label=f"$\\sigma^2/s = {ratio:g}$: width {w:.2f}")
a.axvline(0, color=P.muted(), lw=0.8, ls=":")
a.text(-5.8, 0.93, "$A_1$ favoured", fontsize=FT["tiny"], color=P.muted())
a.text(5.8, 0.05, "$A_2$ favoured", fontsize=FT["tiny"], color=P.muted(), ha="right")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", bbox_to_anchor=(0, 0.88))
charts.style_axes(a, "distance $x$", "frequency of $A_2$")
charts.title(a, "A  Cline in a step environment")

b = axs[1]
x = np.arange(-8, 8.0001, 0.04)
D = 0.5  # sigma = 1, s* = 1
p = steady(lambda p: p * (1 - p) * (2 * p - 1), x, 0.5 + 0.5 * np.tanh(x), D, 0.0016, 50000)
exact = 1 / (1 + np.exp(-x * np.sqrt(2)))
w = np.sqrt(8)
b.plot(x, p, color=charts.line("dna"), lw=2, label="tension zone (numerical)")
b.scatter(x[::12], exact[::12], s=10, color=charts.line("rna"), zorder=3, label="exact front")
tt = w**2 / (2 * np.pi)
b.plot(x, 0.5 * (1 + erf(x / np.sqrt(2 * tt))), color=P.muted(), lw=1.4, ls="--", label="neutral mixing, same width")
b.annotate("", xy=(w / 2, 0.5), xytext=(-w / 2, 0.5), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
b.text(0, 0.54, "$w = \\sqrt{8\\sigma^2/s^*}$", ha="center", fontsize=FT["tiny"], color=P.ink())
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "distance $x\\sqrt{s^*}/\\sigma$", "frequency of arrangement 2")
charts.title(b, "B  Tension zone (selection against heterozygotes)")
