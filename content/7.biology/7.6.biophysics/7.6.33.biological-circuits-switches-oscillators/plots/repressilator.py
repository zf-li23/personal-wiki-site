"""The repressilator of Elowitz and Leibler (2000): dm_i/dt = -m_i + alpha/(1 + p_j^n) + alpha0,
dp_i/dt = -beta (p_i - m_i), where protein j represses gene i around the cycle lacI -| tetR -| cI -| lacI.
Time in mRNA lifetimes; beta is the ratio of mRNA to protein lifetimes. A: protein levels for
alpha = 216, alpha0 = 0.216, n = 2, beta = 5 (the parameters of the original paper): sustained
oscillations with a phase lag of a third of a period between successive genes. B: the region of the
(alpha, beta) plane in which the symmetric steady state is unstable (shaded), computed from the
eigenvalues of the 6 x 6 Jacobian, for n = 2 and n = 3 (alpha0 = 0): oscillations need strong
promoters, cooperative repression and similar mRNA and protein lifetimes."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P


def rhs(t, y, a, a0, n, b):
    m, p = y[:3], y[3:]
    rep = p[[2, 0, 1]]
    return np.concatenate([-m + a / (1 + rep ** n) + a0, -b * (p - m)])


fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.4), gridspec_kw=dict(width_ratios=(1.4, 1)))
fig.subplots_adjust(wspace=0.28, left=0.07, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
sol = solve_ivp(rhs, (0, 60), [1, 0, 0, 2, 1, 3], args=(216, 0.216, 2, 5), max_step=0.02)
for i, (name, tok) in enumerate((("LacI", "dna"), ("TetR", "protein"), ("cI", "blood"))):
    ax.plot(sol.t, sol.y[3 + i], color=charts.line(tok), lw=1.3, label=name)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), ncol=3, loc="upper right")
ax.set_ylim(0, 80)
charts.style_axes(ax, "time (mRNA lifetimes)", "protein (units of K)")
charts.title(ax, "A  Sustained oscillations")


def unstable(a, b, n):
    p = brentq(lambda x: x - a / (1 + x ** n), 0, a + 1)
    s = -a * n * p ** (n - 1) / (1 + p ** n) ** 2
    J = np.zeros((6, 6))
    for i in range(3):
        J[i, i] = -1
        J[i, 3 + (i + 2) % 3] = s
        J[3 + i, 3 + i] = -b
        J[3 + i, i] = b
    return np.linalg.eigvals(J).real.max() > 0


ax = axs[1]
A = np.logspace(0, 4, 120)
B = np.logspace(-2, 2, 120)
for n, tok, alpha in ((2, "protein", 0.55), (3, "dna", 0.3)):
    Z = np.array([[unstable(a, b, n) for a in A] for b in B])
    ax.contourf(A, B, Z, levels=[0.5, 1.5], colors=[P.fill(tok)], alpha=alpha)
    ax.contour(A, B, Z, levels=[0.5], colors=[charts.line(tok)], linewidths=1.2)
ax.plot(216, 5, "*", ms=8, color=P.ink())
ax.text(8, 0.018, "n = 3 only", fontsize=bio.core.FONT["tiny"], color=charts.line("dna"))
ax.text(1.2e3, 1.0, "n = 2 and 3", fontsize=bio.core.FONT["tiny"], color=charts.line("protein"))
ax.set_xscale("log")
ax.set_yscale("log")
charts.style_axes(ax, "promoter strength α", "lifetime ratio β")
charts.title(ax, "B  Oscillatory region")
