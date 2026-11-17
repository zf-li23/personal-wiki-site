"""Lotka-Volterra mutualism in dimensionless form: x' = x (s - x + a y), y' = rho y (s - y + b x).

A: facultative mutualism (s = 1) with weak mutual benefit, a = 0.5, b = 0.6 (ab = 0.3 < 1): the
isoclines x = 1 + a y and y = 1 + b x cross at x* = (1 + a)/(1 - ab) = 2.14, y* = (1 + b)/(1 - ab) = 2.29,
above both carrying capacities (1, 1); every trajectory converges to it.
B: strong benefit, a = 1.2, b = 1.1 (ab = 1.32 > 1): the isoclines diverge and both populations grow
without bound (May's "orgy of mutual benefaction").
C: obligate mutualism (s = -1, both species decline alone) with a = 2, b = 1.5 (ab = 3): the isoclines
cross at a saddle, x* = (1 + a)/(ab - 1) = 1.5, y* = (1 + b)/(ab - 1) = 1.25; below its stable manifold
(dashed) both species go extinct, above it both explode. rho = 1 in all panels.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 11.5)


def field(s, a, b, rho=1.0):
    def f(t, z):
        x, y = z
        return [x * (s - x + a * y), rho * y * (s - y + b * x)]
    return f


def blow(t, z):
    return 40.0 - max(z)


blow.terminal = True

cases = [
    (1.0, 0.5, 0.6, 4.0, "A", "Weak benefit, ab = 0.3: stable coexistence"),
    (1.0, 1.2, 1.1, 6.0, "B", "Strong benefit, ab = 1.32: unbounded growth"),
    (-1.0, 2.0, 1.5, 4.0, "C", "Obligate mutualists, ab = 3: a threshold"),
]
xc = Q.line_color("dna")
yc = Q.line_color("negative")
for i, (s, a, b, lim, letter, title) in enumerate(cases):
    x0 = 2.0 + 11.0 * i
    pa = C.axes_at(ax, (x0, 1.7, 8.2, 8.2))
    g = np.linspace(0.001, lim, 23)
    X, Y = np.meshgrid(g, g)
    U = X * (s - X + a * Y)
    V = Y * (s - Y + b * X)
    sp = np.hypot(U, V) + 1e-9
    pa.quiver(X, Y, U / sp, V / sp, color=P.mix(P.muted(), P.surface(), 0.35), scale=40, width=0.0035,
              headwidth=3.5, headlength=4)
    yy = np.linspace(0, lim, 200)
    # x-isocline: x = s + a y ; y-isocline: y = s + b x
    pa.plot(s + a * yy, yy, color=xc, lw=1.6, label="x-isocline")
    xx = np.linspace(0, lim, 200)
    pa.plot(xx, s + b * xx, color=yc, lw=1.6, label="y-isocline")
    f = field(s, a, b)
    if s > 0:
        starts = [(0.2, 3.6), (3.5, 0.2), (0.1, 0.1), (3.8, 3.8), (2.5, 0.05), (0.05, 2.0)]
        if a * b > 1:
            starts = [(0.2, 1.0), (1.0, 0.2), (0.1, 0.1), (0.5, 0.5)]
        for z0 in starts:
            sol = solve_ivp(f, (0, 60), z0, events=blow, max_step=0.02, rtol=1e-8)
            pa.plot(sol.y[0], sol.y[1], color=P.ink(), lw=1.0)
            k = len(sol.t) // 4
            pa.annotate("", xy=(sol.y[0][k + 1], sol.y[1][k + 1]), xytext=(sol.y[0][k], sol.y[1][k]),
                        arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=0.9))
    else:
        xs, ys = (1 + a) / (a * b - 1), (1 + b) / (a * b - 1)
        # stable manifold: integrate backwards from points near the saddle along the stable eigenvector
        J = np.array([[-xs, a * xs], [b * ys, -ys]])
        w, vec = np.linalg.eig(J)
        vs = vec[:, np.argmin(w)]
        for sgn in (1, -1):
            sol = solve_ivp(lambda t, z: [-c for c in f(t, z)], (0, 30), [xs + sgn * 1e-4 * vs[0], ys + sgn * 1e-4 * vs[1]],
                            max_step=0.02, events=lambda t, z: min(z) - 1e-3)
            pa.plot(sol.y[0], sol.y[1], color=P.ink(), lw=1.2, ls=(0, (4, 2)))
        for z0 in [(1.0, 0.6), (0.6, 1.2), (2.0, 1.2), (1.6, 1.7), (3.0, 0.4), (0.4, 3.0), (2.5, 3.6)]:
            sol = solve_ivp(f, (0, 30), z0, events=blow, max_step=0.02, rtol=1e-8)
            pa.plot(sol.y[0], sol.y[1], color=P.ink(), lw=1.0)
            k = min(len(sol.t) - 2, 25)
            pa.annotate("", xy=(sol.y[0][k + 1], sol.y[1][k + 1]), xytext=(sol.y[0][k], sol.y[1][k]),
                        arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=0.9))
        pa.plot([xs], [ys], "o", ms=6, mfc=P.surface(), mec=P.ink(), mew=1.2)
        pa.text(xs + 0.12, ys - 0.3, "saddle", fontsize=FS["tiny"], color=P.ink())
        pa.text(0.15, 0.25, "extinction", fontsize=FS["tiny"], color=P.muted())
        pa.text(2.6, 3.2, "explosion", fontsize=FS["tiny"], color=P.muted())
    if s > 0 and a * b < 1:
        xs, ys = (1 + a) / (1 - a * b), (1 + b) / (1 - a * b)
        pa.plot([xs], [ys], "o", ms=6, color=P.ink())
        pa.plot([1, 0], [0, 1], "o", ms=4.5, mfc=P.surface(), mec=P.ink(), mew=1.0)
    pa.set_xlim(0, lim)
    pa.set_ylim(0, lim)
    C.style_axes(pa, "species 1, x", "species 2, y")
    if i == 0:
        pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
    bio.panel(ax, letter, (x0 - 1.7, 11.3))
    bio.label(ax, (x0, 10.6), title, size="small", bold=True, ha="left")
