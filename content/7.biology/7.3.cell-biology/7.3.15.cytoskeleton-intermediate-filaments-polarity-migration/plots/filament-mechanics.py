"""Stiffness of the three cytoskeletal filaments: persistence length and the worm-like chain.

A filament of contour length L with bending stiffness kappa = l_p k_B T is simulated in two dimensions as a
chain of 400 segments whose successive tangent angles change by Gaussian increments of variance ds/l_p
(the discrete worm-like chain; in 2D <cos theta(s)> = exp(-s / 2 l_p)).
A: ten thermal conformations each of a 10 um intermediate filament (l_p = 1 um), actin filament
(l_p = 17 um) and microtubule (l_p = 5 mm, Gittes et al. 1993), all starting at the origin along x.
B: tangent correlation along the contour from the simulations (points, 500 chains each) against
exp(-s / 2 l_p) (lines).
C: mean squared end-to-end distance relative to L^2 as a function of L / l_p (worm-like chain in 2D):
rodlike for L << l_p, random coil (proportional to L) for L >> l_p; dots mark 10 um filaments.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(7)
L, n = 10.0, 400
ds = L / n
kinds = (("intermediate filament", 1.0, "positive"), ("actin filament", 17.0, "actin"), ("microtubule", 5000.0, "channel"))


def chains(lp, m):
    dth = rng.normal(0, np.sqrt(ds / lp), size=(m, n))
    th = np.cumsum(dth, axis=1)
    x = np.cumsum(np.cos(th) * ds, axis=1)
    y = np.cumsum(np.sin(th) * ds, axis=1)
    return th, x, y


fig, ax = bio.canvas(27.0, 8.4)
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.5, 1.4, 8.2, 6.0))
for name, lp, tk in kinds:
    th, x, y = chains(lp, 10)
    for i in range(10):
        pa.plot(np.r_[0, x[i]], np.r_[0, y[i]], color=quant.line_color(tk), lw=0.9, alpha=0.8)
    pa.plot([], [], color=quant.line_color(tk), lw=1.5, label=f"{name}, ℓp = {lp:g} µm" if lp < 1000 else f"{name}, ℓp = 5 mm")
pa.set_aspect("equal")
pa.set_xlim(-1, 10.5)
pa.set_ylim(-5, 5)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(pa, "x / µm", "y / µm")
charts.title(pa, "Thermal shapes of 10 µm filaments")

bio.panel(ax, "B", (10.8, 8.3))
pb = charts.axes_at(ax, (12.4, 1.4, 6.0, 6.0))
s = np.arange(1, n + 1) * ds
for name, lp, tk in kinds:
    th, _, _ = chains(lp, 500)
    c = np.cos(th).mean(axis=0)
    pb.plot(s[::25], c[::25], "o", color=quant.line_color(tk), ms=3.5)
    pb.plot(s, np.exp(-s / (2 * lp)), color=quant.line_color(tk), lw=1.4)
pb.set_ylim(0, 1.05)
charts.style_axes(pb, "contour distance s / µm", "⟨cos θ(s)⟩")
charts.title(pb, "Tangent correlation")

bio.panel(ax, "C", (19.6, 8.3))
pc = charts.axes_at(ax, (21.2, 1.4, 5.4, 6.0))
u = np.logspace(-3, 2, 200)  # L / l_p
r2 = 4 / u * (1 - 2 / u * (1 - np.exp(-u / 2)))  # <R^2>/L^2 for the 2D worm-like chain
pc.loglog(u, r2, color=quant.line_color("ink"), lw=1.6)
for name, lp, tk in kinds:
    uu = L / lp
    pc.plot([uu], [4 / uu * (1 - 2 / uu * (1 - np.exp(-uu / 2)))], "o", color=quant.line_color(tk), ms=6)
pc.text(0.003, 0.6, "rod", fontsize=bio.core.FONT["tiny"], color=P.muted())
pc.text(8, 0.06, "coil", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(pc, "L / ℓp", "⟨R²⟩ / L²")
charts.title(pc, "Rod or coil")
