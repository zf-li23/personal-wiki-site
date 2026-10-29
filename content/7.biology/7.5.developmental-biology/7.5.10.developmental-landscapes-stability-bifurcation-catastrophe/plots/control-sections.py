"""Sections of the bifurcation sets of the codimension-3 catastrophes, and of a symmetric unfolding.

A: swallowtail phi = x^5 + 10 u x^3 + 10 v x^2 + 5 w x, section u = -1 of the bifurcation set in the
(v, w) plane, parametrized by the degenerate critical point x: v = -x^3 - 3 u x, w = 3 x^4 + 6 u x^2
(two cusps and a self-intersection: the swallowtail).
B: hyperbolic umbilic phi = x^3/3 + x y^2 + u (y^2 - x^2) + v x + w y (alpha = 1), section u = 1:
v = -y^2 + 2 u x - x^2, w = -2 y (x + u) on y^2 = x^2 - u^2.
C: elliptic umbilic (alpha = -1): v = -y^2 - 2 u x + x^2, w = -2 y (x + u) on y^2 = u^2 - x^2: a
curvilinear triangle with three cusps (a deltoid).
D: the bilaterally symmetric unfolding phi = alpha (x^4 - 6 x^2 y^2 + y^4) + beta (3 x y^2 - x^3)
+ gamma (x^2 + y^2) + u x + v y with alpha = 1, beta = 0.2: bifurcation set in the (u, v) plane
(image of the curve det Hess = 0 under (u, v) = -grad of the u, v-independent part) for
gamma = 0.05 (solid) and gamma = 0.2 (dashed): four-cusped figures, symmetric under v -> -v.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(36.0, 9.6)
col = quant.line_color("protein")

bio.panel(ax, "A", (0.1, 9.5))
pa = charts.axes_at(ax, (1.8, 1.8, 6.6, 6.6))
u = -1.0
x = np.linspace(-1.6, 1.6, 600)
pa.plot(-x ** 3 - 3 * u * x, 3 * x ** 4 + 6 * u * x ** 2, color=col, lw=1.8)
pa.set_xlim(-2.5, 2.5)
pa.set_ylim(-4, 3)
charts.style_axes(pa, "v", "w")
charts.title(pa, "Swallowtail (u = −1)")

bio.panel(ax, "B", (9.3, 9.5))
pb = charts.axes_at(ax, (11.0, 1.8, 6.6, 6.6))
u = 1.0
for side in (-1, 1):
    xx = side * np.linspace(1.0, 2.2, 300)
    for sg in (-1, 1):
        y = sg * np.sqrt(np.maximum(xx ** 2 - u ** 2, 0))
        pb.plot(-y ** 2 + 2 * u * xx - xx ** 2, -2 * y * (xx + u), color=col, lw=1.8)
pb.set_xlim(-12, 3)
pb.set_ylim(-8, 8)
charts.style_axes(pb, "v", "w")
charts.title(pb, "Hyperbolic umbilic (u = 1)")

bio.panel(ax, "C", (18.5, 9.5))
pc = charts.axes_at(ax, (20.2, 1.8, 6.6, 6.6))
th = np.linspace(0, 2 * np.pi, 600)
xx, y = u * np.cos(th), u * np.sin(th)
pc.plot(-y ** 2 - 2 * u * xx + xx ** 2, -2 * y * (xx + u), color=col, lw=1.8)
pc.set_aspect("equal")
charts.style_axes(pc, "v", "w")
charts.title(pc, "Elliptic umbilic (u = 1)")

bio.panel(ax, "D", (27.6, 9.5))
pd = charts.axes_at(ax, (29.3, 1.8, 6.4, 6.6))
X, Y = np.meshgrid(np.linspace(-1.2, 1.2, 900), np.linspace(-1.2, 1.2, 900))
import matplotlib.pyplot as plt
for ga, ls in ((0.05, "-"), (0.2, (0, (3, 2)))):
    al, be = 1.0, 0.2
    pxx = al * (12 * X ** 2 - 12 * Y ** 2) - 6 * be * X + 2 * ga
    pyy = al * (-12 * X ** 2 + 12 * Y ** 2) + 6 * be * X + 2 * ga
    pxy = -24 * al * X * Y + 6 * be * Y
    tmpfig = plt.figure()
    cs = tmpfig.gca().contour(X, Y, pxx * pyy - pxy ** 2, [0])
    segs = cs.allsegs[0]
    plt.close(tmpfig)
    for sgm in segs:
        x1, y1 = sgm[:, 0], sgm[:, 1]
        uu = -(al * (4 * x1 ** 3 - 12 * x1 * y1 ** 2) + be * (3 * y1 ** 2 - 3 * x1 ** 2) + 2 * ga * x1)
        vv = -(al * (-12 * x1 ** 2 * y1 + 4 * y1 ** 3) + be * (6 * x1 * y1) + 2 * ga * y1)
        pd.plot(uu, vv, color=quant.line_color("mesoderm"), lw=1.5, ls=ls)
pd.set_xlim(-0.12, 0.12)
pd.set_ylim(-0.12, 0.12)
pd.set_aspect("equal")
charts.style_axes(pd, "u", "v")
charts.title(pd, "Bilaterally symmetric unfolding")
