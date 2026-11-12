"""Three arrangements of the contractile filaments in animal muscle cells (schematic, not to scale).
A: cross-striated muscle; sarcomeres of neighbouring myofibrils lie in register, so the dark A bands and the
light I bands form transverse stripes; below, one sarcomere between two Z lines, thick myosin filaments in
the middle, thin actin filaments anchored at the Z lines. B: obliquely striated muscle (nematodes,
annelids, many molluscs); the sarcomeres of neighbouring myofilament rows are staggered, so the bands run
obliquely (helically around the cell); below, the staggered thick filaments and the dense bodies that take
the place of Z lines. C: smooth muscle; thick and thin filaments are not aligned, and the thin filaments are
anchored to dense bodies in the cytoplasm and at the membrane.
"""

import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 10.4)

THICK = P.edge("myosin")
THIN = P.edge("actin")
CELL_F = P.light("muscle")
CELL_E = P.edge("muscle")


def fiber(x0, y0, w, h):
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.35", facecolor=CELL_F,
                                edgecolor=CELL_E, lw=1.4, zorder=3))


def nucleus(c, rx, ry):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.9, zorder=8))


# ---------- A: cross-striated, bands in register
bio.panel(ax, "A", (0.3, 10.1))
bio.label(ax, (4.6, 9.75), "Cross-striated", size="title", bold=True)
x0, y0, w, h = 0.6, 5.6, 8.0, 3.2
fiber(x0, y0, w, h)
period = 1.0
for k in range(8):
    xa = x0 + 0.35 + k * period
    ax.add_patch(Polygon([(xa, y0 + 0.08), (xa + 0.55, y0 + 0.08), (xa + 0.55, y0 + h - 0.08), (xa, y0 + h - 0.08)],
                         closed=True, facecolor=P.fill("muscle"), edgecolor="none", zorder=4))
    zx = xa + 0.775
    if zx < x0 + w - 0.1:
        ax.plot([zx, zx], [y0 + 0.08, y0 + h - 0.08], color=CELL_E, lw=0.9, zorder=5)
for cx in (2.1, 5.3, 7.6):
    nucleus((cx, y0 + 0.32), 0.42, 0.17)
bio.callout(ax, (x0 + 0.62, y0 + h - 0.4), (1.2, 9.25), "A band", size="small")
bio.callout(ax, (x0 + 1.12, y0 + h - 0.4), (3.0, 9.25), "Z line", size="small")
bio.callout(ax, (5.3, y0 + 0.32), (6.9, 5.05), "Peripheral nuclei", size="small")

# sarcomere close-up
sy = 2.6
for zx in (1.4, 7.8):
    ax.plot([zx, zx], [sy - 1.2, sy + 1.2], color=CELL_E, lw=2.2, zorder=6)
for dy in (-0.8, 0.0, 0.8):
    ax.plot([2.9, 6.3], [sy + dy, sy + dy], color=THICK, lw=4.0, solid_capstyle="round", zorder=6)
for dy in (-1.05, -0.4, 0.4, 1.05):
    ax.plot([1.4, 3.9], [sy + dy, sy + dy], color=THIN, lw=1.4, zorder=5)
    ax.plot([5.3, 7.8], [sy + dy, sy + dy], color=THIN, lw=1.4, zorder=5)
bio.label(ax, (1.4, 0.95), "Z", size="small", bold=True)
bio.label(ax, (7.8, 0.95), "Z", size="small", bold=True)
bio.label(ax, (4.6, 0.95), "one sarcomere, about 2–3 µm", size="small", color=P.muted())
bio.callout(ax, (4.6, sy + 0.8), (4.6, 4.55), "Thick filament (myosin)", size="small")
bio.callout(ax, (2.2, sy - 1.05), (1.3, 0.2), "Thin filament (actin)", size="small")

