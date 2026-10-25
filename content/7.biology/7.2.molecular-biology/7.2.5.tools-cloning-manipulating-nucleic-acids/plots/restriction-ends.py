# Cleavage geometry of type II restriction enzymes. Each row shows a recognition site (boxed) in its duplex
# (top strand 5'->3'), the staggered cut through both strands (red line), and the two products. EcoRI
# (G^AATTC) leaves 4-nt 5' overhangs, PstI (CTGCA^G) 4-nt 3' overhangs and SmaI (CCC^GGG) blunt ends; all
# products carry a 5'-phosphate and a 3'-OH. The type IIS enzyme BsaI recognizes the asymmetric site GGTCTC
# and cuts 1 nt (top) and 5 nt (bottom) beyond it, so the 4-nt overhang (coloured letters) can be any sequence
# and the recognition site stays on the discarded fragment.
import wikibio as bio
from wikibio.sequence import MONO

P = bio.P
COMP = {"A": "T", "T": "A", "G": "C", "C": "G"}
DX = 0.36
fig, ax = bio.canvas(20.0, 12.4)

rows = [
    ("EcoRI", "G^AATTC", "TCA", "GAATTC", "TGA", 1, 5, "5′ overhang (AATT)"),
    ("PstI", "CTGCA^G", "ACT", "CTGCAG", "TCA", 5, 1, "3′ overhang (TGCA)"),
    ("SmaI", "CCC^GGG", "TAC", "CCCGGG", "ATG", 3, 3, "blunt ends"),
    ("BsaI (type IIS)", "GGTCTC(1/5)", "TA", "GGTCTC", "AGCTTACG", 7, 11, "overhang of any sequence (GCTT)"),
]


def letters(x0, y, seq, colours=None, start=0):
    for k, ch in enumerate(seq):
        col = colours[k + start] if colours else P.ink()
        ax.text(x0 + (k + start) * DX, y, ch, ha="center", va="center", fontsize=8.6, family=MONO, color=col,
                weight="bold" if colours and col != P.ink() else "normal", zorder=12)


for r, (name, site_txt, fl, site, fr, ct, cb, what) in enumerate(rows):
    y = 10.6 - r * 2.9
    top = fl + site + fr
    bot = "".join(COMP[c] for c in top)
    i, j = len(fl) + ct, len(fl) + cb  # cut positions on top and bottom strand (top coordinates)
    lo, hi = min(i, j), max(i, j)
    over = [P.NUCLEOTIDE[c] if lo <= k < hi else P.ink() for k, c in enumerate(top)]
    overb = [P.NUCLEOTIDE[c] if lo <= k < hi else P.ink() for k, c in enumerate(bot)]
    bio.label(ax, (0.3, y + 0.75), name, size="normal", bold=True, ha="left")
    bio.label(ax, (0.3, y + 0.25), site_txt, size="small", ha="left", color=P.muted())
    # duplex
    x0 = 4.0
    yt, yb = y + 0.28, y - 0.28
    letters(x0, yt, top)
    letters(x0, yb, bot)
    bio.label(ax, (x0 - 0.45, yt), "5′", size="tiny")
    bio.label(ax, (x0 - 0.45, yb), "3′", size="tiny")
    bio.label(ax, (x0 + len(top) * DX - 0.05, yt), "3′", size="tiny")
    bio.label(ax, (x0 + len(top) * DX - 0.05, yb), "5′", size="tiny")
    s0 = x0 + len(fl) * DX - DX / 2
    ax.add_patch(bio.core.FancyBboxPatch((s0, yb - 0.24), len(site) * DX, 1.04, boxstyle="round,pad=0,rounding_size=0.08",
                                         fill=False, edgecolor=P.edge("highlight"), lw=1.1, zorder=8))
    xi, xj = x0 + i * DX - DX / 2, x0 + j * DX - DX / 2
    ax.plot([xi, xi, xj, xj], [yt + 0.3, y, y, yb - 0.3], color=P.edge("negative"), lw=1.5, zorder=13)
    # products
    bio.arrow(ax, (x0 + len(top) * DX + 0.3, y), (x0 + len(top) * DX + 1.3, y), kind="process")
    p0 = x0 + len(top) * DX + 1.9
    letters(p0, yt, top[:i], over)
    letters(p0, yb, bot[:j], overb)
    gap = 1.3
    q0 = p0 + gap
    for k in range(i, len(top)):
        ax.text(q0 + k * DX, yt, top[k], ha="center", va="center", fontsize=8.6, family=MONO, color=over[k],
                weight="bold" if over[k] != P.ink() else "normal")
    for k in range(j, len(bot)):
        ax.text(q0 + k * DX, yb, bot[k], ha="center", va="center", fontsize=8.6, family=MONO, color=overb[k],
                weight="bold" if overb[k] != P.ink() else "normal")
    # 5' phosphate / 3' OH marks at the new ends
    bio.label(ax, (p0 + i * DX - 0.1, yt + 0.38), "OH", size="tiny", color=P.muted())
    bio.label(ax, (q0 + i * DX - 0.25, yt + 0.38), "P", size="tiny", color=P.muted())
    bio.label(ax, (q0 + len(top) * DX + 0.2, y), what, size="small", ha="left")
