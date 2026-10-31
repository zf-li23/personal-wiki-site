"""The birth-death process of mRNA (production k = 20, degradation gamma = 1 per molecule; time in
mRNA lifetimes), simulated with the Gillespie algorithm. A: five trajectories from m = 0 with the
exact mean k(1 - e^-t) and the band mean +- one standard deviation (the distribution is Poisson at
all times). B: stationary distribution from a long run against Poisson(20). C: waiting times between
production events (exponential, rate k) and between every fourth event (gamma, shape 4)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
k, g = 20.0, 1.0


def gillespie(m0, tmax):
    t, m = 0.0, m0
    ts, ms, births = [0.0], [m0], []
    while t < tmax:
        a1, a2 = k, g * m
        a0 = a1 + a2
        t += rng.exponential(1 / a0)
        if rng.random() < a1 / a0:
            m += 1
            births.append(t)
        else:
            m -= 1
        ts.append(t)
        ms.append(m)
    return np.array(ts), np.array(ms), np.array(births)


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.34, left=0.06, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
tt = np.linspace(0, 5, 200)
mean = k * (1 - np.exp(-tt))
ax.fill_between(tt, mean - np.sqrt(mean), mean + np.sqrt(mean), color=P.light("mrna"), lw=0)
for i in range(5):
    ts, ms, _ = gillespie(0, 5)
    ax.step(ts, ms, where="post", color=charts.line("mrna"), lw=0.7, alpha=0.8)
ax.plot(tt, mean, color=P.ink(), lw=1.4)
charts.style_axes(ax, r"time $\gamma t$", "mRNA number $m$")
charts.title(ax, "A  Relaxation from m = 0")

ax = axs[1]
ts, ms, births = gillespie(20, 4000)
dt = np.diff(ts)
w = np.bincount(ms[:-1], weights=dt)
w = w / w.sum()
n = np.arange(w.size)
ax.bar(n, w, width=0.85, color=P.fill("mrna"), edgecolor=P.edge("mrna"), lw=0.4, label="simulation")
nn = np.arange(0, 45)
ax.plot(nn, stats.poisson.pmf(nn, k / g), "o", ms=3, color=P.ink(), label="Poisson(k/γ)")
avg = np.sum(n * w)
var = np.sum(n ** 2 * w) - avg ** 2
ax.text(0.97, 0.95, f"Fano = {var / avg:.2f}", transform=ax.transAxes, ha="right", va="top",
        fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xlim(0, 45)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "m", "probability")
charts.title(ax, "B  Stationary distribution")

ax = axs[2]
wt = np.diff(births)
w4 = np.diff(births[::4])
bins = np.linspace(0, 0.5, 41)
ax.hist(wt, bins=bins, density=True, color=P.fill("mrna"), edgecolor=P.edge("mrna"), lw=0.3)
ax.hist(w4, bins=bins, density=True, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.3, alpha=0.7)
x = np.linspace(0, 0.5, 300)
ax.plot(x, stats.expon.pdf(x, scale=1 / k), color=charts.line("mrna"), lw=1.4, label="1st event: Exp(k)")
ax.plot(x, stats.gamma.pdf(x, 4, scale=1 / k), color=charts.line("protein"), lw=1.4, label="4th event: Γ(4, k)")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, r"waiting time $\gamma\tau$", "density")
charts.title(ax, "C  Waiting times")
