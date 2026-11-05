# Root symbioses, schematic anatomy. (A) Indeterminate legume nodule (e.g. pea, alfalfa), longitudinal
# section: apical meristem, infection zone, nitrogen-fixation zone (large infected cells interspersed with
# small uninfected cells) and basal senescence zone; vascular bundles run in the nodule periphery,
# inside the nodule cortex, and join the stele of the parent root. (B) Ectomycorrhiza (e.g. pine) in
# transverse section: a hyphal mantle around the root and the Hartig net between epidermal and outer
# cortical cells; no hyphae inside cells, no root hairs. (C) Arbuscular mycorrhiza (e.g. maize) in
# longitudinal section: an extraradical hypha forms an appressorium, enters the root, spreads between
# cortical cells and forms arbuscules inside inner cortical cells and lipid-filled vesicles; spores in soil.
import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(37.6, 14.0)
rng = np.random.default_rng(1)
HY = P.edge("lipid_tail")

# ---- A: nodule
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (0.85, 13.77), "Indeterminate nodule", size="title", ha="left", va="top")
# parent root (horizontal band at the bottom)
ax.add_patch(FancyBboxPatch((0.6, 1.0), 9.6, 1.6, boxstyle="round,pad=0,rounding_size=0.6", facecolor=P.fill("cytoplasm"),
                            edgecolor=P.edge("cell_wall"), lw=1.0, zorder=3))
ax.add_patch(FancyBboxPatch((0.6, 1.6), 9.6, 0.4, boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill("xylem"),
                            edgecolor=P.edge("xylem"), lw=0.6, zorder=3.5))
bio.label(ax, (1.0, 0.55), "parent root (stele)", size="tiny", color=P.muted(), ha="left")
# nodule body: cylinder rising from the root
cx = 5.4
outline = bio.smooth_closed([(cx - 1.9, 2.4), (cx - 2.1, 6.0), (cx - 1.8, 9.6), (cx - 0.9, 11.6), (cx, 12.0), (cx + 0.9, 11.6),
                             (cx + 1.8, 9.6), (cx + 2.1, 6.0), (cx + 1.9, 2.4)], n=240)
ax.add_patch(Polygon(outline, closed=True, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=1.2, zorder=4))
zones = [(10.6, 11.8, "highlight", "Meristem (I)"), (9.0, 10.6, "plant", "Infection zone (II)"),
         (4.6, 9.0, "negative", "Fixation zone (III)"), (2.6, 4.6, "neutral", "Senescence zone (IV)")]
inner = lambda y: 1.35 if y < 10 else 1.35 * max(0.2, (11.9 - y) / 1.9)
for y0, y1, tok, name in zones:
    ys = np.linspace(y0, y1, 30)
    xs = np.array([inner(y) for y in ys])
    poly = np.vstack([np.c_[cx - xs, ys], np.c_[cx + xs, ys][::-1]])
    ax.add_patch(Polygon(poly, closed=True, facecolor=P.light(tok) if tok != "negative" else P.fill(tok), edgecolor=P.edge(tok),
                         lw=0.6, zorder=5))
    bio.callout(ax, (cx + 0.6, (y0 + y1) / 2), (11.0, (y0 + y1) / 2), name, size="small")
# infected cells in the fixation zone (large, dotted with bacteroids) and small uninfected cells
for y in np.arange(5.0, 8.8, 0.75):
    for x in np.arange(cx - 1.05, cx + 1.1, 0.7):
        if rng.random() < 0.75:
            ax.add_patch(Circle((x, y), 0.3, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.5, zorder=6))
            for _ in range(5):
                ax.add_patch(Circle((x + rng.uniform(-0.15, 0.15), y + rng.uniform(-0.15, 0.15)), 0.04, color=P.edge("bacterium"),
                                    zorder=6.5))
        else:
            ax.add_patch(Circle((x, y), 0.15, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=0.5, zorder=6))
for sg in (-1, 1):  # peripheral vascular bundles
    vb = np.c_[cx + sg * np.r_[1.6, 1.62, 1.55, 1.3, 0.9], [1.9, 5.0, 8.0, 10.0, 11.0]]
    ax.plot(vb[:, 0], vb[:, 1], color=P.edge("xylem"), lw=2.2, zorder=6)
