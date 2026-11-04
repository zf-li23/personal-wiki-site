"""Peptidoglycan: the glycan tetrapeptide unit, direct DAP-D-Ala cross-links (E. coli) and pentaglycine
interbridges (S. aureus); sites of lysozyme and of transpeptidases blocked by penicillin."""
import numpy as np
from matplotlib.patches import Circle, RegularPolygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 12.5)
ax.set_ylim(1.8, 12.5)


def sugar(c, tok, text, r=0.42):
    ax.add_patch(RegularPolygon(c, 6, radius=r, orientation=0, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1,
                                zorder=6))
    bio.label(ax, c, text, size="tiny", color=P.on_fill(), zorder=8)


def aa(c, text, tok="peptide", r=0.27):
    ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=6))
    bio.label(ax, c, text, size=5.6, color=P.on_fill(), zorder=8)


def strand(x0, y, n, step=1.0):
    """A glycan strand NAG-NAM-...; returns x positions of the NAM residues."""
    ax.plot([x0 - 0.5, x0 + step * (2 * n - 1) + 0.5], [y, y], color=P.edge("carbohydrate"), lw=1.4, zorder=4)
    nams = []
    for k in range(2 * n):
        x = x0 + step * k
        if k % 2 == 0:
            sugar((x, y), "nag", "G", r=0.36)
        else:
            sugar((x, y), "receptor", "M", r=0.36)
            nams.append(x)
    return nams


# ---- A: repeating unit
bio.panel(ax, "A", (0.2, 12.3))
bio.label(ax, (4.3, 12.0), "Glycan tetrapeptide", size="normal", bold=True)
ax.plot([0.8, 7.6], [10.3, 10.3], color=P.edge("carbohydrate"), lw=1.6, zorder=4)
sugar((2.6, 10.3), "nag", "NAG")
sugar((4.6, 10.3), "receptor", "NAM")
bio.label(ax, (3.6, 9.8), "β(1→4)", size="tiny")
ax.annotate("", xy=(3.6, 10.45), xytext=(3.6, 11.4), arrowprops=dict(arrowstyle="-|>", color=P.edge("negative"), lw=1.0))
bio.label(ax, (3.6, 11.6), "lysozyme cuts here", size="tiny", color=P.edge("negative"))
names = ["L-Ala", "D-Glu", "DAP or\nL-Lys", "D-Ala"]
ys = [9.2, 8.3, 7.4, 6.5]
ax.plot([4.6, 4.6], [9.9, 6.5], color=P.edge("peptide"), lw=1.2, zorder=4)
for y, nm in zip(ys, names):
    aa((4.6, y), "")
    bio.label(ax, (5.05, y), nm, size="tiny", ha="left")
aa((4.6, 5.6), "", tok="neutral")
bio.label(ax, (5.05, 5.6), "D-Ala (removed\nin cross-linking)", size="tiny", ha="left", color=P.muted())
ax.plot([4.6, 4.6], [6.25, 5.85], color=P.muted(), lw=1.0, ls=":", zorder=4)
bio.label(ax, (1.8, 8.6), "G = N-acetylglucosamine\nM = N-acetylmuramic acid", size="tiny", ha="center",
          color=P.muted())

# ---- B: E. coli direct cross-link
bio.panel(ax, "B", (9.0, 12.3))
bio.label(ax, (13.9, 12.0), r"Direct cross-link ($\it{E.\ coli}$)", size="normal", bold=True)
top = strand(10.2, 10.6, 4)
bot = strand(10.2, 5.2, 4)
for k, (xt, xb) in enumerate(zip(top, bot)):
    # peptides down from top strand and up from bottom strand
    for j in range(4):
        aa((xt, 10.0 - 0.55 * j), "", r=0.2)
    for j in range(3):
        aa((xb, 5.8 + 0.55 * j), "", r=0.2)
    aa((xb + 0.5, 6.9 + 0.3), "", r=0.2)          # D-Ala 4 of the acceptor peptide, to the side
    ax.plot([xb, xb + 0.5], [6.9, 7.2], color=P.edge("peptide"), lw=1.0, zorder=4)
    ax.plot([xt, xt], [10.3, 8.35], color=P.edge("peptide"), lw=1.0, zorder=4)
    ax.plot([xb, xb], [5.5, 6.9], color=P.edge("peptide"), lw=1.0, zorder=4)
    if k in (0, 2):
        # D-Ala 4 of the donor (top) peptide to DAP 3 of the acceptor (bottom) peptide
        ax.plot([xt, xb], [8.35, 6.9], color=P.edge("highlight"), lw=2.4, zorder=5)
ax.text(15.8, 7.9, "DAP–D-Ala\npeptide bond", fontsize=6.8, color=P.edge("highlight"), ha="left", va="center")
bio.label(ax, (14.0, 4.2), "penicillin blocks the transpeptidase\nthat forms each cross-link", size="tiny",
          color=P.edge("negative"))

# ---- C: S. aureus pentaglycine bridge
bio.panel(ax, "C", (18.6, 12.3))
bio.label(ax, (23.3, 12.0), r"Pentaglycine interbridge ($\it{S.\ aureus}$)", size="normal", bold=True)
top = strand(19.6, 10.6, 4)
bot = strand(19.6, 5.2, 4)
for k, (xt, xb) in enumerate(zip(top, bot)):
    for j in range(4):
        aa((xt, 10.0 - 0.45 * j), "", r=0.18)
        aa((xb, 5.8 + 0.45 * j), "", r=0.18)
    ax.plot([xt, xt], [10.3, 8.65], color=P.edge("peptide"), lw=1.0, zorder=4)
    ax.plot([xb, xb], [5.5, 7.15], color=P.edge("peptide"), lw=1.0, zorder=4)
    if k < 3:
        # bridge from L-Lys (3rd residue of bottom peptide k) to D-Ala of top peptide k+1
        a = np.array([xb, 5.8 + 0.45 * 2])
        b = np.array([top[k + 1], 10.0 - 0.45 * 3])
        pts = [a + (b - a) * t for t in np.linspace(0.18, 0.82, 5)]
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("enzyme"), lw=1.0, zorder=4)
        for p in pts:
            aa(tuple(p), "", tok="enzyme", r=0.14)
ax.text(26.8, 7.9, "Gly5", fontsize=6.8, color=P.edge("enzyme"), ha="left", va="center")
for x, txt in ((10.0, ""),):
    pass
# shared legend
yl = 2.6
items = [("nag", "NAG"), ("receptor", "NAM"), ("peptide", "amino acid of the stem peptide"), ("highlight", "direct cross-link"),
         ("enzyme", "glycine of the interbridge")]
x = 1.0
for tok, txt in items:
    if tok == "highlight":
        ax.plot([x - 0.25, x + 0.2], [yl, yl], color=P.edge(tok), lw=2.4)
    else:
        ax.add_patch(Circle((x, yl), 0.2, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9))
    bio.label(ax, (x + 0.35, yl), txt, size="tiny", ha="left")
    x += 1.2 + 0.13 * len(txt)
