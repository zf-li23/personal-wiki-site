"""ESCRT machinery and membrane topology.
(A) Sorting of a ubiquitylated receptor into an intralumenal vesicle on the limiting membrane of a maturing
endosome (cytosol above, lumen below): ESCRT-0 binds ubiquitin and PI(3)P and clusters cargo (1); ESCRT-I
and ESCRT-II bind in turn and the membrane begins to bend away from the cytosol (2); ESCRT-III filaments
polymerize at the neck of the bud while deubiquitylating enzymes remove the ubiquitin (3); the AAA ATPase
Vps4 disassembles ESCRT-III, the neck is cut and the vesicle, carrying the receptor, is free in the lumen (4).
(B) Three topologically equivalent ESCRT-dependent scissions, each cutting a membrane neck from its
cytosolic side: intralumenal vesicles of multivesicular bodies, budding of enveloped viruses such as HIV
from the plasma membrane, and abscission of the cytokinetic bridge."""

import numpy as np

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(23.0, 10.0, scale=0.42)
TH = 0.14


def bez(p0, p1, p2, p3, n=40):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2, p3 = map(np.asarray, (p0, p1, p2, p3))
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def arc(c, r, a0, a1, n=50):
    a = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + r * np.cos(a), c[1] + r * np.sin(a)]


def band(pts, token="membrane", zorder=6, closed=False):
    q, nrm, _ = bio.core.polyline(pts, n=900 if not closed else 300, closed=closed)
    o, i = q + nrm * TH / 2, q - nrm * TH / 2
    bio.shape(ax, np.vstack([o, i[::-1]]), token, lw=0, zorder=zorder)
    for ln in (o, i):
        ax.plot(ln[:, 0], ln[:, 1], color=P.edge(token), lw=0.8, zorder=zorder + 1)


def ub(c, k=2):
    for j in range(k):
        ax.add_patch(bio.core.Circle((c[0] + 0.17 * j, c[1] + 0.1 * j), 0.1, facecolor=P.fill("highlight"),
                                     edgecolor=P.edge("highlight"), lw=0.6, zorder=14))


def receptor(x, y, up=1, tail=True, ubq=True, lig=True):
    """Transmembrane receptor through a membrane at height y; cytosolic tail points up (up=1)."""
    ax.plot([x, x], [y - 0.55 * up, y + 0.35 * up], color=P.edge("receptor"), lw=2.4, zorder=12, solid_capstyle="round")
    if lig:
        ax.add_patch(bio.core.Circle((x, y - 0.68 * up), 0.15, facecolor=P.fill("negative"), edgecolor=P.edge("negative"),
                                     lw=0.6, zorder=13))
    if ubq:
        ub((x + 0.08, y + 0.48 * up))


def escrt(c, text, w=1.0, h=0.5, token="protein"):
    bio.box(ax, c, w, h, token, text=text, size="tiny", radius=0.12, zorder=13)


Y = 6.2
# ---- A --------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.9))
x_bud = 8.3
neck = 0.32
pts = np.vstack([np.array([[0.4, Y], [3.9, Y]]),
                 bez((3.9, Y), (4.4, Y), (4.6, Y - 0.35), (5.1, Y - 0.35)),
                 bez((5.1, Y - 0.35), (5.6, Y - 0.35), (5.8, Y), (6.3, Y)),
                 np.array([[6.3, Y], [x_bud - 0.9, Y]]),
                 bez((x_bud - 0.9, Y), (x_bud - neck, Y), (x_bud - neck, Y - 0.2), (x_bud - neck, Y - 0.45)),
                 arc((x_bud, Y - 1.25), 0.86, 112, 428, 70)[0:70],
                 bez((x_bud + neck, Y - 0.45), (x_bud + neck, Y - 0.2), (x_bud + neck, Y), (x_bud + 0.9, Y)),
                 np.array([[x_bud + 0.9, Y], [14.2, Y]])])
bio.shape(ax, np.vstack([pts, [[14.2, 9.4], [0.4, 9.4]]]), "cytoplasm", lw=0, zorder=1)
bio.shape(ax, np.vstack([pts, [[14.2, 1.0], [0.4, 1.0]]]), "extracellular", lw=0, zorder=1)
band(pts)
bio.label(ax, (0.6, 9.0), "Cytosol", size="small", ha="left", color=P.muted(), bold=True)
bio.label(ax, (0.6, 1.4), "Endosome lumen", size="small", ha="left", color=P.muted(), bold=True)
# 1: ESCRT-0 on PI(3)P with clathrin
for x in (1.4, 2.2):
    receptor(x, Y)
