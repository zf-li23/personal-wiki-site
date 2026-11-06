# Three modes of phloem loading in source-leaf minor veins (schematic). Each row runs from mesophyll to
# sieve element; short bars across shared walls are plasmodesmata (their number suggests the frequency).
# (A) Apoplastic loading: sucrose reaches phloem parenchyma symplastically, is released by SWEET
# uniporters into the cell wall and taken up against its gradient by sucrose-H+ symporters (SUC2/SUT1)
# in the companion-cell membrane, powered by the H+-ATPase. (B) Polymer trapping: sucrose diffuses into an
# intermediary cell through abundant plasmodesmata and is converted to raffinose and stachyose, which are
# too large to diffuse back but pass into the sieve element. (C) Passive symplastic loading: sucrose
# diffuses down a concentration gradient from mesophyll with a high sugar concentration.
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(21, 16)
W, H = 3.1, 2.7


def cell(x, y, token, name, w=W):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - H / 2), w, H, boxstyle="round,pad=0,rounding_size=0.35",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.3, zorder=5))
    bio.label(ax, (x, y - H / 2 - 0.35), name, size="tiny", color=P.muted())


def pd(xw, y, n):
    for yy in np.linspace(y - 0.9, y + 0.9, n) if n > 1 else [y]:
        ax.plot([xw - 0.22, xw + 0.22], [yy, yy], color=P.ink(), lw=1.6, zorder=8, solid_capstyle="butt")


def suc(x, y, n=1, tok="carbohydrate", r=0.13):
    for i in range(n):
        ax.add_patch(Circle((x + i * 2.1 * r, y), r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=12))


rows = [(12.9, "A", "Apoplastic loading"), (7.7, "B", "Polymer trapping"), (2.5, "C", "Passive symplastic loading")]
for y, letter, title in rows:
    bio.panel(ax, letter, (0.4, y + 2.0))
    bio.label(ax, (1.0, y + 2.0), title, size="small", bold=True, ha="left")

# Row A
y = rows[0][0]
xs = [2.2, 5.6, 9.0, 14.0, 17.6]
cell(xs[0], y, "chloroplast", "Mesophyll")
cell(xs[1], y, "plant", "Bundle sheath")
cell(xs[2], y, "vacuole", "Phloem parenchyma")
cell(xs[3], y, "cytoplasm", "Companion cell")
cell(xs[4], y, "vesicle", "Sieve element")
pd((xs[0] + xs[1]) / 2, y, 3)
pd((xs[1] + xs[2]) / 2, y, 3)
pd((xs[3] + xs[4]) / 2, y, 5)
bio.label(ax, ((xs[2] + xs[3]) / 2, y + 1.65), "cell wall (apoplast)", size="tiny", color=P.muted())
ax.add_patch(FancyBboxPatch(((xs[2] + W / 2) + 0.1, y - H / 2), xs[3] - xs[2] - W - 0.2, H,
                            boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill("cell_wall"),
                            edgecolor="none", alpha=0.35, zorder=4))
for x0, x1 in ((xs[0] + 0.6, xs[1] - 0.6), (xs[1] + 0.6, xs[2] - 0.6)):
    bio.arrow(ax, (x0, y + 0.4), (x1, y + 0.4), kind="process", lw=1.4, head=0.16, color=P.edge("dna"))
suc(xs[0] - 0.3, y - 0.4)
suc(xs[1] - 0.15, y - 0.4)
bio.box(ax, (xs[2] + W / 2, y + 0.4), 0.95, 0.5, token="channel", text="SWEET", size="tiny")
bio.box(ax, (xs[3] - W / 2, y + 0.4), 0.95, 0.5, token="enzyme", text="SUC2", size="tiny")
bio.box(ax, (xs[3] - W / 2, y - 0.75), 0.95, 0.5, token="atp", text="ATPase", size="tiny")
bio.arrow(ax, (xs[2] + W / 2 + 0.5, y + 0.4), (xs[3] - W / 2 - 0.5, y + 0.4), kind="process", lw=1.4, head=0.16, color=P.edge("dna"))
suc((xs[2] + xs[3]) / 2 - 0.12, y - 0.05)
bio.arrow(ax, (xs[3] - W / 2 - 0.5, y - 0.75), (xs[3] - W / 2 - 1.1, y - 0.75), kind="process", lw=1.0, head=0.14,
          color=P.edge("h"))
