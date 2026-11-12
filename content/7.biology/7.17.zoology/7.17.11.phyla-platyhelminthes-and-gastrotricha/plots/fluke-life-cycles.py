# Life cycles of Clonorchis sinensis (A) and Schistosoma japonicum (B). Shaded: asexual multiplication in the snail.
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


bio.panel(ax, "A", (0.2, 13.4))
bio.label(ax, (6.9, 13.2), "Clonorchis sinensis", size="title", bold=True, italic=True)
eco.cycle(ax, (6.9, 6.6), 4.4, [
    dict(text="Adult in bile ducts\n(human, cat, dog)", icon="phylopic/human", icon_size=1.9, token="animal", bold=True),
    dict(text="Egg with miracidium\nin faeces", draw=egg, icon_size=1.0),
    dict(text="Snail (1st intermediate):\nsporocyst, rediae", icon="phylopic/snail", icon_size=1.3, token="animal"),
    dict(text="Cercaria", draw=cercaria, icon_size=1.2),
    dict(text="Fish (2nd intermediate):\nmetacercaria in muscle", icon="phylopic/cod", icon_size=1.0, token="animal"),
    dict(text="Metacercaria", draw=cyst, icon_size=1.0),
], start=90, arrow_labels=["Eggs passed", "Eaten by snail", "Leave snail", "Penetrate fish", "Raw fish eaten", "Excysts, migrates\nto bile ducts"],
    sectors=[dict(start=1.6, end=2.4, token="positive", r0=2.7, r1=6.2)], size="small")

bio.panel(ax, "B", (14.2, 13.4))
bio.label(ax, (21.0, 13.2), "Schistosoma japonicum", size="title", bold=True, italic=True)
eco.cycle(ax, (21.0, 6.6), 4.4, [
    dict(text="Adult pairs in portal veins\n(human, cattle, buffalo)", icon="phylopic/cattle", icon_size=1.5, token="animal", bold=True),
    dict(text="Egg in faeces", draw=lambda a, xy, s: egg(a, xy, s, operculum=False), icon_size=1.0),
    dict(text="Miracidium in water", draw=miracidium, icon_size=1.0),
    dict(text="Snail Oncomelania:\ntwo sporocyst generations", icon="phylopic/snail", icon_size=1.3, token="animal"),
    dict(text="Fork-tailed cercaria", draw=lambda a, xy, s: cercaria(a, xy, s, forked=True), icon_size=1.2),
], start=90, arrow_labels=["Eggs pass gut wall", "Hatches", "Penetrates\nsnail", "Leave snail", "Penetrate skin;\nschistosomulum migrates"],
    sectors=[dict(start=2.6, end=3.4, token="positive", r0=2.7, r1=6.2)], size="small")
