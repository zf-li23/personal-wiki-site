# Annelid body organization (schematic, not to scale). A: transverse section of an earthworm trunk segment,
# layers coloured by germ layer (zoology.body_plan), with the typhlosole, blood vessels, nerve cord, a ring of
# chaetae (perichaetine, as in Amynthas) and a nephridium. B: longitudinal view of four trunk segments: septa,
# a metanephridium whose nephrostome opens in one segment and whose pore lies on the next, ganglia of the
# ventral nerve cord, dorsal and ventral vessels with the direction of blood flow. C: a polychaete parapodium.
import numpy as np
from matplotlib.patches import Polygon
import wikibio as bio
from wikibio import zoology as zoo

P = bio.P
fig, ax = bio.canvas(30, 11.6)


def disc(c, r, token, z=30, lw=0.9):
    t = np.linspace(0, 2 * np.pi, 60)
    ax.fill(c[0] + r * np.cos(t), c[1] + r * np.sin(t), facecolor=P.fill(token), edgecolor=P.edge(token), lw=lw, zorder=z)


# ---------------- A: transverse section ----------------
bio.panel(ax, "A", (0.2, 11.3))
bio.label(ax, (5.4, 11.0), "Transverse section", size="normal", bold=True)
c, r = (5.4, 5.6), 3.6
a = zoo.body_plan(ax, c, r, "coelomate")
cx, cy = c
# typhlosole: dorsal infolding of the gut wall into the lumen
ty = np.array([[-0.09, 0.35], [-0.07, 0.05], [0.0, -0.02], [0.07, 0.05], [0.09, 0.35]]) * r + c
bio.shape(ax, np.vstack([ty, [[cx + 0.06 * r, cy + 0.36 * r], [cx - 0.06 * r, cy + 0.36 * r]]]), token="endoderm", zorder=28)
# chloragogen cells on the splanchnic layer
for th in np.linspace(0.15, 2 * np.pi - 0.15, 26):
    if abs(np.sin(th)) > 0.97:
        continue
    p = (cx + 0.455 * r * np.cos(th), cy + 0.455 * r * np.sin(th))
    disc(p, 0.05 * r, "lipid", z=29, lw=0.5)
disc((cx, cy + 0.50 * r), 0.075 * r, "blood")               # dorsal vessel
disc((cx, cy - 0.50 * r), 0.06 * r, "blood")                # ventral vessel
disc((cx, cy - 0.66 * r), 0.075 * r, "neuron")              # ventral nerve cord
disc((cx, cy - 0.765 * r), 0.03 * r, "blood", z=31)         # subneural vessel
# chaetae: a ring of short rods through the body wall
for th in np.linspace(0, 2 * np.pi, 40, endpoint=False):
    if np.sin(th) > 0.9:
        continue
    ax.plot([cx + 0.88 * r * np.cos(th), cx + 1.1 * r * np.cos(th)], [cy + 0.88 * r * np.sin(th), cy + 1.1 * r * np.sin(th)],
            color=P.edge("neutral"), lw=1.2, zorder=32, solid_capstyle="round")
# nephridium: coiled tubule in the coelom with a duct to a ventrolateral pore
t = np.linspace(0, 3 * np.pi, 120)
nx = cx - 0.42 * r + 0.06 * r * np.cos(t) + 0.02 * r * t
ny = cy - 0.40 * r + 0.08 * r * np.sin(t)
ax.plot(nx, ny, color=P.edge("enzyme"), lw=1.6, zorder=33)
ax.plot([nx[-1], cx - 0.62 * r], [ny[-1], cy - 0.78 * r], color=P.edge("enzyme"), lw=1.6, zorder=33)
L = cx - 4.6
bio.callout(ax, (cx - 0.97 * r * 0.6, cy + 0.97 * r * 0.8), (L, 10.2), "Cuticle and epidermis")
bio.callout(ax, (cx - 0.80 * r * 0.75, cy + 0.80 * r * 0.66), (L, 9.5), "Circular and longitudinal muscle")
bio.callout(ax, (cx - 0.6 * r * 0.8, cy + 0.6 * r * 0.6), (L, 8.8), "Coelom (paired, per segment)")
bio.callout(ax, (cx - 0.455 * r * 0.98, cy + 0.455 * r * 0.2), (L, 8.1), "Chloragogen tissue")
bio.callout(ax, (cx - 0.39 * r, cy - 0.1 * r), (L, 6.4), "Splanchnic mesoderm")
bio.callout(ax, (cx - 0.28 * r, cy + 0.02 * r), (L, 5.7), "Gut epithelium")
bio.callout(ax, (cx - 0.39 * r, cy - 0.40 * r), (L, 3.6), "Nephridium")
bio.callout(ax, (cx - 1.05 * r * 0.8, cy - 1.05 * r * 0.6), (L, 2.4), "Chaeta")
R = cx + 4.4
bio.callout(ax, (cx, cy + 0.56 * r), (R, 10.2), "Dorsal vessel")
bio.callout(ax, (cx + 0.6 * r * 0.05, cy + 0.66 * r), (R, 9.5), "Dorsal mesentery")
bio.callout(ax, (cx + 0.05 * r, cy + 0.15 * r), (R, 7.6), "Typhlosole")
bio.callout(ax, (cx + 0.12 * r, cy - 0.08 * r), (R, 6.8), "Gut lumen")
bio.callout(ax, (cx + 0.04 * r, cy - 0.50 * r), (R, 3.6), "Ventral vessel")
bio.callout(ax, (cx + 0.06 * r, cy - 0.66 * r), (R, 2.9), "Ventral nerve cord")
bio.callout(ax, (cx + 0.02 * r, cy - 0.77 * r), (R, 2.2), "Subneural vessel")
zoo.germ_layer_legend(ax, (1.0, 0.5), items=("ectoderm", "mesoderm", "endoderm"), cavities=("coelom",), step=2.4, size="tiny")

