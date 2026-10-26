"""Two-component signaling in bacteria and its descendants in plants.

A: domain architectures (N-terminus left). A bacterial sensor histidine kinase (for example EnvZ)
with a periplasmic input domain between two transmembrane helices and a cytoplasmic kinase made of
a dimerization/phosphotransfer domain with the phosphorylated His (DHp) and a catalytic ATP-binding
domain (CA); its response regulator (OmpR) has a receiver domain with the phosphorylated Asp and a
DNA-binding output domain. The phosphoryl group goes ATP -> His -> Asp. The ethylene receptor ETR1 of
Arabidopsis has three transmembrane helices that bind ethylene (with a Cu+ cofactor) in the ER
membrane, a GAF domain, a His kinase domain and a receiver domain. The cytokinin receptor AHK4 (CRE1)
has an extracellular CHASE domain that binds cytokinin, a His kinase and a receiver domain; the
phosphoryl group is relayed through the histidine phosphotransfer protein AHP to the receiver Asp of a
type-B response regulator (ARR), a transcription factor (a His-Asp-His-Asp phosphorelay).
B: logic of ethylene signaling (SBGN activity flow). Without ethylene the receptors keep the Raf-like
kinase CTR1 active; CTR1 phosphorylates EIN2 and keeps it inactive. Ethylene inactivates the receptors,
CTR1 is switched off, the C-terminal part of EIN2 is cleaved off and acts in the nucleus to stabilize
the transcription factors EIN3/EIL1, which induce the ethylene responses: a chain of negative regulators.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(25.0, 11.0)
bio.panel(ax, "A", (0.1, 10.9))


def tm(x, y):
    bio.domains(ax, x, y, [("TM", 0.45, "neutral")], height=0.45)


def row(y, title, parts, x0=0.8):
    if title:
        bio.label(ax, (x0, y + 0.6), title, size="small", bold=True, ha="left")
    x = x0
    for name, L, tok in parts:
        if name == "TM":
            tm(x, y)
            x += 0.5
        else:
            x = bio.domains(ax, x, y, [(name, L, tok)], height=0.45)
    return x


y1, y2, y3, y4 = 9.6, 7.9, 6.2, 4.3
row(y1, "sensor kinase", [("TM", 0, ""), ("input", 1.3, "receptor"), ("TM", 0, ""), ("DHp (His)", 1.7, "enzyme"), ("CA (ATP)", 1.4, "antibody")])
xr = row(y2, "", [("receiver (Asp)", 2.0, "protein"), ("output (DNA binding)", 2.7, "metabolite")], x0=4.1)
bio.label(ax, (xr + 0.2, y2), "response regulator", size="small", bold=True, ha="left")
bio.arrow(ax, (4.8, y1 - 0.3), (4.85, y2 + 0.3), kind="process")
bio.label(ax, (5.0, (y1 + y2) / 2 + 0.1), "P: His → Asp", size="tiny", ha="left")
bio.label(ax, (8.6, y1), "e.g. EnvZ / OmpR (osmolarity)", size="tiny", ha="left", color=P.muted())
x = row(y3, "ethylene receptor ETR1", [("TM", 0, ""), ("TM", 0, ""), ("TM", 0, ""), ("GAF", 1.0, "neutral"), ("His kinase", 1.8, "enzyme"),
                                        ("receiver", 1.3, "protein")])
bio.label(ax, (x + 0.2, y3), "ER membrane; Cu⁺ binds ethylene", size="tiny", ha="left", color=P.muted())
x = row(y4, "cytokinin receptor AHK4", [("CHASE", 1.4, "receptor"), ("TM", 0, ""), ("His kinase", 1.8, "enzyme"), ("receiver", 1.3, "protein")])
bio.domains(ax, 4.0, 2.6, [("AHP (His)", 1.5, "highlight")], height=0.45)
bio.domains(ax, 8.6, 1.1, [("receiver (Asp)", 2.0, "protein"), ("Myb-like DNA binding", 2.9, "metabolite")], height=0.45)
bio.label(ax, (13.8, 1.1), "type-B ARR", size="small", bold=True, ha="left")
bio.arrow(ax, (x - 0.6, y4 - 0.3), (4.8, 2.9), kind="process")
bio.arrow(ax, (5.6, 2.35), (9.4, 1.4), kind="process")
bio.label(ax, (6.0, 2.85), "phosphorelay to the nucleus", size="tiny", ha="left", color=P.muted())

# B: ethylene activity flow
bio.panel(ax, "B", (16.6, 10.9))
d = network.Diagram(ax, size="small")
xb = 20.6
d.activity("eth", (xb, 9.6), "ethylene", token="drug")
d.activity("etr", (xb, 8.0), "ETR1 family receptors", token="receptor")
d.activity("ctr", (xb, 6.4), "CTR1 (Raf-like kinase)", token="enzyme")
d.activity("ein2", (xb, 4.8), "EIN2 (C-terminal part)", token="protein")
d.activity("ein3", (xb, 3.2), "EIN3 / EIL1", token="metabolite")
d.phenotype("resp", (xb, 1.5), "ethylene responses", token="highlight")
d.connect("eth", "etr", "negative")
d.connect("etr", "ctr", "positive")
d.connect("ctr", "ein2", "negative")
d.connect("ein2", "ein3", "positive")
d.connect("ein3", "resp", "positive")
bio.label(ax, (xb + 2.6, 7.2), "air: ON", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (xb + 2.6, 4.0), "ethylene: EIN2-C\nto nucleus", size="tiny", color=P.muted(), ha="left")
