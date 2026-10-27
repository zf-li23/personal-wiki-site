"""Mechanical gating by membrane tension.

A: schematic of a Piezo channel in side view. Closed: the three curved blades bend the surrounding
membrane into a dome that bulges into the cytoplasm. Open: tension in the membrane flattens the dome,
which increases the in-plane area of the channel by Delta A and opens the central pore.
B: two-state Boltzmann model P_o = 1 / (1 + exp(-(tau - tau_half) Delta A / kT)), 37 C, for
the bacterial MscS (tau_half = 5.5 mN/m, Delta A = 8 nm^2), MscL (10 mN/m, 20 nm^2), and Piezo1
(1.4 mN/m; Delta A = 6 nm^2, an illustrative value that reproduces a graded response).
Tensions above which bilayers usually rupture (about 12 mN/m) are shaded.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch
import wikibio as bio
from wikibio import cellbio as CB
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(23.0, 8.4)

# ---- A: schematic
bio.panel(ax, "A", (0.1, 8.2))
for k, (x0, closed, title) in enumerate(((0.6, True, "Closed: membrane dome"), (5.9, False, "Open: dome flattened"))):
    w = 4.8
    xc = x0 + w / 2
    ax.add_patch(FancyBboxPatch((x0, 4.3), w, 2.5, boxstyle="square,pad=0", facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
    ax.add_patch(FancyBboxPatch((x0, 1.0), w, 3.3, boxstyle="square,pad=0", facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
    x = np.linspace(x0, x0 + w, 120)
    depth = 1.0 if closed else 0.12
    yv = 4.3 - depth * np.exp(-((x - xc) / 1.0) ** 2)
    bio.bilayer(ax, np.column_stack([x, yv]), spacing=0.24)
    # blades
    for side in (-1, 1):
        xb = xc + side * np.linspace(0.25, 1.5, 20)
        yb = 4.3 - depth * np.exp(-((xb - xc) / 1.0) ** 2)
        ax.plot(xb, yb, color=P.edge("channel"), lw=6.5, solid_capstyle="round", zorder=12)
        ax.plot(xb, yb, color=P.fill("channel"), lw=4.5, solid_capstyle="round", zorder=12.1)
    yc = 4.3 - depth
    for side in (-1, 1):
        gap = 0.16 if closed else 0.36
        bio.protein(ax, (xc + side * (gap + 0.2), yc), 0.38, 1.05, "channel", wobble=0.04)
    if not closed:
        bio.arrow(ax, (xc, yc + 1.0), (xc, yc - 1.1), kind="process")
        bio.label(ax, (xc + 0.2, yc - 1.3), "cations (Ca²⁺, Na⁺)", size="tiny", ha="left")
        for side in (-1, 1):
            bio.arrow(ax, (xc + side * 1.5, 5.6), (xc + side * 2.3, 5.6), kind="process")
        bio.label(ax, (xc - 1.9, 6.0), "tension", size="tiny")
        bio.label(ax, (xc + 1.9, 6.0), "tension", size="tiny")
    bio.label(ax, (xc, 7.3), title, size="small", bold=True)
bio.label(ax, (0.8, 6.4), "Outside", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.8, 1.3), "Cytoplasm", size="tiny", ha="left", color=P.muted())

# ---- B: gating curves
bio.panel(ax, "B", (11.4, 8.2))
pb = charts.axes_at(ax, (13.0, 1.3, 9.2, 6.2))
kT = 1.380649e-23 * 310  # J
tau = np.linspace(0, 16, 400)  # mN/m
for name, th, dA, tok in (("Piezo1", 1.4, 6, "receptor"), ("MscS", 5.5, 8, "channel"), ("MscL", 10.0, 20, "negative")):
    x = (tau - th) * 1e-3 * dA * 1e-18 / kT
    pb.plot(tau, 1 / (1 + np.exp(-x)), color=charts.line(tok), lw=2.0, label=f"{name}: τ½ = {th} mN m⁻¹, ΔA = {dA} nm²")
pb.axvspan(12, 16, color=P.fill("negative"), alpha=0.15, lw=0)
pb.text(15.6, 0.04, "bilayer lysis", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
pb.set_xlim(0, 16)
pb.set_ylim(0, 1.03)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(pb, "membrane tension τ / (mN m⁻¹)", r"open probability $P_{\mathrm{o}}$")
charts.title(pb, "Two-state gating by tension")
