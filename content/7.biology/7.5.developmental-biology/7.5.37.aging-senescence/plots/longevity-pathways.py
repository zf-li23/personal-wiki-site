"""Conserved nutrient-sensing pathways that set lifespan (activity flow, SBGN AF).

Insulin and IGF-1 activate their receptors (DAF-2 in C. elegans, InR in Drosophila, IGF-1R in mammals), which act
through PI3K (AGE-1 in the worm) and AKT. AKT phosphorylates and inhibits FOXO (DAF-16), the transcription factor
that switches on stress-resistance, DNA-repair, autophagy and metabolic genes; AKT also activates mTORC1, which
together with amino acids drives translation and growth and inhibits autophagy. AMPK, activated by low energy,
inhibits mTORC1; rapamycin inhibits mTORC1. Dietary restriction lowers insulin/IGF-1, amino acids and mTORC1
activity. Reduced signaling through the upper arm or the mTORC1 branch extends lifespan in yeast, worms, flies
and mice; the gene names of the model organizms are given in the table on the right.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(34.0, 15.0)
d = network.Diagram(ax)
d.activity("ins", (3.5, 12.5), "insulin / IGF-1", token="metabolite", w=4.4, h=1.2)
d.activity("rec", (3.5, 9.7), "InR / IGF-1R", token="receptor", w=4.4, h=1.2)
d.activity("pi3k", (3.5, 6.9), "PI3K", token="enzyme", w=3.0, h=1.2)
d.activity("akt", (3.5, 4.1), "AKT", token="enzyme", w=3.0, h=1.2)
d.activity("foxo", (10.5, 4.1), "FOXO", token="protein", w=3.0, h=1.2)
d.activity("mtor", (10.5, 9.7), "mTORC1", token="protein", w=3.4, h=1.2)
d.activity("aa", (10.5, 12.5), "amino acids", token="metabolite", w=3.8, h=1.2)
d.activity("ampk", (16.0, 12.5), "AMPK", token="enzyme", w=3.0, h=1.2)
d.perturbation("rapa", (16.0, 9.7), "rapamycin", w=3.6, h=1.2)
d.perturbation("dr", (16.0, 6.6), "dietary restriction", w=5.0, h=1.2)
d.phenotype("growth", (10.5, 6.9), "translation, growth", token="highlight", w=5.0, h=1.2)
d.phenotype("auto", (16.0, 3.6), "autophagy", token="positive", w=3.8, h=1.2)
d.phenotype("stress", (10.5, 1.3), "stress resistance, repair", token="positive", w=6.0, h=1.2)
d.phenotype("life", (16.0, 1.3), "longevity", token="positive", w=3.6, h=1.2)
d.connect("ins", "rec", kind="positive")
d.connect("rec", "pi3k", kind="positive")
d.connect("pi3k", "akt", kind="positive")
d.connect("akt", "foxo", kind="negative")
d.connect("akt", "mtor", kind="positive", via=[(6.5, 4.6), (6.5, 9.7)])
d.connect("aa", "mtor", kind="positive")
d.connect("ampk", "mtor", kind="negative")
d.connect("rapa", "mtor", kind="negative")
d.connect("mtor", "growth", kind="positive")
d.connect("mtor", "auto", kind="negative", via=[(13.2, 9.0), (13.2, 3.6)])
d.connect("foxo", "stress", kind="positive")
d.connect("stress", "life", kind="positive")
d.connect("auto", "life", kind="positive")
d.connect("dr", "mtor", kind="negative", dashed=True)
d.connect("dr", "ins", kind="negative", dashed=True, via=[(19.2, 6.6), (19.2, 14.2), (3.5, 14.2)])

rows = (("", "worm", "fly", "mouse / human"),
        ("receptor", "daf-2", "InR", "Igf1r, Insr"),
        ("PI3K", "age-1", "Dp110", "Pik3ca"),
        ("substrate", "-", "chico (IRS)", "Irs1"),
        ("FOXO", "daf-16", "dFOXO", "FOXO1, FOXO3"),
        ("mTORC1", "let-363", "Tor", "MTOR"),
        ("S6 kinase", "rsks-1", "S6k", "Rps6kb1 (yeast: Sch9)"))
x0 = 21.5
for i, r in enumerate(rows):
    y = 13.0 - 1.1 * i
    for j, s in enumerate(r):
        bio.label(ax, (x0 + [0, 3.3, 6.0, 8.8][j], y), s, size="tiny", ha="left", bold=(i == 0 or j == 0),
                  italic=(i > 0 and j > 0 and s not in ("-", "")))
bio.label(ax, (x0, 4.8), "Lifespan extension by reduced signaling:", size="tiny", ha="left", bold=True)
for i, s in enumerate((r"worm $\it{daf}$-$\it{2}$ (weak alleles): about 2x", r"fly $\it{chico}$ (homozygous females): about 1.5x",
                       r"mouse $\it{Igf1r}^{+/-}$: females about +30 %", "mouse rapamycin from 20 months: +9-14 %",
                       r"yeast $\it{sch9}$ deletion: chronological lifespan about 3x")):
    bio.label(ax, (x0, 4.0 - 0.75 * i), s, size="tiny", ha="left")
