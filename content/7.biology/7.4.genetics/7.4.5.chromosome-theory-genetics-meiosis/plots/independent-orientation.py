"""Independent orientation of two bivalents at metaphase I (Aa on one pair, Bb on another) and the
four kinds of gametes it produces, each with probability 1/4."""
import wikibio as bio
from wikibio import cytogenetics as C

fig, ax = bio.canvas(16.0, 10.6)
pairs = [("dna", "receptor"), ("dna", "receptor")]
alle = [("A", "a"), ("B", "b")]
for k, (flips, title) in enumerate((([False, False], "Orientation 1 (probability 1/2)"),
                                     ([False, True], "Orientation 2 (probability 1/2)"))):
    y = 7.9 - k * 5.0
    bio.panel(ax, "AB"[k], (0.2, y + 2.6))
    bio.label(ax, (3.2, y + 2.2), title, size="small")
    C.metaphase_I(ax, (3.2, y), pairs, flips=flips, alleles=alle)
    for side, gy in ((0, y + 1.0), (1, y - 1.0)):
        xy = (10.0, gy)
        hs = [side if not flips[p] else 1 - side for p in range(2)]
        for rep in range(2):
            c = (xy[0] + rep * 1.9, gy)
            C.round_cell(ax, c, 0.72)
            C.chromosome_set(ax, c, [(pairs[p][hs[p]], False) for p in range(2)], length=0.85, width=0.24, spacing=0.4)
        lab = "".join(alle[p][hs[p]] for p in range(2))
        bio.label(ax, (13.5, gy), lab, size="normal", italic=True, ha="left")
        bio.arrow(ax, (5.4, y + (0.35 if side == 0 else -0.35)), (9.1, gy), kind="process", lw=1.0, head=0.16)
    bio.label(ax, (7.2, y + 1.55), "meiosis I and II", size="tiny", color=bio.P.muted())
bio.label(ax, (8.0, 0.45), "Total over both orientations:  AB : Ab : aB : ab = 1 : 1 : 1 : 1", size="small")
