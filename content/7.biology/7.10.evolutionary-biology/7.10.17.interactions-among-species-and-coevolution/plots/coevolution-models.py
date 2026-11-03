"""Coevolution of a prey trait x and a predator trait y (Example 17.2.1).

Gradient dynamics dx/dt = Gx d/dx [-a - k x^2 / 2], dy/dt = Gy d/dy [a - k y^2 / 2], k = 0.2.
A: escalation, a = 1 / (1 + exp(-(y - x))), Gx = Gy = 1, costs kx = 0.3 (prey) and ky = 0.2 (predator),
start x = y = 0. B: matching, a = exp(-(x - y)^2 / (2 sigma^2)), sigma = 1, k = 0.5, Gx = 3.5, Gy = 1,
start x = 0.1, y = 0.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio.quant import odeint_rk4

P = bio.P
FS = bio.core.FONT
k = 0.2


def esc(_, v):
    x, y = v
    a = 1 / (1 + np.exp(-(y - x)))
    da = a * (1 - a)  # derivative of a with respect to (y - x)
    return np.array([1.0 * (da - 0.3 * x), 1.0 * (da - 0.2 * y)])


def mat(_, v, Gx=3.5, Gy=1.0, s2=1.0, k=0.5):
    x, y = v
    a = np.exp(-(x - y) ** 2 / (2 * s2))
    return np.array([Gx * (a * (x - y) / s2 - k * x), Gy * (a * (x - y) / s2 - k * y)])


fig, ax = bio.canvas(30.0, 10.0)
t1 = np.linspace(0, 60, 1201)
X = odeint_rk4(esc, np.array([0.0, 0.0]), t1)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.plot(t1, X[:, 0], color=C.line("dna"), lw=1.9, label="prey trait x")
pa.plot(t1, X[:, 1], color=C.line("negative"), lw=1.9, ls=(0, (4, 2)), label="predator trait y")
pa.set_xlim(0, 60)
C.style_axes(pa, "time", "mean trait")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Difference interaction: an arms race", size="small", bold=True, ha="left")
t2 = np.linspace(0, 150, 6001)
Y = odeint_rk4(mat, np.array([0.1, 0.0]), t2)
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
pb.plot(t2, Y[:, 0], color=C.line("dna"), lw=1.7, label="prey trait x")
pb.plot(t2, Y[:, 1], color=C.line("negative"), lw=1.7, ls=(0, (4, 2)), label="predator trait y")
pb.set_xlim(0, 150)
pb.set_ylim(-1.0, 1.25)
C.style_axes(pb, "time", "mean trait")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center", ncol=2)
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Matching interaction: coevolutionary cycles", size="small", bold=True, ha="left")