bio.callout(ax, (cx - 1.62, 6.5), (0.9, 7.5), "Peripheral vascular bundle", size="small")
bio.callout(ax, (cx - 1.95, 4.0), (0.9, 4.0), "Nodule cortex", size="small")

# ---- B: ectomycorrhiza, transverse section
bio.panel(ax, "B", (13.6, 13.8))
bio.label(ax, (14.25, 13.77), "Ectomycorrhiza", size="title", ha="left", va="top")
c = np.array([18.4, 6.8])
ax.add_patch(Circle(c, 4.0, facecolor=P.fill("lipid_tail"), edgecolor=HY, lw=1.0, zorder=2))  # mantle
for k in range(900):  # mantle texture
    a = rng.uniform(0, 2 * math.pi)
    r = rng.uniform(3.45, 3.98)
    t = a + rng.uniform(-0.12, 0.12)
    ax.plot([c[0] + r * math.cos(a), c[0] + r * math.cos(t)], [c[1] + r * math.sin(a), c[1] + r * math.sin(t)], color=HY, lw=0.4,
            zorder=2.5)
ax.add_patch(Circle(c, 3.42, facecolor=HY, edgecolor="none", zorder=2.8))  # hyphae in the walls (Hartig net)
for ring_r, n, tok in ((3.05, 26, "cell_wall"), (2.4, 20, "cytoplasm"), (1.75, 15, "cytoplasm")):
    for i in range(n):
        a = 2 * math.pi * (i + 0.5 * (ring_r < 3)) / n
        w = 2 * math.pi * ring_r / n
        ax.add_patch(Ellipse((c[0] + ring_r * math.cos(a), c[1] + ring_r * math.sin(a)), w * 0.86, 0.58, angle=math.degrees(a) + 90,
                             facecolor=P.fill(tok), edgecolor=P.edge("cell_wall"), lw=0.6, zorder=3))
ax.add_patch(Circle(c, 1.4, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("endodermis"), lw=1.4, zorder=3))
ax.add_patch(Circle(c, 1.2, facecolor=P.fill("pericycle"), edgecolor="none", zorder=3.1))
for i in range(4):
    a = math.pi / 4 + i * math.pi / 2
    ax.add_patch(Polygon([c, c + 1.0 * np.array([math.cos(a + 0.25), math.sin(a + 0.25)]),
                          c + 1.0 * np.array([math.cos(a - 0.25), math.sin(a - 0.25)])], facecolor=P.fill("xylem"),
                         edgecolor=P.edge("xylem"), lw=0.5, zorder=3.2))
