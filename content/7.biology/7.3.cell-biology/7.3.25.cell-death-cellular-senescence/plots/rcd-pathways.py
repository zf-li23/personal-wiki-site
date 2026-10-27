"""Three forms of regulated necrosis (SBGN activity flow; open arrows activate, bars inhibit; notched boxes
are drugs).

(A) Necroptosis: TNF bound to TNFR1 activates RIPK1; when caspase-8 is active it cleaves RIPK1 and RIPK3
and the cell survives or dies by apoptosis (only the cleavage of RIPK1 is drawn), but when caspase-8 is inhibited (viral inhibitors, zVAD) RIPK1
and RIPK3 assemble through their RHIM motifs into an amyloid-like necrosome, RIPK3 phosphorylates MLKL,
and MLKL oligomers permeabilize the plasma membrane. Necrostatin-1 inhibits RIPK1.
(B) Pyroptosis: microbial products and danger signals assemble an inflammasome (for example NLRP3 with ASC)
that activates caspase-1; cytosolic LPS activates caspase-11 (caspase-4 and -5 in humans) directly. The
caspases cleave gasdermin D, whose N-terminal fragment forms membrane pores, and caspase-1 matures IL-1β
and IL-18, released through the pores.
(C) Ferroptosis: iron-dependent peroxidation of phospholipids containing polyunsaturated fatty acids
(incorporated by ACSL4). GPX4, using glutathione made from cystine imported by system xc⁻ (SLC7A11),
reduces the lipid hydroperoxides; FSP1 with ubiquinol traps lipid radicals. Erastin blocks system xc⁻,
RSL3 inhibits GPX4, ferrostatin-1 and liproxstatin-1 trap radicals.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(30.0, 10.6, scale=0.45)
d = network.Diagram(ax, size="small")

# ---------------------------------------------------------------- A necroptosis
d.compartment("A", (0.3, 0.3, 9.6, 9.6), "necroptosis", token="cytoplasm")
d.activity("tnf", (2.6, 8.4), "TNF–TNFR1", token="receptor", w=2.4)
d.activity("r1", (2.6, 6.4), "RIPK1", token="enzyme", w=1.8)
d.activity("c8", (6.8, 8.4), "caspase-8", token="enzyme", w=2.0)
d.activity("r3", (2.6, 4.4), "RIPK3\n(necrosome)", token="enzyme", w=2.2, h=1.1)
d.activity("mlkl", (2.6, 2.4), "MLKL-P", token="negative", w=2.0)
d.phenotype("lysisA", (6.6, 1.3), "membrane\nrupture", token="negative", w=2.8, h=1.1)
d.phenotype("apoA", (7.6, 4.6), "apoptosis", token="highlight", w=2.4, h=0.9)
d.perturbation("nec1", (5.6, 6.4), "necrostatin-1", w=2.4)
d.connect("tnf", "r1", "positive")
d.connect("tnf", "c8", "positive")
d.connect("c8", "r1", "negative")
d.connect("c8", "apoA", "positive")
d.connect("nec1", "r1", "negative")
d.connect("r1", "r3", "positive")
d.connect("r3", "mlkl", "positive")
d.connect("mlkl", "lysisA", "positive")

# ---------------------------------------------------------------- B pyroptosis
d.compartment("B", (10.2, 0.3, 19.6, 9.6), "pyroptosis", token="cytoplasm")
d.activity("pamp", (12.6, 8.4), "PAMPs, DAMPs", token="neutral", w=2.6)
d.activity("lps", (17.4, 8.4), "cytosolic LPS", token="neutral", w=2.4)
d.activity("infl", (12.6, 6.4), "inflammasome\n(NLRP3, ASC)", token="protein", w=2.6, h=1.1)
d.activity("c1", (12.6, 4.4), "caspase-1", token="enzyme", w=2.0)
d.activity("c11", (17.4, 6.4), "caspase-11\n(-4, -5)", token="enzyme", w=2.2, h=1.1)
d.activity("gsdmd", (16.6, 3.4), "gasdermin D\nN-terminal pores", token="negative", w=2.8, h=1.1)
d.activity("il1", (12.6, 2.4), "IL-1β, IL-18", token="drug", w=2.2)
d.phenotype("lysisB", (16.6, 1.3), "lysis,\ninflammation", token="negative", w=2.8, h=1.0)
d.connect("pamp", "infl", "positive")
d.connect("infl", "c1", "positive")
d.connect("lps", "c11", "positive")
d.connect("c1", "gsdmd", "positive")
d.connect("c11", "gsdmd", "positive")
d.connect("c1", "il1", "positive")
d.connect("gsdmd", "lysisB", "positive")
d.connect("il1", "lysisB", "positive", dashed=True, via=[(12.6, 1.3)], start=(12.6, 1.95), text="released\nthrough pores",
          text_offset=(0.6, 0.45))

# ---------------------------------------------------------------- C ferroptosis
d.compartment("C", (20.1, 0.3, 29.7, 9.6), "ferroptosis", token="cytoplasm")
d.activity("xc", (22.4, 8.4), "system xc⁻\n(SLC7A11)", token="channel", w=2.4, h=1.1)
d.activity("gsh", (22.4, 6.4), "glutathione", token="metabolite", w=2.2)
d.activity("gpx4", (22.4, 4.4), "GPX4", token="positive", w=1.6)
d.activity("acsl4", (27.4, 8.4), "ACSL4: PUFA\nphospholipids", token="lipid", w=2.6, h=1.1)
d.activity("fe", (28.5, 6.0), "Fe²⁺, ROS", token="highlight", w=1.9)
d.activity("lox", (26.4, 3.6), "lipid\nperoxides", token="negative", w=2.2, h=1.1)
d.activity("fsp1", (22.4, 2.4), "FSP1–CoQH₂", token="positive", w=2.4)
d.phenotype("lysisC", (26.4, 1.3), "ferroptotic\ndeath", token="negative", w=2.8, h=1.0)
d.perturbation("era", (25.4, 8.9), "erastin", w=1.6)
d.perturbation("rsl3", (25.0, 5.5), "RSL3", w=1.3)
d.connect("xc", "gsh", "positive")
d.connect("gsh", "gpx4", "positive")
d.connect("gpx4", "lox", "negative")
d.connect("fsp1", "lox", "negative")
d.connect("acsl4", "lox", "positive", start=(27.0, 7.85), end=(26.2, 4.15))
d.connect("fe", "lox", "positive")
d.connect("lox", "lysisC", "positive")
d.connect("era", "xc", "negative")
d.connect("rsl3", "gpx4", "negative")
