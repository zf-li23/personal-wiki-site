# Morphotypes of archaeal viruses, drawn to scale (1 unit = 50 nm) against a head-and-tail phage.
# Shapes are built from parametric outlines, not traced from any micrograph; dimensions follow the
# published particle sizes given in the text (SSV1 40x80 nm, SIFV 50x900-1500 nm, ATV ~100 nm body).
import numpy as np

import wikibio as bio

P = bio.P
NM = 1 / 50.0  # canvas units per nm
fig, ax = bio.canvas(19.4, 6.6)


def spindle(center, length_nm, width_nm, angle=90.0, token="virus", zorder=8, lw=1.1):
    """A lemon-shaped (fusiform) particle: |sin| profile sharpened to points at both ends."""
    t = np.linspace(0, np.pi, 160)
    u = (t / np.pi - 0.5) * length_nm * NM
    v = 0.5 * width_nm * NM * np.sin(t) ** 0.72
    pts = np.concatenate([np.stack([u, v], 1), np.stack([u[::-1], -v[::-1]], 1)])
    a = np.radians(angle - 90.0)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    pts = pts @ R.T + np.asarray(center)
    bio.shape(ax, pts, token=token, lw=lw, zorder=zorder)
    return pts


def rod(a, b, width_nm, token="virus", zorder=8, cap=0.5):
    """A rigid filament with rounded ends."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = np.hypot(*d)
    e = d / L
    n = np.array([-e[1], e[0]])
    w = 0.5 * width_nm * NM
    th = np.linspace(-np.pi / 2, np.pi / 2, 40)
    end_b = np.stack([b + w * cap * np.cos(t) * e + w * np.sin(t) * n for t in th])
    end_a = np.stack([a - w * cap * np.cos(t) * e - w * np.sin(t) * n for t in th])
    bio.shape(ax, np.concatenate([end_b, end_a]), token=token, lw=1.1, zorder=zorder)


# ------------------------------------------------------------------ SSV1, spindle with rosette
x = 2.1
spindle((x, 4.3), 80, 40)
for k, ang in enumerate((200, 260, 320)):
    a = np.radians(ang)
    spindle((x + 0.95 * np.cos(a), 4.3 + 0.95 * np.sin(a)), 80, 40, angle=np.degrees(a) + 90,
            token="virus", zorder=6, lw=0.8)
bio.label(ax, (x, 5.9), "SSV1", size="normal", bold=True)
bio.label(ax, (x, 5.5), "spindle, $40 \\times 80$ nm", size="tiny", color=P.muted())
bio.label(ax, (x, 2.45), "Sulfolobus solfataricus", size="tiny", color=P.muted(), italic=True)
bio.label(ax, (x, 2.0), "circular dsDNA, 15 kb;\nreleased in rosettes,\nwithout lysis",
          size="tiny", color=P.muted())

# ------------------------------------------------------------------ SIFV, rigid filament
x = 5.7
rod((x - 0.55, 2.9), (x + 0.55, 5.1), 50)
for s in np.linspace(0.08, 0.92, 9):          # the helical nucleoprotein inside
    p = np.array([x - 0.55, 2.9]) + s * np.array([1.1, 2.2])
    ax.plot([p[0] - 0.14, p[0] + 0.14], [p[1] - 0.03, p[1] + 0.03], color=P.edge("virus"), lw=0.7,
            zorder=9, solid_capstyle="round")
for end in ((x - 0.55, 2.9), (x + 0.55, 5.1)):  # terminal fibres
    for dx in (-0.12, 0.12):
        ax.plot([end[0], end[0] + dx * 1.6], [end[1], end[1] + (0.24 if end[1] > 4 else -0.24)],
                color=P.edge("virus"), lw=0.7, zorder=9)
bio.label(ax, (x, 5.9), "SIFV", size="normal", bold=True)
bio.label(ax, (x, 5.5), "filament, $50 \\times 900$ nm", size="tiny", color=P.muted())
bio.label(ax, (x, 2.45), "Sulfolobus solfataricus", size="tiny", color=P.muted(), italic=True)
bio.label(ax, (x, 2.0), "linear dsDNA; drawn short —\nthe particle is 20 times\nthis long",
          size="tiny", color=P.muted())

# ------------------------------------------------------------------ ABV, bottle-shaped
x = 9.3
t = np.linspace(0, 1, 120)
half = 0.5 * NM * (18 + 42 * t ** 1.6)                    # neck 18 nm, base 60 nm
yy = 3.25 + t * (75 * NM)
outline = np.concatenate([np.stack([x + half, yy], 1), np.stack([x - half[::-1], yy[::-1]], 1)])
bio.shape(ax, outline, token="virus", lw=1.1, zorder=8)
for k in range(7):                                        # filaments on the broad end
    ax.plot([x - 0.45 + 0.15 * k, x - 0.55 + 0.183 * k], [3.25, 2.85], color=P.edge("virus"), lw=0.7, zorder=7)
bio.label(ax, (x, 5.9), "ABV", size="normal", bold=True)
bio.label(ax, (x, 5.5), "bottle, $\\approx 75$ nm long", size="tiny", color=P.muted())
bio.label(ax, (x, 2.45), "Acidianus convivator", size="tiny", color=P.muted(), italic=True)
bio.label(ax, (x, 2.0), "asymmetric: a pointed neck,\na broad end carrying\nfilaments",
          size="tiny", color=P.muted())

# ------------------------------------------------------------------ ATV, development outside the cell
x = 13.6
spindle((x - 1.5, 4.3), 100, 62)
bio.label(ax, (x - 1.5, 3.4), "on release", size="tiny", color=P.muted())
spindle((x + 1.4, 4.3), 100, 44)
for s in (-1, 1):                                         # the two hollow tails
    rod((x + 1.4 + s * 0.5, 4.3), (x + 1.4 + s * 1.45, 4.3), 14, zorder=7)
bio.label(ax, (x + 1.4, 3.4), "after hours at $85\\,^\\circ$C, pH 1.5", size="tiny", color=P.muted())
bio.arrow(ax, (x - 0.8, 4.3), (x - 0.15, 4.3), kind="process")
bio.label(ax, (x, 5.9), "ATV", size="normal", bold=True)
bio.label(ax, (x, 5.5), "two-tailed spindle", size="tiny", color=P.muted())
bio.label(ax, (x, 2.45), "Acidianus convivator", size="tiny", color=P.muted(), italic=True)
bio.label(ax, (x, 2.0), "the tails grow outside any cell, with no host\nand no external energy source",
          size="tiny", color=P.muted())

# ------------------------------------------------------------------ a head-and-tail phage for scale
x = 18.0
bio.structures.virus(ax, (x, 4.75), r=0.65, kind="icosahedral", token="neutral", spikes=0, zorder=8)
ax.plot([x, x], [4.1, 3.25], color=P.edge("neutral"), lw=3.0, solid_capstyle="butt", zorder=7)
for dx in (-0.22, 0.0, 0.22):
    ax.plot([x + dx * 0.7, x + dx], [3.25, 2.95], color=P.edge("neutral"), lw=0.8, zorder=7)
bio.label(ax, (x, 5.9), "head and tail", size="normal", bold=True)
bio.label(ax, (x, 5.5), "for comparison", size="tiny", color=P.muted())
bio.label(ax, (x, 2.45), "the usual phage of", size="tiny", color=P.muted())
bio.label(ax, (x, 2.0), "Bacteria, and of halophilic\nand methanogenic Archaea", size="tiny", color=P.muted())

bio.scale_bar(ax, (0.9, 1.05), 100 * NM, "100 nm")
bio.label(ax, (10.4, 0.5),
          "all characterized archaeal viruses have DNA genomes, almost all double-stranded and circular",
          size="tiny", color=P.muted())
