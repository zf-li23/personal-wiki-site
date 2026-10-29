"""Gastrulation as a nonlinear steepening of the surface tension (Percus and Childress). If the surface
streaming caused by a P1 tension profile continues with velocity proportional to the tension gradient,
u_θ = k ∂T/∂θ, and the tension is carried with the cells, then T obeys T_t + k (T_θ)² = 0 (θ from the vegetal
pole, T = cos θ at t = 0, k = 1). Its slope g = 2k T_θ obeys the inviscid Burgers equation g_t + g g_θ = 0. A:
characteristics θ(t) = θ0 + g(θ0, 0) t converge on the vegetal pole and first cross at t* = 1/(2k) = 0.5.
B: the tension profile sharpens into a cusp at the vegetal pole. C: the curvature T_θθ at the pole,
−1/(1 − 2kt), diverges at t*: from a smooth, linearly neutral initial state a localized, "catastrophic"
concentration of tension, and hence of invagination, develops in finite time."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22, 7.4)
k = 1.0
th0 = np.linspace(-np.pi, np.pi, 41)
a = charts.axes_at(ax, (1.6, 1.4, 5.6, 4.8))
tt = np.linspace(0, 0.5, 50)
for t0 in th0:
    g0 = -2 * k * np.sin(t0)
    a.plot(np.degrees(t0 + g0 * tt), tt, color=charts.line("dna"), lw=0.7)
a.axhline(0.5, color=charts.line("receptor"), lw=0.9, ls=(0, (3, 2)))
a.text(-170, 0.51, "t* = 1/(2k)", fontsize=7, color=charts.line("receptor"), va="bottom")
a.set_xlim(-180, 180)
a.set_ylim(0, 0.6)
a.set_xticks([-180, -90, 0, 90, 180])
charts.style_axes(a, "θ / degree (0: vegetal pole)", "time t")
charts.title(a, "A  Characteristics")

b = charts.axes_at(ax, (8.9, 1.4, 5.6, 4.8))
s0 = np.linspace(-np.pi, np.pi, 2001)
for t, tk in ((0, "neutral"), (0.25, "dna"), (0.4, "positive"), (0.49, "receptor")):
    g0 = -2 * k * np.sin(s0)
    th = s0 + g0 * t
    T = np.cos(s0) + g0**2 * t / (4 * k)
    o = np.argsort(th)
    b.plot(np.degrees(th[o]), T[o], color=charts.line(tk), lw=1.6, label=f"t = {t:g}")
b.set_xlim(-180, 180)
b.set_xticks([-180, -90, 0, 90, 180])
charts.style_axes(b, "θ / degree", "surface tension T")
charts.title(b, "B  Sharpening at the vegetal pole")
lg = b.legend(fontsize=6.5, frameon=False, loc="lower center")
[x.set_color(P.ink()) for x in lg.get_texts()]

c = charts.axes_at(ax, (16.2, 1.4, 5.2, 4.8))
t = np.linspace(0, 0.48, 200)
c.plot(t, 1 / (1 - 2 * k * t), color=charts.line("receptor"), lw=1.7)
c.set_yscale("log")
charts.style_axes(c, "time t", "−T_θθ at the pole")
charts.title(c, "C  Finite-time blow-up")
