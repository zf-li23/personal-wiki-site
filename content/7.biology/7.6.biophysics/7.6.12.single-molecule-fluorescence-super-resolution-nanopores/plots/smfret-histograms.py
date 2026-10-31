# Single-molecule FRET histograms of freely diffusing molecules (simulated bursts).
# Two conformations with E = 0.30 and E = 0.75, equal populations. Each burst lasts a random time
# (exponential, mean 1 ms) and contains a Poisson number of photons (rate 100 per ms, bursts with fewer than
# 40 photons discarded); each photon is an acceptor photon with probability equal to the instantaneous E.
# A: static (no interconversion during bursts): two peaks whose widths match the shot-noise limit
#    sqrt(E (1 - E) / N). B: fast exchange (k = 2e4 /s each way, much faster than the burst): one peak at the
#    average E. C: exchange on the burst time scale (k = 1e3 /s): a broad distribution filling the space
#    between the states, wider than shot noise, which signals dynamics.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
E1, E2 = 0.30, 0.75


def bursts(k, nb=5000, rate=100.0):
    out, nph = [], []
    for _ in range(nb):
        T = rng.exponential(1.0)
        n = rng.poisson(rate * T)
        if n < 40:
            continue
        ts = np.sort(rng.uniform(0, T, n))
        state = rng.integers(2)
        if k == 0:
            st = np.full(n, state)
        else:
            # telegraph process sampled at photon times (rates in 1/ms)
            t, switches = 0.0, []
            while t < T:
                t += rng.exponential(1 / k)
                switches.append(t)
            st = (state + np.searchsorted(np.array(switches), ts)) % 2
        E = np.where(st == 0, E1, E2)
        nA = np.sum(rng.random(n) < E)
        out.append(nA / n)
        nph.append(n)
    return np.array(out), np.array(nph)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0), sharey=True)
for ax, (k, title) in zip(axs, ((0, "A   Static: two shot-noise-limited peaks"),
                                (20.0, "B   Fast exchange: one averaged peak"),
                                (1.0, "C   Exchange during bursts: broadening"))):
    E, n = bursts(k)
    ax.hist(E, bins=50, range=(0, 1), density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
    # shot-noise-limited prediction for the static case, using the actual photon numbers
    grid = np.linspace(0, 1, 400)
    means = (E1, E2) if k == 0 else ((E1 + E2) / 2,)
    pred = np.zeros_like(grid)
    for m in means:
        for nn in rng.choice(n, 400):
            sd = np.sqrt(m * (1 - m) / nn)
            pred += np.exp(-(grid - m) ** 2 / (2 * sd**2)) / (np.sqrt(2 * np.pi) * sd)
    pred /= 400 * len(means)
    ax.plot(grid, pred, color=charts.line("negative"), lw=1.4, label="shot-noise limit")
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    charts.style_axes(ax, "FRET efficiency E", "probability density" if k == 0 else None)
    charts.title(ax, title)
fig.tight_layout()
