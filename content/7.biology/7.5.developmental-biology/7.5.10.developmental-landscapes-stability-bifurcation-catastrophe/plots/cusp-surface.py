"""The equilibrium surface of the cusp catastrophe phi = x^4 + 6 u x^2 + 4 v x.

Critical points satisfy x^3 + 3 u x + v = 0, a folded surface over the control plane (u, v). The
fold lines (x^2 = -u, v = 2 x^3, dark) separate the stable sheets (minima, upper and lower) from the
unstable middle sheet (maxima); their projection onto the control plane is the cusp v^2 + 4 u^3 = 0
(drawn on the floor). A path at fixed u < 0 with v increasing stays on the upper sheet
until the fold and then jumps (red), the hysteresis of perfect delay.
"""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax0 = bio.canvas(16.0, 12.0)
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], projection="3d")
ax.set_facecolor("none")
xg = np.linspace(-1.2, 1.2, 120)
ug = np.linspace(-1.0, 0.4, 80)
Xg, Ug = np.meshgrid(xg, ug)
Vg = -Xg ** 3 - 3 * Ug * Xg
stable = 3 * Xg ** 2 + 3 * Ug > 0
cm = __import__("matplotlib").colormaps["viridis"]
colors = np.where(stable[..., None], np.array(cm(0.65)), np.array(cm(0.15)))
ax.plot_surface(Ug, Vg, Xg, facecolors=colors, alpha=0.8, linewidth=0, rstride=1, cstride=1, shade=True)
xf = np.linspace(-1.0, 1.0, 200)
uf, vf = -xf ** 2, 2 * xf ** 3
ax.plot(uf, vf, xf, color=P.ink(), lw=2.0)
floor = -1.9
ax.plot(uf, vf, np.full_like(xf, floor), color=P.edge("mesoderm"), lw=1.6)
ax.plot([-1.0, 0.0], [0, 0], [floor, floor], color=P.muted(), lw=0.8, ls=(0, (1, 1.5)))
# hysteresis path at u = -0.6
u0 = -0.6
xs = np.linspace(1.2, np.sqrt(-u0), 100)
ax.plot(np.full_like(xs, u0), -xs ** 3 - 3 * u0 * xs, xs, color=P.edge("mesoderm"), lw=2.2)
xj = np.sqrt(-u0)
vj = 2 * xj ** 3
ax.plot([u0, u0], [vj, vj], [xj, -2 * xj], color=P.edge("mesoderm"), lw=1.6, ls=(0, (3, 2)))
ax.set_xlabel("u", color=P.ink(), fontsize=9)
ax.set_ylabel("v", color=P.ink(), fontsize=9)
ax.set_zlabel("state x", color=P.ink(), fontsize=9)
ax.set_zlim(floor, 1.3)
ax.set_ylim(-2.2, 2.2)
for a in (ax.xaxis, ax.yaxis, ax.zaxis):
    a.set_tick_params(colors=P.muted(), labelsize=6)
    a.set_pane_color((1, 1, 1, 0))
    a._axinfo["grid"]["color"] = P.mix(P.muted(), P.surface(), 0.6)
ax.view_init(elev=28, azim=-145)
