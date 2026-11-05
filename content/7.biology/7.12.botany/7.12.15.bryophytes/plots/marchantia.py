"""Marchantia polymorpha (schematic). A: female and male thalli (side view): forked thallus with gemma cups;
the male plant bears a stalked, disc-shaped antheridiophore, the female plant an umbrella-like
archegoniophore with finger-like rays. B: transverse section of the thallus: upper epidermis with a
barrel-shaped (chimney) pore that cannot close, air chambers with photosynthetic filaments, storage
parenchyma with oil cells, lower epidermis, scales and unicellular rhizoids. C: archegoniophore in
section: sporophytes hang beneath the disc; each has a foot, a short seta and a capsule with spores and
elaters."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34, 13)


def ell(c, rx, ry, a0=0, a1=360, n=60):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def thallus(x0, y, length):
    pts = [[x0, y], [x0 + length * 0.45, y + 0.35], [x0 + length * 0.55, y + 0.1], [x0 + length, y + 0.5],
           [x0 + length * 0.98, y + 0.1], [x0 + length * 0.6, y - 0.25], [x0 + length * 0.1, y - 0.3]]
    bio.shape(ax, bio.smooth_closed(pts), token="plant", lw=1.0, zorder=4)
    for k in range(6):
        xx = x0 + 0.3 + k * length / 6.5
        ax.plot([xx, xx - 0.15], [y - 0.3, y - 0.9], color=P.muted(), lw=0.7, zorder=3)


def cup(x, y):
    bio.shape(ax, [[x - 0.35, y + 0.45], [x - 0.2, y], [x + 0.2, y], [x + 0.35, y + 0.45]], token="plant", lw=0.9, zorder=6)
    for dx in (-0.12, 0.0, 0.12):
        bio.shape(ax, ell((x + dx, y + 0.3), 0.08, 0.08), token="chloroplast", lw=0.5, zorder=7)


# ---------------- A ----------------
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (5.6, 12.3), "Female and male gametophytes", size="normal", bold=True)
thallus(0.8, 2.6, 4.6)
cup(2.0, 2.9)
ax.plot([3.6, 3.7], [2.9, 7.6], color=P.edge("plant"), lw=2.6, zorder=5)
bio.shape(ax, ell((3.7, 7.75), 0.8, 0.3, 0, 180).tolist() + [[2.9, 7.75]], token="plant", lw=1.0, zorder=6)
for k in range(9):
    a = np.radians(200 + k * 17.5)
    x = 3.7 + 0.75 * np.cos(np.radians(180 - k * 22.5))
    ax.plot([x, x + 0.15 * np.cos(a)], [7.7, 7.0 - 0.1 * (k % 2)], color=P.edge("plant"), lw=2.2, zorder=6, solid_capstyle="round")
bio.label(ax, (3.0, 1.2), "Female", size="small", bold=True)
bio.callout(ax, (4.4, 7.4), (5.4, 9.2), "Archegoniophore", size="small")
bio.callout(ax, (2.0, 3.1), (1.3, 5.3), "Gemma cup", size="small")
thallus(6.4, 2.6, 4.6)
cup(7.6, 2.9)
ax.plot([9.2, 9.3], [2.9, 6.6], color=P.edge("plant"), lw=2.6, zorder=5)
disc = [[9.3 + 0.9 * np.cos(a), 6.8 + 0.22 * np.sin(a) + 0.08 * np.cos(8 * a)] for a in np.linspace(0, 2 * np.pi, 80)]
bio.shape(ax, disc, token="plant", lw=1.0, zorder=6)
bio.label(ax, (8.6, 1.2), "Male", size="small", bold=True)
bio.callout(ax, (10.0, 6.85), (10.6, 9.2), "Antheridiophore", size="small")
bio.callout(ax, (8.5, 2.2), (9.6, 0.6), "Rhizoids", size="small")

# ---------------- B: section ----------------
bio.panel(ax, "B", (12.0, 12.8))
bio.label(ax, (17.6, 12.3), "Thallus, transverse section", size="normal", bold=True)
X0, X1 = 13.0, 22.4
YT = 10.2
# upper epidermis
for i in range(24):
    x = X0 + i * (X1 - X0) / 24
    bio.shape(ax, [[x, YT - 0.32], [x + 0.39, YT - 0.32], [x + 0.39, YT], [x, YT]], token="cell_wall", lw=0.6, zorder=5)
# air chambers
for j in range(3):
    xa = X0 + 0.3 + j * 3.1
    bio.shape(ax, [[xa, YT - 2.4], [xa + 2.8, YT - 2.4], [xa + 2.8, YT - 0.32], [xa, YT - 0.32]], token="extracellular", lw=0.9,
              zorder=4)
    for f in range(6):
        fx = xa + 0.3 + f * 0.45
        for c in range(3):
            bio.shape(ax, ell((fx, YT - 2.2 + c * 0.32), 0.15, 0.15), token="chloroplast", lw=0.5, zorder=6)
    px = xa + 1.4
    for lev in range(4):  # chimney pore, 4 tiers
        for sg in (-1, 1):
            bio.shape(ax, ell((px + sg * 0.32, YT + 0.12 + lev * 0.16 - 0.3), 0.14, 0.09), token="cell_wall", lw=0.5, zorder=7)
    ax.plot([xa, xa], [YT - 2.4, YT - 0.32], color=P.edge("chloroplast"), lw=1.0, zorder=6)
# storage parenchyma
for r in range(4):
    for i in range(12):
        x = X0 + i * (X1 - X0) / 12 + (0.35 if r % 2 else 0)
        if x + 0.7 > X1:
            continue
        tok = "lipid" if (r, i) in ((1, 3), (2, 8)) else "cytoplasm"
        bio.shape(ax, ell((x + 0.39, YT - 2.85 - r * 0.72), 0.38, 0.34), token=tok, lw=0.6, zorder=5)
# lower epidermis, scales and rhizoids
YL = YT - 5.6
for i in range(24):
    x = X0 + i * (X1 - X0) / 24
    bio.shape(ax, [[x, YL - 0.28], [x + 0.39, YL - 0.28], [x + 0.39, YL], [x, YL]], token="cell_wall", lw=0.6, zorder=5)
for k in range(9):
    x = X0 + 0.6 + k * 1.0
    if k % 3 == 1:
        bio.shape(ax, [[x - 0.2, YL - 0.28], [x + 0.3, YL - 0.28], [x + 0.5, YL - 1.2]], token="animal", lw=0.7, zorder=4)
    else:
        t = np.linspace(0, 1, 20)
        ax.plot(x + 0.15 * np.sin(t * 5), YL - 0.28 - t * 2.2, color=P.muted(), lw=0.9, zorder=4)
bio.callout(ax, (X0 + 1.7, YT + 0.25), (X0 + 0.3, YT + 1.4), "Chimney pore (no guard cells)", size="small")
bio.callout(ax, (X0 + 4.5, YT - 1.4), (X0 + 4.6, YT + 1.4), "Air chamber", size="small")
bio.callout(ax, (X0 + 7.2, YT - 1.9), (X1 + 0.3, YT - 0.8), "Photosynthetic filaments", size="small")
bio.callout(ax, (X1 - 0.7, YT - 0.15), (X1 + 0.3, YT + 0.5), "Upper epidermis", size="small")
bio.callout(ax, (X1 - 1.5, YT - 3.6), (X1 + 0.3, YT - 3.0), "Storage parenchyma", size="small")
bio.callout(ax, (X0 + 5.9, YT - 3.57), (X1 + 0.3, YT - 4.2), "Oil cell", size="small")
bio.callout(ax, (X1 - 0.5, YL - 0.15), (X1 + 0.3, YL - 0.4), "Lower epidermis", size="small")
bio.callout(ax, (X0 + 1.8, YL - 0.8), (X0 + 0.0, YL - 2.6), "Scale", size="small")
bio.callout(ax, (X0 + 5.75, YL - 1.6), (X0 + 6.8, YL - 2.6), "Rhizoids (unicellular)", size="small")

# ---------------- C: archegoniophore ----------------
bio.panel(ax, "C", (26.6, 12.8))
bio.label(ax, (30.4, 12.3), "Archegoniophore, section", size="normal", bold=True)
cx, cy = 30.4, 8.6
ax.plot([cx, cx], [2.0, cy - 0.5], color=P.edge("plant"), lw=3.0, zorder=4)
bio.shape(ax, ell((cx, cy - 0.2), 2.4, 1.0, 0, 180).tolist() + [[cx - 2.4, cy - 0.5], [cx + 2.4, cy - 0.5]], token="plant", lw=1.0,
          zorder=5)
for sg in (-1, 1):
    ax.plot([cx + sg * 2.3, cx + sg * 2.8], [cy - 0.4, cy - 1.6], color=P.edge("plant"), lw=2.4, zorder=5, solid_capstyle="round")
for k, dx in enumerate((-1.4, -0.5, 0.5, 1.4)):
    x = cx + dx
    ax.plot([x, x], [cy - 0.5, cy - 0.85], color=P.edge("receptor"), lw=2.0, zorder=6)  # foot + seta
    bio.shape(ax, ell((x, cy - 0.65), 0.12, 0.14), token="receptor", lw=0.6, zorder=7)
    bio.shape(ax, ell((x, cy - 1.45), 0.36, 0.5), token="animal", lw=0.9, zorder=7)
    for s in range(5):
        bio.shape(ax, ell((x - 0.15 + 0.08 * s, cy - 1.3 - 0.13 * (s % 3)), 0.05, 0.05), token="lipid", lw=0.3, zorder=8)
    t = np.linspace(0, 1, 15)
    ax.plot(x - 0.1 + 0.2 * t, cy - 1.6 + 0.05 * np.sin(t * 20), color=P.edge("animal"), lw=0.6, zorder=8)
bio.callout(ax, (cx + 1.4, cy - 1.45), (cx + 2.0, cy - 3.3), "Capsule: spores\nand elaters", size="small")
bio.callout(ax, (cx + 0.5, cy - 0.65), (cx + 2.4, cy + 1.4), "Foot", size="small")
bio.callout(ax, (cx - 0.5, cy - 0.85), (cx - 2.4, cy - 3.3), "Short seta", size="small")
bio.callout(ax, (cx - 2.7, cy - 1.4), (cx - 2.6, cy + 1.6), "Ray", size="small")
bio.callout(ax, (cx, 4.0), (cx + 1.2, 3.0), "Stalk", size="small")
