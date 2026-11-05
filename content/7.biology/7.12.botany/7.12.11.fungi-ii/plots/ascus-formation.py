"""Formation of asci and ascospores (after Pyronema; schematic). Orange and blue: nuclei of the two
parents; purple: the diploid nucleus after karyogamy."""
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(34, 11)


def nuc(xy, tok, r=0.13):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=14))


def tube(pts, w=0.5, tip=True):
    q = np.asarray(pts, float)
    from wikibio.core import smooth_closed  # noqa: F401
    plant.hypha(ax, q, width=w, septa=None, nuclei=0, tip=tip)


def septum(p, d, w=0.5):
    d = np.asarray(d, float); d /= np.hypot(*d); n = np.array([-d[1], d[0]])
    a, b = np.asarray(p) + n * w / 2, np.asarray(p) - n * w / 2
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("hypha" if False else "lipid_tail"), lw=1.6, zorder=13)


def lab(x, letter, text):
    bio.panel(ax, letter, (x - 0.2, 10.8))
    bio.label(ax, (x + 1.3, 1.0), text, size="tiny")


# A gametangia
lab(0.4, "A", "Antheridium and\nascogonium; plasmogamy")
ax.add_patch(Ellipse((1.6, 5.0), 1.6, 1.9, facecolor=P.light("rna"), edgecolor=P.edge("rna"), lw=1.0, zorder=8))
ax.add_patch(Ellipse((3.3, 5.6), 0.8, 2.4, angle=-15, facecolor=P.light("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=8))
tube([[1.4, 5.9], [1.8, 7.0], [2.7, 7.2], [3.3, 6.8]], w=0.18, tip=False)
rng = np.random.default_rng(1)
for k in range(8):
    nuc((1.2 + 0.25 * (k % 4), 4.6 + 0.35 * (k // 4)), "rna", 0.1)
    nuc((1.25 + 0.25 * (k % 4), 5.3 + 0.0 * k if k < 4 else 4.25), "dna", 0.1) if k < 4 else None
for k in range(3):
    nuc((3.25 + 0.08 * k, 5.0 + 0.5 * k), "dna", 0.1)
bio.callout(ax, (1.0, 4.3), (0.6, 2.8), "Ascogonium")
bio.callout(ax, (3.5, 6.4), (3.9, 8.6), "Antheridium")
bio.callout(ax, (2.2, 7.15), (1.2, 8.6), "Trichogyne")

# B ascogenous hyphae
lab(5.2, "B", "Ascogenous hyphae\n(dikaryotic)")
ax.add_patch(Ellipse((6.4, 3.2), 1.6, 1.6, facecolor=P.light("rna"), edgecolor=P.edge("rna"), lw=1.0, zorder=8))
for dx, top in [(-0.5, (5.6, 7.6)), (0.0, (6.5, 8.2)), (0.5, (7.4, 7.4))]:
    tube([[6.4 + dx * 0.6, 3.8], [6.4 + dx, 5.6], top], w=0.34)
    for t in (0.35, 0.7):
        p = np.array([6.4 + dx * 0.6, 3.8]) * (1 - t) + np.array(top) * t
        nuc(p + [-0.07, 0], "rna", 0.07); nuc(p + [0.07, 0], "dna", 0.07)


def hook(x0, stage):
    """A crozier: straight part up, then curled back down."""
    pts = [[x0, 2.5], [x0, 6.0], [x0 + 0.3, 7.2], [x0 + 1.1, 7.6], [x0 + 1.8, 7.0], [x0 + 1.9, 6.2]]
    tube(pts, w=0.5)
    if stage == "hook":
        nuc((x0 + 0.9, 7.55), "rna"); nuc((x0 + 0.35, 7.0), "dna")
    elif stage == "divide":
        nuc((x0 + 1.85, 6.4), "rna"); nuc((x0 + 0.95, 7.6), "dna"); nuc((x0 + 0.45, 7.25), "rna"); nuc((x0, 4.8), "dna")
        septum((x0 + 1.55, 7.35), (1, -1)); septum((x0, 6.0), (0, 1))
    elif stage == "fuse":
        nuc((x0 + 0.95, 7.6), "dna"); nuc((x0 + 0.45, 7.25), "rna")
        septum((x0 + 1.55, 7.35), (1, -1)); septum((x0, 6.0), (0, 1))
        tube([[x0 + 1.9, 6.2], [x0 + 1.4, 5.6], [x0 + 0.25, 5.4]], w=0.3, tip=False)
        nuc((x0, 4.9), "dna"); nuc((x0 + 0.05, 4.4), "rna")


lab(9.6, "C", "Crozier: hooked tip,\nconjugate division")
hook(10.0, "hook")
lab(13.4, "D", "Septa: tip cell, ascus\nmother cell, stalk cell")
hook(13.8, "divide")
bio.callout(ax, (15.85, 6.45), (16.6, 4.6), "Tip (n)")
bio.callout(ax, (14.7, 7.45), (14.4, 9.6), "Ascus mother cell (n + n)")
bio.callout(ax, (13.8, 4.8), (12.9, 3.2), "Stalk (n)")
lab(17.6, "E", "Tip fuses with stalk:\nnew dikaryotic cell")
hook(18.0, "fuse")

# F-I ascus development
lab(22.0, "F", "Karyogamy")
plant.ascus(ax, (23.3, 2.4), 6.0, stage="karyogamy")
lab(25.0, "G", "Meiosis:\n4 nuclei")
plant.ascus(ax, (26.3, 2.4), 6.0, stage="meiosis")
lab(28.0, "H", "Mitosis:\n8 nuclei")
plant.ascus(ax, (29.3, 2.4), 6.0, stage="mitosis")
lab(31.0, "I", "8 ascospores")
plant.ascus(ax, (32.3, 2.4), 6.0, stage="mature")
