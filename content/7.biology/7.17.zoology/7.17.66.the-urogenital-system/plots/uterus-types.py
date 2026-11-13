# Uterine types of placental mammals, the marsupial tract and the bird oviduct, schematic ventral views.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(28.5, 8.2)
OVI, UT, CX, VA = "lysosome", "receptor", "protein", "channel"


def tube(pts, tok, w=0.32):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=P.edge(tok), lw=w * 30 + 1.4, solid_capstyle="round", solid_joinstyle="round", zorder=4)
    ax.plot(p[:, 0], p[:, 1], color=P.fill(tok), lw=w * 30, solid_capstyle="round", solid_joinstyle="round", zorder=4.1)


def ovary(c):
    bio.shape(ax, vs.oval(c, 0.28, 0.2), token="highlight", zorder=5, lw=0.7)


def uterus(cx, fuse, title):
    """fuse: 0 duplex, 1 bipartite, 2 bicornuate, 3 simplex."""
    bio.label(ax, (cx, 7.7), title, size="small")
    top, mid = 6.0, {0: 2.4, 1: 3.0, 2: 3.9, 3: 5.4}[fuse]
    for s in (-1, 1):
        ovary((cx + s * 1.5, top + 0.6))
        tube([(cx + s * 1.5, top + 0.4), (cx + s * 1.3, top), (cx + s * 1.1, top - 0.2)], OVI, w=0.08)
        if fuse < 3:
            tube([(cx + s * 1.05, top - 0.25), (cx + s * 0.75, (top + mid) / 2), (cx + s * (0.32 if fuse else 0.38), mid)], UT, w=0.17)
        else:
            tube([(cx + s * 1.05, top - 0.25), (cx + s * 0.4, top - 0.6)], OVI, w=0.08)
    if fuse == 0:
        for s in (-1, 1):
            tube([(cx + s * 0.38, mid), (cx + s * 0.2, mid - 0.6)], CX, w=0.12)
    elif fuse == 3:
        bio.shape(ax, vs.smooth([(cx - 0.65, top - 0.5), (cx, top - 0.3), (cx + 0.65, top - 0.5), (cx + 0.5, 3.0), (cx, 2.6),
                                 (cx - 0.5, 3.0)]), token=UT, zorder=4)
        mid = 2.6
    else:
        bio.shape(ax, vs.smooth([(cx - 0.45, mid + 0.1), (cx, mid + 0.25), (cx + 0.45, mid + 0.1), (cx + 0.38, 2.4), (cx, 2.2),
                                 (cx - 0.38, 2.4)]), token=UT, zorder=4)
        if fuse == 1:
            ax.plot([cx, cx], [mid + 0.2, 2.6], color=P.edge(UT), lw=1.2, zorder=5)
        mid = 2.2
    tube([(cx, mid), (cx, 1.5)], CX, w=0.12)
    bio.shape(ax, np.array([(cx - 0.3, 1.5), (cx + 0.3, 1.5), (cx + 0.35, 0.3), (cx - 0.35, 0.3)]), token=VA, zorder=4)


uterus(2.2, 0, "A  Duplex")
uterus(6.4, 1, "B  Bipartite")
uterus(10.6, 2, "C  Bicornuate")
uterus(14.8, 3, "D  Simplex")
# E marsupial
cx = 19.0
bio.label(ax, (cx, 7.7), "E  Marsupial", size="small")
for s in (-1, 1):
    ovary((cx + s * 1.5, 6.6))
    tube([(cx + s * 1.5, 6.4), (cx + s * 1.1, 5.8)], OVI, w=0.08)
    tube([(cx + s * 1.05, 5.7), (cx + s * 0.55, 4.6)], UT, w=0.17)
    tube([(cx + s * 0.5, 4.4), (cx + s * 1.1, 3.4), (cx + s * 0.9, 1.6), (cx + s * 0.25, 0.9)], VA, w=0.1)
tube([(cx, 4.3), (cx, 0.9)], VA, w=0.12)
bio.shape(ax, np.array([(cx - 0.4, 0.9), (cx + 0.4, 0.9), (cx + 0.4, 0.3), (cx - 0.4, 0.3)]), token="neutral", zorder=4)
bio.callout(ax, (cx + 1.0, 2.6), (cx + 2.0, 3.0), "lateral vaginae", size="tiny")
bio.callout(ax, (cx, 2.6), (cx + 1.9, 1.6), "median birth canal", size="tiny")
bio.callout(ax, (cx, 0.6), (cx + 1.6, 0.4), "urogenital sinus", size="tiny")
# F bird
cx = 23.4
bio.label(ax, (cx, 7.7), "F  Bird", size="small")
ovary((cx + 0.8, 6.7))
pts = [(cx + 0.6, 6.3), (cx + 0.3, 5.6), (cx + 0.5, 4.6), (cx + 0.2, 3.8), (cx + 0.3, 2.9), (cx + 0.1, 2.0), (cx + 0.1, 1.1)]
toks = [OVI, "rrna", "trna", UT, VA, VA]
for (a, b), tk, lab in zip(zip(pts[:-1], pts[1:]), toks, ["infundibulum", "magnum", "isthmus", "shell gland", "vagina", None]):
    tube([a, b], tk, w=0.14)
    if lab:
        bio.label(ax, (max(a[0], b[0]) + 0.35, (a[1] + b[1]) / 2), lab, size="tiny", ha="left")
bio.shape(ax, vs.oval((cx - 0.2, 0.8), 0.5, 0.3), token="neutral", zorder=4)
tube([(cx - 0.7, 4.0), (cx - 0.6, 1.2)], OVI, w=0.04)
# legend
ly = 6.6
for tok, t in ((OVI, "oviduct"), (UT, "uterus"), (CX, "cervix"), (VA, "vagina"), ("highlight", "ovary")):
    bio.shape(ax, np.array([(26.2, ly - 0.15), (26.6, ly - 0.15), (26.6, ly + 0.15), (26.2, ly + 0.15)]), token=tok, lw=0.6)
    bio.label(ax, (26.75, ly), t, size="tiny", ha="left")
    ly -= 0.6
