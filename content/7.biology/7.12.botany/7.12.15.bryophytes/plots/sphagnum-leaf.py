"""Leaf cells of Sphagnum (schematic). A: surface view: large, empty hyaline cells (dead, with helical wall
thickenings and pores) form the meshes of a net of narrow, living chlorophyllous cells. B: transverse
section: the chlorophyllous cells lie between the inflated hyaline cells, triangular to trapezoid in
section; the hyaline cells fill with water."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 13)


def ell(c, rx, ry, n=40):
    t = np.linspace(0, 2 * np.pi, n)
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


# ---------------- A: surface view ----------------
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (8.6, 12.3), "Leaf, surface view", size="normal", bold=True)
DX, DY = 2.4, 0.8  # tessellating rhombs: the green bands form a continuous net
for i in range(-1, 8):
    for j in range(-1, 15):
        cx = 2.0 + i * DX + (DX / 2 if j % 2 else 0)
        cy = 1.2 + j * DY
        if not (0.6 < cx < 16.4 and 0.8 < cy < 11.4):
            continue
        rh = np.array([[cx - 1.2, cy], [cx, cy + 0.8], [cx + 1.2, cy], [cx, cy - 0.8]])
        bio.shape(ax, rh, token="chloroplast", lw=0.5, zorder=3)
        inner = np.array([[cx - 0.98, cy], [cx, cy + 0.62], [cx + 0.98, cy], [cx, cy - 0.62]])
        bio.shape(ax, inner, token="extracellular", lw=0.8, zorder=4)
        for k in range(-3, 4):  # helical fibrils
            x = cx + k * 0.24
            h = 0.62 * (1 - abs(k * 0.24) / 0.98)
            ax.plot([x - 0.08, x + 0.08], [cy - h, cy + h], color=P.edge("vacuole"), lw=0.7, zorder=5)
        bio.shape(ax, ell((cx + 0.36, cy + 0.12), 0.11, 0.08), token="vacuole", lw=0.6, zorder=6)
        for dx, dy in ((-0.6, 0.4), (0.6, -0.4)):  # chloroplasts in the narrow cells
            bio.shape(ax, ell((cx + dx * 1.0, cy + dy * 1.0), 0.07, 0.05), token="thylakoid", lw=0.3, zorder=6)
c0 = (2.0 + 3 * DX, 1.2 + 6 * DY)
bio.callout(ax, (c0[0] - 0.2, c0[1]), (18.0, 9.8), "Hyaline cell (dead, stores water)", size="small")
bio.callout(ax, (c0[0] + 0.35, c0[1] + 0.12), (18.0, 8.8), "Pore", size="small")
bio.callout(ax, (c0[0] + 0.45, c0[1] - 0.25), (18.0, 7.8), "Helical thickening", size="small")
bio.callout(ax, (c0[0] + 0.6, c0[1] + 0.4), (18.0, 6.8), "Chlorophyllous cell (living)", size="small")

# ---------------- B: section ----------------
bio.panel(ax, "B", (17.8, 5.6))
bio.label(ax, (23.6, 5.2), "Leaf, transverse section", size="normal", bold=True)
y = 2.6
for k in range(5):
    x = 19.0 + k * 2.2
    bio.shape(ax, ell((x, y), 1.0, 0.85), token="extracellular", lw=0.9, zorder=4)
    for a in np.linspace(0.3, 2.8, 4):
        ax.plot([x + 0.9 * np.cos(a), x + 1.0 * np.cos(a)], [y + 0.75 * np.sin(a), y + 0.85 * np.sin(a)], color=P.edge("vacuole"),
                lw=0.8, zorder=5)
    if k < 4:
        xc = x + 1.1
        bio.shape(ax, [[xc - 0.25, y + 0.75], [xc + 0.25, y + 0.75], [xc, y - 0.1]], token="chloroplast", lw=0.8, zorder=6)
bio.callout(ax, (19.0 + 2 * 2.2, y - 0.3), (22.0, 0.6), "Hyaline cell", size="small")
bio.callout(ax, (19.0 + 1.1, y + 0.5), (19.2, 4.6), "Chlorophyllous cell", size="small")
