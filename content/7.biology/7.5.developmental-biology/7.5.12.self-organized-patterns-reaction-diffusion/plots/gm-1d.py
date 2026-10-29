"""One-dimensional Gierer-Meinhardt patterns (simulations, no-flux boundaries).

Model: a_t = eps2 a_xx + rho(x) a^2 / (h (1 + kappa a^2)) - a, tau h_t = D h_xx + a^2 - h, with eps2 = 1e-4 and
tau = 0.5 (activator lifetime 1). A: from 1 % random noise on a tissue of length 4 with a short inhibitor range
(D = 0.02, kappa = 0), peaks with a roughly regular spacing appear, their number and positions set by the noise.
B: with a long inhibitor range (D = 1, L = 1) and no noise but a source density rising by 2 % from left to right,
rho = 1 + 0.02 x, one peak forms, at the end where the source is highest: a weak graded bias decides polarity.
C: with saturation (kappa = 0.5) the activated region is a plateau, and with D = 20 its width is a constant
fraction (about 16 %) of tissues of length 1 and 2 (rho = 1 + 0.02 x / L): relative size regulation.
"""

import numpy as np
from scipy.sparse import diags, identity
from scipy.sparse.linalg import splu
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT


def run(L, D, kap=0.0, rho=lambda x: 1 + 0 * x, T=3000.0, dt=0.05, noise=0.0, e2=1e-4, tau=0.5, dx=0.005):
    n = int(round(L / dx)) + 1
    x = np.linspace(0, L, n)
    dx = x[1] - x[0]
    lap = diags([np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)], [-1, 0, 1]).tolil()
    lap[0, 1] = 2
    lap[-1, -2] = 2
    lap = (lap / dx**2).tocsc()
    I = identity(n, format="csc")
    La = splu((I - dt * e2 * lap).tocsc())
    Lh = splu((I - dt * D / tau * lap).tocsc())
    a0 = 1.0
    for _ in range(200):
        a0 = 0.5 * a0 + 0.5 / (1 + kap * a0 * a0)
    rng = np.random.default_rng(0)
    a = np.full(n, a0) * (1 + noise * rng.standard_normal(n))
    h = np.full(n, a0 * a0)
    r = rho(x)
    for _ in range(int(T / dt)):
        f = r * a * a / (h * (1 + kap * a * a)) - a
        g = (a * a - h) / tau
        a = La.solve(a + dt * f)
        h = Lh.solve(h + dt * g)
    return x, a, h


fig, ax = bio.canvas(30.0, 9.2)
x, a, h = run(4.0, 0.02, T=300.0, dt=0.01, noise=0.01)
pa = C.axes_at(ax, (1.6, 1.4, 7.4, 6.4))
pa.plot(x, a, color=Q.line_color("protein"), lw=1.5, label="activator a")
pa.plot(x, h, color=Q.line_color("na"), lw=1.2, ls=(0, (3, 2)), label="inhibitor h")
pa.set_xlim(0, 4)
C.style_axes(pa, "x", "concentration")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.6, 8.6), "From noise: spaced peaks", size="small", bold=True, ha="left")

x, a, h = run(1.0, 1.0, rho=lambda x: 1 + 0.02 * x)
pb = C.axes_at(ax, (11.6, 1.4, 7.4, 6.4))
pb.plot(x, a, color=Q.line_color("protein"), lw=1.8, label="activator a")
pb.plot(x, h, color=Q.line_color("na"), lw=1.2, ls=(0, (3, 2)), label="inhibitor h")
pb.set_xlim(0, 1)
C.style_axes(pb, "x", "concentration")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
pb.text(0.05, 0.6 * pb.get_ylim()[1], "source ρ = 1 + 0.02x", color=P.muted(), fontsize=FS["tiny"])
bio.panel(ax, "B", (10.3, 8.6))
bio.label(ax, (11.6, 8.6), "A weak gradient sets polarity", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (21.6, 1.4, 7.4, 6.4))
for L, tk, ls in ((1.0, "protein", "-"), (2.0, "negative", (0, (4, 2)))):
    x, a, h = run(L, 20.0, kap=0.5, rho=lambda x, L=L: 1 + 0.02 * x / L)
    frac = (a > 0.5 * a.max()).mean()
    pc.plot(x / L, a, color=Q.line_color(tk), lw=1.8, ls=ls, label=f"L = {L:g}: activated {100 * frac:.0f} %")
pc.set_xlim(0, 1)
C.style_axes(pc, "x / L", "activator a")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (20.3, 8.6))
bio.label(ax, (21.6, 8.6), "Saturation: the plateau scales", size="small", bold=True, ha="left")
