"""A two-variable model of the embryonic cell cycle of Xenopus (SH Eq. 20-1, after Ferrell, Tsai and
Yang, 2011): dC/dt = a1 - b1 C A^n/(K^n + A^n) + a3 (1 - C) C^n/(K^n + C^n) and
dA/dt = a2 (1 - A) C^n/(K^n + C^n) - b2 A, with C the active fraction of cyclin B-Cdk1 and A that of
APC/C-Cdc20; a1 = 0.1, a2 = a3 = 3, b1 = 3, b2 = 1 (per minute), K = 0.5, n = 8. A: the
Cdk1 nullcline (red) is S-shaped because of the positive feedback, the APC/C nullcline (blue) is
monotonic; they cross at an unstable fixed point (open circle) surrounded by a stable limit cycle
(violet, with dots at equal time intervals). B: time courses: Cdk1 rises slowly, jumps, activates
APC/C, and is switched off; period about 2.2 min in these units. C: with the positive feedback
removed (a3 = 0, a1 raised to 0.3) the fixed point is stable and the oscillation is damped."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
K, n = 0.5, 8
H = lambda x: x ** n / (K ** n + x ** n)


def rhs(t, y, a1=0.1, a3=3.0):
    C, A = y
    return [a1 - 3 * C * H(A) + a3 * (1 - C) * H(C), 3 * (1 - A) * H(C) - A]


sol = solve_ivp(rhs, (0, 30), [0.05, 0.05], max_step=0.005, rtol=1e-8)
fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.4), gridspec_kw=dict(width_ratios=(1, 1.2, 1.2)))
fig.subplots_adjust(wspace=0.33, left=0.06, right=0.98, bottom=0.16, top=0.88)
ax = axs[0]
c = np.linspace(0.001, 0.999, 2000)
ax.plot(c, 3 * H(c) / (3 * H(c) + 1), color=charts.line("dna"), lw=1.5, label="dA/dt = 0")
a = np.linspace(0.001, 0.999, 2000)
cc = np.linspace(0.001, 0.999, 2000)
CC, AA = np.meshgrid(cc, a)
F = 0.1 - 3 * CC * H(AA) + 3 * (1 - CC) * H(CC)
ax.contour(CC, AA, F, levels=[0], colors=[charts.line("blood")], linewidths=1.5)
ax.plot([], [], color=charts.line("blood"), lw=1.5, label="dC/dt = 0")
m = sol.t > 10
tt = np.arange(10, 30, 0.04)
ax.plot(np.interp(tt, sol.t, sol.y[0]), np.interp(tt, sol.t, sol.y[1]), ".", ms=2, color=charts.line("protein"))
cs = brentq(lambda x: 0.1 - 3 * x * H(3 * H(x) / (3 * H(x) + 1)) + 3 * (1 - x) * H(x), 0.3, 0.6)
ax.plot(cs, 3 * H(cs) / (3 * H(cs) + 1), "o", ms=5, mfc=P.surface(), mec=P.ink())
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "active Cdk1, C", "active APC/C, A")
charts.title(ax, "A  Phase plane")
ax = axs[1]
ax.plot(sol.t, sol.y[0], color=charts.line("blood"), lw=1.3, label="Cdk1")
ax.plot(sol.t, sol.y[1], color=charts.line("dna"), lw=1.3, label="APC/C")
ax.set_xlim(0, 15)
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), ncol=2, loc="upper right")
charts.style_axes(ax, "time / min", "activity")
charts.title(ax, "B  Sustained oscillation")
ax = axs[2]
s2 = solve_ivp(rhs, (0, 15), [0.05, 0.05], args=(0.3, 0.0), max_step=0.005, rtol=1e-8)
ax.plot(s2.t, s2.y[0], color=charts.line("blood"), lw=1.3, label="Cdk1")
ax.plot(s2.t, s2.y[1], color=charts.line("dna"), lw=1.3, label="APC/C")
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), ncol=2, loc="upper right")
charts.style_axes(ax, "time / min", "activity")
charts.title(ax, "C  No positive feedback")
