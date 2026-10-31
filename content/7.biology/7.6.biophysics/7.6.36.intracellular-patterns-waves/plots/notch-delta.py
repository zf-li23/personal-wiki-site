"""Lateral inhibition between two cells (the two-cell version of the Collier model). Notch activity
N_i and Delta activity D_i obey dN_i/dt = f(D_j) - N_i and dD_i/dt = v[g(N_i) - D_i] (time in units of
the Notch decay time), with f(x) = x^2/(0.01 + x^2) (activation of Notch by the neighbor's Delta) and
g(x) = 1/(1 + 100 x^2) (repression of Delta by the cell's own Notch). A: for fast Delta (v >> 1),
D_i = g(N_i) and the dynamics reduces to the (N1, N2) plane: nullclines N1 = f(g(N2)) and
N2 = f(g(N1)), the flow (streamlines), the unstable symmetric fixed point (open circle) and the two
stable asymmetric ones (filled), and trajectories of the full four-variable model with v = 10 started
near the symmetric state. B: time courses of Notch in the two cells from initial values differing by
1 %: the difference is amplified until one cell has low Notch (high Delta, primary fate) and the
other high Notch."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P


def f(x):
    return x ** 2 / (0.01 + x ** 2)


def g(x):
    return 1 / (1 + 100 * x ** 2)


def full(t, y, v=10.0):
    N1, N2, D1, D2 = y
    return [f(D2) - N1, f(D1) - N2, v * (g(N1) - D1), v * (g(N2) - D2)]


fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.8), gridspec_kw=dict(width_ratios=(1, 1.2)))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.14, top=0.89)
ax = axs[0]
n = np.linspace(0, 1, 40)
X, Y = np.meshgrid(n, n)
U = f(g(Y)) - X
V = f(g(X)) - Y
ax.streamplot(X, Y, U, V, color=P.mix(P.muted(), P.surface(), 0.35), density=0.9, linewidth=0.5, arrowsize=0.6)
s = np.linspace(0, 1, 400)
ax.plot(f(g(s)), s, color=charts.line("receptor"), lw=1.5, label=r"$\dot N_1 = 0$")
ax.plot(s, f(g(s)), color=charts.line("enzyme"), lw=1.5, label=r"$\dot N_2 = 0$")
ns = brentq(lambda x: f(g(x)) - x, 1e-4, 1)
ax.plot(ns, ns, "o", mfc=P.surface(), mec=P.ink(), ms=6)
for y0 in ([ns * 1.02, ns, g(ns), g(ns)], [ns, ns * 1.02, g(ns), g(ns)]):
    sol = solve_ivp(full, (0, 40), y0, max_step=0.05)
    ax.plot(sol.y[0], sol.y[1], color=P.ink(), lw=1.0)
    ax.plot(sol.y[0, -1], sol.y[1, -1], "o", color=P.ink(), ms=5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.legend(frameon=False, fontsize=7, loc="upper right")
charts.style_axes(ax, r"Notch in cell 1, $N_1$", r"Notch in cell 2, $N_2$")
charts.title(ax, "A  phase plane (fast Delta)")

ax = axs[1]
sol = solve_ivp(full, (0, 30), [ns * 1.01, ns, g(ns), g(ns)], max_step=0.05)
ax.plot(sol.t, sol.y[0], color=charts.line("receptor"), lw=1.5, label="Notch, cell 1")
ax.plot(sol.t, sol.y[1], color=charts.line("enzyme"), lw=1.5, label="Notch, cell 2")
ax.plot(sol.t, sol.y[3], color=charts.line("enzyme"), lw=1.0, ls="--", label="Delta, cell 2")
ax.legend(frameon=False, fontsize=7, loc="center right")
charts.style_axes(ax, "time (Notch lifetimes)", "activity")
charts.title(ax, "B  symmetry breaking")