escrt((1.8, 7.55), "ESCRT-0", w=1.4)
bio.label(ax, (1.8, 8.1), "Hrs/STAM · clathrin", size="tiny", color=P.muted())
for x in (1.0, 2.6):
    ax.add_patch(bio.core.Circle((x, Y + 0.17), 0.07, color=P.edge("lipid"), lw=0, zorder=13))
bio.label(ax, (2.95, Y + 0.42), "PI(3)P", size="tiny", color=P.edge("lipid"), ha="left")
bio.label(ax, (1.8, 4.6), "1", size="small", bold=True)
# 2: ESCRT-I and -II, shallow bud
for x in (4.75, 5.45):
    receptor(x, Y - 0.33)
escrt((5.1, 7.25), "ESCRT-I", w=1.3)
escrt((5.1, 7.85), "ESCRT-II", w=1.3, token="enzyme")
bio.label(ax, (5.1, 4.6), "2", size="small", bold=True)
# 3: deep bud with ESCRT-III spiral at the neck
for ang in (230, 300):
    a = np.radians(ang)
    c = np.array([x_bud, Y - 1.25]) + 0.86 * np.array([np.cos(a), np.sin(a)])
    ax.plot([c[0], c[0] + 0.45 * np.cos(a)], [c[1], c[1] + 0.45 * np.sin(a)], color=P.edge("receptor"), lw=2.4, zorder=12)
    ax.add_patch(bio.core.Circle(c + 0.6 * np.array([np.cos(a), np.sin(a)]), 0.15, facecolor=P.fill("negative"),
                                 edgecolor=P.edge("negative"), lw=0.6, zorder=13))
for k in range(5):
    w = 0.95 - 0.13 * k
    yy = Y - 0.05 - 0.1 * k
    ax.plot([x_bud - w / 2, x_bud + w / 2], [yy + 0.06, yy - 0.06], color=P.edge("positive"), lw=2.6, zorder=14,
            solid_capstyle="round")
bio.label(ax, (x_bud + 0.85, Y + 0.65), "ESCRT-III", size="tiny", color=P.edge("positive"), ha="left", bold=True)
ub((x_bud - 1.4, 7.6))
bio.arrow(ax, (x_bud - 0.9, 7.1), (x_bud - 1.25, 7.45), kind="process", head=0.12)
bio.label(ax, (x_bud - 1.25, 8.1), "DUB removes Ub", size="tiny", color=P.muted())
bio.label(ax, (x_bud, 3.6), "3", size="small", bold=True)
# 4: Vps4 and the free intralumenal vesicle
x4 = 12.2
escrt((x4, 7.2), "Vps4", w=1.0, token="atp")
for k in range(4):
    ax.plot([x4 - 0.7 + 0.35 * k, x4 - 0.55 + 0.35 * k], [7.9 + 0.15 * (k % 2), 8.15 + 0.1 * (k % 2)],
            color=P.edge("positive"), lw=2.2, zorder=14, solid_capstyle="round")
bio.label(ax, (x4 + 0.8, 8.1), "ESCRT-III subunits\nrecycled", size="tiny", color=P.muted(), ha="left")
ilv = (x4, 3.7)
band(arc(ilv, 0.8, 0, 360, 120), "membrane", closed=True)
for ang in (210, 330):
    a = np.radians(ang)
    c = np.array(ilv) + 0.8 * np.array([np.cos(a), np.sin(a)])
    ax.plot([c[0] - 0.3 * np.cos(a), c[0] + 0.35 * np.cos(a)], [c[1] - 0.3 * np.sin(a), c[1] + 0.35 * np.sin(a)],
            color=P.edge("receptor"), lw=2.4, zorder=12)
    ax.add_patch(bio.core.Circle(c + 0.5 * np.array([np.cos(a), np.sin(a)]), 0.15, facecolor=P.fill("negative"),
                                 edgecolor=P.edge("negative"), lw=0.6, zorder=13))
bio.label(ax, (ilv[0], 2.4), "4  intralumenal vesicle", size="small")
bio.arrow(ax, (x_bud + 1.2, 4.6), (x4 - 1.1, 4.0), kind="process", head=0.16)

