# One and two crossovers at the four-chromatid stage and the chromatids they produce
import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(26, 15.5)
loci = [(0.25, ("A", "a")), (0.85, ("B", "b"))]
lf = [0.25, 0.85]


def tags(g):
    return ["P" if (x[0], x[1]) in (("A", "B"), ("a", "b")) else "R" for x in g]


bio.panel(ax, "A", (0.2, 15.3))
bio.label(ax, (3.6, 14.7), "Single crossover", size="normal", bold=True)
pr = T.four_chromatids(ax, 1.0, 6.2, 12.6, crossovers=[(0.55, 1, 2)], loci=loci, numbers=True)
bio.arrow(ax, (6.7, 12.6), (7.7, 12.6))
T.chromatid_set(ax, 8.1, 13.3, 12.6, pr, loci_f=lf, tags=tags(pr["genotypes"]))
bio.label(ax, (17.0, 12.6), "2 of 4 chromatids\nrecombinant", size="small", ha="left")

bio.panel(ax, "B", (0.2, 9.9))
bio.label(ax, (6.6, 9.4), r"Double crossovers between $\it{A}$ and $\it{B}$ (second exchange at random)", size="normal", bold=True)
kinds = [("Two-strand", [(0.45, 1, 2), (0.65, 1, 2)]), ("Three-strand", [(0.45, 1, 2), (0.65, 0, 2)]),
         ("Three-strand", [(0.45, 1, 2), (0.65, 1, 3)]), ("Four-strand", [(0.45, 1, 2), (0.65, 0, 3)])]
for k, (name, co) in enumerate(kinds):
    col, row = k % 2, k // 2
    x0 = 0.9 + col * 13.0
    y = 7.3 - row * 4.2
    pr = T.four_chromatids(ax, x0, x0 + 4.2, y, crossovers=co, loci=loci, height=0.2, spacing=0.34)
    bio.arrow(ax, (x0 + 4.55, y), (x0 + 5.35, y))
    T.chromatid_set(ax, x0 + 5.7, x0 + 9.9, y, pr, loci_f=lf, tags=tags(pr["genotypes"]), spacing=0.34, height=0.2)
    nrec = tags(pr["genotypes"]).count("R")
    bio.label(ax, (x0 + 2.1, y + 1.25), f"{name}: {nrec} of 4 recombinant", size="small")
