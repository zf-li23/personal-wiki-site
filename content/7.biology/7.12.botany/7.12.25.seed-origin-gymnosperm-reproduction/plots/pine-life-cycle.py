"""Life cycle of a pine (Pinus). Blue: diploid phase; orange: haploid phase. The tree bears pollen cones
(microsporophylls with two pollen sacs) and seed cones (bract-scale complexes with two ovules each). Meiosis
gives microspores and a linear tetrad of megaspores of which only the chalazal one survives. The microspore
develops into a winged pollen grain (two prothallial cells, generative cell, tube cell) that is caught by the
pollination drop in spring of the first year. The female gametophyte is free-nuclear through the first
winter, becomes cellular and forms archegonia; fertilization by one of two non-motile sperm brought by the
pollen tube occurs about 13 to 15 months after pollination. The seed (embryo 2n, female gametophyte n,
seed coat 2n of the parent) is shed in the autumn of the second year."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(24, 19)


def tree(ax_, xy, s):
    bio.icon(ax, "wikimedia/pine-tree", at=(xy[0], xy[1] + 0.2), height=s * 1.35)


def cones(ax_, xy, s):
    bio.icon(ax, "wikimedia/pine-pollen-cone", at=(xy[0] - 0.75, xy[1] + 0.2), height=s * 0.85)
    bio.icon(ax, "wikimedia/pine-seed-cone-section", at=(xy[0] + 0.75, xy[1] + 0.2), height=s * 0.95)


def spores(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.2
    for k in range(4):  # microspore tetrad
        a = np.pi / 4 + k * np.pi / 2
        ax.add_patch(Circle((x - 0.75 + 0.22 * np.cos(a), y + 0.22 * np.sin(a)), 0.2, facecolor=P.fill("anther"),
                            edgecolor=P.edge("anther"), lw=0.7, zorder=12))
    for k in range(4):  # linear megaspore tetrad, chalazal one functional
        big = k == 0
        ax.add_patch(Ellipse((x + 0.75, y - 0.55 + 0.37 * k), 0.4 if big else 0.28, 0.34 if big else 0.22,
                             facecolor=P.fill("lipid") if big else P.light("lipid"), edgecolor=P.edge("lipid"), lw=0.7, zorder=12))


def pollen(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.2
    for sgn in (-1, 1):
        ax.add_patch(Ellipse((x + sgn * 0.5, y - 0.1), 0.65, 0.75, facecolor=P.light("anther"), edgecolor=P.edge("anther"), lw=0.8,
                             zorder=11))
    ax.add_patch(Ellipse((x, y), 0.95, 0.8, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9, zorder=12))
    for dx in (-0.25, -0.12):
        ax.add_patch(Ellipse((x + dx, y + 0.28), 0.1, 0.18, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.4, zorder=13))
    ax.add_patch(Circle((x + 0.05, y + 0.2), 0.11, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, zorder=13))
    ax.add_patch(Circle((x + 0.12, y - 0.12), 0.16, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.5, zorder=13))


def female(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.25
    t = np.linspace(-np.pi * 0.85, np.pi * 0.85, 80)
    outer = np.c_[x + 0.95 * np.sin(t), y - 0.2 - 0.95 * np.cos(t) * 1.2]
    inner = np.c_[x + 0.7 * np.sin(t[::-1]), y - 0.1 - 0.75 * np.cos(t[::-1]) * 1.2]
    ax.add_patch(Polygon(np.vstack([outer, inner]), closed=True, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.8,
                         zorder=11))
    ax.add_patch(Ellipse((x, y - 0.15), 1.3, 1.75, facecolor=P.light("ovule"), edgecolor=P.edge("ovule"), lw=0.8, zorder=11))
    ax.add_patch(Ellipse((x, y - 0.35), 1.0, 1.25, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=12))
    for dx in (-0.22, 0.22):
        ax.add_patch(Ellipse((x + dx, y + 0.08), 0.24, 0.38, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6,
                             zorder=13))
    ax.plot([x + 0.05, x + 0.12, x + 0.2], [y + 0.95, y + 0.6, y + 0.3], color=P.edge("anther"), lw=1.6, zorder=13)
    ax.add_patch(Ellipse((x + 0.03, y + 1.05), 0.36, 0.26, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=13))


def seed(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.2
    ax.add_patch(Polygon([(x + 0.25, y + 0.25), (x + 1.4, y + 0.95), (x + 1.25, y - 0.15), (x + 0.3, y - 0.25)], closed=True,
                         facecolor=P.light("bract"), edgecolor=P.edge("bract"), lw=0.7, zorder=11))
    ax.add_patch(Ellipse((x - 0.2, y), 1.1, 0.7, facecolor=P.fill("bone"), edgecolor=P.edge("bone"), lw=0.9, zorder=12))
    ax.add_patch(Ellipse((x - 0.2, y), 0.88, 0.5, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.6, zorder=13))
    ax.plot([x - 0.55, x + 0.1], [y, y], color=P.edge("plant"), lw=2.2, solid_capstyle="round", zorder=14)
    for dy in (-0.07, 0.07):
        ax.plot([x + 0.1, x + 0.22], [y, y + dy], color=P.edge("plant"), lw=1.0, zorder=14)


stages = [
    dict(text="Sporophyte (2n)", draw=tree, icon_size=2.6, bold=True),
    dict(text="Pollen cone and seed cone:\nmicrosporangia, ovules", draw=cones, icon_size=2.2),
    dict(text="Microspores (left);\nlinear megaspore tetrad (right)", draw=spores, icon_size=1.4),
    dict(text="Male gametophyte:\nwinged 4-celled pollen", draw=pollen, icon_size=1.4, bold=True),
    dict(text="Female gametophyte with\narchegonia; pollen tube", draw=female, icon_size=2.0, bold=True),
    dict(text="Seed: embryo (2n), female\ngametophyte (n), seed coat (2n)", draw=seed, icon_size=1.4),
]
plant.alternation_of_generations(ax, (12.0, 9.2), 6.2, stages, meiosis=1, fertilization=4, gap=0.3,
                                 arrow_labels=[None, "spring, year 1", "pollination drop", "pollen tube waits\nover winter", None,
                                               "germination"])
bio.label(ax, (12.0, 0.6), "Pollination: spring of year 1   |   fertilization: summer of year 2 (13-15 months later)   |   "
          "seed shed: autumn of year 2", size="small", color=P.muted())
