# What a single enzyme molecule shows that the ensemble hides (simulated turnover of a fluorogenic enzyme
# cycling E (fluorescent) -> ES -> E* (dark) -> E, as for cholesterol oxidase with its FAD cofactor).
# Scheme: bright state E binds substrate with pseudo-first-order rate k1 = 20 /s, then turns over with
# k2 = 30 /s into the dark state; the dark state returns with k3 = 10 /s. Photon counts in 1 ms bins.
# A: a fluorescence trace: on and off periods of random length. B: distribution of on times; because leaving
# the on state requires two sequential steps (binding, then chemistry), the distribution rises and then decays,
# f(t) = k1 k2/(k2 - k1) (exp(-k1 t) - exp(-k2 t)), unlike a single exponential. C: the ensemble average of
# 2000 unsynchronized molecules started together: a smooth relaxation that hides both steps.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
k1, k2, k3 = 20.0, 30.0, 10.0


def trajectory(T):
    t, state, times, states = 0.0, 0, [0.0], [0]
    rates = (k1, k2, k3)
    while t < T:
        t += rng.exponential(1 / rates[state])
        state = (state + 1) % 3
        times.append(t)
        states.append(state)
    return np.array(times), np.array(states)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0), gridspec_kw={"width_ratios": [1.5, 1, 1]})
times, states = trajectory(2.0)
dt = 1e-3
grid = np.arange(0, 2.0, dt)
idx = np.searchsorted(times, grid, side="right") - 1
bright = states[idx] < 2                     # E and ES are fluorescent, E* is dark
counts = rng.poisson(np.where(bright, 25.0, 2.0))
axs[0].plot(grid, counts, color=charts.line("dna"), lw=0.6)
axs[0].set_xlim(0, 1.0)
charts.style_axes(axs[0], "time / s", "photons per ms")
charts.title(axs[0], "A   One molecule: stochastic on-off cycles")

times, states = trajectory(4000.0)
dur = np.diff(times)
# on period = time in E plus time in ES (both bright)
on = dur[:-1][states[:-2] == 0] + dur[1:][states[:-2] == 0]
h, edges = np.histogram(on, bins=60, range=(0, 0.3), density=True)
c = 0.5 * (edges[1:] + edges[:-1])
axs[1].bar(c, h, width=edges[1] - edges[0], color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
tt = np.linspace(0, 0.3, 300)
axs[1].plot(tt, k1 * k2 / (k2 - k1) * (np.exp(-k1 * tt) - np.exp(-k2 * tt)), color=charts.line("negative"), lw=1.6,
            label="two-step theory")
km = 1 / on.mean()
axs[1].plot(tt, km * np.exp(-km * tt), color=P.muted(), lw=1.2, ls="--", label="single exponential, same mean")
axs[1].legend(fontsize=7.5, frameon=False)
charts.style_axes(axs[1], "on time / s", "probability density / s⁻¹")
charts.title(axs[1], "B   Dwell times reveal hidden steps")

N, T = 2000, 0.6
grid = np.linspace(0, T, 300)
frac = np.zeros_like(grid)
for _ in range(N):
    tm, st = trajectory(T)
    frac += st[np.searchsorted(tm, grid, side="right") - 1] < 2
axs[2].plot(grid, frac / N, color=charts.line("dna"), lw=1.8)
axs[2].axhline((1 / k1 + 1 / k2) / (1 / k1 + 1 / k2 + 1 / k3), color=P.muted(), lw=0.8, ls=":")
axs[2].set_ylim(0, 1.05)
charts.style_axes(axs[2], "time / s", "fraction fluorescent")
charts.title(axs[2], "C   The ensemble: a smooth average")
fig.tight_layout()
