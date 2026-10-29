"""A developmental landscape that branches: the potential E(x; u) = x^4/4 - u x^2/2 + v x over time.

The control parameter u rises with developmental time t (u = t - 1), so a single valley (one cell
state) splits into two (two fates) at t = 1 (a pitchfork, the symmetric section v = 0 of the cusp
catastrophe). A small bias v = 0.04 makes the right valley slightly deeper. The surface is the
landscape; the dark line follows a cell that tracks the nearest minimum (gradient flow) and ends
in the left valley because a small fluctuation pushed it there just after the branch point.
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax0 = bio.canvas(16.0, 11.0)
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], projection="3d")
ax.set_facecolor("none")
x = np.linspace(-1.25, 1.25, 120)
t = np.linspace(0, 3, 90)
X, Tt = np.meshgrid(x, t)
U = Tt - 1
V = 0.04
E = X ** 4 / 4 - U * X ** 2 / 2 + V * X
E = E - E.min(axis=1, keepdims=True)
cm = __import__("matplotlib").colormaps["viridis"]
ax.plot_surface(X, Tt, E, cmap=cm, alpha=0.85, linewidth=0, antialiased=True, rstride=2, cstride=2)
# tracked minimum
xs, ts = [], []
xc = 0.0
for tt in np.linspace(0, 3, 400):
    u = tt - 1
    for _ in range(40):
        xc -= 0.05 * (xc ** 3 - u * xc + V)
    if abs(tt - 1.15) < 0.004:
        xc -= 0.08
    xs.append(xc)
    ts.append(tt)
xs, ts = np.array(xs), np.array(ts)
ee = xs ** 4 / 4 - (ts - 1) * xs ** 2 / 2 + V * xs
emin = np.array([(x ** 4 / 4 - (tt - 1) * x ** 2 / 2 + V * x).min() for tt in ts])
ax.plot(xs, ts, ee - emin + 0.03, color=P.ink(), lw=2.2)
ax.set_xlabel("cell state x", color=P.ink(), fontsize=8)
ax.set_ylabel("developmental time t", color=P.ink(), fontsize=8)
ax.set_zlabel("potential E", color=P.ink(), fontsize=8)
for a in (ax.xaxis, ax.yaxis, ax.zaxis):
    a.set_tick_params(colors=P.muted(), labelsize=6)
    a.set_pane_color((1, 1, 1, 0))
    a._axinfo["grid"]["color"] = P.mix(P.muted(), P.surface(), 0.6)
ax.view_init(elev=30, azim=-72)
