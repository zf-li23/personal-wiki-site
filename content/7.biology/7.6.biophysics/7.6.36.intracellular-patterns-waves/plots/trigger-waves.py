"""Trigger waves in one dimension (lengths in units of sqrt(D/k), times in 1/k). A: profiles every
10 time units of a bistable front, du/dt = u_xx + u(1 - u)(u - a) with a = 0.25 (solid), and of a
Fisher-KPP front, du/dt = u_xx + u(1 - u) (dashed), both started from a step. B: front positions
(u = 1/2) against time: the bistable front moves at sqrt(1/2)(1 - 2a) and the Fisher front
approaches 2 (lines show these speeds); the point where a step spreading by diffusion alone
reaches u = 0.1 advances only as sqrt(t) (dotted). C: speed of the bistable front against the threshold a, from
simulations (points) and the exact formula (line): the front reverses direction at a = 1/2, where
the two stable states have equal 'strength' (Theorem 36.5.1)."""

import numpy as np
from scipy.special import erfcinv
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
dx, dt = 0.25, 0.02
x = np.arange(0, 160, dx)


def lap(u):
    out = np.empty_like(u)
    out[1:-1] = u[2:] - 2 * u[1:-1] + u[:-2]
    out[0] = u[1] - u[0]
    out[-1] = u[-2] - u[-1]
    return out / dx ** 2


def run(f, T, u0):
    u = u0.copy()
    snaps, pos, ts = [], [], []
    for i in range(int(T / dt) + 1):
        t = i * dt
        if i % int(1 / dt) == 0:
            ts.append(t)
            pos.append(x[np.argmax(u < 0.5)])
            if i % int(10 / dt) == 0:
                snaps.append(u.copy())
        u = u + dt * (lap(u) + f(u))
    return np.array(ts), np.array(pos), snaps


step = np.where(x < 10, 1.0, 0.0)
a = 0.25
fb = lambda u: u * (1 - u) * (u - a)
ff = lambda u: u * (1 - u)
tb, pb, sb = run(fb, 60, step)
tf, pf, sf = run(ff, 60, step)

fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.35, left=0.06, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
for s in sb:
    ax.plot(x, s, color=charts.line("ca"), lw=1.1)
for s in sf:
    ax.plot(x, s, color=charts.line("enzyme"), lw=1.0, ls="--")
ax.set_xlim(0, 140)
charts.style_axes(ax, "position x", "u")
charts.title(ax, "A  front profiles")

ax = axs[1]
vb = np.sqrt(0.5) * (1 - 2 * a)
ax.plot(tb, pb, "o", color=charts.line("ca"), ms=2.5, label="bistable")
ax.plot(tb, 10 + vb * tb, color=charts.line("ca"), lw=0.8)
ax.plot(tf, pf, "s", color=charts.line("enzyme"), ms=2.5, label="Fisher-KPP")
ax.plot(tf, 10 + 2 * tf, color=charts.line("enzyme"), lw=0.8)
# diffusion alone: the point where a released step reaches u = 0.1 moves as sqrt(t)
td = np.linspace(0.01, 60, 200)
ax.plot(td, 10 + 2 * np.sqrt(td) * erfcinv(0.2), ":", color=P.muted(), lw=1.2, label="diffusion only (u = 0.1)")
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, "time t", "front position")
charts.title(ax, "B  constant speed")

ax = axs[2]
As = np.linspace(0.05, 0.75, 8)
sp = []
for aa in As:
    t2, p2, _ = run(lambda u, aa=aa: u * (1 - u) * (u - aa), 40, np.where(x < 80, 1.0, 0.0))
    sl = t2 > 15
    sp.append(np.polyfit(t2[sl], p2[sl], 1)[0])
af = np.linspace(0, 0.8, 100)
ax.plot(af, np.sqrt(0.5) * (1 - 2 * af), color=charts.line("ca"), lw=1.2)
ax.plot(As, sp, "o", color=charts.line("ca"), ms=3.5)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(0.5, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(ax, "threshold a", "front speed")
charts.title(ax, "C  speed and direction")
