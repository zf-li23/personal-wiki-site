# Two cnidarian life cycles (metagenesis): A, Obelia (Hydrozoa); B, Aurelia (Scyphozoa).
import numpy as np
import wikibio as bio
from wikibio import ecology as eco
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(27, 13.4)


def planula(ax, xy, s):
    ax.add_patch(Ellipse(xy, s * 0.9, s * 0.42, angle=20, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.8, zorder=12))
    th = np.linspace(0, 2 * np.pi, 28)
    for t in th:
        p = np.array(xy) + np.array([np.cos(t) * s * 0.45, np.sin(t) * s * 0.21])
        ax.plot([p[0], p[0] * 1.0 + np.cos(t) * s * 0.07], [p[1], p[1] + np.sin(t) * s * 0.07], color=P.muted(), lw=0.5, zorder=11)


def colony(ax, xy, s):
    x, y = xy
    col = P.edge("ectoderm")
    ax.plot([x - s * 0.6, x + s * 0.6], [y - s * 0.45, y - s * 0.45], color=col, lw=1.6, zorder=12)
    ax.plot([x, x], [y - s * 0.45, y + s * 0.3], color=col, lw=1.4, zorder=12)
    for sgn, yy in ((-1, y - s * 0.1), (1, y + s * 0.05), (-1, y + s * 0.25)):
        tip = (x + sgn * s * 0.35, yy + s * 0.2)
        ax.plot([x, tip[0]], [yy, tip[1]], color=col, lw=1.1, zorder=12)
        ax.add_patch(Polygon([(tip[0] - 0.12 * s, tip[1]), (tip[0] + 0.12 * s, tip[1]), (tip[0], tip[1] - 0.15 * s)],
                             facecolor=P.fill("ectoderm"), edgecolor=col, lw=0.7, zorder=13))
        for k in (-1, 0, 1):
            ax.plot([tip[0] + k * 0.08 * s, tip[0] + k * 0.16 * s], [tip[1], tip[1] + 0.12 * s], color=col, lw=0.7, zorder=13)
    # a gonangium with medusa buds
    gx, gy = x + s * 0.4, y - s * 0.3
    ax.plot([x, gx], [y - s * 0.45 + 0.02, gy], color=col, lw=1.0, zorder=12)
    ax.add_patch(Ellipse((gx, gy + 0.14 * s), 0.18 * s, 0.32 * s, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=13))


def strobila(ax, xy, s):
    x, y = xy
    for k in range(5):
        ax.add_patch(Ellipse((x, y - s * 0.4 + k * s * 0.18), s * 0.5, s * 0.13, facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.7, zorder=12 + k))
    ax.plot([x, x], [y - s * 0.55, y - s * 0.45], color=P.edge("ectoderm"), lw=2.0, zorder=12)


def ephyra(ax, xy, s):
    th = np.linspace(0, 2 * np.pi, 400)
    r = s * (0.22 + 0.16 * np.clip(np.cos(8 * th), 0, None) ** 0.5)
    ax.add_patch(Polygon(np.c_[xy[0] + r * np.cos(th), xy[1] + r * np.sin(th)], facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.7, zorder=12))


def gametes(ax, xy, s):
    ax.add_patch(Ellipse((xy[0] - s * 0.2, xy[1]), s * 0.34, s * 0.34, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=12))
    for dy in (-0.12, 0.12):
        ax.plot([xy[0] + 0.1 * s, xy[0] + 0.3 * s], [xy[1] + dy * s, xy[1] + dy * s], color=P.ink(), lw=1.0, zorder=12)
        ax.add_patch(Ellipse((xy[0] + 0.08 * s, xy[1] + dy * s), 0.08 * s, 0.06 * s, facecolor=P.ink(), edgecolor="none", zorder=12))


bio.panel(ax, "A", (0.2, 13.2))
bio.label(ax, (6.6, 13.0), "Obelia (Hydrozoa)", size="title", bold=True, italic=False)
eco.cycle(ax, (6.6, 6.6), 4.2, [
    dict(text="Polyp colony\n(hydranths, gonangia)", draw=colony, icon_size=1.9, bold=True),
    dict(text="Medusa buds\nin gonangium", draw=lambda a, xy, s: None, icon_size=0.2),
    dict(text="Medusa (2n)\nwith velum", icon="phylopic/jellyfish", icon_size=1.5, token="ectoderm", bold=True),
    dict(text="Eggs and sperm (n)", draw=gametes, icon_size=1.0),
    dict(text="Planula (2n)", draw=planula, icon_size=1.0),
], start=90, arrow_labels=["Budding\n(asexual)", "Released", "Meiosis", "Fertilization", "Settles, grows"],
    sectors=[dict(start=2.5, end=3.5, token="highlight", text="n", r0=2.6, r1=6.0, text_r=5.6)])

bio.panel(ax, "B", (13.6, 13.2))
bio.label(ax, (20.2, 13.0), "Aurelia (Scyphozoa)", size="title", bold=True)
eco.cycle(ax, (20.2, 6.6), 4.4, [
    dict(text="Medusa (2n)", icon="phylopic/jellyfish", icon_size=1.9, token="ectoderm", bold=True),
    dict(text="Eggs and sperm (n)", draw=gametes, icon_size=1.0),
    dict(text="Planula (2n)", draw=planula, icon_size=1.0),
    dict(text="Scyphistoma\n(polyp)", icon="phylopic/hydra", icon_size=1.3, token="ectoderm", bold=True),
    dict(text="Strobila", draw=strobila, icon_size=1.3),
    dict(text="Ephyra", draw=ephyra, icon_size=1.0),
], start=90, arrow_labels=["Meiosis", "Fertilization", "Settles", "Strobilation\n(asexual)", "Released", "Grows"],
    sectors=[dict(start=0.5, end=1.5, token="highlight", text="n", r0=2.7, r1=6.2, text_r=5.8)])
bio.label(ax, (20.2, 6.6), "Scyphistoma also buds\nnew polyps", size="tiny", color=P.muted())