for i in range(8):  # extramatrical hyphae
    a = 2 * math.pi * i / 8 + 0.2
    p = c + 4.0 * np.array([math.cos(a), math.sin(a)])
    q = c + 4.9 * np.array([math.cos(a + 0.1), math.sin(a + 0.1)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=HY, lw=1.0, zorder=2)
bio.callout(ax, tuple(c + 3.75 * np.array([0.6, 0.8])), (24.2, 12.6), "Hyphal mantle", size="small")
bio.callout(ax, tuple(c + 2.75 * np.array([0.87, 0.5])), (24.2, 11.6), "Hartig net (between cells)", size="small")
bio.callout(ax, tuple(c + 3.05 * np.array([1.0, 0.0])), (24.2, 7.4), "Epidermis", size="small")
bio.callout(ax, tuple(c + 2.4 * np.array([0.8, -0.6])), (24.2, 4.4), "Cortex", size="small")
bio.callout(ax, tuple(c + 0.5 * np.array([0.0, -1.0])), (24.2, 2.0), "Stele", size="small")

# ---- C: arbuscular mycorrhiza, longitudinal section
bio.panel(ax, "C", (28.40, 13.8))
bio.label(ax, (29.05, 13.77), "Arbuscular mycorrhiza", size="title", ha="left", va="top")
x0, x1 = 31.0, 37.0
rows = [(9.7, "cell_wall", 0.6), (8.6, "cytoplasm", 1.0), (7.5, "cytoplasm", 1.0), (6.4, "cytoplasm", 1.0), (5.6, "endodermis", 0.7)]
cells = {}
for r, (y, tok, h) in enumerate(rows):
    n = 5
    w = (x1 - x0) / n
    for i in range(n):
        ax.add_patch(FancyBboxPatch((x0 + i * w + 0.04, y), w - 0.08, h - 0.08, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=P.fill(tok), edgecolor=P.edge("cell_wall"), lw=0.7, zorder=3))
        cells[(r, i)] = (x0 + i * w + w / 2, y + h / 2, w, h)
# extraradical hypha and appressorium
ext = np.array([(28.80, 11.6), (30.40, 11.0), (32.30, 10.45)])
ax.plot(ext[:, 0], ext[:, 1], color=HY, lw=1.6, zorder=6)
ax.add_patch(Ellipse((32.40, 10.38), 0.5, 0.25, facecolor=P.fill("lipid_tail"), edgecolor=HY, lw=0.8, zorder=6.5))
ax.add_patch(Circle((29.40, 12.5), 0.42, facecolor=P.fill("lipid_tail"), edgecolor=HY, lw=1.0, zorder=6))  # spore
ax.plot([29.7, 30.6], [12.2, 11.0], color=HY, lw=1.0, zorder=6)
# intercellular hypha down through the epidermis and along the cortex
w = (x1 - x0) / 5
path = np.array([(32.40, 10.3), (32.4, 9.6), (x0 + w * 2, 9.0), (x0 + w * 2, 7.45), (x0 + w * 4.0, 7.45)])
ax.plot(path[:, 0], path[:, 1], color=HY, lw=1.4, zorder=6)
path2 = np.array([(x0 + w * 2, 8.0), (x0 + w * 1, 7.45), (x0 + w * 0.2, 7.45)])
ax.plot(path2[:, 0], path2[:, 1], color=HY, lw=1.4, zorder=6)


def arbuscule(cxy):
    x, y = cxy
    tips = [(x, y - 0.05)]
    ax.plot([x, x], [y - 0.4, y - 0.05], color=HY, lw=1.0, zorder=7)
    for lvl in range(3):
        new = []
        for (tx, ty) in tips:
            for sg in (-1, 1):
                nx, ny = tx + sg * 0.22 / (lvl + 1), ty + 0.15
                ax.plot([tx, nx], [ty, ny], color=HY, lw=1.0 - 0.25 * lvl, zorder=7)
                new.append((nx, ny))
        tips = new


for i in (1, 3):
    arbuscule((cells[(3, i)][0], cells[(3, i)][1] - 0.1))
for i in (0, 4):
    arbuscule((cells[(2, i)][0], cells[(2, i)][1] - 0.1))
ax.add_patch(Ellipse((cells[(2, 2)][0], cells[(2, 2)][1]), 0.6, 0.42, facecolor=P.fill("lipid"), edgecolor=HY, lw=1.0, zorder=7))
bio.callout(ax, (cells[(3, 3)][0], cells[(3, 3)][1] + 0.2), (35.60, 4.6), "Arbuscule (in cell)", size="small")
bio.callout(ax, (cells[(2, 2)][0] + 0.3, cells[(2, 2)][1]), (33.40, 4.6), "Vesicle", size="small")
bio.callout(ax, (32.40, 10.38), (34.20, 11.7), "Appressorium", size="small")
bio.callout(ax, (29.40, 12.5), (31.00, 13.0), "Spore", size="small")
bio.callout(ax, (x0 + w * 3.3, 7.45), (36.00, 3.6), "Intercellular hypha", size="small")
bio.label(ax, (x0 - 0.2, 10.0), "Epidermis", size="tiny", ha="right", color=P.muted())
bio.label(ax, (x0 - 0.2, 7.5), "Cortex", size="tiny", ha="right", color=P.muted())
bio.label(ax, (x0 - 0.2, 5.9), "Endodermis", size="tiny", ha="right", color=P.muted())
