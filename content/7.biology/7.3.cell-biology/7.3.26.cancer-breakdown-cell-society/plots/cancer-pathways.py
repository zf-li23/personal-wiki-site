"""The core pathways hit in cancer (SBGN activity flow; open arrows activate, bars inhibit).

Products of proto-oncogenes (gain of function in cancer) are drawn in warm colors, products of tumor
suppressor genes (loss of function) in blue; notched boxes are the oncoproteins of human papillomavirus.
Growth-factor receptor tyrosine kinases (EGFR, HER2) activate Ras and the Raf-MEK-ERK cascade, which induces
Myc and cyclin D, and PI3K, which activates Akt and mTORC1 for growth and survival; NF1 (a Ras GAP) and
PTEN (a PIP3 phosphatase) oppose them. Cyclin D-Cdk4/6 phosphorylates and inactivates Rb, releasing E2F
to drive S-phase entry; p16INK4a inhibits Cdk4/6. Oncogenic signaling (excess Myc and E2F) induces ARF,
and DNA damage activates ATM; both stabilize p53 by inhibiting Mdm2. p53 induces p21 (which inhibits
Cdks: arrest) and Puma and Bax (apoptosis). HPV E7 binds Rb and E6 targets p53 for degradation.
"""

from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(23.0, 13.6, scale=0.45)
d = network.Diagram(ax, size="small")
d.compartment("cell", (0.3, 0.3, 22.7, 11.6), "cell", token="cytoplasm", label_pos="br")
ONC, TSG = "highlight", "channel"

d.activity("gf", (2.2, 12.7), "growth factor", token="neutral", w=2.6)
d.activity("rtk", (2.2, 11.6), "RTK (EGFR, HER2)", token=ONC, w=3.2)
d.activity("ras", (2.2, 9.6), "Ras", token=ONC, w=1.6)
d.activity("nf1", (4.6, 8.6), "NF1", token=TSG, w=1.4)
d.activity("raf", (2.2, 7.8), "Raf (BRAF)", token=ONC, w=2.2)
d.activity("erk", (2.2, 6.0), "MEK–ERK", token="enzyme", w=2.2)
d.activity("myc", (2.2, 4.0), "Myc", token=ONC, w=1.6)

d.activity("pi3k", (8.6, 9.6), "PI3K", token=ONC, w=1.6)
d.activity("pten", (11.6, 9.6), "PTEN", token=TSG, w=1.6)
d.activity("akt", (8.6, 7.8), "Akt", token=ONC, w=1.6)
d.activity("mtor", (8.6, 6.0), "mTORC1", token="enzyme", w=1.8)
d.phenotype("growth", (8.6, 4.2), "cell growth", token="positive", w=2.6, h=0.9)

d.activity("cycd", (6.0, 2.4), "cyclin D–Cdk4/6", token=ONC, w=3.0)
d.activity("p16", (6.0, 0.95), "p16INK4a", token=TSG, w=2.2)
d.activity("rb", (10.6, 2.4), "Rb", token=TSG, w=1.4)
d.activity("e2f", (14.0, 2.4), "E2F", token="dna", w=1.4)
d.phenotype("sphase", (18.0, 2.4), "proliferation\n(S-phase entry)", token="positive", w=3.2, h=1.1)

d.activity("dna", (19.6, 9.8), "DNA damage → ATM", token="neutral", w=3.2)
d.activity("arf", (14.6, 7.8), "ARF", token=TSG, w=1.4)
d.activity("mdm2", (17.2, 7.8), "Mdm2", token=ONC, w=1.6)
d.activity("p53", (17.2, 5.8), "p53", token=TSG, w=1.6)
d.activity("p21", (14.6, 4.4), "p21", token=TSG, w=1.4)
d.phenotype("apo", (20.6, 4.4), "apoptosis\n(Puma, Bax)", token="negative", w=2.8, h=1.1)
d.phenotype("surv", (12.6, 6.0), "survival", token="positive", w=2.0, h=0.9)

d.perturbation("e7", (10.6, 0.95), "HPV E7", token="virus", w=1.8)
d.perturbation("e6", (20.6, 6.6), "HPV E6", token="virus", w=1.8)

d.connect("gf", "rtk", "positive")
d.connect("rtk", "ras", "positive")
d.connect("nf1", "ras", "negative")
d.connect("ras", "raf", "positive")
d.connect("raf", "erk", "positive")
d.connect("erk", "myc", "positive")
d.connect("ras", "pi3k", "positive")
d.connect("rtk", "pi3k", "positive", start=(3.8, 11.35), end=(8.2, 10.0))
d.connect("pten", "akt", "negative")
d.connect("pi3k", "akt", "positive")
d.connect("akt", "mtor", "positive")
d.connect("mtor", "growth", "positive")
d.connect("akt", "surv", "positive")
d.connect("erk", "cycd", "positive")
d.connect("myc", "cycd", "positive")
d.connect("p16", "cycd", "negative")
d.connect("cycd", "rb", "negative")
d.connect("rb", "e2f", "negative")
d.connect("e7", "rb", "negative")
d.connect("e2f", "sphase", "positive")
d.connect("myc", "arf", "positive", via=[(2.2, 3.2), (13.4, 3.2), (13.4, 7.8)], start=(2.2, 3.62), end=(13.9, 7.8))
d.connect("e2f", "arf", "positive", start=(14.1, 2.8), end=(14.6, 7.4))
d.connect("arf", "mdm2", "negative")
d.connect("dna", "p53", "positive", start=(19.6, 9.45), end=(17.7, 6.2))
d.connect("mdm2", "p53", "negative", start=(16.9, 7.42), end=(16.9, 6.18))
d.connect("p53", "mdm2", "positive", start=(17.5, 6.18), end=(17.5, 7.42))
d.connect("e6", "p53", "negative")
d.connect("p53", "p21", "positive")
d.connect("p21", "cycd", "negative", via=[(14.6, 3.4), (7.0, 3.4)], start=(14.6, 4.02), end=(7.0, 2.8))
d.connect("p53", "apo", "positive")
d.connect("akt", "apo", "negative", dashed=True, via=[(9.8, 7.0), (19.6, 7.0)], start=(9.4, 7.6), end=(20.0, 4.95))

ax.add_patch(Rectangle((12.0, 12.45), 0.5, 0.4,
             facecolor=P.fill(ONC), edgecolor=P.edge(ONC), lw=0.8))
bio.label(ax, (12.7, 12.65), "proto-oncogene product", size="tiny", ha="left")
ax.add_patch(Rectangle((17.0, 12.45), 0.5, 0.4,
             facecolor=P.fill(TSG), edgecolor=P.edge(TSG), lw=0.8))
bio.label(ax, (17.7, 12.65), "tumor suppressor product", size="tiny", ha="left")
