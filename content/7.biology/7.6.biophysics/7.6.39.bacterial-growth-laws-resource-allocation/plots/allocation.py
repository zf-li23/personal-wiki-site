# Proteome allocation as an optimization, and a regulation that finds the optimum.
# A: the two capacity constraints of Formula 39.2.2 in the plane of ribosomal fraction phi_R (as
# RNA/protein, r) and growth rate: lambda <= kappa_t (phi_R - phi_0) (translation, rising line) and
# lambda <= kappa_n (phi_max - phi_R) (nutrient supply, falling lines for three media); the feasible
# region lies below both, and growth is fastest at their intersection (circles).
# B, C: a dynamic model with an amino-acid pool a (per unit protein): translation
# lambda = kappa_t a/(a + K) (phi_R - phi_0), da/dt = kappa_n (phi_max - phi_R) - lambda (1 + a),
# d phi_R/dt = lambda (chi_R - phi_R), where chi_R is the fraction of new protein that is ribosomal.
# With "flux-controlled" regulation chi_R = phi_0 + (phi_max - phi_0) a/(a + K_chi) (the pool, sensed
# through charged tRNA and ppGpp, sets ribosome synthesis), the steady state lies within 1 % of the best
# possible growth in every medium (B). C: nutrient upshift from kappa_n = 0.6 to 3 per hour at t = 0:
# with regulation the cell reallocates and reaches the new optimum; with chi_R frozen at its preshift
# value, growth stays slow. Parameters: kappa_t = 4.5 per hour, phi_0 = 0.087, phi_max = 0.65,
# K = 0.05, K_chi = 0.3.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

import wikibio as bio
from wikibio import charts

P = bio.P
kt, phi0, phimax, K, Kc = 4.5, 0.087, 0.65, 0.05, 0.3

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
x = np.linspace(0, 0.7, 200)
ax.plot(x, kt * (x - phi0), color=P.ink(), lw=1.6, label="translation: $\\kappa_t(\\phi_R - \\phi_0)$")
for kn, tok in ((0.6, "rna"), (1.5, "enzyme"), (3.0, "dna")):
    ax.plot(x, kn * (phimax - x), color=charts.line(tok), lw=1.6, label=f"nutrients, $\\kappa_n$ = {kn} h$^{{-1}}$")
    xs = (kn * phimax + kt * phi0) / (kn + kt)
    ax.plot([xs], [kt * (xs - phi0)], "o", ms=7, color=charts.line(tok))
    lim = np.minimum(kt * (x - phi0), kn * (phimax - x))
    ax.fill_between(x, 0, np.clip(lim, 0, None), color=P.fill(tok), alpha=0.18, lw=0)
ax.set_xlim(0, 0.7); ax.set_ylim(0, 1.7)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "ribosomal fraction $\\phi_R$ (RNA/protein)", "growth rate $\\lambda$ / h$^{-1}$")
charts.title(ax, "A   The optimum lies at the corner")


def g(a):
    return a / (a + K)


def chi(a):
    return phi0 + (phimax - phi0) * a / (a + Kc)


def steady_lam(phiR, kn):
    f = lambda a: kt * g(a) * (phiR - phi0) * (1 + a) - kn * (phimax - phiR)
    a = brentq(f, 1e-12, 1e6)
    return kt * g(a) * (phiR - phi0), a


def regulated(kn):
    p = brentq(lambda p: p - chi(steady_lam(p, kn)[1]), phi0 + 1e-6, phimax - 1e-6)
    return p, *steady_lam(p, kn)


ax = axs[1]
kns = np.linspace(0.2, 6, 40)
opt = [-minimize_scalar(lambda p: -steady_lam(p, kn)[0], bounds=(phi0 + 1e-4, phimax - 1e-4), method="bounded").fun for kn in kns]
reg = [regulated(kn)[1] for kn in kns]
p_fixed = regulated(0.6)[0]
fix = [steady_lam(p_fixed, kn)[0] for kn in kns]
ax.plot(kns, opt, color=P.ink(), lw=2.6, alpha=0.4, label="best possible allocation")
ax.plot(kns, reg, color=charts.line("enzyme"), lw=1.6, label="flux-controlled regulation")
ax.plot(kns, fix, color=charts.line("negative"), lw=1.4, ls="--", label="allocation fixed for $\\kappa_n$ = 0.6 h$^{-1}$")
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "nutrient quality $\\kappa_n$ / h$^{-1}$", "steady growth rate $\\lambda$ / h$^{-1}$")
charts.title(ax, "B   Regulation tracks the optimum")

ax = axs[2]
p1, l1, a1 = regulated(0.6)


def rhs(t, y, mode):
    phiR, a = y
    lam = kt * g(a) * (phiR - phi0)
    target = chi(a) if mode == "reg" else p1
    return [lam * (target - phiR), 3.0 * (phimax - phiR) - lam * (1 + a)]


for mode, tok, lab in (("reg", "enzyme", "regulated"), ("fix", "negative", "allocation frozen")):
    sol = solve_ivp(rhs, (0, 8), [p1, a1], args=(mode,), max_step=0.01)
    lam = kt * g(sol.y[1]) * (sol.y[0] - phi0)
    ax.plot(np.r_[-1, 0, sol.t], np.r_[l1, l1, lam], color=charts.line(tok), lw=1.8, label=f"$\\lambda$, {lab}")
    if mode == "reg":
        ax.plot(np.r_[-1, 0, sol.t], np.r_[p1, p1, sol.y[0]] * 4, color=charts.line("rrna"), lw=1.2, ls=":",
                label="$4\\phi_R$, regulated")
ax.axvline(0, color=P.muted(), lw=0.6)
ax.legend(fontsize=7.5, frameon=False, loc="center right")
charts.style_axes(ax, "time after upshift / h", "growth rate / h$^{-1}$")
charts.title(ax, "C   Nutrient upshift")
fig.tight_layout()
