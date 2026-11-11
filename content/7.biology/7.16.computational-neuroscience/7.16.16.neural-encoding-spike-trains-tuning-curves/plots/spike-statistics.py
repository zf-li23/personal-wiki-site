"""Interspike-interval statistics and Fano factors of three renewal processes with the same rate (20 Hz).

1. Poisson: exponential ISIs, C_V = 1.
2. Poisson with an absolute refractory period tau_ref = 10 ms (dead time): ISI = tau_ref + Exp,
   C_V = 1 - r tau_ref = 0.8.
3. Gamma process of order 4: ISI ~ Gamma(4, 4r), C_V = 1/2.
A: ISI histograms (simulated) with the theoretical densities. B: Fano factor of spike counts against
counting window T; for a renewal process F(T) tends to C_V^2 for long windows.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

import wikibio as bio

P = bio.P
rng = np.random.default_rng(2)
r, tref, N = 20.0, 0.010, 200000
procs = {
    "Poisson ($C_V$ = 1)": rng.exponential(1 / r, N),
    "dead time 10 ms ($C_V$ = 0.8)": tref + rng.exponential(1 / r - tref, N),
    "gamma, order 4 ($C_V$ = 0.5)": rng.gamma(4, 1 / (4 * r), N),
}
dens = [lambda x: r * np.exp(-r * x),
        lambda x: np.where(x > tref, np.exp(-(x - tref) / (1 / r - tref)) / (1 / r - tref), 0),
        lambda x: stats.gamma.pdf(x, 4, scale=1 / (4 * r))]
cols = [P.edge("dna"), P.edge("rna"), P.edge("positive")]

fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
x = np.linspace(0, 0.25, 500)
bins = np.arange(0, 0.25, 0.004)
for (lab, isi), d, c in zip(procs.items(), dens, cols):
    ax.hist(isi, bins=bins, density=True, histtype="step", color=c, lw=1.0)
    ax.plot(x, d(x), color=c, lw=1.8, label=lab)
ax.set_xlabel("Interspike interval / s")
ax.set_ylabel("Probability density / s$^{-1}$")
ax.set_xlim(0, 0.25)
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  ISI distributions (rate 20 Hz)", loc="left", fontsize=10)

bx = axs[1]
Ts = np.logspace(-2.3, 0.5, 22)
for (lab, isi), c, cv in zip(procs.items(), cols, (1.0, 0.8, 0.5)):
    st = np.cumsum(isi)
    F = []
    for Tw in Ts:
        nwin = int(st[-1] // Tw)
        cnt = np.bincount((st // Tw).astype(int), minlength=nwin + 1)[:nwin]
        F.append(cnt.var() / cnt.mean())
    bx.plot(Ts, F, "o-", ms=3.5, color=c, lw=1.4, label=lab)
    bx.axhline(cv ** 2, color=c, lw=0.8, ls=":")
bx.set_xscale("log")
bx.set_xlabel("Counting window T / s")
bx.set_ylabel("Fano factor F = Var(n) / E[n]")
bx.set_ylim(0, 1.15)
bx.text(0.006, 0.22, "dotted: C$_V^2$", fontsize=8, color=P.muted())
bx.set_title("B  Fano factor approaches C$_V^2$ for long windows", loc="left", fontsize=10)
fig.tight_layout()
