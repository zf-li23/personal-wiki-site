"""mTORC1 as a coincidence detector on the lysosome (SBGN activity flow).

Growth factors and insulin act through PI3K and PKB, which inhibit the TSC complex, the GTPase-activating
protein of Rheb; energy stress (through AMPK) and hypoxia (through REDD1) activate TSC. Amino acids,
sensed in the cytosol and in the lysosome, inhibit GATOR1, the GTPase-activating protein of the Rag
GTPases. The Rags recruit mTORC1 to the lysosomal surface, and Rheb-GTP on the same membrane activates
it: only when both arms are on (AND) is the kinase active. mTORC1 promotes protein, lipid and
nucleotide synthesis and inhibits autophagy (ULK1) and lysosome biogenesis (TFEB); S6K feeds back
negatively on IRS1 (dashed), and AMPK also inhibits mTORC1 directly by phosphorylating raptor.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(20.0, 10.4)
d = network.Diagram(ax)
d.compartment("lys", (8.0, 2.7, 17.6, 6.6), "Lysosome surface", token="lysosome")

d.activity("gf", (2.6, 9.4), "growth factors, insulin", token="drug")
d.activity("en", (6.6, 9.4), "energy stress (AMP ↑)", token="atp")
d.activity("hyp", (10.6, 9.4), "hypoxia", token="neutral")
d.activity("aa", (15.4, 9.4), "amino acids", token="metabolite")

d.activity("pkb", (2.6, 7.6), "PI3K → PKB", token="enzyme")
d.activity("ampk", (6.6, 7.6), "AMPK", token="atp")
d.activity("redd", (10.6, 7.6), "REDD1", token="neutral")
d.activity("gator", (15.4, 7.6), "GATOR1 (Rag GAP)", token="negative")
d.activity("tsc", (6.6, 5.6), "TSC (Rheb GAP)", token="negative")

d.activity("rheb", (10.2, 5.4), "Rheb·GTP", token="receptor")
d.activity("rag", (15.4, 5.4), "Rag GTPases", token="receptor")
d.logic("and", (12.8, 4.6), "AND", angle=-90)
d.activity("mtor", (12.8, 3.4), "mTORC1", token="protein")

d.phenotype("prot", (2.6, 1.0), "protein synthesis (S6K, 4E-BP)", token="positive")
d.phenotype("lip", (7.8, 1.0), "lipid, nucleotide synthesis", token="positive")
d.phenotype("aut", (12.8, 1.0), "autophagy (ULK1)", token="negative")
d.phenotype("tfeb", (17.3, 1.0), "lysosome biogenesis (TFEB)", token="negative")

d.connect("gf", "pkb", "positive")
d.connect("en", "ampk", "positive")
d.connect("hyp", "redd", "positive")
d.connect("pkb", "tsc", "negative")
d.connect("ampk", "tsc", "positive")
d.connect("redd", "tsc", "positive")
d.connect("aa", "gator", "negative")
d.connect("tsc", "rheb", "negative")
d.connect("gator", "rag", "negative")
d.connect("rheb", "and", "logic", via=[(12.8, 5.4)])
d.connect("rag", "and", "logic", via=[(12.8, 5.4)])
d.connect("and", "mtor", "positive")
d.connect("ampk", "mtor", "negative", via=[(8.6, 7.0), (8.6, 4.0), (12.0, 4.0)])
d.connect("mtor", "prot", "positive", via=[(12.2, 2.6), (2.6, 2.6)])
d.connect("mtor", "lip", "positive", via=[(12.2, 2.6), (7.8, 2.6)])
d.connect("mtor", "aut", "negative")
d.connect("mtor", "tfeb", "negative", via=[(17.3, 3.4)])
d.connect("mtor", "pkb", "negative", dashed=True, via=[(13.4, 2.1), (1.2, 2.1), (1.2, 7.6)])
bio.label(ax, (0.9, 4.8), "S6K ⊣ IRS1", size="tiny", color=P.muted(), rotation=90)
