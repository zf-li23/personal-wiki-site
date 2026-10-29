"""Tension-driven Stokes flow of a cell aggregate: how fast shapes relax and aggregates fuse.

A: decay of a small ellipsoidal deformation of a very viscous drop (viscosity eta, radius R, surface
tension gamma, inviscid surroundings): rate (20/19) gamma/(eta R) (the limit of Rallison's result for
a drop in a much less viscous medium); dashed: a short surface wave of wavenumber k, which decays at
the planar rate gamma k/(2 eta), here k R = 6.
B: fusion of two equal spherical aggregates of radius a by viscous sintering, early stage
(Frenkel 1945): neck radius x with (x/a)^2 = 3 gamma t / (2 eta a). Upper time axis: hours for
gamma = 10 mN/m, eta = 2 x 10^5 Pa s, a = 200 um (t unit eta a / gamma = 4000 s).
C: outlines of two fusing spheres with neck radius x/a = 0.2, 0.5, 0.8 (sketch: overlapping spheres).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(32.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.0, 1.8, 8.4, 7.0))
tt = np.linspace(0, 4, 200)
pa.plot(tt, np.exp(-20 / 19 * tt), color=quant.line_color("mesoderm"), lw=2.2, label="ellipsoidal mode (l = 2)")
pa.plot(tt, np.exp(-tt * 3), color=quant.line_color("ectoderm"), lw=1.4, ls=(0, (3, 2)), label="short wave, kR = 6")
pa.set_xlim(0, 4)
pa.set_ylim(0, 1.02)
charts.style_axes(pa, "time t γ / (η R)", "deformation (relative)")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper right")
for tx in leg.get_texts():
    tx.set_color(P.ink())
charts.title(pa, "Rounding up of a deformed aggregate")
bio.panel(ax, "B", (11.6, 9.9))
pb = charts.axes_at(ax, (13.4, 1.8, 8.6, 7.0))
tt = np.linspace(0, 0.5, 200)
pb.plot(tt, np.sqrt(1.5 * tt), color=quant.line_color("ectoderm"), lw=2.2)
pb.set_xlim(0, 0.5)
pb.set_ylim(0, 1)
charts.style_axes(pb, "time t γ / (η a)", "neck radius x / a")
charts.title(pb, "Frenkel sintering: x² ∝ t")
top = pb.secondary_xaxis("top", functions=(lambda v: v * 4000 / 3600, lambda h: h * 3600 / 4000))
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
top.set_xlabel("hours (γ = 10 mN/m, η = 2×10⁵ Pa s, a = 200 µm)", fontsize=bio.core.FONT["tiny"], color=P.ink())

bio.panel(ax, "C", (23.2, 9.9))
th = np.linspace(0, 2 * np.pi, 400)
for k, xr in enumerate((0.2, 0.5, 0.8)):
    cy = 7.6 - 2.7 * k
    d = np.sqrt(1 - xr ** 2)
    a = 1.1
    pts = []
    for sgn in (-1, 1):
        cx = sgn * d * a
        ang = np.linspace(0, 2 * np.pi, 400)
        X = cx + a * np.cos(ang)
        Y = a * np.sin(ang)
        keep = (sgn * X >= 0)
        ax.plot(27.5 + X[keep], cy + Y[keep], color=P.edge("mesoderm"), lw=1.4)
    ax.fill_between([], [], [])
    bio.label(ax, (30.6, cy), f"x/a = {xr:g}", size="tiny", ha="left")
