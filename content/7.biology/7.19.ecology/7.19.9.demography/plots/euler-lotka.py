"""The Euler-Lotka equation (Section 9.4.2).

A: phi(r) = sum_x exp(-r x) l_x m_x for the barnacle Balanus glandula (Connell 1970) and female
yellow-bellied marmots (Schwartz et al. 1998), both as tabulated by Begon & Townsend (2021); the root of
phi(r) = 1 is the intrinsic rate of increase, phi(0) = R0.
B: accuracy of r ~ ln R0 / Tc (first order) and of the second-order correction
ln R0 / Tc + (ln R0)^2 sigma^2 / (2 Tc^3), when every m_x of the barnacle is multiplied by a factor c
(so that R0 = 1.283 c while the shape of l_x m_x, hence Tc and sigma^2, is unchanged).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

xb = np.arange(9)
lb = np.array([1e6, 62, 34, 20, 15.5, 11, 6.5, 2, 2]) / 1e6
mb = np.array([0, 4600, 8700, 11600, 12700, 12700, 12700, 12700, 12700])
lmb = lb * mb

am = np.array([773, 420, 208, 139, 106, 67, 44, 31, 22, 12, 7, 3, 2, 2, 2, 1.0])
Fm = np.array([0, 0, 95, 102, 106, 75, 45, 34, 37, 16, 9, 0, 0, 0, 0, 0.0])
xm = np.arange(16)
lmm = Fm / am[0]  # l_x m_x = (a_x / a_0)(F_x / a_x)


def phi(r, x, lm):
    return (np.exp(-np.outer(np.atleast_1d(r), x)) * lm).sum(axis=1)


def root(x, lm):
    return brentq(lambda r: phi(r, x, lm)[0] - 1, -3, 3)


fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axes[0]
rr = np.linspace(-0.3, 0.3, 300)
for x, lm, col, name in ((xb, lmb, C.line("dna"), "barnacle"), (xm, lmm, C.line("animal"), "marmot")):
    ax.plot(rr, phi(rr, x, lm), color=col, lw=2, label=name)
    r0 = root(x, lm)
    R0 = lm.sum()
    ax.plot([r0], [1], "o", color=col, ms=5)
    ax.plot([0], [R0], "s", color=col, ms=4, mfc="none")
    ax.annotate(f"r = {r0:+.3f}", (r0, 1), (r0 + 0.02, 1.35 if name == "barnacle" else 0.55),
                fontsize=FS["tiny"], color=col, arrowprops=dict(arrowstyle="-", color=col, lw=0.7))
ax.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
ax.axvline(0, color=P.muted(), lw=0.6)
ax.text(0.005, 2.3, "squares: φ(0) = R₀", fontsize=FS["tiny"], color=P.muted())
ax.set_ylim(0, 2.6)
C.style_axes(ax, "r (per year)", "φ(r) = Σ e⁻ʳˣ lₓmₓ")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "A  Solving the Euler–Lotka equation")

ax = axes[1]
R0b = lmb.sum()
w = lmb / R0b
Tc = (xb * w).sum()
s2 = ((xb - Tc) ** 2 * w).sum()
cs = np.geomspace(0.1, 30, 60)
exact = np.array([root(xb, c * lmb) for c in cs])
R0s = cs * R0b
first = np.log(R0s) / Tc
second = first + np.log(R0s) ** 2 * s2 / (2 * Tc ** 3)
ax.plot(R0s, exact, color=P.ink(), lw=2, label="exact root")
ax.plot(R0s, first, color=C.line("rna"), lw=1.6, ls=(0, (4, 2)), label="ln R₀ / T_c")
ax.plot(R0s, second, color=C.line("positive"), lw=1.6, ls=(0, (1, 1.5)), label="second order")
ax.axvline(R0b, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
ax.text(R0b * 1.08, -0.6, "observed\nR₀ = 1.28", fontsize=FS["tiny"], color=P.muted())
ax.set_xscale("log")
C.style_axes(ax, "R₀ (fecundity rescaled)", "r (per year)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "B  How good is r ≈ ln R₀ / T_c?")

fig.tight_layout()
