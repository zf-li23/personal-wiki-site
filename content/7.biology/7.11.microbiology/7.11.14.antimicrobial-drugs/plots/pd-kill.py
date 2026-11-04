# Pharmacodynamic function (Regoes et al. 2004): net growth rate of a bacterial population at a
# constant drug concentration c,
#   psi(c) = psi_max - (psi_max - psi_min) (c/MIC)^kappa / ((c/MIC)^kappa - psi_min/psi_max),
# a Hill-type (sigmoid) curve that crosses zero at the MIC. psi_max = 1.0 per h (growth without drug);
# psi_min is the maximal killing rate; kappa (Hill coefficient) sets the steepness.
# Illustrative parameter sets: a "time-dependent" drug (steep, kappa = 4, psi_min = -2 per h: killing
# saturates just above the MIC), a "concentration-dependent" drug (shallow, kappa = 1, psi_min = -6 per h:
# killing keeps increasing over a wide range), and a bacteriostatic drug (psi_min = -0.1 per h).
# A: psi(c). B, C: time-kill curves N(t) = N0 exp(psi(c) t) at multiples of the MIC, with a detection
# limit of 10 CFU/mL.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
pmax = 1.0


def psi(c, pmin, kappa):
    x = (c) ** kappa  # c in units of the MIC
    return pmax - (pmax - pmin) * x / (x - pmin / pmax)


drugs = [
    ("time-dependent (κ = 4)", -2.0, 4.0, "drug"),
    ("concentration-dependent (κ = 1)", -6.0, 1.0, "dna"),
    ("bacteriostatic", -0.1, 2.0, "neutral"),
]
fig = plt.figure(figsize=(13.5, 4.1))
gs = fig.add_gridspec(1, 3, wspace=0.32)
ax = fig.add_subplot(gs[0, 0])
c = np.logspace(-2, 2.3, 400)
for name, pmin, k, tok in drugs:
    ax.plot(c, psi(c, pmin, k), color=charts.line(tok), lw=1.8, label=name)
ax.axhline(0, color=P.muted(), lw=0.7)
ax.axvline(1, color=P.muted(), lw=0.7, ls="--")
ax.text(1.12, 0.75, "MIC", fontsize=7.5, color=P.muted())
ax.set_xscale("log")
ax.set_ylim(-6.5, 1.5)
ax.legend(fontsize=7, frameon=False, loc="lower left", labelcolor=P.ink())
charts.style_axes(ax, "concentration / MIC", "net growth rate $\\psi$ / h$^{-1}$")
charts.title(ax, "A   Pharmacodynamic function")

t = np.linspace(0, 6, 200)
mult = [0.25, 0.5, 1, 2, 4, 16, 64]
shades = np.linspace(0.75, 0.0, len(mult))
for j, (name, pmin, k, tok) in enumerate(drugs[:2]):
    ax = fig.add_subplot(gs[0, j + 1])
    for m, s in zip(mult, shades):
        N = 1e6 * np.exp(psi(m, pmin, k) * t)
        N = np.where(N < 10, np.nan, N)
        ax.plot(t, N, color=P.mix(charts.line(tok), P.surface(), s * 0.8), lw=1.5)
        last = np.nanmax(np.where(np.isnan(N), -1, np.arange(len(t))))
        labels = {0.25: "0.25×", 1: "1×", 2: "2×", 16: "4-64×"} if j == 0 else {0.25: "0.25×", 1: "1×", 4: "4×", 64: "64×"}
        if m in labels:
            ax.text(t[int(last)] + 0.08 if last < len(t) - 1 else 6.05, N[int(last)], labels[m], fontsize=6.8,
                    color=P.ink(), va="center")
    ax.axhline(10, color=P.muted(), lw=0.6, ls=":")
    ax.set_yscale("log")
    ax.set_ylim(5, 1e9)
    ax.set_xlim(0, 6.6)
    charts.style_axes(ax, "time / h", "viable cells / (CFU mL$^{-1}$)" if j == 0 else None)
    charts.title(ax, ("B   " if j == 0 else "C   ") + name.split(" (")[0])
