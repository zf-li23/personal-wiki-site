"""Decoding a circular stimulus from a Poisson population: ML versus population vector.

N neurons with preferred directions evenly spaced on the circle, von Mises tuning
f_i(s) = r0 + A exp(kappa (cos(s - s_i) - 1)) with r0 = 2, A = 20 (mean spike counts in the
decoding window), independent Poisson counts. ML decoder: maximise sum_i n_i ln f_i(s) - sum_i f_i(s)
over a grid of 720 values; population vector: direction of sum_i n_i (cos s_i, sin s_i).
A: tuning curves of 12 of the neurons. B: root-mean-square error of the two decoders against N
(2000 random stimuli per N) and the Cramer-Rao bound 1/sqrt(I_F), I_F = sum_i f_i'^2 / f_i.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
r0, A, kap = 2.0, 20.0, 2.0
grid = np.linspace(-np.pi, np.pi, 720, endpoint=False)


def tuning(s, pref):
    return r0 + A * np.exp(kap * (np.cos(s[..., None] - pref) - 1))


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1), gridspec_kw={"width_ratios": [1, 1.1]})
ax = axs[0]
ss = np.linspace(-np.pi, np.pi, 400)
pref = np.linspace(-np.pi, np.pi, 12, endpoint=False)
for k, p in enumerate(pref):
    ax.plot(np.degrees(ss), tuning(ss, p), color=P.edge("dna") if k % 3 else P.edge("rna"), lw=1.3)
ax.set_xlabel("Stimulus direction / deg")
ax.set_ylabel("Mean spike count")
ax.set_xlim(-180, 180)
ax.set_title("A  Tuning curves (12 of N neurons)", loc="left", fontsize=10)

ax = axs[1]
Ns = np.array([4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128])
ml, pv, cr = [], [], []
for N in Ns:
    pref = np.linspace(-np.pi, np.pi, N, endpoint=False)
    s = rng.uniform(-np.pi, np.pi, 2000)
    n = rng.poisson(tuning(s, pref))
    ll = n @ np.log(tuning(grid, pref)).T - tuning(grid, pref).sum(1)
    sh = grid[np.argmax(ll, axis=1)]
    sp = np.arctan2(n @ np.sin(pref), n @ np.cos(pref))
    ml.append(np.sqrt(np.mean(wrap(sh - s) ** 2)))
    pv.append(np.sqrt(np.mean(wrap(sp - s) ** 2)))
    sg = np.linspace(-np.pi, np.pi, 200)
    f = tuning(sg, pref)
    df = -A * kap * np.sin(sg[:, None] - pref) * np.exp(kap * (np.cos(sg[:, None] - pref) - 1))
    cr.append(np.mean(1 / np.sqrt((df ** 2 / f).sum(1))))
d = np.degrees
ax.loglog(Ns, d(pv), "s-", color=P.edge("rna"), lw=1.8, ms=4, label="population vector")
ax.loglog(Ns, d(ml), "o-", color=P.edge("dna"), lw=1.8, ms=4, label="maximum likelihood")
ax.loglog(Ns, d(cr), "--", color=P.ink(), lw=1.3, label="Cramer-Rao bound")
ax.set_xlabel("Number of neurons N")
ax.set_ylabel("RMS error / deg")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Decoding error", loc="left", fontsize=10)
fig.tight_layout()
