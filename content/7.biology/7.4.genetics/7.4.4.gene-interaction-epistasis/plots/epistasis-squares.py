"""The six classical epistatic F2 ratios as colored Punnett squares of AaBb x AaBb, each with its pathway model.

Phenotype of each cell from the genotypic class (A_B_, A_bb, aaB_, aabb):
recessive epistasis 9:3:4 (1,2,3,3); complementary 9:7 (1,2,2,2); dominant epistasis 12:3:1 (1,1,2,3);
dominant suppression 13:3 (1,1,2,1); duplicate genes 15:1 (1,1,1,2); cumulative duplicate 9:6:1 (1,2,2,3).
"""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(25.0, 15.0)

cases = [
    ("Recessive epistasis  9 : 3 : 4", (1, 2, 3, 3), ("highlight", "receptor", "neutral"),
     "precursor →(A)→ intermediate →(B)→ product\naa blocks step 1: B/b invisible"),
    ("Complementary genes  9 : 7", (1, 2, 2, 2), ("enzyme", "neutral"),
     "precursor →(A)→ intermediate →(B)→ pigment\nloss of either step: no pigment"),
    ("Dominant epistasis  12 : 3 : 1", (1, 1, 2, 3), ("neutral", "highlight", "positive"),
     "A masks the pathway;\nin aa: B yellow, bb green"),
    ("Dominant suppression  13 : 3", (1, 1, 2, 1), ("neutral", "receptor"),
     "B makes color, A suppresses it:\ncolor only in aaB_"),
    ("Duplicate genes  15 : 1", (1, 1, 1, 2), ("positive", "neutral"),
     "A or B suffices (parallel\npathways): only aabb mutant"),
    ("Cumulative duplicate  9 : 6 : 1", (1, 2, 2, 3), ("dna", "trna", "neutral"),
     "products of A and B add:\ntwo, one or none active"),
]
cell = 0.82
for k, (title, cls, toks, path) in enumerate(cases):
    col, row = k % 3, k // 3
    x0, y0 = 2.6 + col * 8.2, 12.9 - row * 7.2

    def pheno(loci, cls=cls):
        a = any(ch.isupper() for ch in loci[0])
        b = any(ch.isupper() for ch in loci[1])
        idx = {(True, True): 0, (True, False): 1, (False, True): 2, (False, False): 3}[(a, b)]
        return f"class {cls[idx]}"

    colors = {f"class {i + 1}": t for i, t in enumerate(toks)}
    G.punnett(ax, (x0, y0), "AaBb", "AaBb", cell=cell, phenotype=pheno, colors=colors, legend=False,
              text_size=6.0)
    bio.label(ax, (x0 + 2 * cell, y0 + 1.75), title, size="normal", bold=True)
    bio.label(ax, (x0 + 2 * cell, y0 - 4 * cell - 0.75), path, size="small", color=P.muted())
