# Guard-cell signalling for stomatal opening (blue light) and closure (ABA, high CO2) as an SBGN
# Activity Flow map (simplified; after the models in Taiz et al. 6e, Figs 16.26 and 24.26).
# Opening: phototropins -> BLUS1 -> PP1 -> (unknown kinase) -> phosphorylation of the plasma-membrane
# H+-ATPase and 14-3-3 binding -> hyperpolarization -> K+ uptake through inward-rectifying channels.
# Closure: ABA-PYR/PYL inhibits clade-A PP2Cs, releasing OST1 (SnRK2.6); OST1 activates SLAC1 directly
# and via RBOH -> ROS -> Ca2+ -> CPK; anion efflux depolarizes the membrane, opening GORK (K+ out).
# Cross-talk: Ca2+ inhibits KAT1; ABA, via phosphatidic acid, inhibits PP1; ABA inhibits the H+-ATPase.
import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(22, 12.4)
d = network.Diagram(ax)
d.compartment("gc", (2.9, 0.4, 21.7, 12.0), "Guard cell", token="cytoplasm", label_pos="tr")
bio.label(ax, (1.45, 11.6), "Signals", size="small", bold=True, color=P.muted())

yo, yc = 10.3, 4.0
# opening branch
d.perturbation("blue", (1.45, yo), "Blue light", token="highlight")
d.activity("phot", (5.0, yo), "phot1/phot2", token="receptor")
d.activity("blus", (8.3, yo), "BLUS1", token="enzyme")
d.activity("pp1", (11.2, yo), "PP1", token="protein")
d.activity("atp", (14.6, yo), "H⁺-ATPase", token="channel", units=["P + 14-3-3"])
d.activity("hyp", (18.6, yo), "Hyperpolarization", token="neutral")
d.activity("kat", (18.6, 8.0), "KAT1 (K⁺ in)", token="channel")
d.phenotype("open", (14.6, 8.0), "Opening")
d.connect("blue", "phot", "positive")
d.connect("phot", "blus", "positive")
d.connect("blus", "pp1", "positive")
d.connect("pp1", "atp", "positive", dashed=True)
d.connect("atp", "hyp", "positive")
d.connect("hyp", "kat", "positive")
d.connect("kat", "open", "positive")

# closure branch
d.perturbation("aba", (1.45, yc + 1.6), "ABA", token="drug")
d.perturbation("co2", (1.45, 1.6), "High CO₂", token="neutral")
d.activity("pyr", (5.0, yc + 1.6), "PYR/PYL", token="receptor")
d.activity("pp2c", (8.3, yc + 1.6), "PP2C", token="negative")
d.activity("ost1", (11.2, yc + 1.6), "OST1", token="enzyme")
d.activity("rboh", (11.2, 7.9), "RBOH", token="enzyme")
d.activity("ros", (8.3, 7.9), "ROS", token="metabolite")
d.activity("ca", (5.0, 7.9), "Ca²⁺", token="ca")
d.activity("cpk", (8.3, 2.6), "CPK", token="enzyme")
d.activity("slac", (13.2, 2.6), "SLAC1 (anion out)", token="channel")
d.activity("dep", (18.6, 2.6), "Depolarization", token="neutral")
d.activity("gork", (18.6, 5.3), "GORK (K⁺ out)", token="channel")
d.phenotype("close", (14.9, 5.3), "Closure")
d.activity("pa", (8.3, 12.0 - 0.55), "PA", token="lipid")

d.connect("aba", "pyr", "positive")
d.connect("pyr", "pp2c", "negative")
d.connect("pp2c", "ost1", "negative")
d.connect("ost1", "rboh", "positive")
d.connect("rboh", "ros", "positive")
d.connect("ros", "ca", "positive")
d.connect("ca", "cpk", "positive", via=[(3.7, 7.9), (3.7, 2.6)])
d.connect("cpk", "slac", "positive")
d.connect("ost1", "slac", "positive")
d.connect("slac", "dep", "positive")
d.connect("dep", "gork", "positive")
d.connect("gork", "close", "positive")
d.connect("co2", "slac", "positive", dashed=True, via=[(13.2, 1.6)])
# cross-talk
d.connect("ca", "kat", "negative", via=[(5.0, 9.0), (16.4, 9.0)], dashed=False)
d.connect("aba", "pa", "positive", via=[(2.6, 7.0), (2.6, 11.45)])
d.connect("pa", "pp1", "negative", via=[(11.2, 11.45)])
