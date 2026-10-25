"""Allosteric enzymes in the concerted (MWC) model with n = 4 catalytic sites; alpha = [S]/K_R,
c = K_R/K_T, L = [T0]/[R0]. Heterotropic modulators that bind only R (activators) or only T
(inhibitors) change L: L' = L (1 + [I]/K_I)^n / (1 + [A]/K_A)^n.

A: K system (T binds substrate weakly, c = 0.01; both states have the same k_cat): v/V_max = fraction
of sites occupied. L = 10^3 without modulator, 10 with an activator and 10^5 with an inhibitor: K_0.5
changes, V_max does not; the dashed hyperbola has the same K_0.5 as the central curve.
B: V system (both states bind substrate equally, c = 1, but T has k_T = 0.05 k_R): every curve is a
hyperbola with K_0.5 = K_R, and the modulators change V_max."""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
n = 4


def k_system(a, L, c=0.01):
    return (a * (1 + a) ** (n - 1) + L * c * a * (1 + c * a) ** (n - 1)) / ((1 + a) ** n + L * (1 + c * a) ** n)


def v_system(a, L, kt=0.05):
    fr = 1 / (1 + L)  # fraction of molecules in R (c = 1: binding does not shift the equilibrium)
    return a / (1 + a) * (fr + (1 - fr) * kt)


fig, ax = bio.canvas(20.0, 8.0)
a = np.linspace(0, 40, 800)

bio.panel(ax, "A", (0.1, 7.9))
p = charts.axes_at(ax, (1.3, 1.0, 8.0, 6.0))
curves = ((10.0, "positive", "activator ($L$ = 10)"), (1e3, "enzyme", "no modulator ($L$ = 10$^3$)"),
          (1e5, "negative", "inhibitor ($L$ = 10$^5$)"))
for L, tok, lab in curves:
    p.plot(a, k_system(a, L), color=charts.line(tok), lw=2.0, label=lab)
k05 = brentq(lambda x: k_system(x, 1e3) - 0.5, 1e-6, 1e4)
p.plot(a, a / (k05 + a), color=P.muted(), lw=1.0, ls="--", label="hyperbola, same $K_{0.5}$")
p.plot([k05, k05], [0, 0.5], color=charts.line("enzyme"), lw=0.8, ls=":")
p.text(k05 + 0.5, 0.03, "$K_{0.5}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
p.set_xlim(0, 40)
p.set_ylim(0, 1.05)
p.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(p, r"[S] / $K_\mathrm{R}$", r"$v_0/v_{\max}$")
charts.title(p, "K system: modulators shift $K_{0.5}$")

bio.panel(ax, "B", (10.6, 7.9))
q = charts.axes_at(ax, (11.8, 1.0, 7.8, 6.0))
a2 = np.linspace(0, 12, 400)
for L, tok, lab in ((0.01, "positive", "activator ($L$ = 0.01)"), (1.0, "enzyme", "no modulator ($L$ = 1)"),
                    (100.0, "negative", "inhibitor ($L$ = 100)")):
    q.plot(a2, v_system(a2, L), color=charts.line(tok), lw=2.0, label=lab)
q.axvline(1.0, color=P.muted(), lw=0.8, ls=":")
q.text(1.15, 0.92, "$K_{0.5} = K_\\mathrm{R}$ for all", fontsize=bio.core.FONT["tiny"], color=P.ink())
q.set_xlim(0, 12)
q.set_ylim(0, 1.05)
q.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.25))
charts.style_axes(q, r"[S] / $K_\mathrm{R}$", r"$v_0/v_{\max}^{\mathrm{R}}$")
charts.title(q, "V system: modulators change $v_{\\max}$")
