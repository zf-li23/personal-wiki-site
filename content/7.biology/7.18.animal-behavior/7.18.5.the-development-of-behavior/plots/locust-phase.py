"""Phase change in the desert locust as a bistable switch with fast gregarization and slow solitarization.

g in [0, 1] is behavioral gregariousness; dg/dt = (D + b g^4 / (K^4 + g^4) - g) / tau, with crowding cue D,
positive feedback b = 0.9, K = 0.6, and tau = 1 h when g increases, 12 h when it decreases. Illustrative.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
b, K = 0.9, 0.6


def f(g, D):
    return D + b * g ** 4 / (K ** 4 + g ** 4) - g


fig, ax = bio.canvas(28.0, 10.0)
pa = C.axes_at(ax, (2.4, 1.6, 10.6, 7.2))
Ds = np.linspace(0, 0.4, 400)
gs = np.linspace(0, 1.4, 4000)
pts_s, pts_u = [], []
for D in Ds:
    v = f(gs, D)
    idx = np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]
    for j in idx:
        g0 = gs[j]
        slope = (f(g0 + 1e-4, D) - f(g0 - 1e-4, D))
        (pts_s if slope < 0 else pts_u).append((D, g0))
pts_s, pts_u = np.array(pts_s), np.array(pts_u)
pa.plot(pts_s[:, 0], pts_s[:, 1], ".", color=C.line("rna"), ms=2)
if len(pts_u):
    pa.plot(pts_u[:, 0], pts_u[:, 1], ".", color=P.muted(), ms=1)
pa.text(0.02, 0.06, "solitarious", color=C.line("plant"), fontsize=FS["tiny"])
pa.text(0.27, 1.25, "gregarious", color=C.line("rna"), fontsize=FS["tiny"])
pa.text(0.17, 0.62, "unstable", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(0, 0.4)
pa.set_ylim(0, 1.4)
C.style_axes(pa, "crowding cue D (density, touch, sight, smell)", "gregariousness g at equilibrium")
bio.panel(ax, "A", (0.4, 9.7))

t = np.arange(0, 96, 0.02)
g = np.zeros_like(t)
D = np.where((t >= 4) & (t < 28), 0.3, 0.0)
for i in range(1, len(t)):
    r = f(g[i - 1], D[i - 1])
    tau = 1.0 if r > 0 else 12.0
    g[i] = g[i - 1] + r / tau * 0.02
pb = C.axes_at(ax, (16.6, 1.6, 10.6, 7.2))
pb.axvspan(4, 28, color=C.line("rna"), alpha=0.12, lw=0)
pb.plot(t, g, color=C.line("rna"), lw=2.0)
pb.text(16, 1.3, "crowded", color=C.line("rna"), fontsize=FS["tiny"], ha="center")
pb.text(60, 1.3, "isolated", color=P.muted(), fontsize=FS["tiny"], ha="center")
pb.set_xlim(0, 96)
pb.set_ylim(0, 1.4)
C.style_axes(pb, "time / h", "gregariousness g")
bio.panel(ax, "B", (14.6, 9.7))
