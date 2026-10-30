"""Three relations between genes and syndromes (activity flow).

A, mosaic pleiotropy: KIT is needed independently by melanoblasts, hematopoietic stem cells and germ cells, so a
loss of function affects all three (in mice with severe Kit alleles: white spotting, anemia, sterility).
B, relational pleiotropy: MITF is needed in the retinal pigment epithelium; its failure leads to a defective
choroid fissure, loss of vitreous fluid and a small eye, so lens and cornea are small although they do not
express MITF. C, genetic heterogeneity: mutations in SHH, in genes needed for its release or response (DISP1, GLI2) or in
cholesterol synthesis (DHCR7, Smith-Lemli-Opitz syndrome; cholesterol is needed for Hedgehog signaling) all reduce Hedgehog signaling in the prechordal
midline and give the same spectrum, holoprosencephaly with cyclopia at its extreme.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(38.0, 11.5)
d = network.Diagram(ax)

bio.panel(ax, "A", (0.2, 11.1))
bio.label(ax, (1.0, 10.8), "Mosaic pleiotropy", size="small", bold=True, ha="left")
d.activity("kit", (5.5, 8.4), "KIT (+ ligand SCF)", token="receptor", w=5.2, h=1.2)
for i, (nid, txt) in enumerate((("mel", "melanoblasts"), ("hsc", "blood stem cells"), ("pgc", "germ cells"))):
    d.activity(nid, (2.0 + 3.6 * i, 5.4), txt, token="protein", w=3.3, h=1.1)
    d.connect("kit", nid, kind="positive")
for i, (nid, txt) in enumerate((("p1", "white spotting"), ("p2", "anemia"), ("p3", "sterility"))):
    d.phenotype(nid, (2.0 + 3.6 * i, 2.4), txt, token="negative", w=3.3, h=1.1)
    d.connect(["mel", "hsc", "pgc"][i], nid, kind="positive", dashed=True)

bio.panel(ax, "B", (12.4, 11.1))
bio.label(ax, (13.2, 10.8), "Relational pleiotropy", size="small", bold=True, ha="left")
d.activity("mitf", (17.5, 9.0), "MITF in pigment epithelium", token="receptor", w=6.4, h=1.1)
d.activity("fis", (17.5, 7.0), "choroid fissure closes", token="protein", w=6.0, h=1.1)
d.activity("vit", (17.5, 5.0), "vitreous fluid retained", token="protein", w=6.0, h=1.1)
d.activity("grow", (17.5, 3.0), "eye enlarges", token="protein", w=4.4, h=1.1)
d.phenotype("lens", (17.5, 1.1), "lens, cornea of normal size", token="positive", w=6.4, h=1.1)
d.connect("mitf", "fis", kind="positive")
d.connect("fis", "vit", kind="positive")
d.connect("vit", "grow", kind="positive")
d.connect("grow", "lens", kind="positive")
bio.label(ax, (21.0, 0.2), "lens and cornea express no MITF", size="tiny", color=P.muted(), ha="left")

bio.panel(ax, "C", (24.4, 11.1))
bio.label(ax, (25.2, 10.8), "Genetic heterogeneity", size="small", bold=True, ha="left")
for i, (nid, txt) in enumerate((("shh", "SHH"), ("ptc", "DISP1, GLI2"), ("dhc", "DHCR7"))):
    d.activity(nid, (26.8 + 3.9 * i, 8.4), txt, token="enzyme", w=3.6, h=1.1)
d.activity("sig", (30.7, 5.6), "Hedgehog signaling in the midline", token="receptor", w=7.4, h=1.1)
for nid in ("shh", "ptc", "dhc"):
    d.connect(nid, "sig", kind="positive")
d.phenotype("hpe", (30.7, 2.6), "holoprosencephaly, cyclopia", token="negative", w=6.8, h=1.1)
d.connect("sig", "hpe", kind="negative")
bio.label(ax, (30.7, 1.2), "loss of any input gives the same phenotype", size="tiny", color=P.muted())
