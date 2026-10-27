"""The junctions of a simple columnar epithelium (schematic, not to scale).

A: three absorptive cells on a basal lamina. From apex to base: the tight junction seals the lateral
space; the adherens junction forms a continuous belt linked to a bundle of actin filaments; desmosomes are
spot welds anchoring keratin intermediate filaments; gap junctions couple the cytoplasms; at the base,
hemidesmosomes anchor keratin and actin-linked cell-matrix junctions anchor actin to the basal lamina.
B-E: close-ups between two cells (cell 1 left, cell 2 right). B: tight junction strands make kissing
points between the outer leaflets (claudins, with occludin), linked to actin through ZO scaffolds.
C: adherens junction: classical cadherins (five EC domains, Ca2+ ions in the linkers) meet tip to tip;
p120-catenin and beta-catenin bind the tails, alpha-catenin and vinculin link to actin. D: desmosome:
desmogleins and desmocollins, the dense plaque (plakoglobin, plakophilin) and desmoplakin, with keratin
filaments looping into it. E: gap junction: docked connexons bridge a gap of about 3 nm; ions and small
molecules pass, proteins do not.
"""

import wikibio as bio
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(30.0, 15.6)

bio.panel(ax, "A", (0.1, 15.5))
a = J.epithelium(ax, 0.8, 9.6, 1.4, 11.0, n=3)
items = (("tight", "Tight junction", 14.0), ("adherens", "Adherens junction (belt)", 13.1), ("desmosome", "Desmosome", 9.9),
         ("gap", "Gap junction", 4.9), ("hemidesmosome", "Hemidesmosome", 1.0), ("lamina", "Basal lamina", 0.35))
for key, txt, y in items:
    bio.callout(ax, a[key], (10.6, y), txt)
bio.callout(ax, a["keratin"], (10.6, 8.3), "Keratin filaments")
bio.callout(ax, a["focal"], (10.6, 2.1), "Actin-linked cell–matrix junction")
bio.callout(ax, a["belt"] + (1.2, 0), (5.6, 14.9), "Actin bundle of the belt")
bio.label(ax, (5.2, 15.15), "Apical (lumen)", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (0.8, 0.45), "Connective tissue", size="tiny", color=P.muted(), ha="left")

# close-ups
pos = {"B": (19.0, 8.6), "C": (26.0, 8.6), "D": (19.0, 0.9), "E": (26.0, 0.9)}
H = 5.6
bio.panel(ax, "B", (15.2, 15.5))
t = J.tight_junction(ax, pos["B"][0], pos["B"][1], pos["B"][1] + H, strands=4)
bio.label(ax, (19.0, 15.1), "Tight junction", size="small", bold=True)
bio.callout(ax, t["claudin"], (16.4, 13.6), "Claudin")
bio.callout(ax, t["occludin"], (16.4, 9.2), "Occludin")
bio.callout(ax, t["zo"], (21.4, 14.6), "ZO-1")
bio.callout(ax, t["kiss"][2], (21.6, 11.6), "Kissing point")

bio.panel(ax, "C", (22.4, 15.5))
c = J.adherens_junction(ax, pos["C"][0], pos["C"][1], pos["C"][1] + H, pairs=3, gap=1.9)
bio.label(ax, (26.0, 15.1), "Adherens junction", size="small", bold=True)
L, R = c["left"], c["right"]
bio.callout(ax, L["cadherin"], (25.4, 8.15), "Cadherin")
top, bot = c["pairs_right"][-1], c["pairs_right"][0]
bio.callout(ax, top["p120"], (27.0, 14.65), "p120-catenin")
bio.callout(ax, top["beta"], (29.9, 14.65), "β-catenin")
bio.callout(ax, bot["alpha"], (29.9, 8.15), "α-catenin")
bio.callout(ax, R["vinculin"], (29.9, 10.6), "Vinculin")
bio.callout(ax, L["ca"], (22.6, 9.0), "Ca²⁺")
bio.callout(ax, L["actin"], (22.6, 13.9), "Actin")

bio.panel(ax, "D", (15.2, 7.6))
d = J.desmosome(ax, pos["D"][0], pos["D"][1], pos["D"][1] + H, gap=1.4, reach=1.6)
bio.label(ax, (19.0, 7.2), "Desmosome", size="small", bold=True)
bio.callout(ax, d["midline"], (19.0, 6.75), "Desmogleins, desmocollins", size="tiny")
bio.callout(ax, d["left"]["plaque"], (15.5, 6.3), "Dense plaque")
bio.callout(ax, d["left"]["desmoplakin"], (15.6, 1.0), "Desmoplakin")
bio.callout(ax, d["right"]["if"], (22.2, 5.6), "Keratin")

bio.panel(ax, "E", (22.4, 7.6))
g = J.gap_junction(ax, pos["E"][0], pos["E"][1], pos["E"][1] + H, connexons=4)
bio.label(ax, (26.0, 7.2), "Gap junction", size="small", bold=True)
bio.callout(ax, g["connexon"], (28.6, 6.4), "Connexon pair")
bio.callout(ax, g["flux"], (28.6, 3.5), "Ions, metabolites < 1 kDa")
bio.callout(ax, g["protein"], (23.2, 1.3), "Proteins: no")
for k, (x, txt) in enumerate(((pos["E"][0] - 1.6, "Cell 1"), (pos["E"][0] + 1.6, "Cell 2"))):
    bio.label(ax, (x, 0.55), txt, size="tiny", color=P.muted())
