"""Phosphatidic acid is the branch point of triacylglycerol and glycerophospholipid synthesis (mammals).

Glycerol 3-phosphate comes from dihydroxyacetone phosphate (glycerol 3-phosphate dehydrogenase, NADH) or,
in liver and kidney, from glycerol (glycerol kinase). Two acyl-CoA acylate it to lysophosphatidic acid
(GPAT) and phosphatidic acid (AGPAT). Strategy 2 (Kennedy pathway): phosphatidic acid phosphatase (lipin)
gives diacylglycerol, which receives a third acyl group (DGAT) to make triacylglycerol, or a phospho-head
group from CDP-choline or CDP-ethanolamine to make phosphatidylcholine (PC) or phosphatidylethanolamine
(PE). Strategy 1: CDP-diacylglycerol synthase activates phosphatidic acid with CTP; CDP-diacylglycerol
reacts with inositol (PI) or glycerol 3-phosphate (phosphatidylglycerol phosphate, then PG); PG and a second
CDP-diacylglycerol give cardiolipin in mitochondria. Interconversions: phosphatidylserine (PS) is made by
head-group exchange from PE or PC (PS synthases 1 and 2), decarboxylated to PE in mitochondria (PSD), and PE
is methylated three times by S-adenosylmethionine to PC in the liver (PEMT).
"""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(27.0, 14.4, scale=0.42)
pw = M.Pathway(ax, size="small")
pw.node("dhap", (2.4, 13.2), "Dihydroxyacetone phosphate")
pw.node("gly", (8.2, 13.2), "Glycerol")
pw.node("g3p", (2.4, 10.4), "Glycerol 3-phosphate")
pw.node("lpa", (2.4, 7.2), "Lysophosphatidic acid")
pw.node("pa", (7.4, 7.2), "Phosphatidic acid", token="highlight", bold=True)
pw.step("dhap", "g3p", enzyme="G3P DH", side=("NADH", "NAD⁺"), enzyme_offset=0.2, flip=True)
pw.step("gly", "g3p", enzyme="glycerol kinase\n(liver, kidney)", side=("ATP", "ADP"), enzyme_offset=0.2, flip=True)
pw.step("g3p", "lpa", enzyme="GPAT", side=("acyl-CoA", "CoA"), enzyme_offset=0.2, flip=True)
pw.step("lpa", "pa", enzyme="AGPAT", side=("acyl-CoA", "CoA"), enzyme_offset=0.2)

# strategy 2: diacylglycerol + CDP-alcohol
pw.node("dag", (12.4, 10.4), "Diacylglycerol", bold=True)
pw.node("tag", (18.6, 13.2), "Triacylglycerol", token="lipid", bold=True)
pw.node("pc", (18.6, 10.4), "Phosphatidylcholine", token="lipid_head", bold=True)
pw.node("pe", (18.6, 7.6), "Phosphatidylethanolamine", token="lipid_head", bold=True)
pw.step("pa", "dag", enzyme="PA phosphatase\n(lipin)", side=("H₂O", "Pᵢ"), enzyme_offset=0.2, flip=True)
pw.step("dag", "tag", enzyme="DGAT (acyl-CoA)", enzyme_offset=0.2, flip=True)
pw.step("dag", "pc", side=("CDP-choline", "CMP"), side_span=1.0, flip=True)
pw.step("dag", "pe", side=("CDP-ethanol-\namine", "CMP"), side_span=1.0, flip=True, side_reach=0.7)

# strategy 1: CDP-diacylglycerol + head-group alcohol
pw.node("cdpdag", (12.4, 4.2), "CDP-diacylglycerol", bold=True)
pw.node("pi", (18.6, 5.0), "Phosphatidylinositol", token="lipid_head", bold=True)
pw.node("pg", (18.6, 2.0), "Phosphatidylglycerol", token="lipid_head")
pw.node("cl", (24.4, 2.0), "Cardiolipin", token="lipid_head", bold=True)
pw.step("pa", "cdpdag", enzyme="CDS", side=("CTP", "PPᵢ"), enzyme_offset=0.2)
pw.step("cdpdag", "pi", side=("inositol", "CMP"), side_span=0.9)
pw.step("cdpdag", "pg", side=("G3P", "CMP + Pᵢ"), side_span=0.9, flip=True)
pw.step("pg", "cl", enzyme="cardiolipin synthase\n(mitochondria)", side=("CDP-DAG", "CMP"), enzyme_offset=0.2)

# interconversions of head groups
pw.node("ps", (24.6, 10.4), "Phosphatidylserine", token="lipid_head", bold=True)
pw.step("pe", "pc")
bio.label(ax, (17.45, 9.3), "PEMT\n(3 SAM)", size="tiny", bold=True, color=P.edge("enzyme"), ha="right")
pw.step("pc", "ps")
bio.label(ax, (22.1, 10.85), "PSS1", size="tiny", bold=True, color=P.edge("enzyme"))
pw.step("pe", "ps", reversible=True)
bio.label(ax, (23.6, 8.2), "PSS2: Ser in, ethanolamine out\nPSD (mitochondria): − CO₂", size="tiny", bold=True,
          color=P.edge("enzyme"))
bio.box(ax, (13.0, 13.2), 4.6, 1.1, "lipid_head", text="strategy 2: CDP-alcohol\n(Kennedy pathway)", size="tiny")
bio.box(ax, (12.4, 1.4), 5.0, 1.1, "highlight", text="strategy 1: CDP-diacylglycerol\n(also bacteria)", size="tiny")
bio.label(ax, (2.4, 4.4), "acyl groups: usually saturated\nat C-1, unsaturated at C-2;\nremodelled later (Lands cycle)",
          size="tiny", color=P.muted())