# ---------------- B: longitudinal view of four segments ----------------
bio.panel(ax, "B", (11.6, 11.3))
bio.label(ax, (16.6, 11.0), "Four trunk segments (side view, anterior left)", size="normal", bold=True)
x0, x1, yb, yt = 12.4, 21.2, 2.6, 8.4
seg = (x1 - x0) / 4
bio.shape(ax, [[x0, yb], [x1, yb], [x1, yt], [x0, yt]], token="ectoderm", zorder=5, lw=0.9)
bio.shape(ax, [[x0, yb + 0.25], [x1, yb + 0.25], [x1, yt - 0.25], [x0, yt - 0.25]], token="coelom", zorder=6, lw=0.6)
bio.shape(ax, [[x0, 4.7], [x1, 4.7], [x1, 6.3], [x0, 6.3]], token="endoderm", zorder=8, lw=0.8)
bio.label(ax, ((x0 + x1) / 2, 5.5), "Gut", size="small", color=P.on_fill(), zorder=30)
for k in range(5):
    xs = x0 + k * seg
    if 0 < k < 4:
        ax.plot([xs, xs], [yb + 0.25, 4.7], color=P.edge("mesoderm"), lw=2.2, zorder=9)
        ax.plot([xs, xs], [6.3, yt - 0.25], color=P.edge("mesoderm"), lw=2.2, zorder=9)
    if k < 4:
        xm = xs + seg / 2
        for yy, d in ((yt, 1), (yb, -1)):       # chaetae
            ax.plot([xm - 0.15, xm - 0.05], [yy - 0.05 * d, yy + 0.3 * d], color=P.edge("neutral"), lw=1.2, zorder=12)
            ax.plot([xm + 0.05, xm + 0.15], [yy - 0.05 * d, yy + 0.3 * d], color=P.edge("neutral"), lw=1.2, zorder=12)
        disc((xm, 3.15), 0.22, "neuron", z=14)  # ganglion
ax.plot([x0, x1], [3.15, 3.15], color=P.edge("neuron"), lw=3.0, zorder=13)
ax.plot([x0, x1], [7.25, 7.25], color=P.fill("blood"), lw=4.0, zorder=13)
ax.plot([x0, x1], [4.15, 4.15], color=P.fill("blood"), lw=3.0, zorder=13)
for k in range(4):                               # segmental vessels
    xm = x0 + (k + 0.5) * seg
    ax.plot([xm + 0.55, xm + 0.55], [4.15, 4.7], color=P.fill("blood"), lw=1.5, zorder=12)
    ax.plot([xm + 0.55, xm + 0.55], [6.3, 7.25], color=P.fill("blood"), lw=1.5, zorder=12)
bio.arrow(ax, (x1 - 0.6, 7.65), (x1 - 2.2, 7.65), kind="process", lw=1.0)
bio.label(ax, (x1 - 1.4, 7.95), "blood forward", size="tiny", color=P.muted())
bio.arrow(ax, (x0 + 0.6, 3.75), (x0 + 2.2, 3.75), kind="process", lw=1.0)
bio.label(ax, (x0 + 1.4, 3.5), "blood backward", size="tiny", color=P.muted())
# one metanephridium: funnel in segment 2, tubule through septum into segment 3, pore ventral
xs2 = x0 + 2 * seg
fx, fy = xs2 - 0.35, 3.9
ax.add_patch(Polygon(
    [[fx - 0.25, fy + 0.25], [fx + 0.25, fy + 0.25], [fx + 0.05, fy - 0.05], [fx - 0.05, fy - 0.05]],
    closed=True, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.9, zorder=20))
