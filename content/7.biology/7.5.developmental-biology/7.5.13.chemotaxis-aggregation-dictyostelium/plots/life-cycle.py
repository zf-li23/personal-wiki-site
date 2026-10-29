"""The asexual life cycle of the social amoeba Dictyostelium discoideum (schematic, not to scale).

Spores germinate into amoebae that feed on bacteria and divide. Starvation starts cAMP signaling: cells relay
pulses of cAMP and move towards them, joining streams that converge on aggregation centres (about 1e5 cells).
The aggregate forms a mound with a tip, which elongates into a migrating slug: prestalk cells (red) in the front
fifth, prespore cells (blue) behind. At culmination the prestalk cells form the stalk, a column of dead,
vacuolated cells, and lift the prespore cells, which become spores in the sorus of the fruiting body.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon
import wikibio as bio
from wikibio import ecology as E

P = bio.P


def amoeba(ax, xy, r, tok="animal", seed=0):
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path
    o = bio.core.blob(xy, r, r * 0.8, wobble=0.18, seed=seed, k=7)
    ax.add_patch(PathPatch(Path(o, closed=True), facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=12))
    ax.add_patch(Circle(xy, r * 0.3, facecolor=P.edge(tok), edgecolor="none", zorder=13))


def d_spores(ax, xy, s):
    for k, (dx, dy) in enumerate(((-0.5, 0), (0.4, 0.3), (0.1, -0.45), (0.6, -0.3), (-0.2, 0.45))):
        ax.add_patch(Ellipse((xy[0] + dx, xy[1] + dy), 0.42, 0.26, angle=30 * k, facecolor=P.fill("na"), edgecolor=P.edge("na"), lw=1.0, zorder=12))


def d_amoebae(ax, xy, s):
    for k, (dx, dy) in enumerate(((-0.6, 0.3), (0.5, 0.4), (0.0, -0.4), (0.7, -0.5))):
        amoeba(ax, (xy[0] + dx, xy[1] + dy), 0.32, seed=k)
    for dx, dy in ((-0.2, 0.7), (0.9, 0.0), (-0.8, -0.4)):
        ax.add_patch(Ellipse((xy[0] + dx, xy[1] + dy), 0.18, 0.09, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=0.6, zorder=12))


def d_streams(ax, xy, s):
    for k in range(6):
        th = 2 * np.pi * k / 6 + 0.3
        for j in range(4):
            rr = 0.35 + 0.22 * j
            ax.add_patch(Circle((xy[0] + rr * np.cos(th + 0.08 * j), xy[1] + rr * np.sin(th + 0.08 * j)), 0.11,
                                facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.6, zorder=12))
    ax.add_patch(Circle(xy, 0.28, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.0, zorder=12))


def d_mound(ax, xy, s):
    t = np.linspace(0, np.pi, 50)
    pts = np.c_[xy[0] + 0.9 * np.cos(t), xy[1] - 0.3 + 0.8 * np.sin(t)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("na"), edgecolor=P.edge("na"), lw=1.0, zorder=12))
    ax.add_patch(Ellipse((xy[0], xy[1] + 0.5), 0.45, 0.35, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.0, zorder=13))


def d_slug(ax, xy, s):
    ax.add_patch(Ellipse((xy[0] - 0.2, xy[1]), 1.9, 0.6, facecolor=P.fill("na"), edgecolor=P.edge("na"), lw=1.0, zorder=12))
    ax.add_patch(Ellipse((xy[0] + 0.62, xy[1] + 0.03), 0.55, 0.45, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.0, zorder=13))
    bio.arrow(ax, (xy[0] + 1.0, xy[1] - 0.55), (xy[0] + 1.5, xy[1] - 0.55), kind="process", head=0.15)


def d_fruit(ax, xy, s):
    ax.plot([xy[0], xy[0]], [xy[1] - 0.9, xy[1] + 0.5], color=P.edge("negative"), lw=2.2, zorder=12)
    ax.add_patch(Ellipse((xy[0], xy[1] - 0.9), 0.6, 0.15, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=12))
    ax.add_patch(Circle((xy[0], xy[1] + 0.75), 0.42, facecolor=P.fill("na"), edgecolor=P.edge("na"), lw=1.0, zorder=13))


def lift(fn, dy=0.6):
    return lambda ax, xy, s: fn(ax, (xy[0], xy[1] + dy), s)


fig, ax = bio.canvas(18.0, 15.0)
steps = [dict(text="spores", draw=lift(d_spores), shape="none", extent=(2.6, 2.8)),
         dict(text="amoebae feed\nand divide", draw=lift(d_amoebae), shape="none", extent=(2.6, 2.8)),
         dict(text="aggregation\nstreams (cAMP)", draw=lift(d_streams), shape="none", extent=(2.6, 2.8)),
         dict(text="tipped mound", draw=lift(d_mound), shape="none", extent=(2.6, 2.8)),
         dict(text="migrating slug", draw=lift(d_slug), shape="none", extent=(2.6, 2.8)),
         dict(text="fruiting body\n(stalk, sorus)", draw=lift(d_fruit), shape="none", extent=(2.6, 2.8))]
E.cycle(ax, (9.0, 7.6), 5.4, steps, start=90, clockwise=True, size="small",
        arrow_labels=["germination", "starvation", "", "", "culmination", "dispersal"], label_size="tiny")
bio.label(ax, (9.0, 8.2), "Dictyostelium discoideum", size="small", italic=True)
bio.label(ax, (9.0, 7.3), "red: prestalk   blue: prespore", size="tiny", color=P.muted())
