"""Clamp connection (A-D) and basidium development (E-I), schematic. Orange and blue: nuclei from the two
compatible primary hyphae; purple: the diploid nucleus."""
import numpy as np
from matplotlib.patches import Circle, Arc

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(32, 10)
W = 0.7


def nuc(xy, tok, r=0.16):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=14))


def septum(x, y0, y1):
    ax.plot([x, x], [y0, y1], color=P.edge("lipid_tail"), lw=1.8, zorder=13)


def hypha_seg(y, x0, x1):
    plant.hypha(ax, np.array([[x0, y], [x1, y]]), width=W, septa=None, nuclei=0, tip=True)


def clamp(xc, y, closed):
    # a small backwards-pointing hook on top of the hypha
    th = np.linspace(0, np.pi, 30)
    xs = xc + 0.55 * np.cos(th); ys = y + W / 2 + 0.45 * np.sin(th)
    ax.plot(xs, ys, color=P.edge("lipid_tail"), lw=0.35 * 22, zorder=6, solid_capstyle="round", alpha=1)
    ax.plot(xs, ys, color=P.fill("lipid_tail"), lw=0.35 * 16, zorder=6.5, solid_capstyle="round")
    if not closed:
        ax.add_patch(Circle((xc - 0.55, y + W / 2 + 0.02), 0.13, facecolor=bio.P.surface(), edgecolor="none", zorder=7))


steps = [("A", "Hook grows back\nbetween the nuclei"), ("B", "Conjugate division;\none nucleus in the hook"),
         ("C", "Septa form"), ("D", "Hook fuses: two\ndikaryotic cells")]
for i, (letter, txt) in enumerate(steps):
    x0 = 0.6 + i * 4.3
    y = 6.0
    bio.panel(ax, letter, (x0 - 0.2, 9.8))
    bio.label(ax, (x0 + 1.9, 3.6), txt, size="tiny")
    hypha_seg(y, x0, x0 + 3.8)
    xc = x0 + 2.0
    clamp(xc, y, closed=(i == 3))
    if i == 0:
        nuc((xc + 1.0, y), "rna"); nuc((xc - 0.2, y), "dna")
    elif i == 1:
        nuc((xc + 1.4, y), "rna"); nuc((xc + 0.6, y), "rna"); nuc((xc + 0.9, y + 0.05), "dna"); nuc((xc - 0.55, y + W / 2 + 0.3), "dna")
        ax.lines[-1:]
    else:
        nuc((xc + 1.2, y), "rna"); nuc((xc + 0.6, y), "dna")
        septum(xc + 0.0, y - W / 2, y + W / 2)
        if i == 2:
            nuc((xc - 1.0, y), "rna"); nuc((xc - 0.5, y + W / 2 + 0.35), "dna")
            septum(xc + 0.4, y + W / 2, y + W / 2 + 0.45)
        else:
            nuc((xc - 1.0, y), "rna"); nuc((xc - 0.5, y - 0.02), "dna")
            septum(xc + 0.4, y + W / 2, y + W / 2 + 0.45)
for i, st in enumerate(["dikaryotic", "karyogamy", "meiosis", "sterigmata", "mature"]):
    x = 19.0 + i * 2.8
    plant.basidium(ax, (x, 3.0), 3.6, stage=st)
    bio.panel(ax, "EFGHI"[i], (x - 1.0, 9.8))
    bio.label(ax, (x, 2.2), ["Young basidium\n(n + n)", "Karyogamy\n(2n)", "Meiosis:\n4 nuclei", "4 sterigmata", "4 basidiospores"][i],
              size="tiny", va="top")