bio.label(ax, (xs[3] - W / 2 - 1.35, y - 0.75), "H⁺", size="tiny", color=P.edge("h"))
bio.label(ax, (xs[3] - W / 2 - 1.15, y + 0.95), "H⁺ + sucrose", size="tiny", color=P.muted())
suc(xs[3] - 0.3, y - 0.2, 3)
bio.arrow(ax, (xs[3] + 0.9, y + 0.4), (xs[4] - 0.9, y + 0.4), kind="process", lw=1.4, head=0.16, color=P.edge("dna"))
suc(xs[4] - 0.4, y - 0.2, 4)
bio.label(ax, (xs[3], y + 0.95), "high [sucrose]", size="tiny", color=P.ink())

# Row B
y = rows[1][0]
xs = [2.2, 6.2, 11.0, 15.4]
cell(xs[0], y, "chloroplast", "Mesophyll")
cell(xs[1], y, "plant", "Bundle sheath")
cell(xs[2], y, "cytoplasm", "Intermediary cell", w=3.6)
cell(xs[3], y, "vesicle", "Sieve element")
pd((xs[0] + xs[1]) / 2, y, 4)
pd((xs[1] + W / 2 + xs[2] - 1.8) / 2, y, 6)
pd((xs[2] + 1.8 + xs[3] - W / 2) / 2, y, 4)
for x0, x1 in ((xs[0] + 0.6, xs[1] - 0.6), (xs[1] + 0.6, xs[2] - 1.3)):
    bio.arrow(ax, (x0, y + 0.45), (x1, y + 0.45), kind="process", lw=1.4, head=0.16, color=P.edge("dna"))
suc(xs[0] - 0.3, y - 0.4, 2)
suc(xs[1] - 0.2, y - 0.4, 1)
bio.label(ax, (xs[2], y + 0.95), "sucrose + galactinol", size="tiny")
bio.arrow(ax, (xs[2], y + 0.7), (xs[2], y + 0.05), kind="process", lw=1.0, head=0.14)
bio.label(ax, (xs[2], y - 0.2), "raffinose, stachyose", size="tiny", bold=True)
suc(xs[2] - 0.65, y - 0.62, 7, tok="metabolite")
bio.arrow(ax, (xs[2] + 1.3, y + 0.45), (xs[3] - 0.7, y + 0.45), kind="process", lw=1.4, head=0.16, color=P.edge("dna"))
bio.label(ax, (xs[2], y - 1.1), "too large to diffuse back", size="tiny", color=P.muted())
suc(xs[3] - 0.6, y - 0.3, 3, tok="metabolite")

# Row C
y = rows[2][0]
xs = [2.2, 6.2, 10.2, 14.2]
cell(xs[0], y, "chloroplast", "Mesophyll")
cell(xs[1], y, "plant", "Bundle sheath")
cell(xs[2], y, "cytoplasm", "Companion cell")
cell(xs[3], y, "vesicle", "Sieve element")
for i in range(3):
    pd((xs[i] + xs[i + 1]) / 2, y, 5)
for i in range(3):
    bio.arrow(ax, (xs[i] + 0.6, y + 0.45), (xs[i + 1] - 0.6, y + 0.45), kind="process", lw=1.4, head=0.16, color=P.edge("dna"))
for i, n in enumerate((5, 4, 4, 3)):
    suc(xs[i] - 0.55, y - 0.4, n)
bio.label(ax, (xs[0], y + 0.95), "high [sugar]", size="tiny", color=P.on_fill())
bio.label(ax, (17.9, y), "diffusion down\nthe gradient", size="tiny", color=P.muted())

# legend
lx, ly = 17.2, 7.9
suc(lx, ly + 0.5)
bio.label(ax, (lx + 0.4, ly + 0.5), "sucrose", size="tiny", ha="left")
suc(lx, ly)
ax.patches[-1].set_facecolor(P.fill("metabolite")); ax.patches[-1].set_edgecolor(P.edge("metabolite"))
bio.label(ax, (lx + 0.4, ly), "raffinose / stachyose", size="tiny", ha="left")
ax.plot([lx - 0.2, lx + 0.2], [ly - 0.5, ly - 0.5], color=P.ink(), lw=1.6)
bio.label(ax, (lx + 0.4, ly - 0.5), "plasmodesma", size="tiny", ha="left")
