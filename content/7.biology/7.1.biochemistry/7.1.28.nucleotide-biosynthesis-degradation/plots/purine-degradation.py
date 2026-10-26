"""Catabolism of purine nucleotides. AMP is dephosphorylated to adenosine (5'-nucleotidase) and deaminated to
inosine (adenosine deaminase, ADA), or deaminated first to IMP (AMP deaminase, muscle) and then
dephosphorylated. Purine nucleoside phosphorylase (PNP) cleaves inosine and guanosine by phosphorolysis to the
free bases and ribose 1-phosphate. Guanine is deaminated to xanthine (guanine deaminase). Xanthine
oxidoreductase oxidizes hypoxanthine to xanthine and xanthine to uric acid (inhibited by allopurinol, through
oxypurinol, and by febuxostat). Uric acid is excreted by primates, birds, reptiles and insects; other animals
degrade it further (urate oxidase, allantoinase, allantoicase, urease), the extent of degradation shown on the
right. Dashed arrows: salvage of hypoxanthine and guanine by HGPRT with PRPP."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(27.0, 12.4)
neg = P.edge("negative")

pw = M.Pathway(ax, size="small")
Y1, Y2 = 8.6, 4.6
pw.node("amp", (1.8, Y1), "AMP", bold=True, token="highlight")
pw.node("ado", (6.2, Y1), "Adenosine")
pw.node("ino", (10.6, Y1), "Inosine")
pw.node("hx", (15.0, Y1), "Hypoxanthine")
pw.node("imp", (6.2, 11.4), "IMP", token="highlight")
pw.node("gmp", (1.8, Y2), "GMP", bold=True, token="highlight")
pw.node("guo", (6.2, Y2), "Guanosine")
pw.node("gua", (10.6, Y2), "Guanine")
pw.node("xan", (19.2, Y1), "Xanthine")
pw.node("ua", (23.4, Y1), "Uric acid", bold=True, token="highlight")
pw.step("amp", "ado", enzyme="5′-nucleotidase", side=("H₂O", "Pᵢ"))
pw.step("ado", "ino", enzyme="adenosine deaminase", side=("H₂O", "NH₄⁺"))
pw.step("ino", "hx", enzyme="PNP", side=("Pᵢ", "ribose 1-P"))
pw.step("amp", "imp", enzyme="AMP deaminase", side=(None, "NH₄⁺"), flip=True)
pw.step("imp", "ino", enzyme="5′-nucleotidase", side=(None, "Pᵢ"))
pw.step("gmp", "guo", enzyme="5′-nucleotidase", side=("H₂O", "Pᵢ"))
pw.step("guo", "gua", enzyme="PNP", side=("Pᵢ", "ribose 1-P"))
mg, _, _ = pw.step("gua", "xan", enzyme="guanine deaminase", side=("H₂O", "NH₄⁺"), enzyme_flip=True)
m1, _, _ = pw.step("hx", "xan", enzyme="xanthine\noxidase", side=("O₂ + H₂O", "H₂O₂"))
m2, _, _ = pw.step("xan", "ua", enzyme="xanthine\noxidase", side=("O₂ + H₂O", "H₂O₂"))

# allopurinol
bio.box(ax, (21.3, 11.4), 5.2, 0.7, token="drug", text="allopurinol (→ oxypurinol), febuxostat", size="tiny")
for m in (m1, m2):
    bio.arrow(ax, (21.3, 11.05), (m[0], m[1] + 0.85), kind="inhibition", color=neg, lw=1.5)

# salvage
bio.arrow(ax, pw.anchor("hx", "t"), pw.anchor("imp", "r"), kind="process", color=P.edge("positive"), dashed=True,
          bend=-0.3, shrink=0.05)
bio.label(ax, (12.6, 11.75), "HGPRT (PRPP → PPᵢ)", size="tiny", color=P.edge("positive"), bold=True)
bio.arrow(ax, pw.anchor("gua", "b"), pw.anchor("gmp", "b"), kind="process", color=P.edge("positive"), dashed=True,
          bend=0.35, shrink=0.05)
bio.label(ax, (6.2, 2.15), "HGPRT (PRPP → PPᵢ)", size="tiny", color=P.edge("positive"), bold=True)

# further degradation of uric acid
X = 23.4
ys = [Y1, 6.9, 5.2, 3.5, 1.8]
names = [("ua", None), ("aln", "Allantoin"), ("alt", "Allantoate"), ("urea", "Urea + glyoxylate"), ("nh4", "NH₄⁺ + CO₂")]
for (k, t), y in zip(names[1:], ys[1:]):
    pw.node(k, (X, y), t)
for (a, _), (b, _), e in zip(names, names[1:], ["urate oxidase", "allantoinase", "allantoicase", "urease"]):
    pw.step(a, b, enzyme=e, enzyme_size="tiny")
groups = ["primates, birds,\nreptiles, insects", "most other mammals", "bony fishes",
          "amphibians, cartilaginous\nfishes", "marine invertebrates"]
for g, y in zip(groups, ys):
    bio.label(ax, (X + 1.7, y - 0.45 if y == Y1 else y), g, size="tiny", color=P.muted(), ha="left")
bio.label(ax, (X + 1.7, 10.1), "excreted by:", size="tiny", color=P.muted(), ha="left", bold=True)
