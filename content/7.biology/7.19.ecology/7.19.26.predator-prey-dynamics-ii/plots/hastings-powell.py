"""Chaos in a three-species food chain (Hastings and Powell 1991), Section 26.4:
x' = x (1 - x) - a1 x y / (1 + b1 x)
y' = a1 x y / (1 + b1 x) - a2 y z / (1 + b2 y) - d1 y
z' = a2 y z / (1 + b2 y) - d2 z
with a1 = 5, a2 = 0.1, b2 = 2, d1 = 0.4, d2 = 0.01.
A: the "teacup" attractor for b1 = 3 (after a transient). B: time series of the top predator z
and the intermediate consumer y. C: bifurcation diagram: the local maxima of z on the attractor
against b1; a single maximum means a limit cycle, a cloud of maxima chaos.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
a1, a2, b2, d1, d2 = 5.0, 0.1, 2.0, 0.4, 0.01


def rhs(t, u, b1):
    x, y, z = u
    f1 = a1 * x / (1 + b1 * x)
    f2 = a2 * y / (1 + b2 * y)
    return [x * (1 - x) - f1 * y, f1 * y - f2 * z - d1 * y, f2 * z - d2 * z]


def run(b1, T0, T1, u0=(0.76, 0.16, 9.9)):
    s = solve_ivp(rhs, [0, T1], u0, args=(b1,), method="LSODA", rtol=1e-8, atol=1e-10, dense_output=True)
    t = np.linspace(T0, T1, int((T1 - T0) * 10))
    return t, s.sol(t)


fig = plt.figure(figsize=(14.5, 4.5))
ax = fig.add_subplot(1, 3, 1, projection="3d")
t, (x, y, z) = run(3.0, 2000, 6000)
ax.plot(x, y, z, color=C.line("dna"), lw=0.35)
ax.set_xlabel("x (resource)", fontsize=FS["tiny"], color=P.ink())
ax.set_ylabel("y (consumer)", fontsize=FS["tiny"], color=P.ink())
ax.set_zlabel("z", fontsize=FS["tiny"], color=P.ink(), labelpad=-1)
ax.tick_params(labelsize=FS["tiny"], colors=P.muted())
for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
    pane.set_facecolor("none")
ax.view_init(elev=25, azim=-60)
C.title(ax, "A  Chaotic attractor, b1 = 3 (z: top predator)")

ax = fig.add_subplot(1, 3, 2)
sel = t < 3000
ax.plot(t[sel], z[sel], color=C.line("negative"), lw=1.0, label="top predator z")
ax.plot(t[sel], 10 * y[sel], color=C.line("positive"), lw=0.6, label="consumer 10 y")
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
ax.set_ylim(0, 13)
C.style_axes(ax, "Time", "Density")
C.title(ax, "B  Irregular fluctuations")

ax = fig.add_subplot(1, 3, 3)
for b1 in np.linspace(2.2, 3.2, 70):
    t, (x, y, z) = run(b1, 3000, 6000)
    k = np.where((z[1:-1] > z[:-2]) & (z[1:-1] > z[2:]))[0] + 1
    ax.plot(np.full(k.size, b1), z[k], ".", ms=1.6, color=P.ink(), alpha=0.7)
C.style_axes(ax, "Half-saturation parameter b1", "Local maxima of z")
C.title(ax, "C  Route to chaos")
fig.tight_layout()
