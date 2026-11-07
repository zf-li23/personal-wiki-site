# Flowering pathways of Arabidopsis converging on the floral integrators (SBGN activity flow, simplified).
# Leaf (left): photoperiod (CO), ambient temperature (PIF4; SVP-FLM repressor) and FLC regulate FT.
# Shoot apex (right): FT moves through the phloem and forms a complex with FD; FLC is repressed by
# vernalization and the autonomous pathway and activated by FRI; GA and the age pathway (miR156 -> SPL)
# act on SOC1, LFY and AP1; LFY and AP1 activate each other; TFL1 opposes them in the shoot.
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(19, 10.5)
d = network.Diagram(ax)
d.compartment("leaf", (0.3, 0.3, 7.2, 10.2), "Leaf (companion cells)", token="cytoplasm")
d.compartment("sam", (8.0, 0.3, 18.7, 10.2), "Shoot apical meristem", token="nucleus")

# leaf
d.perturbation("ld", (1.6, 9.0), "Long days")
d.activity("co", (1.6, 7.2), "CO")
d.perturbation("warm", (5.6, 9.0), "Warm")
d.activity("pif4", (5.6, 7.2), "PIF4")
d.activity("svp", (5.6, 3.0), "SVP-FLM")
d.activity("ftl", (3.6, 5.0), "FT", token="highlight")
d.activity("flcl", (1.6, 3.0), "FLC", token="negative")
d.connect("ld", "co", kind="positive")
d.connect("warm", "pif4", kind="positive")
d.connect("co", "ftl", kind="positive")
d.connect("pif4", "ftl", kind="positive")
d.connect("svp", "ftl", kind="negative")
d.connect("flcl", "ftl", kind="negative")

# apex
d.perturbation("cold", (9.4, 9.0), "Prolonged cold")
d.activity("auto", (12.0, 9.0), "Autonomous")
d.activity("fri", (9.4, 6.2), "FRI")
d.activity("flc", (11.2, 7.2), "FLC", token="negative")
d.activity("ftfd", (11.2, 4.6), "FT-FD", token="highlight")
d.activity("soc1", (14.0, 6.0), "SOC1")
d.perturbation("ga", (17.2, 9.0), "Gibberellin")
d.activity("mir", (15.0, 9.0), "miR156", token="rna")
d.activity("spl", (15.0, 7.6), "SPL")
d.activity("lfy", (14.0, 3.6), "LFY")
d.activity("ap1", (16.8, 3.6), "AP1")
d.activity("tfl1", (11.2, 1.6), "TFL1", token="negative")
d.phenotype("flower", (17.2, 6.0), "Flower")

d.connect("ftl", "ftfd", kind="positive", text="phloem", text_offset=(0, 0.3))
d.connect("cold", "flc", kind="negative")
d.connect("auto", "flc", kind="negative")
d.connect("fri", "flc", kind="positive")
d.connect("flc", "soc1", kind="negative")
d.connect("flc", "ftfd", kind="negative")
d.connect("ftfd", "soc1", kind="positive")
d.connect("ftfd", "ap1", kind="positive", via=[(13.6, 2.6), (16.8, 2.6)])
d.connect("mir", "spl", kind="negative")
d.connect("spl", "soc1", kind="positive")
d.connect("ga", "soc1", kind="positive", via=[(17.2, 7.6), (16.2, 6.6)])
d.connect("soc1", "lfy", kind="positive")
d.connect("lfy", "ap1", kind="positive", bend=0.25)
d.connect("ap1", "lfy", kind="positive", bend=0.25)
d.connect("tfl1", "lfy", kind="negative")
d.connect("ap1", "flower", kind="positive")
