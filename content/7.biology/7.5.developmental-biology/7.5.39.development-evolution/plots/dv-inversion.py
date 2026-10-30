"""Deep homology of dorso-ventral patterning and the inversion of the axis (schematic cross sections).

Left: Drosophila embryo. Dpp (a BMP) is high dorsally and its antagonist Sog (Chordin) ventrally; the
neuroectoderm forms where BMP signaling is lowest, on the ventral side, and is subdivided from the midline
outwards into the columns vnd, ind and msh. Right: a vertebrate (Xenopus) embryo, drawn with the dorsal side
down so that the two diagrams align: BMP4 is high ventrally, Chordin (from the organizer) dorsally; the neural
plate forms dorsally and is subdivided from the midline outwards into Nkx2.2, Gsx and Msx domains, the
homologues of vnd, ind and msh. Ring: ectoderm; bars beside each section: the BMP activity gradient.
"""

import numpy as np
import wikibio as bio
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path

P = bio.P
fig, ax = bio.canvas(30.0, 13.0)


def section(cx, cy, r, title, top, bottom, cols, nerve_label, bmp, antag, italic):
    th = np.linspace(0, 2 * np.pi, 400)
    # ectoderm ring segments: neural sector at the bottom (angles around 270 degrees)
    ax.add_patch(PathPatch(Path(np.c_[cx + r * np.cos(th), cy + r * np.sin(th)]),
                                    facecolor=P.fill("ectoderm"), edgecolor=P.edge("ectoderm"), lw=1.0, zorder=4))
    ax.add_patch(PathPatch(Path(np.c_[cx + 0.86 * r * np.cos(th), cy + 0.86 * r * np.sin(th)]),
                                    facecolor=P.mix(P.fill("neutral"), P.surface(), 0.6), edgecolor=P.edge("ectoderm"), lw=0.8, zorder=5))
    toks = ("drug", "enzyme", "protein")
    for i, (name, tok) in enumerate(zip(cols, toks)):
        for sgn in (-1, 1):
            a0 = 270 + sgn * (6 + 18 * i)
            a1 = 270 + sgn * (6 + 18 * (i + 1))
            aa = np.radians(np.linspace(min(a0, a1), max(a0, a1), 40))
            outer = np.c_[cx + r * np.cos(aa), cy + r * np.sin(aa)]
            inner = np.c_[cx + 0.86 * r * np.cos(aa[::-1]), cy + 0.86 * r * np.sin(aa[::-1])]
            ax.add_patch(PathPatch(Path(np.r_[outer, inner, outer[:1]]),
                                            facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=7))
        aa = np.radians(270 + 6 + 18 * i + 9)
        p0 = (cx + 0.93 * r * np.cos(aa), cy + 0.93 * r * np.sin(aa))
        p1 = (cx + 1.55 * r * np.cos(aa) + 1.6 + 0.2 * i, cy + 1.2 * r * np.sin(aa) - 0.6 - 0.25 * i)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.muted(), lw=0.7, zorder=8)
        ax.plot([p0[0]], [p0[1]], "o", ms=2.5, color=P.muted(), zorder=8)
        bio.label(ax, (p1[0] + 0.15, p1[1]), name, size="tiny", ha="left", italic=True)
    aa = np.radians(np.linspace(264, 276, 20))
    midline = np.r_[np.c_[cx + r * np.cos(aa), cy + r * np.sin(aa)],
                    np.c_[cx + 0.86 * r * np.cos(aa[::-1]), cy + 0.86 * r * np.sin(aa[::-1])]]
    ax.add_patch(PathPatch(Path(np.r_[midline, midline[:1]]), facecolor=P.fill("neutral"),
                                    edgecolor=P.edge("neutral"), lw=0.6, zorder=7))
    bio.label(ax, (cx, cy + r + 1.6), title, size="small", bold=True, italic=italic)
    bio.label(ax, (cx, cy + r + 0.6), top, size="tiny", color=P.muted())
    bio.label(ax, (cx, cy - r - 0.6), bottom, size="tiny", color=P.muted())
    bio.label(ax, (cx - r - 1.7, cy - r + 0.2), nerve_label, size="tiny", ha="center")
    # BMP gradient bar
    bx = cx + r + 1.2
    n = 24
    for k in range(n):
        f = k / (n - 1)
        y0 = cy - r + 2 * r * f
        ax.add_patch(FancyBboxPatch((bx, y0), 0.55, 2 * r / n * 1.08, boxstyle="square,pad=0",
                                             facecolor=P.mix(P.fill("drug"), P.surface(), 1 - f), lw=0, zorder=4))
    bio.label(ax, (bx + 0.28, cy + r + 0.35), bmp, size="tiny")
    bio.label(ax, (bx + 0.28, cy - r - 0.35), antag, size="tiny")


section(6.5, 6.3, 3.6, "Drosophila", "dorsal", "ventral", ("vnd", "ind", "msh"), "ventral\nnerve cord",
        "Dpp high", "Sog high", True)
section(21.0, 6.3, 3.6, "Xenopus (drawn dorsal side down)", "ventral", "dorsal", ("Nkx2.2", "Gsx", "Msx"),
        "dorsal\nneural plate", "BMP4 high", "Chordin high", False)
bio.label(ax, (13.8, 6.3), "homologous\ngenes,\ninverted\naxis", size="small", color=P.muted())
