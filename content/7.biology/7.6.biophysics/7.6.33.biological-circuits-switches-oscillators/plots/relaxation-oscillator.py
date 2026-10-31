"""An activator-repressor relaxation oscillator: the activator A activates its own gene and the gene
of the repressor R, which represses the activator's gene; both bind as dimers. In dimensionless
form, dA/dt = (100 + 5000 A^2)/(1 + A^2 + R^2) - 30 A and dR/dt = 120 A^2/(1 + A^2) - R (time in
repressor lifetimes; the activator is 30 times faster). A: nullclines (activator: S-shaped, red;
repressor: blue) and the limit cycle (dots at equal time intervals: dense where the motion is slow):
the trajectory creeps along the outer branches of the activator nullcline and jumps between them.
B: time courses: long phases of slow change punctuated by fast jumps, the signature of a relaxation
oscillation."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P


def rhs(t, y):
    A, R = y
    return [(100 + 5000 * A ** 2) / (1 + A ** 2 + R ** 2) - 30 * A, 120 * A ** 2 / (1 + A ** 2) - R]


sol = solve_ivp(rhs, (0, 40), [0.01, 1.0], max_step=0.002, rtol=1e-8, atol=1e-10)
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
A = np.logspace(-5, 2.5, 800)
q = (100 + 5000 * A ** 2) / (30 * A) - 1 - A ** 2
Rnull = np.sqrt(np.where(q > 0, q, np.nan))
ax.plot(A, Rnull, color=charts.line("blood"), lw=1.6, label="dA/dt = 0")
ax.plot(A, 120 * A ** 2 / (1 + A ** 2), color=charts.line("dna"), lw=1.6, label="dR/dt = 0")
tt = np.arange(15, 40, 0.05)
yy = np.array([np.interp(tt, sol.t, sol.y[i]) for i in range(2)])
ax.plot(yy[0], yy[1], ".", ms=2.2, color=charts.line("protein"))
ax.set_xscale("log")
ax.set_xlim(1e-5, 3e2)
ax.set_ylim(0, 130)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "activator A", "repressor R")
charts.title(ax, "A  Phase plane")
ax = axs[1]
ax.plot(sol.t, sol.y[0], color=charts.line("blood"), lw=1.2, label="activator A")
ax.plot(sol.t, sol.y[1], color=charts.line("dna"), lw=1.2, label="repressor R")
ax.set_xlim(10, 40)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time (repressor lifetimes)", "concentration")
charts.title(ax, "B  Slow phases and fast jumps")
