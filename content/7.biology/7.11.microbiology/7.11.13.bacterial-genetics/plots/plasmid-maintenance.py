# Population biology of a conjugative plasmid in a chemostat (a model in the spirit of Stewart and Levin 1977).
# Plasmid-free cells F and plasmid-bearing cells P compete for one limiting resource R (Monod uptake);
# plasmid carriage lowers the growth rate by the cost c, a fraction lam of divisions of P cells loses the
# plasmid (segregation), and conjugation converts F into P at rate gamma F P (mass action):
#   dR/dt = D (R0 - R) - e psi(R) (F + (1 - c) P)
#   dF/dt = psi(R) F + lam (1 - c) psi(R) P - gamma F P - D F
#   dP/dt = (1 - lam) (1 - c) psi(R) P + gamma F P - D P,     psi(R) = mu_max R / (K + R).
# Parameters (illustrative): mu_max = 1 per h, K = 1 ug/mL, R0 = 100 ug/mL, e = 1e-7 ug per cell, D = 0.2 per h,
# lam = 1e-3.
# A: a few plasmid-bearing cells (1e3 per mL) enter a resident population at equilibrium (c = 0.05):
#    without conjugation, or with transfer too slow, the plasmid is lost; above the threshold it spreads like
#    an infection and persists with plasmid-free segregants.
# B: outcome after 10 000 h (near equilibrium) across transfer rate constants and costs; the dashed line is the invasion
#    condition gamma F* = D [1 - (1 - c)(1 - lam)], obtained by requiring that rare P cells increase.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
mu, K, R0, e, D, lam = 1.0, 1.0, 100.0, 1e-7, 0.2, 1e-3
Rs = K * D / (mu - D)
Fs = (R0 - Rs) / e


def run(gamma, c, T=10000.0, P0=1e3):
    def f(_, u):
        R, F, Pp = np.maximum(u, 0.0)
        psi = mu * R / (K + R)
        g = gamma * F * Pp
        return [D * (R0 - R) - e * psi * (F + (1 - c) * Pp),
                psi * F + lam * (1 - c) * psi * Pp - g - D * F,
                (1 - lam) * (1 - c) * psi * Pp + g - D * Pp]

    return solve_ivp(f, (0, T), [Rs, Fs, P0], method="LSODA", rtol=1e-7, atol=[1e-9, 1e-3, 1e-3],
                     dense_output=False, max_step=50.0)


fig = plt.figure(figsize=(11.5, 4.3))
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.0], wspace=0.34)

ax = fig.add_subplot(gs[0, 0])
cases = [(0.0, "negative", "no conjugation"), (3e-12, "highlight", r"$\gamma = 3\times10^{-12}$ (below threshold)"),
         (1e-10, "positive", r"$\gamma = 10^{-10}$ mL h$^{-1}$")]
for gamma, tok, name in cases:
    sol = run(gamma, 0.05, T=400)
    ax.plot(sol.t, np.maximum(sol.y[2], 1e-2), color=charts.line(tok), lw=2.0, label=f"plasmid-bearing, {name}")
    if gamma == 1e-10:
        ax.plot(sol.t, np.maximum(sol.y[1], 1e-2), color=charts.line(tok), lw=1.2, ls="--", label="plasmid-free, same run")
ax.set_yscale("log")
ax.set_ylim(1, 3e9)
ax.set_xlim(0, 400)
ax.legend(fontsize=6.4, frameon=False, loc="lower right")
charts.style_axes(ax, "time / h", "cells per mL")
charts.title(ax, "A   Invasion of a costly plasmid (c = 0.05)")

ax = fig.add_subplot(gs[0, 1])
gams = np.logspace(-13, -8, 26)
costs = np.linspace(0.0, 0.3, 22)
frac = np.zeros((len(costs), len(gams)))
for i, c in enumerate(costs):
    for j, g in enumerate(gams):
        y = run(g, c).y[:, -1]
        frac[i, j] = y[2] / max(y[1] + y[2], 1.0)
pc = ax.pcolormesh(np.log10(gams), costs, frac, cmap="viridis", vmin=0, vmax=1, shading="nearest")
cb = fig.colorbar(pc, ax=ax, fraction=0.05, pad=0.03)
cb.set_label("plasmid-bearing fraction", fontsize=7, color=P.ink())
cb.ax.tick_params(labelsize=6.5, colors=P.muted(), labelcolor=P.ink())
cc = np.linspace(0, 0.3, 100)
ax.plot(np.log10(D * (1 - (1 - cc) * (1 - lam)) / Fs), cc, color="white", lw=1.4, ls="--")
ax.text(-11.7, 0.26, "plasmid lost", fontsize=7, color="white", ha="center")
ax.text(-9.0, 0.06, "plasmid spreads", fontsize=7, color="#1f2937", ha="center")
ax.text(-12.9, 0.2, "dashed: invasion threshold", fontsize=6.5, color="white", ha="left")
ax.set_xlim(-13, -8)
ax.set_ylim(0, 0.3)
charts.style_axes(ax, r"$\log_{10}$ conjugation rate constant $\gamma$ / (mL h$^{-1}$)", "cost of carriage $c$")
charts.title(ax, "B   Outcome after 10 000 h")
