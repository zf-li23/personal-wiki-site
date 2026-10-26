"""The six biosynthetic families of the 20 amino acids, by carbon precursor (memory chart).

Precursors come from glycolysis (3-phosphoglycerate, phosphoenolpyruvate, pyruvate), the pentose phosphate
pathway (ribose 5-phosphate, erythrose 4-phosphate) and the citric acid cycle (oxaloacetate,
alpha-ketoglutarate). Each chip is one amino acid, coloured by its nutritional status in humans:
essential (must be eaten), conditionally essential (needed in the diet in growth, illness or when its
precursor is short) and nonessential. Isoleucine takes carbons from both pyruvate and threonine (oxaloacetate
family); tyrosine is made in animals by hydroxylation of phenylalanine, and cysteine from the sulfur of
methionine and the carbon of serine.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 14.2, scale=0.42)
STATUS = {"His": "e", "Ile": "e", "Leu": "e", "Lys": "e", "Met": "e", "Phe": "e", "Thr": "e", "Trp": "e", "Val": "e",
          "Arg": "c", "Cys": "c", "Gln": "c", "Gly": "c", "Pro": "c", "Tyr": "c",
          "Ala": "n", "Asp": "n", "Asn": "n", "Glu": "n", "Ser": "n"}
TOK = {"e": "negative", "c": "highlight", "n": "positive"}
rows = [  # precursor, source, route, amino acids
    ("Ribose 5-phosphate", "pentose phosphate", "PRPP + ATP (purine N-1, C-2), Gln", ["His"]),
    ("Erythrose 4-P + 2 PEP", "pentose phosphate,\nglycolysis", "shikimate → chorismate", ["Phe", "Tyr", "Trp"]),
    ("3-Phosphoglycerate", "glycolysis", "3-P-hydroxypyruvate → 3-P-serine", ["Ser", "Gly", "Cys"]),
    ("Pyruvate", "glycolysis", "transamination; hydroxyethyl-TPP", ["Ala", "Val", "Leu", "Ile"]),
    ("Oxaloacetate", "citric acid cycle", "transamination; aspartate β-semialdehyde", ["Asp", "Asn", "Met", "Thr", "Lys"]),
    ("α-Ketoglutarate", "citric acid cycle", "glutamate (GDH or GS–GOGAT)", ["Glu", "Gln", "Pro", "Arg"]),
]
y0, dy = 13.2, 2.2
for k, (pre, src, route, aas) in enumerate(rows):
    y = y0 - k * dy
    bio.label(ax, (2.0, y), src, size="tiny", color=P.muted())
    bio.box(ax, (6.6, y), 4.8, 1.0, "carbohydrate" if k < 4 else "metabolite", text=pre, size="small")
    bio.arrow(ax, (9.1, y), (11.0, y), kind="process", head=0.2)
    bio.label(ax, (13.6, y + 0.0), route, size="tiny", color=P.muted())
    bio.arrow(ax, (16.3, y), (17.1, y), kind="process", head=0.18, color=P.muted())
    for j, aa in enumerate(aas):
        st = STATUS[aa]
        bio.box(ax, (18.0 + 1.75 * j, y), 1.5, 0.9, TOK[st], text=aa, size="small")
bio.label(ax, (19.7, y0 - 3 * dy - 0.85), "Ile: 4 C from pyruvate, 2 from Thr", size="tiny", color=P.muted())
bio.label(ax, (19.7, y0 - 2 * dy - 0.85), "Cys: S from Met in animals", size="tiny", color=P.muted())
bio.label(ax, (19.7, y0 - 1 * dy - 0.85), "Tyr: from Phe in animals", size="tiny", color=P.muted())
for j, (st, t) in enumerate((("e", "essential"), ("c", "conditionally essential"), ("n", "nonessential"))):
    x = 3.0 + 6.5 * j
    bio.box(ax, (x, 0.55), 0.9, 0.6, TOK[st])
    bio.label(ax, (x + 0.7, 0.55), t, size="small", ha="left")
