"""Excitable waves: target and spiral patterns of the kind seen in fields of aggregating Dictyostelium.

A generic excitable medium (Barkley model) stands in for the cAMP relay: u_t = u (1 - u)(u - (v + b) / a) / eps + lap u,
v_t = u - v, with a = 0.75, b = 0.06, eps = 0.02 on a 60 x 60 square with no-flux edges (dx = 0.5). Left: a
periodically firing pacemaker in the centre (stimulated every 8 time units) emits concentric waves; the
refractory tail behind each front keeps waves from re-exciting the region they have passed and makes colliding
waves annihilate. Right: a broken wave front curls up into a rotating spiral, a self-sustained pacemaker that
needs no special cell; spirals dominate late aggregation fields. Shading: excitation u.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts as C

P = bio.P
a_, b_, eps = 0.75, 0.06, 0.02
n, dx, dt = 120, 0.5, 0.01


def lap(u):
    up = np.pad(u, 1, mode="edge")
    return (up[2:, 1:-1] + up[:-2, 1:-1] + up[1:-1, 2:] + up[1:-1, :-2] - 4 * u) / dx**2


def step(u, v):
    uth = (v + b_) / a_
    u2 = u + dt * (u * (1 - u) * (u - uth) / eps + lap(u))
    v2 = v + dt * (u - v)
    return np.clip(u2, 0, 1), v2


def target(T=34.0):
    u = np.zeros((n, n))
    v = np.zeros((n, n))
    c = n // 2
    for i in range(int(T / dt)):
        if i % int(8.0 / dt) == 0:
            u[c - 2:c + 3, c - 2:c + 3] = 1.0
        u, v = step(u, v)
    return u


def spiral(T=30.0):
    u = np.zeros((n, n))
    v = np.zeros((n, n))
    u[:, :6] = 1.0
    for i in range(int(T / dt)):
        if abs(i * dt - 6.0) < dt / 2:
            u[: n // 2, :] = 0.0
            v[: n // 2, :] = 0.0
        u, v = step(u, v)
    return u


cmap = LinearSegmentedColormap.from_list("exc", [P.surface(), P.fill("highlight")])
fig, ax = bio.canvas(20.0, 11.0)
for i, (u, title) in enumerate(((target(), "Pacemaker: target waves"), (spiral(), "Broken front: a spiral"))):
    sub = C.axes_at(ax, (1.0 + 9.6 * i, 1.0, 8.4, 8.4))
    sub.imshow(u, cmap=cmap, origin="lower", vmin=0, vmax=1, interpolation="bilinear")
    sub.set_xticks([])
    sub.set_yticks([])
    for sp in sub.spines.values():
        sp.set_color(P.muted())
    bio.label(ax, (1.0 + 9.6 * i, 10.2), title, size="small", bold=True, ha="left")
