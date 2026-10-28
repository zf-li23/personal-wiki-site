"""Deciding the mode of inheritance of a trait from crosses: the decision steps of the course in one tree.

Questions are rectangles, conclusions hexagons; each conclusion names the algorithm or formula that
completes the analysis. The bottom row lists the anomalies that point to a special mechanism in any
branch. Human pedigrees follow the same logic with Algorithm 7.2.1.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(27.0, 16.0)
d = network.Diagram(ax)

Q, C = "neutral", "highlight"
d.activity("start", (13.5, 15.0), "Data: reciprocal crosses, F1, F2 or testcross counts, sexes", w=13.0, h=1.0,
           token="dna", size="small")
d.activity("ped", (3.4, 15.0), "humans: pedigree (Algorithm 7.2.1)", w=6.2, h=1.0, token=Q, size="small")
d.activity("q1", (13.5, 12.8), "Do reciprocal crosses give the same F1?", w=9.0, h=1.0, token=Q, size="small")

# left: autosomal nuclear genes
d.activity("q2", (6.5, 10.4), "Count the parts T of the F2 ratio", w=8.0, h=1.0, token=Q, size="small")
d.phenotype("one", (3.2, 7.9), "T = 4: one gene\n3:1, 1:2:1, 2:1 lethal", w=5.8, h=1.7, token=C, size="small")
d.phenotype("two", (9.8, 7.9), "T = 16: two genes, 9:3:3:1\nor merged (Algorithm 4.8.1)", w=6.4, h=1.7,
            token=C, size="small")
d.activity("q3", (6.5, 5.4), "Testcross: parental classes in excess?", w=8.6, h=1.0, token=Q, size="small")
d.phenotype("link", (3.2, 2.9), "linked: r and map\n(Algorithm 8.4.1)", w=5.8, h=1.7, token="positive", size="small")
d.phenotype("unl", (9.8, 2.9), "unlinked: 1:1:1:1\n(χ², Algorithm 8.7.1)", w=6.4, h=1.7, token="positive",
            size="small")

# right: sex linkage and the cytoplasm
d.activity("q4", (20.5, 10.4), "Do sons and daughters differ?", w=7.4, h=1.0, token=Q, size="small")
d.phenotype("xl", (24.6, 7.9), "X-linked: criss-cross\n(Algorithm 6.4.1)", w=4.6, h=1.7, token=C, size="small")
d.activity("q5", (18.0, 7.9), "The phenotype follows …", w=5.6, h=1.0, token=Q, size="small")
d.phenotype("org", (14.1, 4.9), "the mother, always:\norganellar (11.1.1)", w=4.5, h=1.7, token="mitochondrion",
            size="small")
d.phenotype("mat", (19.1, 4.9), "the mother's genotype:\nmaternal effect,\nF3 broods 3:1", w=4.6, h=2.1,
            token="protein", size="small")
d.phenotype("imp", (24.1, 4.9), "the parent of origin:\nimprinting (18.2.1)", w=4.5, h=1.7, token="chromatin",
            size="small")

pos = "positive"
d.connect("start", "q1", pos)
d.connect("start", "ped", pos, dashed=True)
d.connect("q1", "q2", pos, text="same", text_offset=(-0.6, 0.3))
d.connect("q1", "q4", pos, text="different", text_offset=(0.8, 0.3))
d.connect("q2", "one", pos)
d.connect("q2", "two", pos)
d.connect("two", "q3", pos, text="two loci", text_offset=(1.0, 0.0))
d.connect("q3", "link", pos, text="yes", text_offset=(-0.75, 0.15))
d.connect("q3", "unl", pos, text="no", text_offset=(0.4, 0.1))
d.connect("q4", "xl", pos, text="yes", text_offset=(0.5, 0.2))
d.connect("q4", "q5", pos, text="no", text_offset=(-0.5, 0.2))
d.connect("q5", "org", pos)
d.connect("q5", "mat", pos)
d.connect("q5", "imp", pos)

# anomalies valid in any branch
bio.label(ax, (13.5, 1.15), "anomalies in any branch", size="small", color=P.muted())
anomalies = [
    (2.9, "2:1, 6:3:2:1\n→ lethal allele (3.4)"),
    (8.2, "skipped generations\n→ penetrance (3.5)"),
    (13.5, "pseudodominance\n→ deletion (15.2)"),
    (18.8, "semisterility, pseudolinkage\n→ translocation (15.5)"),
    (24.1, "continuous variation\n→ polygenes (24.1)"),
]
for x, t in anomalies:
    bio.box(ax, (x, 0.0), 5.0, 1.3, token="neutral", text=None)
    bio.label(ax, (x, 0.0), t, size="small", color=P.on_fill())
ax.set_ylim(-0.9, 15.7)
