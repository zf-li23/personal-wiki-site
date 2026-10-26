"""Control of glycolysis and gluconeogenesis in the liver by fructose 2,6-bisphosphate (SBGN process
description). The bifunctional enzyme PFK-2/FBPase-2 is phosphorylated by protein kinase A (cAMP,
glucagon), which inhibits its kinase and activates its bisphosphatase; a phosphoprotein phosphatase
(PP2A, activated by xylulose 5-phosphate; insulin also favours dephosphorylation) reverses this. The
unphosphorylated form makes fructose 2,6-bisphosphate from fructose 6-phosphate, the phosphorylated
form hydrolyses it. Fructose 2,6-bisphosphate stimulates PFK-1 and inhibits FBPase-1; AMP acts the
same way, citrate inhibits PFK-1."""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(23.0, 15.4, scale=0.42)
d = network.Diagram(ax, size="small")
d.compartment("cyt", (0.3, 0.3, 22.7, 15.1), "Hepatocyte cytosol", token="cytoplasm")

# hormones and signals
d.simple_chemical("glucagon", (2.6, 13.8), "glucagon", token="drug", r=0.62)
d.macromolecule("pka", (2.6, 11.4), "PKA", token="enzyme")
d.connect("glucagon", "pka", "stimulation", text="cAMP", text_offset=(0.45, 0))

# the bifunctional enzyme in two states
d.macromolecule("bif", (5.0, 8.6), "PFK-2/FBPase-2", token="antibody", states=[""])
d.unit("bif", "kinase active", pos="b")
d.macromolecule("bifp", (13.2, 8.6), "PFK-2/FBPase-2", token="antibody", states=["P"])
d.unit("bifp", "phosphatase active", pos="b")
d.reaction(["bif"], ["bifp"], at=(9.1, 9.6), angle=0,
           modifiers=[("pka", "catalysis", {"via": [(9.1, 11.4)]})], id="phos")
d.reaction(["bifp"], ["bif"], at=(9.1, 7.6), angle=180, id="dephos")
d.macromolecule("pp", (9.1, 5.4), "PP2A", token="protein")
d.connect("pp", "dephos", "catalysis")
d.simple_chemical("insulin", (2.9, 4.6), "insulin", token="drug", r=0.62)
d.simple_chemical("xu5p", (2.9, 6.4), "Xu5P", token="metabolite", r=0.55)
d.connect("insulin", "pp", "stimulation", dashed=True, text="indirect", text_offset=(0.0, -0.55))
d.connect("xu5p", "pp", "stimulation")

# fructose 2,6-bisphosphate cycle
d.simple_chemical("f6p", (3.2, 2.4), "F6P", r=0.62)
d.simple_chemical("f26", (12.2, 2.4), "F2,6BP", token="highlight", r=0.75)
d.reaction(["f26"], ["f6p"], at=(7.7, 3.15), angle=180,
           modifiers=[("bifp", "catalysis", {"via": [(13.2, 4.3), (7.7, 4.3)]})])
d.reaction(["f6p"], ["f26"], at=(7.7, 1.45), angle=0,
           modifiers=[("bif", "catalysis", {"via": [(0.9, 8.6), (0.9, 0.7), (7.7, 0.7)]})])
bio.label(ax, (9.0, 3.65), "H₂O → Pᵢ", size="tiny", color=bio.P.muted())
bio.label(ax, (9.0, 1.0), "ATP → ADP", size="tiny", color=bio.P.muted())

# targets
d.activity("pfk1", (19.4, 6.6), "PFK-1", token="positive")
d.activity("fbp1", (19.4, 2.4), "FBPase-1", token="negative")
d.connect("f26", "pfk1", "stimulation", via=[(16.4, 2.4), (16.4, 6.6)])
d.connect("f26", "fbp1", "inhibition")
d.simple_chemical("amp", (21.5, 4.5), "AMP", r=0.5)
d.connect("amp", "pfk1", "stimulation")
d.connect("amp", "fbp1", "inhibition")
d.simple_chemical("cit", (21.5, 8.8), "citrate", r=0.62)
d.connect("cit", "pfk1", "inhibition")
d.phenotype("gly", (19.4, 12.0), "glycolysis", size="tiny")
d.phenotype("gng", (21.0, 0.95), "gluconeogenesis", size="tiny")
d.connect("pfk1", "gly", "stimulation")
d.connect("fbp1", "gng", "stimulation", via=[(19.4, 0.95)])
