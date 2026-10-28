# Cytogenetics: normal meiosis, nondisjunction in meiosis I and II, and the independent orientation of bivalents
import wikibio as bio
from wikibio import cytogenetics as C

fig, ax = bio.canvas(31.5, 7.6)
X = [("receptor", "receptor")]
names = [("X", "X")]
for k, (nd, title) in enumerate(((None, "Normal disjunction"), (("I", 0), "Nondisjunction in meiosis I"),
                                 (("II", 0, 0), "Nondisjunction in meiosis II"))):
    x0 = 1.2 + k * 8.0
    bio.panel(ax, "ABC"[k], (x0 - 1.0, 7.4))
    bio.label(ax, (x0 + 2.6, 7.05), title, size="small")
    C.meiosis_lineage(ax, (x0, 3.6), [("dna", "receptor"), ("enzyme", "enzyme")], nondisjunction=nd,
                      names=[("X", "X"), None])
bio.panel(ax, "D", (24.8, 7.4))
C.metaphase_I(ax, (28.0, 4.6), [("dna", "receptor"), ("dna", "receptor")], flips=[False, True],
              alleles=[("A", "a"), ("B", "b")])
C.gamete_table(ax, (26.6, 2.0), ["XX", "O"], ["X", "Y"],
               lambda i, j: [[("XXX", "negative"), ("XXY", "highlight")], [("XO", "highlight"), ("OY", "negative")]][i][j],
               cell=(1.4, 0.6), row_title="Egg", col_title="Sperm")
