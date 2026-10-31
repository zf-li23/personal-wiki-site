"""Oscillations born in a Hopf bifurcation. A, B: the normal form dr/dt = mu r - r^3,
dtheta/dt = 1 in Cartesian coordinates: for mu = -0.5 trajectories spiral into a stable focus, for
mu = 0.5 onto a stable limit cycle of radius sqrt(mu) (thick circle) around an unstable focus.
C: the Goodwin oscillator dx/dt = 1000/(1 + z^n) - x, dy/dt = x - y, dz/dt = y - z (three
identical stages): oscillation amplitude of z at long times against the Hill coefficient n;
the steady state loses stability at n = 8.02, where the loop gain reaches 8 (the secant condition
for three stages), and the
amplitude grows from zero as sqrt(n - 8) near the bifurcation (dashed fit)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.4))
fig.subplots_adjust(wspace=0.32, left=0.06, right=0.98, bottom=0.16, top=0.88)


def normal(t, y, mu):
    x, v = y
    r2 = x * x + v * v
    return [mu * x - v - r2 * x, x + mu * v - r2 * v]


for ax, mu, lab in ((axs[0], -0.5, "A"), (axs[1], 0.5, "B")):
    for x0, y0 in ((1.4, 0), (-1.2, 1.0), (0.05, 0.0), (0.0, -1.4)):
        s = solve_ivp(normal, (0, 25), [x0, y0], args=(mu,), max_step=0.02)
        ax.plot(s.y[0], s.y[1], color=charts.line("protein"), lw=0.8)
    if mu > 0:
        th = np.linspace(0, 2 * np.pi, 200)
        ax.plot(np.sqrt(mu) * np.cos(th), np.sqrt(mu) * np.sin(th), color=charts.line("blood"), lw=2.2)
    ax.plot(0, 0, "o", ms=5, mfc=P.ink() if mu < 0 else P.surface(), mec=P.ink())
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    charts.style_axes(ax, "x", "y")
    charts.title(ax, f"{lab}  μ = {mu:g}")

ax = axs[2]


def goodwin(t, y, n):
    x, yy, z = y
    return [1000 / (1 + z ** n) - x, x - yy, yy - z]


ns = np.linspace(6, 16, 41)
amp = []
for n in ns:
    s = solve_ivp(goodwin, (0, 1500), [5.0, 4.0, 3.0], args=(n,), max_step=0.1, rtol=1e-8)
    z = s.y[2][s.t > 1100]
    amp.append((z.max() - z.min()) / 2)
amp = np.array(amp)
ax.plot(ns, amp, "o", ms=3.5, color=charts.line("protein"))
nc = 8.02
sel = (ns > 8.3) & (ns < 10)
c = np.polyfit(np.sqrt(ns[sel] - nc), amp[sel], 1)
nn = np.linspace(nc, 11, 100)
ax.plot(nn, c[0] * np.sqrt(nn - nc), color=P.ink(), lw=0.9, ls="--")
ax.axvline(8, color=P.muted(), lw=0.6, ls=":")
ax.text(8.15, amp.max() * 0.95, "n = 8.02", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, "Hill coefficient n", "amplitude of z")
charts.title(ax, "C  Goodwin oscillator")