tt = np.linspace(0, 1, 120)
px = fx + 0.05 + tt * (seg * 0.75)
py = fy - 0.05 + 0.25 * np.sin(tt * 6 * np.pi) - tt * 0.9
ax.plot(px, py, color=P.edge("enzyme"), lw=1.6, zorder=20)
ax.plot([px[-1], px[-1]], [py[-1], yb], color=P.edge("enzyme"), lw=1.6, zorder=20)
bio.callout(ax, (fx, fy + 0.2), (14.0, 1.4), "Nephrostome (ciliated funnel)")
bio.callout(ax, (px[-1], yb + 0.02), (19.6, 1.4), "Nephridiopore on the next segment")
bio.callout(ax, (x0 + seg, 7.9), (13.2, 9.6), "Septum")
bio.callout(ax, (x0 + 2.5 * seg, 7.25), (17.6, 9.6), "Dorsal vessel")
bio.callout(ax, (x0 + 3.5 * seg, 4.15), (22.2, 4.6), "Ventral vessel")
bio.callout(ax, (x0 + 3.5 * seg + 0.2, 3.15), (22.2, 3.2), "Segmental ganglion")
bio.callout(ax, (x0 + 3.5 * seg + 0.1, yt + 0.25), (21.6, 9.6), "Chaetae")

# ---------------- C: parapodium ----------------
bio.panel(ax, "C", (23.4, 11.3))
bio.label(ax, (26.6, 11.0), "Polychaete parapodium", size="normal", bold=True)
bc = (24.6, 6.0)
t = np.linspace(-np.pi / 2, np.pi / 2, 60)
body = np.c_[bc[0] + 1.3 * np.cos(t), bc[1] + 1.6 * np.sin(t)]
bio.shape(ax, np.vstack([body, [[bc[0], bc[1] + 1.6]]]), token="ectoderm", zorder=6)
noto = bio.blob((26.4, 6.85), 0.95, 0.45, wobble=0.05, seed=2, angle=0.15)
neuro = bio.blob((26.5, 5.1), 1.05, 0.5, wobble=0.05, seed=3, angle=-0.15)
bio.shape(ax, noto, token="ectoderm", zorder=7)
bio.shape(ax, neuro, token="ectoderm", zorder=7)
for (y0, ang) in ((6.9, 0.25), (5.05, -0.25)):  # acicula and chaetal bundle
    ax.plot([25.2, 27.2], [y0 - 0.25 * np.sign(ang), y0 + 0.25 * np.sign(ang)], color=P.ink(), lw=2.2, zorder=10)
    for d in np.linspace(-0.35, 0.35, 7):
        ax.plot([26.9, 28.6], [y0 + 0.1 * np.sign(ang), y0 + 0.1 * np.sign(ang) + d + 0.4 * np.sign(ang)],
                color=P.edge("neutral"), lw=0.9, zorder=9)
ax.plot([25.6, 25.9, 26.1], [7.25, 8.1, 8.9], color=P.edge("ectoderm"), lw=2.4, zorder=8, solid_capstyle="round")
ax.plot([25.7, 26.0, 26.2], [4.7, 4.0, 3.3], color=P.edge("ectoderm"), lw=2.4, zorder=8, solid_capstyle="round")
bio.callout(ax, (26.1, 8.8), (27.0, 9.7), "Dorsal cirrus")
bio.callout(ax, (26.6, 7.1), (28.2, 8.7), "Notopodium")
bio.callout(ax, (27.6, 6.95), (28.8, 7.8), "Chaetae")
bio.callout(ax, (25.8, 6.85), (25.2, 9.9), "Aciculum")
bio.callout(ax, (26.9, 4.75), (28.6, 3.9), "Neuropodium")
bio.callout(ax, (26.2, 3.35), (27.4, 2.5), "Ventral cirrus")
bio.callout(ax, (24.4, 6.0), (24.0, 2.0), "Body wall")
bio.label(ax, (24.2, 8.1), "Dorsal", size="tiny", color=P.muted())
bio.label(ax, (24.2, 3.9), "Ventral", size="tiny", color=P.muted())
