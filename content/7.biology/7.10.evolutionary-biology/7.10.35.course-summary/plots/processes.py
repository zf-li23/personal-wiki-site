"""One stochastic mathematics. A: 20 Wright-Fisher populations (N = 50, p_0 = 0.5) with the expected
heterozygosity E[2 p_t q_t] = 2 p_0 q_0 (1 - 1/2N)^t (dashed). B: a trait evolving
by Brownian motion (sigma^2 = 1) and by an Ornstein-Uhlenbeck process (alpha = 0.5, theta = 0,
sigma^2 = 1), 12 paths each from X_0 = 0, with their variances sigma^2 t and sigma^2 (1 - exp(-2 alpha t)) / 2 alpha
(lines; shown as +- 2 standard deviations). C: the Jukes-Cantor chain: proportion of differing sites
p = (3/4)(1 - exp(-4d/3)) against the distance d in expected substitutions per site (line), with
proportions from simulated pairs of sequences of 500 sites (dots), and the large-sample standard error
of the JC69 distance, sqrt(p(1 - p) / n) / (1 - 4p/3), for n = 500 sites (dashed, right axis)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 3.7))
fig.subplots_adjust(left=0.06, right=0.94, bottom=0.17, top=0.88, wspace=0.34)

N, T = 50, 150
for k in range(20):
    p = [0.5]
    for t in range(T):
        p.append(rng.binomial(2 * N, p[-1]) / (2 * N))
    a.plot(range(T + 1), p, color=charts.line("dna"), lw=0.7, alpha=0.55)
t = np.arange(T + 1)
a.plot(t, 0.5 * (1 - 1 / (2 * N)) ** t, color=P.ink(), lw=1.4, ls="--", label="$\\mathbb{E}[2p_tq_t] = 2p_0q_0(1 - 1/2N)^t$")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
a.set_ylim(0, 1)
a.set_xlim(0, T)
charts.style_axes(a, "generations", "allele frequency $p$")
charts.title(a, "A  Drift: Wright–Fisher chain")

dt, tmax, al = 0.02, 10.0, 0.5
ts = np.arange(0, tmax + dt, dt)
for k in range(12):
    inc = rng.normal(0, np.sqrt(dt), len(ts) - 1)
    bm = np.concatenate([[0], np.cumsum(inc)])
    ou = [0.0]
    for e in rng.normal(0, np.sqrt(dt), len(ts) - 1):
        ou.append(ou[-1] - al * ou[-1] * dt + e)
    b.plot(ts, bm, color=charts.line("rna"), lw=0.6, alpha=0.5)
    b.plot(ts, ou, color=charts.line("plant"), lw=0.6, alpha=0.6)
b.plot(ts, 2 * np.sqrt(ts), color=charts.line("rna"), lw=1.4, ls="--", label="Brownian motion")
b.plot(ts, -2 * np.sqrt(ts), color=charts.line("rna"), lw=1.4, ls="--")
vo = (1 - np.exp(-2 * al * ts)) / (2 * al)
b.plot(ts, 2 * np.sqrt(vo), color=charts.line("plant"), lw=1.4, ls="--", label="Ornstein–Uhlenbeck")
b.plot(ts, -2 * np.sqrt(vo), color=charts.line("plant"), lw=1.4, ls="--")
b.set_xlim(0, tmax)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "time", "trait value $X(t)$")
charts.title(b, "B  Traits: diffusion with and without a pull")

d = np.linspace(0, 2.5, 300)
pd = 0.75 * (1 - np.exp(-4 * d / 3))
c.plot(d, pd, color=charts.line("dna"), lw=1.8, label="$p = \\frac{3}{4}(1 - \\mathrm{e}^{-4d/3})$")
c.axhline(0.75, color=P.muted(), lw=0.8, ls=":")
n = 500
for dd in (0.05, 0.2, 0.4, 0.7, 1.0, 1.5, 2.0, 2.5):
    pdiff = 0.75 * (1 - np.exp(-4 * dd / 3))
    for r in range(3):
        c.scatter([dd], [rng.binomial(n, pdiff) / n], s=10, color=charts.line("dna"), zorder=4)
c.set_ylim(0, 0.85)
c.set_xlim(0, 2.5)
c2 = c.twinx()
dd = np.linspace(0.01, 1.6, 200)
pp = 0.75 * (1 - np.exp(-4 * dd / 3))
se = np.sqrt(pp * (1 - pp) / n) / (1 - 4 * pp / 3)
c2.plot(dd, se, color=charts.line("negative"), lw=1.4, ls="--", label="standard error of $\\hat d$")
c2.set_ylim(0, 0.5)
charts.style_axes(c, "distance $d$ (substitutions per site)", "proportion of sites differing $p$")
charts.style_axes(c2, None, "standard error of $\\hat d$, $n = 500$", box=True)
c2.spines["top"].set_visible(False)
h1, l1 = c.get_legend_handles_labels()
h2, l2 = c2.get_legend_handles_labels()
c.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.title(c, "C  Sequences: Markov chain and saturation")
