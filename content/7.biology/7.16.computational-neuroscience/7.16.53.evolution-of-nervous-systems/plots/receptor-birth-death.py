"""Birth-death evolution of a chemoreceptor gene family (odorant receptors of mammals).

Each intact gene duplicates at rate lam (birth) and becomes a pseudogene at rate mu (death);
pseudogenes are deleted at rate delta = 0.025 per Myr. Start: 780 intact genes and 150 pseudogenes,
about the repertoire inferred for the boreoeutherian ancestor (Niimura and Nei 2007), 90 Myr ago.
Rates (per Myr) chosen so that the final intact counts and pseudogene fractions are near the
approximate values for elephant (~2000 intact, many pseudogenes), mouse (~1100, ~20 %) and human
(~400, ~50 %) (Niimura, Matsui and Touhara 2014).
Simulated by tau-leaping (Poisson numbers of events per 0.1 Myr step).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
T, dt, delta = 90.0, 0.1, 0.025
N0, PS0 = 780, 150
REGIMES = [("elephant-like: high turnover, net gain", 0.035, 0.0248, "positive"),
           ("mouse-like: slow net gain", 0.012, 0.0079, "dna"),
           ("human-like: net loss", 0.012, 0.0194, "negative")]
steps = int(round(T / dt))
t = np.arange(steps + 1) * dt


def simulate(lam, mu, reps):
    n = np.full(reps, N0, dtype=np.int64)
    ps = np.full(reps, PS0, dtype=np.int64)
    out_n = np.empty((steps + 1, reps))
    out_p = np.empty((steps + 1, reps))
    out_n[0], out_p[0] = n, ps
    for k in range(steps):
        births = rng.poisson(lam * n * dt)
        deaths = np.minimum(rng.poisson(mu * n * dt), n)
        dels = np.minimum(rng.poisson(delta * ps * dt), ps)
        n = n + births - deaths
        ps = ps + deaths - dels
        out_n[k + 1], out_p[k + 1] = n, ps
    return out_n, out_p


fig, axs = plt.subplots(1, 3, figsize=(13.5, 3.9))
finals = []
for name, lam, mu, tok in REGIMES:
    n, ps = simulate(lam, mu, 400)
    col = P.edge(tok)
    for j in range(8):
        axs[0].plot(t - T, n[:, j], color=col, lw=0.6, alpha=0.6)
    axs[0].plot(t - T, N0 * np.exp((lam - mu) * t), color=col, lw=1.8, ls="--", label=name)
    frac = ps / (n + ps)
    axs[1].plot(t - T, 100 * frac.mean(axis=1), color=col, lw=1.8, label=name.split(":")[0])
    finals.append((name.split(":")[0], n[-1], col, lam, mu))

ax = axs[0]
ax.set_xlabel("Time / Myr (0 = present)")
ax.set_ylabel("Intact receptor genes")
ax.set_title("A  Family size (8 lineages each, mean dashed)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.2, loc="upper left")
ax.grid(True, alpha=0.3)

ax = axs[1]
ax.set_xlabel("Time / Myr (0 = present)")
ax.set_ylabel("Pseudogenes / % of family")
ax.set_title("B  Pseudogene fraction", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_ylim(0, 70)
ax.grid(True, alpha=0.3)

ax = axs[2]
bins = np.linspace(0, 3200, 65)
for name, fin, col, lam, mu in finals:
    ax.hist(fin, bins=bins, color=col, alpha=0.55, label=name)


    ax.axvline(fin.mean(), color=col, lw=0.8, ls=":")
ax.set_xlabel("Intact genes at present (400 lineages)")
ax.set_ylabel("Number of lineages")
ax.set_title("C  Spread among replicate lineages", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5, loc="center right")
fig.tight_layout()
