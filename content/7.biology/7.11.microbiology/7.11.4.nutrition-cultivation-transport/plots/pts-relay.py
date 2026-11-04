"""The glucose phosphotransferase system of E. coli as an SBGN process-description map. Each process
transfers the phosphoryl group from a donor (lower row, phosphorylated, state P) to the next acceptor
(upper row, unphosphorylated): PEP -> Enzyme I -> HPr -> EIIA(Glc) -> EIIB(Glc) -> glucose, the last
step catalyzed by the membrane channel EIIC(Glc), so that glucose from outside appears inside as
glucose 6-phosphate. Regulatory outputs (below and above): EIIA(Glc)-P stimulates adenylate cyclase
(ATP -> cAMP); unphosphorylated EIIA(Glc) inhibits lactose permease (inducer exclusion)."""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(25.0, 14.2)
d = network.Diagram(ax, size="small")
d.compartment("out", (0.3, 12.0, 24.7, 13.9), "Outside", token="extracellular", label_pos="tl")
d.compartment("cyt", (0.3, 0.3, 24.7, 11.0), "Cytoplasm", token="cytoplasm", label_pos="bl")

xs = [2.2, 6.4, 10.6, 14.8, 19.0, 22.8]
yu, yl = 8.8, 5.6
d.simple_chemical("pyr", (xs[0], yu), "pyruvate")
d.simple_chemical("pep", (xs[0], yl), "PEP")
names = ["Enzyme I", "HPr", "EIIA^Glc", "EIIB^Glc"]
labels = ["Enzyme I", "HPr", "EIIAᴳˡᶜ", "EIIBᴳˡᶜ"]
for k, t in enumerate(labels, start=1):
    d.macromolecule(f"u{k}", (xs[k], yu), t, w=2.6, states=[""])
    d.macromolecule(f"p{k}", (xs[k], yl), t, w=2.6, states=["P"])
d.simple_chemical("glc", (xs[5], 12.95), "glucose", token="carbohydrate")
d.simple_chemical("g6p", (xs[5], yl), "glucose 6-P", token="carbohydrate")
d.macromolecule("eiic", (xs[5] - 1.9, 11.5), "EIICᴳˡᶜ", w=2.5, token="channel")

donors = ["pep", "p1", "p2", "p3", "p4"]
after = ["pyr", "u1", "u2", "u3", "u4"]
acc = ["u1", "u2", "u3", "u4", "glc"]
accp = ["p1", "p2", "p3", "p4", "g6p"]
for k in range(5):
    at = ((xs[k] + xs[k + 1]) / 2, (yu + yl) / 2)
    mods = [("eiic", "catalysis")] if k == 4 else []
    d.reaction([donors[k], acc[k]], [after[k], accp[k]], at=at, angle=0, modifiers=mods)

# regulation
d.macromolecule("cya", (xs[3], 2.9), "adenylate cyclase", w=3.6, token="enzyme")
d.simple_chemical("atp", (xs[2] - 0.6, 1.2), "ATP", token="atp")
d.simple_chemical("camp", (xs[4] + 0.6, 1.2), "cAMP", token="atp")
d.reaction(["atp"], ["camp"], at=(xs[3], 1.2), angle=0, modifiers=[("cya", "catalysis")])
d.connect("p3", "cya", kind="stimulation")
d.macromolecule("lacy", (xs[1], 11.5), "LacY (lactose permease)", w=4.4, token="enzyme")
d.connect("u3", "lacy", kind="inhibition", bend=0.15)
bio.label(ax, (xs[3] + 0.4, 4.1), "glucose absent: EIIA mostly ~P", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (2.6, 10.2), "glucose present:\ninducer exclusion", size="tiny", color=P.muted())
bio.label(ax, (12.6, 11.5), "cytoplasmic membrane", size="tiny", color=P.muted())
