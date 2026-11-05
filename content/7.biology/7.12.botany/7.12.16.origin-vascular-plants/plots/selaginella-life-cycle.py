"""Life cycle of Selaginella: a heterosporous lycophyte with endosporic gametophytes. Blue: diploid phase;
orange: haploid phase. The sporophyte bears four-angled strobili with megasporangia (four megaspores)
below and microsporangia (many microspores) above; the microspore forms a male gametophyte of one
prothallial cell and one antheridium; the megaspore forms a female gametophyte that protrudes at the
triradiate scar with archegonia and rhizoids; biflagellate sperm swim to the archegonia."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(22, 18)
SP, SPE = P.fill("animal"), P.edge("animal")


def sporophyte(ax_, xy, s):
    bio.icon(ax, "phylopic/selaginella", at=(xy[0], xy[1] + 0.1), height=s * 1.5, color="plant")


def strobilus(ax_, xy, s):
    plant.cone(ax, (xy[0], xy[1] - s * 0.45), s * 1.35, kind="selaginella")


def spores(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.2
    for k in range(4):
        a = np.pi / 4 + k * np.pi / 2
        ax.add_patch(Circle((x - 0.55 + 0.28 * np.cos(a), y + 0.28 * np.sin(a)), 0.25, facecolor=SP, edgecolor=SPE, lw=0.8, zorder=12))
    rng = np.random.default_rng(1)
    for k in range(18):
        p = (x + 0.65 + rng.uniform(-0.35, 0.35), y + rng.uniform(-0.35, 0.35))
        ax.add_patch(Circle(p, 0.06, facecolor=SP, edgecolor=SPE, lw=0.4, zorder=12))


def gametophytes(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.35
    # female: megaspore wall with gametophyte tissue bulging at the scar
    ax.add_patch(Circle((x - 0.7, y - 0.1), 0.55, facecolor=P.fill("lipid"), edgecolor=SPE, lw=1.2, zorder=12))
    ax.add_patch(Ellipse((x - 0.7, y + 0.38), 0.7, 0.35, facecolor=P.mix(P.surface(), P.fill("plant"), 0.5), edgecolor=P.edge("plant"),
                         lw=0.8, zorder=13))
    for dx in (-0.18, 0.0, 0.18):
        ax.add_patch(Circle((x - 0.7 + dx, y + 0.5), 0.05, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.5, zorder=14))
    for dx in (-0.35, 0.35):
        ax.plot([x - 0.7 + dx, x - 0.7 + dx * 1.6], [y + 0.32, y + 0.65], color=P.muted(), lw=0.6, zorder=14)
    # male: microspore with prothallial cell and antheridium
    ax.add_patch(Circle((x + 0.75, y - 0.1), 0.32, facecolor=P.fill("lipid"), edgecolor=SPE, lw=1.0, zorder=12))
    ax.add_patch(Circle((x + 0.75, y - 0.32), 0.08, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.5, zorder=13))
    ax.add_patch(Circle((x + 0.75, y - 0.02), 0.2, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, zorder=13))


def gametes(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.25
    plant.cell(ax, (x - 0.35, y), 0.55, token="receptor")
    for k, (dx, dy) in enumerate(((0.45, 0.25), (0.6, -0.2))):
        ax.add_patch(Ellipse((x + dx, y + dy), 0.18, 0.1, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, zorder=13))
        for sgn in (1, -1):
            t = np.linspace(0, 1, 20)
            ax.plot(x + dx + 0.08 + 0.45 * t, y + dy + sgn * 0.04 + 0.05 * np.sin(12 * t) + sgn * 0.12 * t, color=P.edge("dna"), lw=0.5,
                    zorder=13)


def embryo(ax_, xy, s):
    x, y = xy[0], xy[1] + 0.4
    ax.add_patch(Circle((x, y - 0.25), 0.5, facecolor=P.fill("lipid"), edgecolor=SPE, lw=1.1, zorder=12))
    ax.plot([x, x], [y + 0.15, y + 0.85], color=P.edge("plant"), lw=1.6, zorder=13)
    for sgn in (1, -1):
        ax.add_patch(Ellipse((x + sgn * 0.22, y + 0.85), 0.42, 0.16, angle=sgn * 25, facecolor=P.fill("plant"), edgecolor=P.edge("plant"),
                             lw=0.6, zorder=14))
    ax.plot([x, x + 0.1], [y - 0.7, y - 1.0], color=P.muted(), lw=0.9, zorder=13)


stages = [
    dict(text="Sporophyte (2n)", draw=sporophyte, icon_size=2.2, bold=True),
    dict(text="Strobilus: mega- and\nmicrosporangia", draw=strobilus, icon_size=2.0),
    dict(text="Megaspores (4, left) and\nmicrospores (many, right)", draw=spores, icon_size=1.4),
    dict(text="Endosporic gametophytes (n):\nfemale (left), male (right)", draw=gametophytes, icon_size=1.4, bold=True),
    dict(text="Egg in archegonium,\nbiflagellate sperm", draw=gametes, icon_size=1.2),
    dict(text="Embryo on the female\ngametophyte", draw=embryo, icon_size=1.6),
]
plant.alternation_of_generations(ax, (11.0, 9.0), 6.0, stages, meiosis=1, fertilization=4, gap=0.3,
                                 arrow_labels=[None, None, "Germination\ninside the wall", None, None, "Growth"])
