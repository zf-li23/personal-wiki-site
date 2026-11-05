"""Where fertilization happens in a fern, a gymnosperm and an angiosperm (schematic, not to scale). Fern: a
free-living prothallus with archegonia; flagellate sperm swim through a film of water. Gymnosperm (pine): a
naked ovule on a cone scale; pollen lands at the micropyle, the pollen tube grows through the nucellus and
releases two non-motile sperm into an archegonium of the large cellular female gametophyte, which later
becomes the nutritive tissue of the seed. Angiosperm: the ovule (two integuments) is enclosed in the ovary;
pollen lands on the stigma, the tube grows down the style and enters the seven-celled embryo sac, one sperm
fusing with the egg and the other with the central cell (double fertilization; triploid endosperm)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 13.5)


def ell(xy, w, h, tok, lw=0.9, z=6, light=False, angle=0):
    ax.add_patch(Ellipse(xy, w, h, angle=angle, facecolor=P.light(tok) if light else P.fill(tok), edgecolor=P.edge(tok), lw=lw,
                         zorder=z))


def sperm(xy, flag=True, ang=0):
    plant.sperm(ax, xy, 0.35, angle=ang, token="dna") if flag else ell(xy, 0.22, 0.14, "dna", lw=0.5, z=12)


# --- fern
cx = 5.0
bio.label(ax, (cx, 12.9), "Fern", size="title", bold=True)
plant.prothallus(ax, (cx, 6.6), 5.0, gametangia=True)
ax.add_patch(Ellipse((cx, 9.0), 5.0, 2.6, facecolor=P.light("vacuole"), edgecolor=P.edge("vacuole"), lw=0.6, zorder=5))
for k, (dx, dy) in enumerate(((-1.2, 3.8), (-0.4, 4.2), (0.5, 3.9))):
    plant.sperm(ax, (cx + dx * 1.2, 4.9 + dy), 0.8, angle=-60 + 20 * k, token="dna", zorder=9)
bio.label(ax, (cx, 11.0), "water film: sperm swim to archegonia", size="small", color=P.edge("vacuole"))

# --- gymnosperm
cx = 15.0
bio.label(ax, (cx, 12.9), "Gymnosperm (pine)", size="title", bold=True)
ax.add_patch(Polygon([(cx - 3.8, 3.4), (cx + 3.2, 4.2), (cx + 3.6, 3.6), (cx - 3.6, 2.8)], closed=True, facecolor=P.fill("animal"),
                     edgecolor=P.edge("animal"), lw=0.9, zorder=4))
t = np.linspace(-np.pi * 0.86, np.pi * 0.86, 90)
outer = np.c_[cx + 2.0 * np.sin(t), 4.0 + 2.9 * (1 - np.cos(t))]
inner = np.c_[cx + 1.6 * np.sin(t[::-1]), 4.3 + 2.6 * (1 - np.cos(t[::-1]))]
ax.add_patch(Polygon(np.vstack([outer, inner]), closed=True, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=1.0, zorder=6))
ell((cx, 6.6), 3.15, 5.2, "ovule", z=5)
ell((cx, 6.0), 2.6, 3.6, "lipid", lw=1.1, z=7)
for gx in np.linspace(cx - 1.0, cx + 1.0, 6):
    ax.plot([gx, gx], [4.6, 7.3], color=P.edge("lipid"), lw=0.3, zorder=8)
for dx in (-0.55, 0.55):
    ell((cx + dx, 7.3), 0.55, 0.9, "receptor", z=9)
    ell((cx + dx, 7.2), 0.3, 0.3, "nucleus", lw=0.5, z=10)
ell((cx, 10.2), 0.8, 0.55, "anther", z=10)
ax.plot([cx, cx + 0.1, cx + 0.45, cx + 0.55], [9.95, 9.0, 8.3, 7.85], color=P.edge("anther"), lw=2.2, solid_capstyle="round", zorder=10)
sperm((cx + 0.45, 8.15), flag=False)
sperm((cx + 0.7, 8.0), flag=False)
bio.callout(ax, (cx + 1.8, 7.5), (cx + 3.4, 9.8), "integument")
bio.callout(ax, (cx - 1.3, 8.4), (cx - 3.2, 9.8), "nucellus")
bio.callout(ax, (cx - 1.0, 5.4), (cx - 3.4, 6.0), "female\ngametophyte (n)")
bio.callout(ax, (cx - 0.55, 7.6), (cx - 3.4, 8.0), "archegonium")
bio.callout(ax, (cx + 0.3, 10.2), (cx + 2.6, 11.4), "pollen grain")
bio.callout(ax, (cx + 2.5, 3.7), (cx + 3.4, 2.2), "cone scale")

# --- angiosperm
cx = 25.0
bio.label(ax, (cx, 12.9), "Angiosperm", size="title", bold=True)
ax.add_patch(Polygon([(cx - 3.0, 2.6), (cx - 3.3, 6.0), (cx - 1.9, 8.5), (cx - 0.35, 9.2), (cx - 0.35, 11.3), (cx - 0.8, 11.8),
                      (cx + 0.8, 11.8), (cx + 0.35, 11.3), (cx + 0.35, 9.2), (cx + 1.9, 8.5), (cx + 3.3, 6.0), (cx + 3.0, 2.6)],
                     closed=True, facecolor=P.light("ovary"), edgecolor=P.edge("ovary"), lw=1.1, zorder=4))
ell((cx, 5.6), 3.8, 4.6, "bract", z=5, light=True)
ell((cx, 5.7), 3.2, 4.1, "bract", z=6)
ell((cx, 5.8), 2.5, 3.5, "ovule", z=7)
ell((cx, 5.8), 1.3, 2.6, "cytoplasm", z=8, light=True)
for dx in (-0.3, 0.0, 0.3):
    ell((cx + dx, 4.8), 0.32, 0.32, "neutral", lw=0.5, z=9)
for dy in (0.12, -0.12):
    ell((cx + 0.05 * (dy > 0), 5.75 + dy), 0.2, 0.2, "nucleus", lw=0.5, z=9)
ell((cx, 6.75), 0.42, 0.55, "receptor", z=9)
for dx in (-0.35, 0.35):
    ell((cx + dx, 6.9), 0.32, 0.6, "neutral", lw=0.5, z=9, light=True)
ell((cx + 0.4, 12.1), 0.7, 0.5, "anther", z=10)
ax.plot([cx + 0.3, cx + 0.05, cx, cx + 0.05, cx + 0.15], [11.9, 10.5, 9.0, 8.0, 7.25], color=P.edge("anther"), lw=2.0,
        solid_capstyle="round", zorder=10)
bio.callout(ax, (cx + 2.6, 4.2), (cx + 3.7, 2.2), "ovary wall")
bio.callout(ax, (cx - 1.9, 6.8), (cx - 3.6, 8.6), "two integuments")
bio.callout(ax, (cx - 0.25, 6.8), (cx - 3.6, 10.2), "egg + synergids")
bio.callout(ax, (cx - 0.15, 5.65), (cx - 3.6, 4.0), "central cell\n(2 polar nuclei)")
bio.callout(ax, (cx + 0.3, 4.75), (cx + 3.7, 5.0), "antipodals")
bio.callout(ax, (cx + 0.7, 12.1), (cx + 2.6, 12.5), "stigma, pollen")

rows = [("Gametophyte", ["free-living, mm to cm", "in the ovule, thousands of cells", "embryo sac, 7 cells"]),
        ("Sperm reach egg", ["swim in water", "pollen tube (cycads, ginkgo: swim\nfrom a haustorial tube)",
                             "pollen tube through stigma and style"]),
        ("Food for embryo", ["gametophyte, then own leaves", "female gametophyte (n)", "endosperm (3n), from fertilization"])]
for k, (h, vals) in enumerate(rows):
    y = 1.55 - k * 0.62
    bio.label(ax, (0.2, y), h, size="small", bold=True, ha="left")
    for xx, v in zip((5.5, 15.0, 25.0), vals):
        bio.label(ax, (xx, y), v.replace("\n", " "), size="tiny", color=P.muted())
