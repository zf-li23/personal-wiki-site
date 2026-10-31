"""Stokes flow past a sphere of radius a (exact solution of the Stokes equations).
A: streamlines in the frame of the sphere (uniform flow U at infinity), coloured by speed;
the pattern is symmetric fore and aft, so reversing U reverses every streamline.
B: the same flow seen from the fluid at rest at infinity (sphere moving with velocity U):
fluid is dragged along over many radii.
C: decay of the disturbance velocity along the axis and in the equatorial plane: it falls as a/r
(the Stokeslet), far more slowly than the a^3/r^3 of inviscid potential flow."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.4))
fig.subplots_adjust(wspace=0.5, left=0.05, right=0.97, bottom=0.16, top=0.88)

g = np.linspace(-4, 4, 401)
Z, X = np.meshgrid(g, g)  # z along the flow, x across
R = np.maximum(np.hypot(Z, X), 1e-6)
ct, st = Z / np.maximum(R, 1e-9), np.abs(X) / np.maximum(R, 1e-9)


def field(frame):
    ur = np.cos(np.arctan2(np.abs(X), Z)) * (1 - 1.5 / R + 0.5 / R**3)
    ut = -np.sin(np.arctan2(np.abs(X), Z)) * (1 - 0.75 / R - 0.25 / R**3)
    if frame == "lab":
        ur = -(ur - ct)
        ut = -(ut + st)
    # Cartesian components (z, x)
    th = np.arctan2(np.abs(X), Z)
    uz = ur * np.cos(th) - ut * np.sin(th)
    ux = (ur * np.sin(th) + ut * np.cos(th)) * np.sign(X + 1e-12)
    inside = R < 1
    uz[inside] = np.nan; ux[inside] = np.nan
    return uz, ux


t = np.linspace(0, 2 * np.pi, 200)
for k, (frame, ttl) in enumerate((("sphere", "A  Frame of the sphere"), ("lab", "B  Frame of the distant fluid"))):
    ax = axs[k]
    uz, ux = field(frame)
    sp = np.hypot(uz, ux)
    im = ax.imshow(sp, extent=(-4, 4, -4, 4), origin="lower", cmap="Blues", vmin=0, vmax=1.0)
    ax.streamplot(g, g, uz, ux, color=P.ink(), linewidth=0.55, density=1.0, arrowsize=0.6)
    ax.fill(np.cos(t), np.sin(t), color=P.fill("bacterium"), ec=P.edge("bacterium"), lw=1, zorder=5)
    if frame == "lab":
        ax.annotate("", (2.0, 0), (1.05, 0), arrowprops=dict(arrowstyle="-|>", color=P.edge("negative"), lw=1.4), zorder=6)
        ax.text(1.6, 0.25, "U", color=P.edge("negative"), fontsize=bio.core.FONT["small"], zorder=6)
    ax.set_aspect("equal")
    charts.style_axes(ax, "z / a", "x / a")
    charts.title(ax, ttl)
cb = fig.colorbar(im, ax=axs[1], fraction=0.045, pad=0.03)
cb.ax.tick_params(labelsize=bio.core.FONT["tiny"], colors=P.muted(), labelcolor=P.ink())
cb.outline.set_edgecolor(P.muted())
cb.set_label("|u| / U", fontsize=bio.core.FONT["small"], color=P.ink())

ax = axs[2]
r = np.logspace(0, 2, 200)
ax.plot(r, 1.5 / r - 0.5 / r**3, color=charts.line("dna"), lw=1.7, label="Stokes, along the axis")
ax.plot(r, 0.75 / r + 0.25 / r**3, color=charts.line("blood"), lw=1.7, label="Stokes, equatorial plane")
ax.plot(r, 1 / r**3, color=P.muted(), lw=1.2, ls="--", label=r"potential flow, $(a/r)^3$")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "r / a", "disturbance speed / U")
charts.title(ax, "C  Long-ranged viscous wake")
