"""Life cycle of a flowering plant. Blue: diploid sporophyte phase; orange: haploid gametophyte phase.
The flowering sporophyte forms anthers and ovules; meiosis gives microspore tetrads and a linear tetrad
of megaspores of which the chalazal one is functional. The microspore becomes a pollen grain (vegetative
cell and generative cell); the megaspore becomes a 7-celled, 8-nucleate embryo sac. The pollen tube
delivers two sperm cells: double fertilization gives the zygote (2n) and the primary endosperm nucleus
(3n). The ovule becomes the seed (embryo 2n, endosperm 3n, seed coat 2n of the parent) inside the fruit;
the seed germinates into a seedling.
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(24, 19)


def adult(ax_, xy, s):
    bio.icon(ax, "bioicons/arabidopsis-flower", at=(xy[0], xy[1] + 0.2), height=s * 1.3)


def flower(ax_, xy, s):
    bio.icon(ax, "wikimedia/flower-section", at=(xy[0], xy[1] + 0.2), height=s * 1.0)


def spores(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.2
    for k in range(4):
        a = np.pi / 4 + k * np.pi / 2
        ax.add_patch(Circle((x - 0.75 + 0.22 * np.cos(a), y + 0.22 * np.sin(a)), 0.2, facecolor=P.fill("anther"),
                            edgecolor=P.edge("anther"), lw=0.7, zorder=12))
    for k in range(4):
        big = k == 3
        ax.add_patch(Ellipse((x + 0.75, y - 0.55 + 0.37 * k), 0.4 if big else 0.28, 0.34 if big else 0.22,
                             facecolor=P.fill("ovule") if big else P.light("ovule"), edgecolor=P.edge("ovule"), lw=0.7,
                             zorder=12))


def pollen(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.2
    ax.add_patch(Circle((x, y), 0.55, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.0, zorder=12))
    ax.add_patch(Circle((x - 0.15, y + 0.1), 0.14, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6,
                        zorder=13))
    ax.add_patch(Ellipse((x + 0.18, y - 0.15), 0.38, 0.2, angle=30, facecolor=P.fill("receptor"),
                         edgecolor=P.edge("receptor"), lw=0.6, zorder=13))


def sac(ax_, xy, s):
    bio.icon(ax, "wikimedia/embryo-sac", at=(xy[0], xy[1] + 0.2), height=s * 1.0)


def seed(ax_, xy, s):
    bio.icon(ax, "wikimedia/seed-dicot-section", at=(xy[0], xy[1] + 0.2), height=s * 0.9)


def seedling(ax_, xy, s):
    bio.icon(ax, "ian/seedling", at=(xy[0], xy[1] + 0.2), height=s * 1.0)


stages = [
    dict(text="Flowering plant:\nsporophyte (2n)", draw=adult, icon_size=2.6, bold=True),
    dict(text="Flower: anthers\nand ovules", draw=flower, icon_size=2.2),
    dict(text="Microspore tetrad (left);\nmegaspores, chalazal one\nfunctional (right)", draw=spores, icon_size=1.4),
    dict(text="Male gametophyte:\npollen grain", draw=pollen, icon_size=1.4, bold=True),
    dict(text="Female gametophyte:\nembryo sac (7 cells);\npollen tube, 2 sperm", draw=sac, icon_size=2.0, bold=True),
    dict(text="Seed: embryo (2n),\nendosperm (3n), seed\ncoat (2n); fruit", draw=seed, icon_size=1.8),
    dict(text="Seedling", draw=seedling, icon_size=1.8),
]
plant.alternation_of_generations(ax, (12.0, 9.4), 6.2, stages, meiosis=1, fertilization=4, gap=0.3,
                                 arrow_labels=[None, None, "mitosis", "pollination", None, "germination", "growth"])
bio.label(ax, (12.0, 0.6), "Double fertilization: sperm + egg = zygote (2n); sperm + 2 polar nuclei = primary "
          "endosperm nucleus (3n)", size="small", color=P.muted())
