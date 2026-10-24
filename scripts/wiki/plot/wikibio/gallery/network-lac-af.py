# The lac operon of E. coli as an SBGN Activity Flow map: induction by lactose (via allolactose and
# LacI), activation by CAP-cAMP, and catabolite repression by glucose (via adenylate cyclase).
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(19.4, 10.6)
d = network.Diagram(ax)

d.compartment("cell", (3.4, 0.4, 19.2, 10.2), "Cytoplasm", token="cytoplasm", label_pos="tr")
bio.label(ax, (1.75, 9.8), "Medium", size="small", bold=True, color=network.container_edge("extracellular"))

y1, y2, y3, y4 = 8.4, 6.2, 4.2, 2.0
d.activity("lac_out", (1.75, y1), "Lactose", token="carbohydrate")
d.activity("glc", (1.75, y4), "Glucose", token="carbohydrate")
d.activity("lac_in", (6.6, y1), "Lactose", token="carbohydrate")
d.activity("allo", (11.0, y1), "Allolactose", token="carbohydrate")
d.activity("laci", (16.6, y1), "LacI", token="negative")
d.activity("lacy", (6.6, y2), "LacY", token="channel")
d.activity("lacz", (11.0, y2), "LacZ", token="enzyme")
d.phenotype("catab", (13.95, y2), "Lactose catabolism")
d.activity("operon", (11.0, y3), "lacZYA", token="dna", italic=True, units=[("ct:gene", "nucleic", "bl")])
d.activity("cya", (6.6, y4), "CyaA", token="protein")
d.activity("camp", (11.0, y4), "cAMP", token="metabolite")
d.activity("cap", (16.6, y4), "CAP", token="antibody")
d.logic("not", (16.6, y2), "NOT", angle=-90)
d.logic("and", (15.0, y3), "AND", angle=180)

# induction: lactose uptake needs LacY, its conversion to allolactose needs LacZ; allolactose inactivates LacI
d.connect("lac_out", "lac_in", "positive")
d.connect("lacy", "lac_in", "necessary")
d.connect("lac_in", "allo", "positive")
d.connect("lacz", "allo", "necessary")
d.connect("allo", "laci", "negative")
d.connect("lacz", "catab", "positive")
# promoter logic: transcription needs CAP-cAMP AND NOT LacI
d.connect("laci", "not", "logic")
d.connect("not", "and", "logic", via=[(16.6, y3)])
d.connect("cap", "and", "logic", via=[(16.6, y3)])
d.connect("and", "operon", "positive")
# catabolite repression: glucose uptake by the PTS keeps adenylate cyclase inactive
d.connect("glc", "cya", "negative")
d.connect("cya", "camp", "positive")
d.connect("camp", "cap", "positive")
# the operon encodes the permease and beta-galactosidase: positive feedback on uptake and induction
d.connect("operon", "lacz", "positive")
d.connect("operon", "lacy", "positive", via=[(6.6, y3)])
# inducer exclusion: dephosphorylated EIIA-Glc binds and inhibits LacY
d.connect("glc", "lacy", "negative", dashed=True, via=[(1.75, y2)])
bio.label(ax, (4.62, y2 + 0.28), "inducer exclusion", size="tiny", color=bio.P.muted())
