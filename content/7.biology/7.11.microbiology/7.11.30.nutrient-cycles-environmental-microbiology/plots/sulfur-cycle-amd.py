"""The sulfur cycle arranged by oxidation state, and the propagation cycle of pyrite oxidation in acid
mine drainage.

A: the main sulfur species with the oxidation state of S (vertical axis). Reductive processes (down):
dissimilatory sulfate reduction by sulfate-reducing bacteria and archaea, sulfur reduction, assimilatory
sulfate reduction into amino acids. Oxidative processes (up): sulfide oxidation to elemental sulfur and
sulfate by chemolithotrophs (Beggiatoa, Thiobacillus, Acidithiobacillus, cable bacteria) and anoxygenic
phototrophs (purple and green sulfur bacteria); release of sulfide from organic matter (desulfurylation).
Dimethylsulfoniopropionate (DMSP) made by marine algae is cleaved to dimethyl sulfide (DMS), the largest
natural biogenic sulfur flux to the atmosphere.
B: pyrite oxidation. Initiation by O2 (1) releases Fe2+ and acid; at pH below about 3.5 the abiotic oxidation
of Fe2+ by O2 is very slow, and acidophilic iron oxidizers (Acidithiobacillus ferrooxidans, Leptospirillum,
Ferroplasma) catalyse it (2); Fe3+ then oxidizes pyrite much faster than O2 does (3), regenerating Fe2+,
so that the cycle of reactions 2 and 3 propagates the dissolution and produces 16 H+ per FeS2.
"""
import wikibio as bio
from wikibio import ecology as E
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27.0, 13.0)

# A: by oxidation state ------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 12.8))
pl = quant.Plot(ax, (1.8, 1.2, 0.01, 10.0), xlim=(0, 1), ylim=(-2.6, 6.6), ylabel="oxidation state of S",
                yticks=[(-2, "−2"), (0, "0"), (2, "+2"), (6, "+6")], frame="l")


def Y(v):
    return pl.Y(v)


so4 = E.node(ax, (7.2, Y(6)), "SO₄²⁻", token="lipid", size="small", w=1.8)
s0 = E.node(ax, (11.0, Y(0)), "S⁰", token="atp", size="small", w=1.4)
s2o3 = E.node(ax, (13.4, Y(2)), "S₂O₃²⁻", token="metabolite", size="small", w=1.8)
h2s = E.node(ax, (7.2, Y(-2)), "H₂S", token="enzyme", size="small", w=1.6)
org = E.node(ax, (3.2, Y(-2)), "organic S\n(Cys, Met)", token="plant", size="small")
dmsp = E.node(ax, (13.4, Y(-2)), "DMSP → DMS", token="neutral", size="small")
E.connect(ax, so4, h2s)
bio.label(ax, (7.0, Y(1.0)), "dissimilatory\nsulfate reduction", size="small", ha="right", color=P.muted())
E.connect(ax, h2s, s0)
bio.label(ax, (11.6, Y(-1.1)), "sulfide\noxidation", size="small", ha="left", color=P.muted())
E.connect(ax, s0, so4)
bio.label(ax, (9.4, Y(3.4)), "S⁰ oxidation", size="small", ha="left", color=P.muted())
E.connect(ax, s0, h2s, bend=0.35, dashed=True)
bio.label(ax, (9.3, Y(-2.45)), "S⁰ reduction", size="tiny", ha="left", color=P.muted())
E.connect(ax, so4, org)
bio.label(ax, (4.4, Y(3.0)), "assimilation", size="small", ha="right", color=P.muted())
E.connect(ax, org, h2s)
bio.label(ax, (5.2, Y(-2.5)), "desulfurylation", size="tiny", color=P.muted())
E.connect(ax, s2o3, so4, dashed=True)
E.connect(ax, s2o3, h2s, dashed=True)
bio.label(ax, (14.6, Y(3.0)), "disproportionation", size="tiny", color=P.muted())
bio.arrow(ax, (13.4, Y(-2) + 0.45), (13.4, Y(-2) + 2.0), kind="process", color=P.muted())
bio.label(ax, (13.6, Y(-2) + 2.2), "to atmosphere", size="tiny", ha="left", color=P.muted())

# B: pyrite oxidation cycle -----------------------------------------------------------------------
bio.panel(ax, "B", (16.0, 12.8))
py = E.node(ax, (21.2, 10.6), "pyrite FeS₂", token="neutral", size="small")
fe2 = E.node(ax, (17.8, 5.2), "Fe²⁺", token="enzyme", size="small", w=1.6)
fe3 = E.node(ax, (24.6, 5.2), "Fe³⁺", token="atp", size="small", w=1.6)
E.connect(ax, py, fe2, text="(1) + O₂", text_side=-1)
E.connect(ax, fe2, fe3, bend=0.25, text="(2) + O₂, iron-oxidizing acidophiles", text_side=1)
E.connect(ax, fe3, fe2, bend=0.25, text="(3) + FeS₂ (fast, also anoxic)", text_side=1)
E.connect(ax, py, fe3, dashed=True, color=P.muted())
eqs = ["(1)  FeS₂ + 3.5 O₂ + H₂O → Fe²⁺ + 2 SO₄²⁻ + 2 H⁺",
       "(2)  Fe²⁺ + 0.25 O₂ + H⁺ → Fe³⁺ + 0.5 H₂O",
       "(3)  FeS₂ + 14 Fe³⁺ + 8 H₂O → 15 Fe²⁺ + 2 SO₄²⁻ + 16 H⁺"]
for k, e in enumerate(eqs):
    bio.label(ax, (16.6, 2.0 - 0.6 * k), e, size="tiny", ha="left")
