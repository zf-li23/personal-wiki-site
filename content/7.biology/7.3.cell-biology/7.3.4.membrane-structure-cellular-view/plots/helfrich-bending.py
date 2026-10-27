"""Bending energy of membranes (Helfrich), with kappa = 20 kT.

A: energy of a spherical vesicle of radius R: E = 2 pi kappa (2 - c0 R)^2 (mean-curvature term).
With c0 = 0 it is 8 pi kappa (about 500 kT) at every radius; a spontaneous curvature c0 makes
R = 2/c0 free of bending cost.
B: a membrane tube (tether) held against tension sigma: radius R_t = sqrt(kappa / (2 sigma)),
force f = 2 pi sqrt(2 kappa sigma), over the tensions measured in cells.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22.0, 8.0)
kT = 1.380649e-23 * 310
kappa = 20  # in kT

bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.7, 1.3, 8.0, 5.8))
R = np.linspace(10, 150, 400)
for c0, tok, name in ((0.0, "neutral", "c₀ = 0"), (1 / 40, "dna", "c₀ = 1/40 nm⁻¹"), (1 / 20, "negative", "c₀ = 1/20 nm⁻¹")):
    E = 2 * np.pi * kappa * (2 - c0 * R) ** 2
    pa.plot(R, E, color=charts.line(tok), lw=1.8, label=name)
    if c0:
        pa.plot([2 / c0], [0], "o", color=charts.line(tok), ms=5)
pa.axhline(8 * np.pi * kappa, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
pa.text(148, 8 * np.pi * kappa + 25, "8πκ ≈ 500 k_BT".replace("k_BT", "kT"), fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
pa.set_xlim(10, 150)
pa.set_ylim(0, 1500)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pa, "vesicle radius R / nm", "bending energy / kT")
charts.title(pa, "A spherical vesicle (κ = 20 kT)")

bio.panel(ax, "B", (11.2, 7.8))
pb = charts.axes_at(ax, (12.8, 1.3, 7.4, 5.8))
sigma = np.logspace(-6, -3, 200)  # N/m
k = kappa * kT
f = 2 * np.pi * np.sqrt(2 * k * sigma) * 1e12
Rt = np.sqrt(k / (2 * sigma)) * 1e9
pb.loglog(sigma * 1e3, f, color=charts.line("protein"), lw=1.8, label="force f / pN")
pb.loglog(sigma * 1e3, Rt, color=charts.line("enzyme"), lw=1.8, ls=(0, (4, 2)), label="radius Rₜ / nm")
pb.axvspan(1e-2, 1e-1, color=P.fill("highlight"), alpha=0.2, lw=0)
pb.text(3.2e-2, 1.4, "cells", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pb.set_xlim(1e-3, 1)
pb.set_ylim(1, 1000)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "membrane tension σ / (mN m⁻¹)", "f / pN,  Rₜ / nm")
charts.title(pb, "Pulling a membrane tether")
