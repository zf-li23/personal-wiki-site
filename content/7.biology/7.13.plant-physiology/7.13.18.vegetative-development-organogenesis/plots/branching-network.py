# Hormonal and nutritional control of axillary bud outgrowth (apical dominance) as an SBGN Activity Flow
# map (simplified; after Domagalska & Leyser 2011, El-Showk et al. 2013, Mason et al. 2014, Taiz et al. 6e
# Figs 19.29-19.34). Auxin from the shoot apex moves rootward in the stem (polar transport); it represses
# local cytokinin synthesis (IPT) and promotes strigolactone synthesis (MAX3/MAX4); strigolactone (via
# D14-MAX2) induces BRC1, cytokinin represses it; BRC1 keeps the bud dormant. A saturated auxin stream in
# the stem also prevents the bud from exporting its own auxin (canalization). Sucrose supply to the bud,
# which rises within hours after decapitation, promotes outgrowth. Low R:FR (phyB) and low nutrients
# (via strigolactone) suppress branching.
import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(20, 10.5)
d = network.Diagram(ax)
d.compartment("stem", (3.2, 0.4, 19.6, 10.1), "Stem node and axillary bud", token="cytoplasm", label_pos="tr")
d.perturbation("dec", (1.6, 9.0), "Decapitation", token="neutral")
d.perturbation("rfr", (1.6, 3.6), "Low R:FR", token="highlight")
d.perturbation("nut", (1.6, 1.6), "Low N, P", token="neutral")
d.activity("aux", (5.6, 9.0), "Auxin (apex)", token="drug")
d.activity("pat", (9.4, 9.0), "Auxin in stem (PIN1)", token="drug")
d.activity("ipt", (9.4, 6.6), "IPT", token="enzyme")
d.activity("ck", (12.9, 6.6), "Cytokinin", token="metabolite")
d.activity("max", (5.6, 5.0), "MAX3 / MAX4", token="enzyme")
d.activity("sl", (9.4, 3.6), "Strigolactone", token="metabolite")
d.activity("brc", (12.9, 3.6), "BRC1", token="protein")
d.activity("suc", (12.9, 1.4), "Sucrose to bud", token="carbohydrate")
d.activity("can", (16.7, 8.4), "Bud auxin export", token="drug")
d.phenotype("bud", (16.7, 4.4), "Bud outgrowth")
d.connect("dec", "aux", "negative")
d.connect("aux", "pat", "positive")
d.connect("pat", "ipt", "negative")
d.connect("ipt", "ck", "positive")
d.connect("pat", "max", "positive", via=[(7.5, 7.7), (5.6, 7.7)])
d.connect("max", "sl", "positive", via=[(5.6, 3.6)])
d.connect("sl", "brc", "positive")
d.connect("ck", "brc", "negative")
d.connect("ck", "bud", "positive", via=[(15.0, 6.6)])
d.connect("brc", "bud", "negative")
d.connect("suc", "bud", "positive", via=[(16.7, 1.4)])
d.connect("suc", "brc", "negative")
d.connect("pat", "can", "negative", via=[(16.7, 9.0)])
d.connect("can", "bud", "positive")
d.connect("rfr", "brc", "positive", via=[(3.6, 2.6), (12.4, 2.6)], dashed=True)
d.connect("nut", "sl", "positive", via=[(8.6, 1.6)], dashed=True)
d.connect("dec", "suc", "positive", via=[(2.9, 9.9), (2.9, 0.75), (12.9, 0.75)], dashed=True)
