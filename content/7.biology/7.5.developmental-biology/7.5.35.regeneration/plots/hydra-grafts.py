"""Grafting experiments on the Hydra head and the molecular circuit behind them.

A-D: schematic polyps (tentacles and hypostome on top, basal disc below); a piece of tissue (orange) is grafted
into the side of the body column of a host. A: hypostome grafted into the column of an intact host induces a
secondary axis, built mostly from host cells (the hypostome is an organizer). B: subhypostomal tissue grafted
just below an intact head forms no head (head inhibition). C: the same graft forms a head if the host is
decapitated; a head also regenerates at the cut. D: the same graft forms a head when placed far down the column,
out of range of the host head. E: the circuit in activity-flow notation: Wnt3 activates beta-catenin/TCF,
which activates Wnt3 expression (self-enhancement) and Sp5; Sp5 represses Wnt3 (inhibition); Wnt signaling is
highest in the hypostome. The loop has the logic of the activator-inhibitor model.
"""

from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon
import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(34.0, 12.5)
LW = bio.core.LINE


def tentacles(cx, top, angle=0.0, n=4, size=1.0, tok="animal"):
    import math
    th = math.radians(angle)
    ux, uy = -math.sin(th), math.cos(th)
    vx, vy = math.cos(th), math.sin(th)
    tip = (cx[0] + 0.45 * size * ux, cx[1] + 0.45 * size * uy)
    ax.add_patch(Polygon([(cx[0] - 0.32 * size * vx, cx[1] - 0.32 * size * vy), tip,
                          (cx[0] + 0.32 * size * vx, cx[1] + 0.32 * size * vy)], closed=True,
                         fc=P.fill(tok), ec=P.edge(tok), lw=LW * 0.8, zorder=6))
    for k in range(n):
        s = (k - (n - 1) / 2) / ((n - 1) / 2)
        bx, by = cx[0] + 0.25 * s * size * vx, cx[1] + 0.25 * s * size * vy
        ex = bx + 1.2 * size * (s * 0.9 * vx + 0.55 * ux)
        ey = by + 1.2 * size * (s * 0.9 * vy + 0.55 * uy)
        ax.plot([bx, ex], [by, ey], color=P.edge(tok), lw=LW * 1.3, solid_capstyle="round", zorder=5)


def polyp(x, y0, h=5.2, w=0.9, head=True):
    ax.add_patch(FancyBboxPatch((x - w / 2, y0), w, h, boxstyle="round,pad=0,rounding_size=0.3",
                                fc=P.fill("animal"), ec=P.edge("animal"), lw=LW, zorder=4))
    ax.add_patch(Ellipse((x, y0), 1.3, 0.35, fc=P.fill("bone"), ec=P.edge("bone"), lw=LW * 0.8, zorder=5))
    if head:
        tentacles((x, y0 + h), y0 + h)
    else:
        ax.plot([x - w / 2 - 0.2, x + w / 2 + 0.2], [y0 + h + 0.15, y0 + h + 0.15], color=P.muted(), lw=0.9,
                ls=(0, (2, 2)), zorder=6)


def graft(x, y, head):
    ax.add_patch(FancyBboxPatch((x + 0.45, y - 0.3), 1.2, 0.6, boxstyle="round,pad=0,rounding_size=0.25",
                                fc=P.fill("drug"), ec=P.edge("drug"), lw=LW, zorder=7))
    if head:
        tentacles((x + 1.65, y), y, angle=-90, size=0.8, tok="drug")


cases = (
    ("A", "Hypostome graft,\nintact host", True, 3.2, True, "secondary axis"),
    ("B", "Subhypostome graft\nnear the head", True, 4.6, False, "no head"),
    ("C", "Same graft,\nhost decapitated", False, 4.6, True, "head forms"),
    ("D", "Same graft far\nfrom the head", True, 1.6, True, "head forms"),
)
for i, (letter, title, head, gy, out, res) in enumerate(cases):
    x = 2.2 + 4.6 * i
    bio.panel(ax, letter, (x - 1.9, 12.2))
    bio.label(ax, (x + 0.3, 11.3), title, size="tiny", ha="center")
    polyp(x, 2.2, head=head)
    if letter == "C":
        tentacles((x, 7.4 + 0.0), 7.4, size=0.7, tok="positive")
    graft(x, 2.2 + gy, out)
    bio.label(ax, (x + 0.4, 1.0), res, size="small", bold=True,
              color=P.edge("negative" if not out else "positive"))

bio.label(ax, (9.2, 0.25), "grafted tissue (orange); green tentacles: head regenerated at the cut", size="tiny",
          color=P.muted())

# E: the circuit
bio.panel(ax, "E", (19.6, 12.2))
bio.label(ax, (20.6, 11.3), "Head organizer circuit", size="small", bold=True, ha="left")
d = network.Diagram(ax)
d.activity("wnt", (23.0, 8.0), "Wnt3", italic=False, token="receptor", w=3.0, h=1.2)
d.activity("bcat", (29.5, 8.0), "β-catenin/TCF", token="protein", w=4.0, h=1.2)
d.activity("sp5", (29.5, 3.8), "Sp5", token="enzyme", w=3.0, h=1.2)
d.phenotype("head", (23.0, 3.8), "head identity", token="highlight", w=4.0, h=1.3)
d.connect("wnt", "bcat", kind="positive", bend=0.25)
d.connect("bcat", "wnt", kind="positive", bend=0.25)
bio.label(ax, (26.3, 9.75), "self-enhancement", size="tiny", color=P.muted())
d.connect("bcat", "sp5", kind="positive")
d.connect("sp5", "wnt", kind="negative")
bio.label(ax, (25.2, 5.4), "inhibition", size="tiny", color=P.muted(), ha="right")
d.connect("bcat", "head", kind="positive", dashed=True)
bio.label(ax, (31.9, 5.9), "induces", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (26.3, 1.4), "activator a ~ Wnt3 / β-catenin; inhibitor h ~ Sp5 (and others)", size="tiny",
          color=P.muted())
