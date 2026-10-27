"""How a mitogen reaches the cell-cycle control system (SBGN activity flow).

A mitogen activates a receptor tyrosine kinase. Through Ras and the MAP kinase cascade, ERK induces
immediate early genes (Fos, Jun: AP-1; Myc) and these the delayed early gene for cyclin D. Cyclin D-Cdk4/6
begins the phosphorylation of Rb, which releases E2F; E2F induces cyclin E, and cyclin E-Cdk2 completes
Rb phosphorylation, a positive feedback loop that makes entry into S phase switch-like and independent of
the mitogen once passed (the restriction point, 7.3.22). The PI3K-PKB branch supports the same decision:
PKB inhibits GSK3, which would otherwise phosphorylate cyclin D and Myc for degradation; it excludes FOXO
from the nucleus, lowering the Cdk inhibitor p27; and through mTORC1 it drives cell growth. Antimitogenic
signals such as TGF-beta induce Cdk inhibitors (p15, p21, p27).
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(21.0, 11.0)
d = network.Diagram(ax, size="small")
d.compartment("cell", (0.3, 0.3, 20.7, 9.3), "Cytoplasm", token="cytoplasm")
d.compartment("nuc", (0.8, 0.7, 20.3, 5.2), "Nucleus", token="nucleus")

d.activity("mit", (4.0, 10.3), "mitogen → RTK", token="drug")
d.activity("tgf", (17.0, 10.3), "TGF-β, contact", token="neutral")
d.activity("ras", (2.2, 8.3), "Ras", token="receptor")
d.activity("erk", (2.2, 6.8), "Raf → MEK → ERK", token="enzyme")
d.activity("pi3k", (6.0, 8.3), "PI3K → PKB", token="enzyme")
d.activity("mtor", (9.6, 8.3), "mTORC1", token="protein")
d.phenotype("growth", (13.4, 8.3), "cell growth", token="positive")
d.activity("gsk", (6.0, 6.6), "GSK3", token="negative")
d.activity("foxo", (9.6, 6.6), "FOXO", token="negative")

d.activity("ieg", (2.2, 4.0), "Fos, Jun, Myc", token="protein", italic=False)
d.activity("cycd", (7.6, 4.0), "cyclin D–Cdk4/6", token="highlight")
d.activity("rb", (11.0, 4.0), "Rb", token="negative")
d.activity("e2f", (14.0, 4.0), "E2F", token="positive")
d.activity("cyce", (17.4, 4.0), "cyclin E–Cdk2", token="highlight")
d.activity("p27", (13.4, 6.6), "p27, p21, p15", token="negative")
d.phenotype("s", (17.4, 1.8), "S-phase entry", token="positive")

d.connect("mit", "ras", "positive")
d.connect("mit", "pi3k", "positive")
d.connect("ras", "erk", "positive")
d.connect("erk", "ieg", "positive")
d.connect("ieg", "cycd", "positive")
d.connect("pi3k", "mtor", "positive")
d.connect("mtor", "growth", "positive")
d.connect("pi3k", "gsk", "negative")
d.connect("gsk", "cycd", "negative")
d.connect("pi3k", "foxo", "negative")
d.connect("foxo", "p27", "positive")
d.connect("tgf", "p27", "positive")
d.connect("p27", "cycd", "negative")
d.connect("p27", "cyce", "negative")
d.connect("cycd", "rb", "negative")
d.connect("rb", "e2f", "negative")
d.connect("e2f", "cyce", "positive")
d.connect("cyce", "rb", "negative", via=[(17.4, 2.9), (11.0, 2.9)])
d.connect("e2f", "s", "positive", via=[(14.0, 1.8)])
bio.label(ax, (12.4, 2.6), "positive feedback", size="tiny", color=P.muted())
