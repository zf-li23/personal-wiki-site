"""Protein bursts and the gamma distribution (time in protein lifetimes, gamma_p = 1). A: bursts at
frequency a = 3 with geometric sizes of mean b = 8, simulated with the Gillespie algorithm (bars),
against the negative binomial of the discrete model (points) and its continuous limit, the gamma
distribution with shape a and scale b (line). B: the same gene when its protein represses the burst
frequency, a(n) = a0 / (1 + (n/K)^2) with a0 = 10, b = 10, K = 30: simulation against the formula
of Friedman, Cai and Xie, p(x) ~ x^(a0-1) e^(-x/b) (1 + (x/K)^2)^(-a0/2), with the unregulated gamma
distribution (dashed) for comparison. C: noise against mean for 300 simulated genes with random burst
sizes and frequencies, each cell also multiplied by a shared factor with CV^2 = 0.1 (extrinsic
noise): at low expression eta^2 = (1 + b)/<n> (lines for b = 1 and 30), at high expression the
extrinsic floor."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import trapezoid
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)


def bursty(rate, b, tmax, n0=0):
    """Bursts at rate(n) with geometric sizes (mean b), first-order decay; time-weighted histogram."""
    q = b / (1 + b)
    t, n = 0.0, n0
    w = np.zeros(2000)
    while t < tmax:
        a1, a2 = rate(n), float(n)
        a0 = a1 + a2
        tau = rng.exponential(1 / a0)
        if t > 10:
            w[min(n, 1999)] += tau
        t += tau
        if rng.random() < a1 / a0:
            n += rng.geometric(1 - q) - 1  # sizes 0, 1, 2, ... with mean b
        else:
            n -= 1
    return w / w.sum()


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.32, left=0.06, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
a, b = 3.0, 8.0
w = bursty(lambda n: a, b, 3000)
n = np.arange(120)
ax.bar(n, w[:120], width=1.0, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.2)
ax.plot(n[::3], stats.nbinom.pmf(n[::3], a, 1 / (1 + b)), "o", ms=2.5, color=P.ink(), label="negative binomial")
x = np.linspace(0.5, 120, 300)
ax.plot(x, stats.gamma.pdf(x, a, scale=b), color=charts.line("blood"), lw=1.3, label="gamma (a, b)")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "protein number n", "probability")
charts.title(ax, "A  a = 3, b = 8")

ax = axs[1]
a0, b, K = 10.0, 10.0, 30.0
w = bursty(lambda n: a0 / (1 + (n / K) ** 2), b, 2000)
n = np.arange(200)
ax.bar(n, w[:200], width=1.0, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.2, label="simulation")
x = np.linspace(0.2, 200, 800)
px = x ** (a0 - 1) * np.exp(-x / b) * (1 + (x / K) ** 2) ** (-a0 / 2)
px /= trapezoid(px, x)
ax.plot(x, px, color=charts.line("blood"), lw=1.4, label="feedback formula")
ax.plot(x, stats.gamma.pdf(x, a0, scale=b), color=P.muted(), lw=1.0, ls="--", label="no feedback")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "protein number n", "probability")
charts.title(ax, "B  Negative autoregulation")

ax = axs[2]
cells = 4000
for _ in range(300):
    bb = 10 ** rng.uniform(0, 1.5)
    aa = 10 ** rng.uniform(-1, 2.5)
    ext = rng.gamma(10, 0.1, cells)
    nn = rng.negative_binomial(aa, 1 / (1 + bb), cells) * ext
    m = nn.mean()
    if m > 0.05:
        ax.plot(m, nn.var() / m ** 2, "o", ms=2.2, color=charts.line("protein"), alpha=0.7)
mm = np.logspace(-1.3, 4, 100)
for bb, ls in ((1, "--"), (30, ":")):
    ax.plot(mm, (1 + bb) / mm, color=P.ink(), lw=0.9, ls=ls, label=f"(1 + b)/⟨n⟩, b = {bb}")
ax.axhline(0.1, color=charts.line("blood"), lw=1.0, label="extrinsic floor")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(0.03, 300)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"mean $\langle n\rangle$", r"noise $\eta^2$")
charts.title(ax, "C  Noise against mean")
