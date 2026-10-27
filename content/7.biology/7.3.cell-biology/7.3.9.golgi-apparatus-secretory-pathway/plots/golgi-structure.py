# The Golgi apparatus. A: a stack of cisternae between the ER and the plasma membrane, with its cis face
# (cis Golgi network, CGN) towards the ER and the ER-Golgi intermediate compartment (ERGIC, vesicular-tubular
# clusters), its medial cisternae and its trans face and trans Golgi network (TGN), where cargo is sorted. COPII
# vesicles bring cargo from the ER, COPI vesicles return material to the ER and between cisternae. The bars
# show the classical cytochemical markers: reduced osmium tetroxide stains the cis cisternae, mannosidase II
# and NADPase the medial ones, nucleoside diphosphatase and thiamine pyrophosphatase the trans cisternae, and
# acid phosphatase (CMPase) the TGN. B: two models of transport through the stack. Vesicular transport:
# cisternae are stable compartments with resident enzymes and cargo moves forward in COPI vesicles.
# Cisternal maturation: cargo stays in a cisterna that forms at the cis face and matures into trans
# cisternae and TGN, while resident enzymes are carried backwards by COPI vesicles to younger cisternae.
import numpy as np
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(23, 10.5)
P = bio.P
bio.panel(ax, "A", (0.2, 10.3))
# ER at the bottom, PM at the top
bio.er(ax, (4.8, 1.2), 7.0, 0.9, sheets=2)
bio.label(ax, (0.5, 1.2), "ER", size="small", bold=True, ha="left")
T.band(ax, [(0.6, 9.6), (9.2, 9.6)], zorder=3)
bio.label(ax, (0.5, 9.95), "Plasma membrane", size="small", ha="left", color=P.muted())
names = ["cis (CGN)", "cis", "medial", "medial", "trans", "TGN"]
ys = [3.4, 4.25, 5.05, 5.85, 6.65, 7.6]
for k, (y, nm) in enumerate(zip(ys, names)):
    w = 5.2 - 0.25 * abs(k - 2.5)
    x = np.linspace(-w / 2, w / 2, 60)
    yy = y + 0.35 * (1 - (2 * x / w) ** 2)
    th = 0.12
    poly = np.c_[np.r_[x, x[::-1]] + 4.8, np.r_[yy + th, (yy - th)[::-1]]]
    if k in (0, 5):  # networks: fenestrated tubules
        for xx in np.linspace(-w / 2 + 0.3, w / 2 - 0.3, 7):
            T.coated_vesicle(ax, (4.8 + xx, y + 0.35 * (1 - (2 * xx / w) ** 2)), 0.16, kind=None, thickness=0.06,
                             lumen="golgi")
    else:
        ax.add_patch(bio.core.Polygon(poly, closed=True, facecolor=P.fill("golgi"), edgecolor=P.edge("golgi"), lw=1.0, zorder=5))
    bio.label(ax, (8.0, y + 0.1), nm, size="tiny", ha="left")
for xy in ((3.3, 2.35), (4.6, 2.45)):
    T.coated_vesicle(ax, xy, 0.17, kind="copii", thickness=0.05)
T.coated_vesicle(ax, (6.3, 2.4), 0.17, kind="copi", thickness=0.05)
bio.label(ax, (2.0, 2.45), "COPII / ERGIC", size="tiny", ha="right")
bio.label(ax, (6.75, 2.4), "COPI", size="tiny", ha="left")
for xy in ((3.2, 8.6), (5.0, 8.9), (6.4, 8.5)):
    bio.vesicle(ax, xy, 0.2, cargo="highlight")
bio.label(ax, (2.2, 8.4), "sorting\nto PM, granules,\nendosomes", size="tiny", ha="right")
markers = [("osmium", 3.15, 4.55, "channel"), ("Man II, NADPase", 4.8, 6.2, "positive"),
           ("NDPase, TPPase", 6.4, 7.0, "drug"), ("CMPase", 7.3, 8.0, "protein")]
for k, (txt, y0, y1, tok) in enumerate(markers):
    xx = 10.3 + 0.35 * k
    ax.plot([xx, xx], [y0, y1], color=P.edge(tok), lw=5, solid_capstyle="butt")
    bio.label(ax, (xx, y1 + 0.15), txt, size="tiny", rotation=90, ha="center", va="bottom")

bio.panel(ax, "B", (12.6, 10.3))


def stack(x0, title, mature):
    bio.label(ax, (x0 + 2.5, 9.7), title, size="small", bold=True)
    for k in range(4):
        y = 3.0 + 1.4 * k
        col = ["channel", "positive", "drug", "protein"][k]
        ax.add_patch(bio.core.FancyBboxPatch((x0, y), 3.2, 0.42, boxstyle="round,pad=0,rounding_size=0.2",
                                             facecolor=P.fill("golgi"), edgecolor=P.edge("golgi"), lw=1.0, zorder=5))
        for j in range(3):  # resident enzymes
            ax.add_patch(bio.core.Circle((x0 + 0.5 + 0.35 * j, y + 0.21), 0.09, facecolor=P.fill(col), edgecolor=P.edge(col),
                                         lw=0.6, zorder=6))
        ax.add_patch(bio.core.Circle((x0 + 2.4, y + 0.21), 0.11, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                                     lw=0.6, zorder=6))
    if not mature:
        bio.label(ax, (x0 - 0.2, 3.2), "cis", size="tiny", ha="right")
        bio.label(ax, (x0 - 0.2, 7.4), "trans", size="tiny", ha="right")
    if not mature:
        for k in range(3):
            y = 3.0 + 1.4 * k
            T.coated_vesicle(ax, (x0 + 3.75, y + 0.9), 0.15, kind="copi", thickness=0.05)
            ax.add_patch(bio.core.Circle((x0 + 3.75, y + 0.9), 0.06, facecolor=P.fill("highlight"), edgecolor="none", zorder=12))
            bio.arrow(ax, (x0 + 3.3, y + 0.35), (x0 + 3.65, y + 0.7), kind="process", head=0.13)
            bio.arrow(ax, (x0 + 3.85, y + 1.1), (x0 + 3.3, y + 1.45), kind="process", head=0.13)
        bio.label(ax, (x0 + 1.6, 2.2), "stable cisternae;\ncargo moves in vesicles", size="tiny")
    else:
        bio.arrow(ax, (x0 + 4.0, 3.0), (x0 + 4.0, 7.6), kind="process", lw=2.0)
        bio.label(ax, (x0 + 4.2, 5.3), "cisterna\nmatures", size="tiny", ha="left")
        for k in range(3):
            y = 3.0 + 1.4 * k
            T.coated_vesicle(ax, (x0 - 0.55, y + 0.9), 0.15, kind="copi", thickness=0.05)
            ax.add_patch(bio.core.Circle((x0 - 0.55, y + 0.9), 0.06, facecolor=P.fill(["positive", "drug", "protein"][k]),
                                         edgecolor="none", zorder=12))
            bio.arrow(ax, (x0 - 0.1, y + 1.45), (x0 - 0.45, y + 1.1), kind="process", head=0.13)
            bio.arrow(ax, (x0 - 0.65, y + 0.7), (x0 - 0.1, y + 0.35), kind="process", head=0.13)
        bio.label(ax, (x0 + 1.6, 2.2), "cargo stays; enzymes\nrecycle backwards in COPI", size="tiny")


stack(13.4, "Vesicular transport", False)
stack(18.9, "Cisternal maturation", True)
bio.label(ax, (17.8, 0.9), "yellow: cargo; small coloured dots: resident enzymes of each cisterna", size="tiny", color=P.muted())
