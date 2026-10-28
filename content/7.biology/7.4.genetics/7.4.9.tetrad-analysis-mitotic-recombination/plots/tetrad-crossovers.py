# Crossovers between two loci and the unordered tetrad types they produce
import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(25, 17)
loci = [(0.3, ("A", "a")), (0.85, ("B", "b"))]
tok = {"AB": "dna", "ab": "receptor", "Ab": "enzyme", "aB": "antibody"}


def kind(g):
    s = sorted("".join(x) for x in g)
    if set(s) <= {"AB", "ab"}:
        return "PD"
    if set(s) <= {"Ab", "aB"}:
        return "NPD"
    return "T"


cases = [("No crossover", []), ("One crossover", [(0.55, 1, 2)]),
         ("Two-strand double", [(0.48, 1, 2), (0.66, 1, 2)]), ("Three-strand double", [(0.48, 1, 2), (0.66, 0, 2)]),
         ("Three-strand double", [(0.48, 1, 2), (0.66, 1, 3)]), ("Four-strand double", [(0.48, 1, 2), (0.66, 0, 3)])]
for k, (name, co) in enumerate(cases):
    col, row = k % 2, k // 2
    x0 = 0.9 + col * 12.4
    y = 14.0 - row * 5.2
    pr = T.four_chromatids(ax, x0, x0 + 5.2, y, crossovers=co, loci=loci)
    bio.label(ax, (x0 + 2.6, y + 1.45), name, size="small", bold=True)
    bio.arrow(ax, (x0 + 5.7, y), (x0 + 6.7, y))
    g = ["".join(x) for x in pr["genotypes"]]
    T.tetrad(ax, (x0 + 8.3, y), g, tokens=[tok[s] for s in g], r=0.42, spread=0.52, size="small")
    bio.label(ax, (x0 + 10.4, y), kind(pr["genotypes"]), size="normal", bold=True, ha="left")
