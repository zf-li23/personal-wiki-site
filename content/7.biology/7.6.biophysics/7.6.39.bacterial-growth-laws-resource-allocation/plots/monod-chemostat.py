# Monod's growth law and the chemostat. A: growth rate against substrate concentration,
# lambda = lambda_max s / (K_s + s), with lambda_max = 1.0 per hour and K_s = 0.1 mM, in linear and
# (inset-free) logarithmic form: half-maximal growth at s = K_s. B: steady states of a chemostat fed
# with s_0 = 5 mM at dilution rate D (yield Y = 0.5 g dry mass per g, glucose 0.18 g per mmol): the
# residual substrate s* = K_s D / (lambda_max - D) is set by D alone, the biomass x* = Y (s_0 - s*)
# falls to zero at washout, D_c = lambda_max s_0 / (K_s + s_0); productivity D x* peaks just below washout.
# C: approach to steady state after inoculation (numerical solution) at D = 0.5 per hour.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
lmax, Ks, s0, Y = 1.0, 0.1, 5.0, 0.5 * 0.18  # Y in g/L biomass per mM substrate

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
s = np.logspace(-3, 1.5, 300)
ax.plot(s, lmax * s / (Ks + s), color=charts.line("bacterium"), lw=2.0)
ax.axvline(Ks, color=P.muted(), lw=0.7, ls=":")
ax.axhline(lmax / 2, color=P.muted(), lw=0.7, ls=":")
ax.text(Ks * 1.15, 0.05, "$K_s$", fontsize=8, color=P.ink())
ax.set_xscale("log")
charts.style_axes(ax, "substrate $s$ / mM", "growth rate $\\lambda$ / h$^{-1}$")
charts.title(ax, "A   Monod's law")

ax = axs[1]
Dc = lmax * s0 / (Ks + s0)
D = np.linspace(0.01, Dc * 0.9999, 400)
ss = Ks * D / (lmax - D)
xs = Y * (s0 - ss)
ax.plot(D, xs, color=charts.line("bacterium"), lw=2.0, label="biomass $x^*$ / (g L$^{-1}$)")
ax.plot(D, D * xs, color=charts.line("enzyme"), lw=1.6, label="productivity $Dx^*$ / (g L$^{-1}$ h$^{-1}$)")
ax2 = ax.twinx()
ax2.plot(D, ss, color=charts.line("metabolite"), lw=1.6, ls="--")
ax2.set_yscale("log")
charts.style_axes(ax2, None, "residual substrate $s^*$ / mM (dashed)")
ax2.spines["right"].set_visible(True)
ax.axvline(Dc, color=P.muted(), lw=0.7)
ax.text(Dc - 0.02, 0.05, "washout", rotation=90, ha="right", fontsize=7.5, color=P.ink())
ax.legend(fontsize=7.5, frameon=False, loc="center left")
charts.style_axes(ax, "dilution rate $D$ / h$^{-1}$", "steady state")
charts.title(ax, "B   The chemostat sets the growth rate")

ax = axs[2]
Dv = 0.5


def rhs(t, y):
    x, sub = y
    lam = lmax * sub / (Ks + sub)
    return [(lam - Dv) * x, Dv * (s0 - sub) - lam * x / Y]


sol = solve_ivp(rhs, (0, 40), [0.001, s0], max_step=0.05)
xst = Y * (s0 - Ks * Dv / (lmax - Dv))
ax.plot(sol.t, sol.y[0] / xst, color=charts.line("bacterium"), lw=2.0, label="biomass $x/x^*$")
ax.plot(sol.t, sol.y[1] / s0, color=charts.line("metabolite"), lw=1.6, ls="--", label="substrate $s/s_0$")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "time / h", "relative value")
charts.title(ax, "C   Inoculation at $D$ = 0.5 h$^{-1}$")
fig.tight_layout()
