"""Elementary oscillators: Lotka-Volterra orbits, the limit cycle model r' = (1 - r^2)/r, and the van der Pol
oscillator with the amplitude predicted by averaging (small epsilon) and a relaxation oscillation (large)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 4, figsize=(13.0, 3.5))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.86, wspace=0.34)

a = axs[0]
toks = ["dna", "protein", "enzyme", "drug"]
for k, h0 in enumerate((1.3, 1.8, 2.6, 3.6)):
    s = solve_ivp(lambda t, y: [y[0] - y[0] * y[1], y[0] * y[1] - y[1]], [0, 12], [h0, 1.0], max_step=0.01, rtol=1e-9)
    a.plot(s.y[0], s.y[1], color=charts.line(toks[k]), lw=1.4)
a.plot([1], [1], "o", color=P_.ink(), ms=3)
charts.style_axes(a, "prey H", "predator L")
charts.title(a, "A  Lotka-Volterra")

b = axs[1]
th = np.linspace(0, 2 * np.pi, 200)
b.plot(np.cos(th), np.sin(th), color=P_.ink(), lw=2.2)
for k, (r0, t0) in enumerate(((0.08, 0.0), (0.3, 2.0), (1.7, 4.0), (1.4, 1.0))):
    t = np.linspace(0, 3.5, 400)
    C = 1 - r0 ** 2
    r = np.sqrt(1 - C * np.exp(-2 * t))
    ang = t0 + 2.5 * t
    b.plot(r * np.cos(ang), r * np.sin(ang), color=charts.line(toks[k]), lw=1.1)
b.set_aspect("equal")
charts.style_axes(b, "x", "y")
charts.title(b, "B  A limit cycle")

c = axs[2]
eps = 0.1
s = solve_ivp(lambda t, y: [y[1], eps * (1 - y[0] ** 2) * y[1] - y[0]], [0, 80], [0.2, 0.0], max_step=0.02, rtol=1e-9)
c.plot(s.t, s.y[0], color=charts.line("dna"), lw=0.7)
tt = np.linspace(0, 80, 300)
C = 4 / 0.2 ** 2 - 1
A = 2 / np.sqrt(1 + C * np.exp(-eps * tt))
c.plot(tt, A, color=charts.line("drug"), lw=2.0)
c.plot(tt, -A, color=charts.line("drug"), lw=2.0)
charts.style_axes(c, "t", "x")
charts.title(c, "C  van der Pol, eps = 0.1")

d = axs[3]
s = solve_ivp(lambda t, y: [y[1], 5 * (1 - y[0] ** 2) * y[1] - y[0]], [0, 40], [0.5, 0.0], max_step=0.01, rtol=1e-8)
d.plot(s.t, s.y[0], color=charts.line("protein"), lw=1.4)
charts.style_axes(d, "t", "x")
charts.title(d, "D  van der Pol, eps = 5")
