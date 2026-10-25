"""Metabolic control analysis of a three-step linear pathway X0 -> S1 -> S2 -> X3.

Reversible Michaelis-Menten rates v_i = e_i (V_i/Ks)(S_{i-1} - S_i/K'_i)/(1 + S_{i-1}/Ks + S_i/Kp),
X0 = 1 mM, X3 = 0.01 mM, Ks = 0.5 mM, Kp = 1 mM; V = (2, 10, 3) mM/s, K' = (10, 5, 100).
Feedback version: v1 divided by 1 + (S2/0.1 mM)^4. Steady states by nested root finding (brentq); flux control
coefficients by central finite differences of ln J against ln e_i."""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
X0, X3, KS, KP = 1.0, 0.01, 0.5, 1.0
V, K = (2.0, 10.0, 3.0), (10.0, 5.0, 100.0)


def rate(i, s, p, e):
    return e * V[i] * (s - p / K[i]) / KS / (1 + s / KS + p / KP)


def rates(S1, S2, e, fb):
    v1 = rate(0, X0, S1, e[0])
    if fb:
        v1 /= 1 + (S2 / fb) ** 4
    return v1, rate(1, S1, S2, e[1]), rate(2, S2, X3, e[2])


def flux(e, fb, guess=None):
    """Steady-state flux by nested root finding: S2 sets J = v3; S1 solves v2 = J; v1 = J closes."""
    def s1_of(S2, J):
        lo = S2 / K[1] * (1 + 1e-12) + 1e-15
        return brentq(lambda S1: rate(1, S1, S2, e[1]) - J, lo, 1e4)

    def resid(S2):
        J = rate(2, S2, X3, e[2])
        if rate(1, 1e4, S2, e[1]) <= J:
            return -J
        S1 = s1_of(S2, J)
        return rates(S1, S2, e, fb)[0] - J

    S2 = brentq(resid, X3 / K[2] * 1.0000001 + 1e-9, X0 * K[0] * K[1] * 0.999999)
    return rate(2, S2, X3, e[2])


def coeffs(fb):
    e = np.ones(3)
    out = []
    for i in range(3):
        h = 1e-4
        ep, em = e.copy(), e.copy()
        ep[i] *= np.exp(h)
        em[i] *= np.exp(-h)
        out.append((np.log(flux(ep, fb)) - np.log(flux(em, fb))) / (2 * h))
    return np.array(out)


fig, ax = bio.canvas(23.0, 13.6)
names = ["E1 (supply)", "E2 (near equilibrium)", "E3 (demand)"]
toks = ["enzyme", "neutral", "drug"]

# --- A: pathway ------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 13.4))
xs = [1.6, 6.0, 10.4, 14.8]
labs = ["X₀", "S₁", "S₂", "X₃"]
for x, t in zip(xs, labs):
    bio.box(ax, (x, 11.6), 1.5, 0.8, "metabolite", t, size="normal")
for k in range(3):
    bio.arrow(ax, (xs[k] + 0.8, 11.6), (xs[k + 1] - 0.8, 11.6), kind="process")
    bio.label(ax, ((xs[k] + xs[k + 1]) / 2, 12.15), names[k], size="small", color=P.edge(toks[k]))
bio.arrow(ax, (10.4, 11.15), (3.8, 11.5), kind="inhibition", bend=0.2, dashed=True)
bio.label(ax, (7.1, 9.75), "feedback inhibition (second version)", size="tiny", color=P.muted())
bio.label(ax, (17.2, 11.6), "fixed source and sink;\nreversible Michaelis–Menten steps", size="tiny", ha="left", color=P.muted())

# --- B, C: flux against enzyme amount ----------------------------------------------------------------
scale = np.logspace(np.log10(0.25), np.log10(4), 41)
C = {}
for panel, fb, x0, title in (("B", 0, 1.4, "Without feedback"), ("C", 0.1, 8.9, "With feedback")):
    bio.panel(ax, panel, (x0 - 1.3, 9.4))
    a = charts.axes_at(ax, (x0, 1.2, 5.6, 7.4))
    J0 = flux(np.ones(3), fb)
    C[fb] = coeffs(fb)
    for i in range(3):
        J = []
        g = (np.log(0.1), np.log(0.1))
        for s in scale:
            e = np.ones(3)
            e[i] = s
            J.append(flux(e, fb, g))
        a.plot(scale, np.array(J) / J0, color=charts.line(toks[i]), lw=2.0, label=f"{names[i]}: C = {C[fb][i]:.2f}")
    a.plot([1], [1], "o", color=P.ink(), ms=5)
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xlim(0.25, 4)
    a.set_ylim(0.2, 3)
    a.set_xticks([0.25, 0.5, 1, 2, 4])
    a.set_xticklabels(["0.25", "0.5", "1", "2", "4"])
    a.set_yticks([0.25, 0.5, 1, 2])
    a.set_yticklabels(["0.25", "0.5", "1", "2"])
    a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(a, "relative amount of one enzyme, $e_i$", "relative flux $J/J_0$")
    charts.title(a, title)

# --- D: control coefficients ----------------------------------------------------------------------
bio.panel(ax, "D", (15.6, 9.4))
d = charts.axes_at(ax, (17.0, 1.2, 5.4, 7.4))
w = 0.36
xx = np.arange(3)
d.bar(xx - w / 2, C[0], w, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.8)
d.bar(xx + w / 2, C[0.1], w, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.8, hatch="//")
for k in range(3):
    d.text(xx[k] - w / 2, C[0][k] + 0.02, f"{C[0][k]:.2f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
    d.text(xx[k] + w / 2, C[0.1][k] + 0.02, f"{C[0.1][k]:.2f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
d.set_xticks(xx)
d.set_xticklabels(["E1", "E2", "E3"])
d.set_ylim(0, 1.05)
charts.style_axes(d, None, "flux control coefficient $C^J_i$")
charts.title(d, "plain: no feedback; hatched: feedback")
d.text(1.0, 0.92, f"Σ = {C[0].sum():.2f} and {C[0.1].sum():.2f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
