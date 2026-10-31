# Two optimization problems of bacterial physiology.
# A: the cost and benefit of the lac proteins (Dekel and Alon 2005). Relative growth rate
# 1 - eta(Z) + b(Z) against the expression level Z (1 = fully induced wild type), with cost
# eta(Z) = eta_0 Z / (1 - Z/M) (eta_0 = 0.02, M = 1.8) and benefit b(Z) = delta Z L/(K + L)
# (delta = 0.17, K = 0.4 mM) for several lactose concentrations L; circles mark the optimal expression.
# B: overflow metabolism from proteome allocation (after Basan and colleagues 2015). Energy demand
# e lambda must be met by respiration (proteome cost 1/eps_r per unit energy flux, high yield) or
# fermentation (cost 1/eps_f = 1/(2 eps_r), low yield); the energy sectors share the proteome left by
# the biomass sector, phi_max - b lambda. Minimizing carbon uptake gives pure respiration below
# lambda_c and a mixed strategy above it, in which fermentation (acetate excretion) rises linearly.
# Parameters: e = 1, phi_max = 0.5, b = 0.3 h, eps_r = 2.79 per hour, giving lambda_c = 0.76 per hour.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
eta0, Mz, delta, Kl = 0.02, 1.8, 0.17, 0.4
Z = np.linspace(0, 1.6, 400)
cost = eta0 * Z / (1 - Z / Mz)
for L, tok in ((0.0, "neutral"), (0.1, "rna"), (0.5, "atp"), (2.0, "enzyme"), (5.0, "dna")):
    w = 1 - cost + delta * Z * L / (Kl + L)
    ax.plot(Z, w, color=charts.line(tok), lw=1.8, label=f"lactose {L} mM")
    i = np.argmax(w)
    ax.plot([Z[i]], [w[i]], "o", ms=6, color=charts.line(tok))
ax.axhline(1, color=P.muted(), lw=0.6)
ax.axvline(1, color=P.muted(), lw=0.6, ls=":")
ax.text(1.02, 0.82, "wild-type\nfull induction", fontsize=7.5, color=P.ink())
ax.set_ylim(0.8, 1.18)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "lac expression $Z$ (relative to wild type)", "relative growth rate")
charts.title(ax, "A   An optimal expression level")

ax = axs[1]
e, phimax, b, er = 1.0, 0.5, 0.3, 2.79
ef = 2 * er
lam = np.linspace(0, 1.04, 300)
lc = phimax / (e / er + b)
Jf = np.where(lam <= lc, 0.0, (e * lam / er - (phimax - b * lam)) / (1 / er - 1 / ef))
Jr = e * lam - Jf
ax.plot(lam, Jr, color=charts.line("mitochondrion"), lw=1.8, label="respiration flux")
ax.plot(lam, Jf, color=charts.line("negative"), lw=2.0, label="fermentation flux (acetate)")
ax.plot(lam, Jr / er + Jf / ef + b * lam, color=P.muted(), lw=1.0, ls="--", label="proteome used (energy + biomass)")
ax.axvline(lc, color=P.muted(), lw=0.6)
ax.text(lc + 0.01, 0.95, "$\\lambda_c$", fontsize=8, color=P.ink())
ax.set_ylim(0, 1.1)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "growth rate $\\lambda$ / h$^{-1}$", "energy flux (units of $e\\lambda$) / proteome fraction")
charts.title(ax, "B   Overflow: proteome-cheap fermentation")
fig.tight_layout()