# ---------- B: obliquely striated
bio.panel(ax, "B", (9.3, 10.1))
bio.label(ax, (13.6, 9.75), "Obliquely striated", size="title", bold=True)
x0 = 9.6
fiber(x0, y0, w, h)
skew = 1.4
for k in range(-2, 9):
    xa = x0 + 0.35 + k * period
    pts = [(xa, y0 + 0.08), (xa + 0.55, y0 + 0.08), (xa + 0.55 + skew, y0 + h - 0.08), (xa + skew, y0 + h - 0.08)]
    poly = Polygon(pts, closed=True, facecolor=P.fill("muscle"), edgecolor="none", zorder=4)
    ax.add_patch(poly)
    poly.set_clip_path(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.35", transform=ax.transData))
nucleus((13.6, y0 + h / 2), 0.55, 0.3)
bio.callout(ax, (13.6, y0 + h / 2), (16.0, 5.05), "Single nucleus", size="small")

# staggered rows of thick filaments with dense bodies
for r, dy in enumerate((-1.0, -0.33, 0.33, 1.0)):
    off = r * 0.55
    for s in range(3):
        xs = 9.9 + off + s * 2.5
        if xs + 1.6 <= 17.9:
            ax.plot([xs, xs + 1.6], [sy + dy, sy + dy], color=THICK, lw=4.0, solid_capstyle="round", zorder=6)
        xd = xs - 0.45
        if 9.7 <= xd <= 17.9:
            ax.add_patch(Ellipse((xd, sy + dy), 0.22, 0.34, facecolor=CELL_E, edgecolor=CELL_E, lw=0.6, zorder=7))
            ax.plot([xd - 0.85, xd + 0.85], [sy + dy + 0.12, sy + dy + 0.12], color=THIN, lw=1.3, zorder=5)
            ax.plot([xd - 0.85, xd + 0.85], [sy + dy - 0.12, sy + dy - 0.12], color=THIN, lw=1.3, zorder=5)
bio.callout(ax, (9.9 + 0.55 + 2.5 - 0.45, sy - 0.33), (11.0, 0.2), "Dense body (in place of a Z line)", size="small")
bio.label(ax, (13.9, 4.55), "Sarcomeres staggered from row to row", size="small", color=P.muted())

# ---------- C: smooth
bio.panel(ax, "C", (18.3, 10.1))
bio.label(ax, (22.6, 9.75), "Smooth", size="title", bold=True)
t = np.linspace(0, 1, 200)
cx, cy = 22.6, 7.2
xs = 18.8 + 7.6 * t
ys = 1.55 * np.sin(np.pi * t) ** 1.6
ax.add_patch(Polygon(np.r_[np.c_[xs, cy + ys], np.c_[xs[::-1], cy - ys[::-1]]], closed=True, facecolor=CELL_F,
                     edgecolor=CELL_E, lw=1.4, zorder=3))
nucleus((cx, cy), 1.1, 0.32)
rng = np.random.default_rng(3)
for _ in range(16):
    px = rng.uniform(19.9, 25.3)
    lim = 1.55 * np.sin(np.pi * (px - 18.8) / 7.6) ** 1.6 - 0.35
    py = cy + rng.uniform(-lim, lim)
    if abs(py - cy) < 0.4 and abs(px - cx) < 1.2:
        continue
    ang = rng.uniform(-0.5, 0.5)
    L = 0.8
    ax.plot([px - L / 2 * np.cos(ang), px + L / 2 * np.cos(ang)], [py - L / 2 * np.sin(ang), py + L / 2 * np.sin(ang)],
            color=THICK, lw=2.4, solid_capstyle="round", zorder=6)
for _ in range(9):
    px = rng.uniform(20.0, 25.2)
    lim = 1.55 * np.sin(np.pi * (px - 18.8) / 7.6) ** 1.6 - 0.3
    py = cy + rng.uniform(-lim, lim)
    if abs(py - cy) < 0.4 and abs(px - cx) < 1.2:
        continue
    ax.add_patch(Ellipse((px, py), 0.2, 0.2, facecolor=CELL_E, edgecolor=CELL_E, lw=0.5, zorder=7))
bio.callout(ax, (cx + 0.9, cy), (25.3, 5.05), "Central nucleus", size="small")
bio.label(ax, (22.6, 4.55), "Filaments not aligned; no striation", size="small", color=P.muted())

# legend
ax.plot([19.4, 20.4], [2.9, 2.9], color=THICK, lw=4.0, solid_capstyle="round")
bio.label(ax, (20.7, 2.9), "Myosin (thick) filament", size="small", ha="left")
ax.plot([19.4, 20.4], [2.1, 2.1], color=THIN, lw=1.4)
bio.label(ax, (20.7, 2.1), "Actin (thin) filament", size="small", ha="left")
ax.add_patch(Ellipse((19.9, 1.3), 0.22, 0.3, facecolor=CELL_E, edgecolor=CELL_E))
bio.label(ax, (20.7, 1.3), "Z line or dense body", size="small", ha="left")
