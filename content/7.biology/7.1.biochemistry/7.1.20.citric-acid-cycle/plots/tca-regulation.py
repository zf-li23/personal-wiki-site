"""Regulation of pyruvate oxidation and the citric acid cycle in mammals (SBGN activity flow).

Filled arrows: the flow of carbon (pyruvate -> acetyl-CoA -> citrate -> ... -> succinyl-CoA). Influences:
open arrows activate, bars inhibit. Signals of energy sufficiency (high ATP/ADP, NADH/NAD+, acetyl-CoA/CoA,
long-chain fatty acids) inhibit the PDH complex allosterically and activate PDH kinase, which inactivates
E1 by phosphorylation; ADP, pyruvate and NAD+ inhibit the kinase. PDH phosphatase, activated by Ca2+ and
insulin, reactivates the complex; dichloroacetate inhibits the kinase. In the cycle, citrate synthase is
inhibited by citrate, succinyl-CoA and ATP (relieved by ADP); isocitrate dehydrogenase is inhibited by ATP
and NADH and activated by ADP and Ca2+; alpha-ketoglutarate dehydrogenase is inhibited by succinyl-CoA and
NADH and activated by Ca2+.
"""

import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(26.0, 14.6, scale=0.42)
d = network.Diagram(ax, size="small")
d.compartment("mx", (0.3, 0.3, 25.7, 14.3), "Mitochondrial matrix", token="matrix", label_pos="bl")

y = 7.4
d.activity("pdh", (8.0, y), "PDH complex", token="enzyme")
d.activity("cs", (12.4, y), "citrate synthase", token="carbohydrate")
d.activity("idh", (17.6, y), "isocitrate DH", token="carbohydrate")
d.activity("kgdh", (22.8, y), "α-KG DH complex", token="carbohydrate")
d.connect("pdh", "cs", "process", text="acetyl-CoA", text_offset=(0, 0.1))
d.connect("cs", "idh", "process", text="citrate", text_offset=(0, 0.1))
d.connect("idh", "kgdh", "process", text="α-KG", text_offset=(0, 0.1))

d.activity("pdk", (2.6, 10.8), "PDH kinase", token="negative")
d.activity("pdp", (2.6, 4.0), "PDH phosphatase", token="positive")
d.connect("pdk", "pdh", "negative", text="P-E1", text_offset=(0.3, 0.2))
d.connect("pdp", "pdh", "positive")

d.unspecified("rich", (9.6, 12.9), "ATP, NADH, acetyl-CoA,\nfatty acids", token="drug", w=5.0, h=1.3)
d.unspecified("poor", (9.6, 1.8), "ADP, AMP, NAD⁺, CoA,\npyruvate", token="positive", w=5.0, h=1.3)
d.connect("rich", "pdk", "positive")
d.connect("rich", "pdh", "negative")
d.connect("rich", "cs", "negative", text="ATP", text_offset=(0.35, 0))
d.connect("rich", "idh", "negative", text="ATP, NADH", text_offset=(0.6, 0.1))
d.connect("poor", "pdk", "negative", via=[(5.2, 1.8), (5.2, 10.8)], text="ADP, NAD⁺,\npyruvate", text_at=0.7,
          text_offset=(-1.0, 0))
d.connect("poor", "pdh", "positive")
d.connect("poor", "cs", "positive", text="ADP", text_offset=(0.3, 0))
d.connect("poor", "idh", "positive", text="ADP", text_offset=(0.35, 0))

d.simple_chemical("ca", (20.2, 12.9), "Ca²⁺", token="ca", r=0.55)
d.connect("ca", "idh", "positive")
d.connect("ca", "kgdh", "positive")
d.connect("ca", "pdp", "positive", via=[(20.2, 13.9), (0.9, 13.9), (0.9, 4.0)], text="(muscle)", text_at=0.35)
d.simple_chemical("ins", (2.6, 1.6), "insulin", token="drug", r=0.6)
d.connect("ins", "pdp", "positive")
d.simple_chemical("dca", (2.6, 13.2), "DCA", token="drug", r=0.5)
d.connect("dca", "pdk", "negative")

d.simple_chemical("cit", (14.9, 4.2), "citrate", r=0.6)
d.connect("cit", "cs", "negative")
d.simple_chemical("scoa", (20.2, 4.2), "succinyl-\nCoA", r=0.7)
d.connect("scoa", "kgdh", "negative")
d.connect("scoa", "cs", "negative", bend=-0.15)
d.simple_chemical("nadh", (24.5, 11.0), "NADH", r=0.55)
d.connect("nadh", "kgdh", "negative")
