# Life cycles of Paragonimus westermani (A) and Echinococcus granulosus (B). Shaded: asexual multiplication in the
# intermediate host (rediae in the snail; brood capsules and protoscoleces in the hydatid cyst).
import numpy as np
import wikibio as bio
from wikibio import ecology as eco
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(28, 13.6)
INK = "endoderm"


def egg(ax, xy, s, operculum=True):
    ax.add_patch(Ellipse(xy, s * 0.42, s * 0.7, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=12))
    ax.add_patch(Ellipse((xy[0], xy[1] - s * 0.05), s * 0.25, s * 0.45, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.6, zorder=13))
    if operculum:
        ax.plot([xy[0] - s * 0.13, xy[0] + s * 0.13], [xy[1] + s * 0.3, xy[1] + s * 0.3], color=P.edge("highlight"), lw=1.2, zorder=14)


def miracidium(ax, xy, s):
    th = np.linspace(0, 2 * np.pi, 80)
    x = xy[0] + s * 0.42 * np.cos(th) * (1 - 0.35 * np.sin(th))
    y = xy[1] + s * 0.22 * np.sin(th)
    ax.add_patch(Polygon(np.c_[x, y], facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.8, zorder=12))
    for k in range(0, 80, 4):
        ax.plot([x[k], x[k] + 0.06 * s * np.cos(th[k])], [y[k], y[k] + 0.06 * s * np.sin(th[k])], color=P.muted(), lw=0.5, zorder=11)


def cercaria(ax, xy, s, forked=False):
    ax.add_patch(Ellipse((xy[0] - s * 0.25, xy[1]), s * 0.45, s * 0.28, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.8, zorder=12))
    t = np.linspace(0, 1, 40)
    tx, ty = xy[0] - s * 0.03 + s * 0.5 * t, xy[1] + s * 0.06 * np.sin(t * 8)
    ax.plot(tx, ty, color=P.edge("ectoderm"), lw=2.2, zorder=12)
    if forked:
        for sg in (1, -1):
            ax.plot([tx[-1], tx[-1] + s * 0.15], [ty[-1], ty[-1] + sg * s * 0.12], color=P.edge("ectoderm"), lw=2.0, zorder=12)


def cyst(ax, xy, s):
    ax.add_patch(Ellipse(xy, s * 0.55, s * 0.45, facecolor=P.mix(P.fill("highlight"), P.surface(), 0.4), edgecolor=P.edge("highlight"), lw=1.2, zorder=12))
    ax.add_patch(Ellipse(xy, s * 0.36, s * 0.26, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.7, zorder=13))




def oncosphere(ax, xy, s):
    ax.add_patch(Ellipse(xy, s * 0.62, s * 0.62, facecolor=P.mix(P.fill("highlight"), P.surface(), 0.3), edgecolor=P.edge("highlight"), lw=1.4, zorder=12))
    ax.add_patch(Ellipse(xy, s * 0.36, s * 0.36, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.7, zorder=13))
    for a in np.linspace(0, 2 * np.pi, 7)[:-1]:
        ax.plot([xy[0] + s * 0.06 * np.cos(a), xy[0] + s * 0.15 * np.cos(a)], [xy[1] + s * 0.06 * np.sin(a), xy[1] + s * 0.15 * np.sin(a)],
                color=P.ink(), lw=0.8, zorder=14)


def hydatid(ax, xy, s):
    ax.add_patch(Ellipse(xy, s * 0.8, s * 0.65, facecolor=P.mix(P.fill("highlight"), P.surface(), 0.55), edgecolor=P.edge("highlight"), lw=1.3, zorder=12))
    for dx, dy in ((-0.17, 0.08), (0.12, 0.12), (0.0, -0.14), (0.2, -0.08)):
        ax.add_patch(Ellipse((xy[0] + dx * s, xy[1] + dy * s), s * 0.18, s * 0.15, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.6, zorder=13))


def short_cercaria(ax, xy, s):
    ax.add_patch(Ellipse((xy[0] - s * 0.08, xy[1]), s * 0.5, s * 0.3, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.8, zorder=12))
    ax.plot([xy[0] + s * 0.17, xy[0] + s * 0.3], [xy[1], xy[1] - s * 0.02], color=P.edge("ectoderm"), lw=2.6, zorder=12, solid_capstyle="round")


bio.panel(ax, "A", (0.2, 13.4))
bio.label(ax, (6.9, 13.2), "Paragonimus westermani", size="title", bold=True, italic=True)
eco.cycle(ax, (6.9, 6.6), 4.4, [
    dict(text="Adults paired in lung cysts\n(human, cat, dog, tiger)", icon="phylopic/human", icon_size=1.9, token="animal", bold=True),
    dict(text="Egg in sputum\nor faeces", draw=egg, icon_size=1.0),
    dict(text="Miracidium in water", draw=miracidium, icon_size=1.0),
    dict(text="Snail (1st intermediate):\nsporocyst, two redia\ngenerations", icon="phylopic/snail", icon_size=1.3, token="animal"),
    dict(text="Short-tailed cercaria", draw=short_cercaria, icon_size=1.2),
    dict(text="Crab or crayfish\n(2nd intermediate):\nmetacercaria", icon="phylopic/crab", icon_size=1.3, token="animal"),
], start=90, arrow_labels=["Coughed up\nor swallowed", "Hatches", "Penetrates snail", "Leaves snail", "Raw crab eaten", "Crosses gut wall,\ndiaphragm, to lungs"],
    sectors=[dict(start=2.6, end=3.4, token="positive", r0=2.7, r1=6.2)], size="small")

bio.panel(ax, "B", (14.2, 13.4))
bio.label(ax, (21.0, 13.2), "Echinococcus granulosus", size="title", bold=True, italic=True)
eco.cycle(ax, (21.0, 6.6), 4.4, [
    dict(text="Adults in small intestine\n(dog, other canids)", icon="phylopic/wolf", icon_size=1.6, token="animal", bold=True),
    dict(text="Egg with oncosphere\nin faeces", draw=oncosphere, icon_size=1.0),
    dict(text="Herbivore (intermediate):\nhydatid cyst in liver, lung", icon="phylopic/cattle", icon_size=1.5, token="animal"),
    dict(text="Brood capsules with\nprotoscoleces", draw=hydatid, icon_size=1.2),
], start=90, arrow_labels=["Eggs passed", "Eaten with grass\nor water", "Germinal layer\nbuds", "Offal eaten by dog"],
    sectors=[dict(start=1.6, end=2.4, token="positive", r0=2.7, r1=6.2)], size="small")
bio.label(ax, (21.0, 12.4), "Humans: accidental intermediate hosts (dead end)", size="small", color=P.muted())
