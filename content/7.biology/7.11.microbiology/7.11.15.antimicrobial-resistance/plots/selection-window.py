# Selection of resistance by drug concentration (model).
# Net growth rates follow the pharmacodynamic function of Regoes et al. (2004) (see 7.11.14):
# wild type: psi_max = 1.0 per h, MIC = 1, psi_min = -3 per h, kappa = 2;
# first-step resistant mutant: fitness cost 10 % (psi_max = 0.9 per h), MIC = 8 (taken as the
# mutant prevention concentration, MPC), same psi_min and kappa.
# A: growth rates and the selection coefficient s = psi_mut - psi_wt. The mutant is favoured above the
#    minimal selective concentration (MSC), which lies below the wild-type MIC; between the MIC and the
#    MPC lies the mutant selection window. Above the MPC both are killed.
# B, C: one-compartment pharmacokinetics (elimination half-life 2 h, a dose every 8 h, instantaneous
#    absorption), with peak concentrations 3 x MIC (B: troughs sit in the window) and 40 x MIC
#    (C: concentration stays above the MPC for most of the interval). Populations start with 1e9 wild-type
#    cells and 10 resistant mutants; dashed: mutants, solid: wild type; detection limit 1 cell; populations
#    are capped at 1e10 cells (carrying capacity). Shaded: drug concentration (right axis) and the window.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P


def psi(c, pmax, mic, pmin=-3.0, kappa=2.0):
    x = (np.asarray(c) / mic) ** kappa
    return pmax - (pmax - pmin) * x / (x - pmin / pmax)


wt = dict(pmax=1.0, mic=1.0)
mu = dict(pmax=0.9, mic=8.0)
msc = brentq(lambda c: psi(c, **mu) - psi(c, **wt), 1e-3, 0.99)

fig = plt.figure(figsize=(14.0, 4.3))
gs = fig.add_gridspec(1, 3, wspace=0.3)
ax = fig.add_subplot(gs[0, 0])
c = np.logspace(-2, 2, 500)
ax.axvspan(msc, 1, color=P.mix(P.fill("highlight"), P.surface(), 0.75), lw=0)
ax.axvspan(1, 8, color=P.mix(P.fill("negative"), P.surface(), 0.8), lw=0)
ax.plot(c, psi(c, **wt), color=charts.line("bacterium"), lw=1.8, label="wild type")
ax.plot(c, psi(c, **mu), color=charts.line("negative"), lw=1.8, ls="--", label="resistant mutant")
ax.plot(c, psi(c, **mu) - psi(c, **wt), color=P.ink(), lw=1.0, ls=":", label="selection coefficient s")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xscale("log")
ax.set_ylim(-3.3, 2.3)
for x, txt in ((msc, "MSC"), (1, "MIC"), (8, "MPC")):
    ax.text(x, 2.0, txt, ha="center", fontsize=7, color=P.ink())
ax.legend(fontsize=6.8, frameon=False, loc="lower left", labelcolor=P.ink())
charts.style_axes(ax, "concentration / wild-type MIC", "net growth rate / h$^{-1}$")
charts.title(ax, "A   Selective windows")

kel = np.log(2) / 2.0
tau = 8.0
T = np.linspace(0, 48, 1200)


def conc(t, peak):
    out = 0.0
    for j in range(7):
        dt = np.asarray(t) - j * tau
        out = out + np.where(dt >= 0, peak * np.exp(-kel * dt), 0.0)
    return out


for j, peak in enumerate((3.0, 40.0)):
    ax = fig.add_subplot(gs[0, j + 1])

    def rhs_log(t, z):
        cc = conc(t, peak)
        return [psi(cc, **wt), psi(cc, **mu)]

    sol = solve_ivp(rhs_log, (0, 48), [np.log(1e9), np.log(10.0)], t_eval=T, max_step=0.05)
    Nw = np.exp(np.minimum(sol.y[0], np.log(1e10)))
    Nm = np.exp(np.minimum(sol.y[1], np.log(1e10)))
    ax2 = ax.twinx()
    ax2.fill_between(T, 0.05, conc(T, peak), color=P.mix(P.fill("drug"), P.surface(), 0.75), lw=0, zorder=0)
    ax2.plot(T, conc(T, peak), color=charts.line("drug"), lw=0.8, zorder=0.5)
    ax2.text(47, 3.0, "window", ha="right", fontsize=6.8, color=P.muted())
    ax2.axhspan(1, 8, color=P.mix(P.fill("negative"), P.surface(), 0.85), lw=0, zorder=0)
    ax2.set_yscale("log")
    ax2.set_ylim(0.05, 500)
    charts.style_axes(ax2, None, "drug / wild-type MIC" if j == 1 else None)
    ax2.spines["right"].set_visible(True)
    ax.set_zorder(ax2.get_zorder() + 1)
    ax.patch.set_visible(False)
    ax.plot(T, np.where(Nw >= 1, Nw, np.nan), color=charts.line("bacterium"), lw=1.8, label="wild type")
    ax.plot(T, np.where(Nm >= 1, Nm, np.nan), color=charts.line("negative"), lw=1.8, ls="--", label="mutant")
    ax.set_yscale("log")
    ax.set_ylim(1, 1e11)
    ax.set_xlim(0, 48)
    charts.style_axes(ax, "time / h", "cells" if j == 0 else None)
    charts.title(ax, ("B   peak 3 × MIC: mutant selected" if j == 0 else "C   peak 40 × MIC: both cleared"))
    if j == 0:
        ax.legend(fontsize=6.8, frameon=False, loc="lower left", labelcolor=P.ink())