# ---- B: topology -----------------------------------------------------------------------------------------
bio.panel(ax, "B", (15.0, 9.9))
bio.label(ax, (19.0, 9.45), "Budding away from the cytosol", size="small", bold=True)


def spiral(x, y, w=0.55, horizontal=True):
    for k in range(3):
        ww = w - 0.12 * k
        if horizontal:
            ax.plot([x - ww / 2, x + ww / 2], [y + 0.08 * k, y + 0.08 * k], color=P.edge("positive"), lw=2.2, zorder=14)
        else:
            ax.plot([x + 0.08 * k, x + 0.08 * k], [y - ww / 2, y + ww / 2], color=P.edge("positive"), lw=2.2, zorder=14)


# (i) MVB: endosome with an inward bud
c1 = np.array([16.6, 6.6])
bio.shape(ax, arc(c1, 1.35, 0, 360, 120), "cytoplasm", lw=0, zorder=1)
bio.shape(ax, arc(c1, 1.15, 0, 360, 120), "extracellular", lw=0, zorder=2)
ring = np.vstack([arc(c1, 1.15, 100, 440, 120)])
band(ring, closed=True)
band(arc(c1 + (0, 0.45), 0.35, 0, 360, 60), closed=True)
spiral(c1[0], c1[1] + 0.95, 0.45)
bio.label(ax, (c1[0], 4.75), "MVB vesicle", size="tiny")
# (ii) virus budding from the plasma membrane (cytosol below)
x2, y2 = 19.6, 6.2
bio.shape(ax, [(18.3, y2), (20.9, y2), (20.9, 5.0), (18.3, 5.0)], "cytoplasm", lw=0, zorder=1)
band(np.vstack([np.array([[18.3, y2], [x2 - 0.45, y2]]), bez((x2 - 0.45, y2), (x2 - 0.15, y2), (x2 - 0.15, y2 + 0.1), (x2 - 0.15, y2 + 0.3)),
                arc((x2, y2 + 0.9), 0.62, 256, -76, 60)[::-1][::-1],
                bez((x2 + 0.15, y2 + 0.3), (x2 + 0.15, y2 + 0.1), (x2 + 0.15, y2), (x2 + 0.45, y2)),
                np.array([[x2 + 0.45, y2], [20.9, y2]])]))
for t in np.linspace(0, 2 * np.pi, 10, endpoint=False):
    ax.add_patch(bio.core.Circle((x2 + 0.45 * np.cos(t), y2 + 0.9 + 0.45 * np.sin(t)), 0.07, color=P.edge("virus"), lw=0, zorder=12))
spiral(x2, y2 - 0.1, 0.45)
bio.label(ax, (x2, 4.75), "HIV budding", size="tiny")
# (iii) cytokinetic bridge
x3, y3 = 19.0, 2.4
for sgn in (-1, 1):
    cc = (x3 + sgn * 1.9, y3)
    bio.shape(ax, arc(cc, 1.2, 0, 360, 100), "cytoplasm", lw=0, zorder=1)
outline = np.vstack([arc((x3 - 1.9, y3), 1.2, 15, 345, 80),
                     bez((x3 - 0.75, y3 - 0.3), (x3 - 0.3, y3 - 0.2), (x3 - 0.1, y3 - 0.13), (x3, y3 - 0.13)),
                     bez((x3, y3 - 0.13), (x3 + 0.1, y3 - 0.13), (x3 + 0.3, y3 - 0.2), (x3 + 0.75, y3 - 0.3)),
                     arc((x3 + 1.9, y3), 1.2, 195, 525, 80),
                     bez((x3 + 0.75, y3 + 0.3), (x3 + 0.3, y3 + 0.2), (x3 + 0.1, y3 + 0.13), (x3, y3 + 0.13)),
                     bez((x3, y3 + 0.13), (x3 - 0.1, y3 + 0.13), (x3 - 0.3, y3 + 0.2), (x3 - 0.75, y3 + 0.3))])
bio.shape(ax, outline, "cytoplasm", lw=0, zorder=2)
band(outline, closed=True)
spiral(x3 - 0.08, y3, 0.24, horizontal=False)
bio.label(ax, (x3, 0.55), "abscission of the cytokinetic bridge", size="tiny")
bio.label(ax, (20.15, 5.75), "ESCRT-III", size="tiny", color=P.edge("positive"), ha="left", bold=True)
