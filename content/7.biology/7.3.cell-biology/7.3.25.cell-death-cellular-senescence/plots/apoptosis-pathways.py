"""The extrinsic and intrinsic pathways of apoptosis (SBGN activity flow; open arrows activate, bars inhibit).

Extrinsic: trimeric death ligands cluster death receptors, which assemble the DISC (FADD and procaspase-8);
FLIP competes with procaspase-8 in the DISC. Active caspase-8 cleaves executioner caspases 3 and 7 directly
(type I cells) and cleaves Bid to tBid, which engages the mitochondrial pathway (type II cells).
Intrinsic: stresses induce or activate BH3-only proteins, which neutralize the anti-apoptotic Bcl-2 proteins
and activate Bax and Bak; survival factors acting through PI3K and PKB inhibit BH3-only proteins (Bad, and
Bim through FOXO). Bax and Bak permeabilize the outer mitochondrial membrane (MOMP) and release cytochrome c,
which assembles the apoptosome (Apaf1 and caspase-9), and Smac and Omi, which neutralize XIAP. Executioner
caspases feed back on the initiator caspases (dashed, partly through caspase-6) and execute apoptosis.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(17.0, 14.0, scale=0.45)
d = network.Diagram(ax, size="small")
d.compartment("cyt", (0.3, 0.3, 16.7, 11.0), "cytosol", token="cytoplasm", label_pos="br")
d.compartment("mito", (7.2, 5.6, 16.2, 9.4), "mitochondrion",
              token="mitochondrion")

d.activity("lig", (2.6, 13.0), "death ligands\n(FasL, TNF, TRAIL)", token="receptor", w=3.2, h=1.1)
d.activity("stress", (9.6, 12.9), "DNA damage (p53), ER stress,\nloss of survival signals", token="neutral", w=4.4, h=1.1)
d.activity("surv", (14.6, 12.9), "survival factors\n(PI3K–PKB)", token="positive", w=3.0, h=1.1)

d.activity("rec", (2.6, 11.0), "death receptor\n(Fas, TNFR1)", token="receptor", w=3.0, h=1.1)
d.activity("disc", (2.6, 8.2), "DISC (FADD,\nprocaspase-8)", token="enzyme", w=3.0, h=1.1)
d.activity("flip", (5.6, 9.0), "FLIP", token="drug", w=1.4)
d.activity("c8", (2.6, 6.2), "caspase-8", token="enzyme", w=2.4)
d.activity("bid", (5.6, 6.2), "tBid", token="drug", w=1.4)

d.activity("bh3", (11.4, 10.2), "BH3-only proteins\n(Bim, Puma, Noxa, Bad)", token="drug", w=3.8, h=1.1)
d.activity("bax", (9.4, 8.2), "Bax, Bak", token="negative", w=2.2)
d.activity("bcl2", (14.2, 8.2), "Bcl-2, Bcl-xL,\nMcl-1", token="positive", w=2.6, h=1.1)
d.activity("cytc", (9.0, 6.5), "cytochrome c", token="mitochondrion", w=2.6)
d.activity("smac", (13.0, 6.5), "Smac, Omi", token="mitochondrion", w=2.2)

d.activity("apo", (9.0, 4.0), "apoptosome\n(Apaf1, caspase-9)", token="enzyme", w=3.2, h=1.1)
d.activity("xiap", (13.0, 4.0), "XIAP", token="drug", w=1.6)
d.activity("c37", (6.0, 2.0), "caspase-3, -7", token="enzyme", w=2.6)
d.phenotype("death", (12.0, 1.6), "apoptosis", token="negative", w=2.8, h=1.0)

d.connect("lig", "rec", "positive")
d.connect("rec", "disc", "positive")
d.connect("flip", "disc", "negative")
d.connect("disc", "c8", "positive")
d.connect("c8", "bid", "positive")
d.connect("bid", "bax", "positive")
d.connect("stress", "bh3", "positive")
d.connect("surv", "bh3", "negative")
d.connect("bh3", "bcl2", "negative")
d.connect("bh3", "bax", "positive")
d.connect("bcl2", "bax", "negative")
d.connect("bax", "cytc", "positive", text="MOMP", text_offset=(0.55, 0.0))
d.connect("bax", "smac", "positive")
d.connect("cytc", "apo", "positive")
d.connect("smac", "xiap", "negative")
d.connect("xiap", "apo", "negative")
d.connect("xiap", "c37", "negative", via=[(13.0, 2.9), (7.6, 2.9)], start=(13.0, 3.55), end=(6.9, 2.45))
d.connect("apo", "c37", "positive")
d.connect("c8", "c37", "positive")
d.connect("c37", "c8", "positive", dashed=True, bend=-0.35, text="feedback", text_offset=(-0.9, 0.0))
d.connect("c37", "death", "positive", via=[(9.0, 1.6)], start=(7.3, 1.75))
bio.label(ax, (2.6, 4.6), "type I cells", size="tiny", color=bio.P.muted())
bio.label(ax, (5.6, 5.3), "type II cells", size="tiny", color=bio.P.muted())
