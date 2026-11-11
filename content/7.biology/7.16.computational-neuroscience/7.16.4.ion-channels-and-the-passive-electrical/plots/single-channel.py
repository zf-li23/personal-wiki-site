"""Stochastic gating of a two-state channel (closed <-> open, opening rate alpha, closing rate beta,
Markov chain with time step 0.02 ms). At t = 0 a voltage step raises alpha from 0.02 to 1.0 ms^-1
(beta = 0.5 ms^-1), so that the open probability rises from 0.04 to 0.67 with time constant
1/(alpha + beta) = 0.67 ms. A: one channel in three trials. B: the mean current of N = 10, 100 and
1000 channels (one trial each, current in units of the single-channel current) with the
deterministic p(t) of the master equation. C: nonstationary fluctuation analysis: from 300 repeated
trials of N = 200 channels, the variance of the current plotted against its mean follows the parabola
var = i I - I^2 / N, from which the single-channel current i and N are estimated."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
dt = 0.02
t = np.arange(-2, 6, dt)
be, a0, a1 = 0.5, 0.02, 1.0
alpha = np.where(t < 0, a0, a1)


def simulate(N, trials):
    n = np.zeros(trials)
    p0 = a0 / (be + a0)
    n = rng.binomial(N, p0, trials).astype(float)
    out = np.empty((len(t), trials))
    for k in range(len(t)):
        out[k] = n
        op = rng.binomial((N - n).astype(int), 1 - np.exp(-alpha[k] * dt))
        cl = rng.binomial(n.astype(int), 1 - np.exp(-be * dt))
        n = n + op - cl
    return out


fig = plt.figure(figsize=(10.4, 4.6))
gs = fig.add_gridspec(2, 2, width_ratios=[1.6, 1], hspace=0.55, wspace=0.28, left=0.07, right=0.98, bottom=0.12, top=0.92)
ax = fig.add_subplot(gs[0, 0])
one = simulate(1, 3)
for j in range(3):
    ax.step(t, one[:, j] + 1.3 * (2 - j), where="post", color=charts.line("channel"), lw=1.0)
ax.axvline(0, color=P.muted(), lw=0.7, ls=":")
ax.set_yticks([0.0, 1.0, 1.3, 2.3, 2.6, 3.6]); ax.set_yticklabels(["C", "O", "C", "O", "C", "O"])
charts.style_axes(ax, "t / ms", "")
charts.title(ax, "A  One channel, three trials")

ax = fig.add_subplot(gs[1, 0])
p = np.where(t < 0, a0 / (be + a0), a1 / (be + a1) + (a0 / (be + a0) - a1 / (be + a1)) * np.exp(-(be + a1) * t))
for N, tok in [(10, "negative"), (100, "highlight"), (1000, "neuron")]:
    x = simulate(N, 1)[:, 0] / N
    ax.plot(t, x, color=charts.line(tok), lw=0.9, label=f"N = {N}")
ax.plot(t, p, color=P.ink(), lw=1.4, label="master equation")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "t / ms", "fraction open")
charts.title(ax, "B  Many channels: the mean current emerges")

N = 200
x = simulate(N, 300)
m = x.mean(1); v = x.var(1)
sel = t >= 0
ax = fig.add_subplot(gs[:, 1])
ax.plot(m[sel] / N, v[sel] / N, ".", ms=2.5, color=charts.line("channel"), alpha=0.6, label="simulation")
pp = np.linspace(0, 1, 100)
ax.plot(pp, pp * (1 - pp), color=P.ink(), lw=1.4, label="$p(1-p)$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "mean open fraction $p$", "variance / N (in units of $i^2$)")
charts.title(ax, "C  Variance versus mean")
