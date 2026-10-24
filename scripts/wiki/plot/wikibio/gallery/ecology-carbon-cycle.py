# The global carbon cycle: pools (boxes and organisms) joined by flux arrows. Biological fluxes in ink,
# the fossil-fuel flux in the "negative" colour; the human perturbation of the budget (Global Carbon
# Budget 2023, Friedlingstein et al. 2023, mean of 2013-2022) in the table. Pool sizes: IPCC AR6 WG1
# Fig. 5.12, rounded (atmosphere for 2019, about 410 ppm CO2).
import wikibio as bio
from wikibio import ecology

fig, ax = bio.canvas(19, 12)
P = bio.P

atm = ecology.node(ax, (9.0, 10.5), "Atmospheric CO₂", sub="≈ 870 PgC", token="extracellular", bold=True, w=3.6)
ocean = ecology.node(ax, (2.2, 10.5), "Ocean", sub="≈ 38,000 PgC", token="dna", bold=True, w=2.9)
plants = ecology.node(ax, (13.0, 5.9), "Producers", sub="vegetation ≈ 450 PgC", icon="phylopic/tree", icon_size=1.8,
                      token="plant")
animals = ecology.node(ax, (17.0, 5.6), "Consumers", icon="phylopic/cattle", icon_size=1.1, token="animal")
soil = ecology.node(ax, (9.0, 2.0), "Dead organic matter, soil", sub="≈ 1,700 PgC", token="lipid_tail", bold=True, w=4.4)
fossil = ecology.node(ax, (3.6, 6.0), "Fossil fuels", sub="coal, oil, gas", token="neutral", bold=True, w=2.8)
microbes = ecology.node(ax, (9.0, 4.25), "Decomposers", icon="phylopic/e-coli", icon_size=0.75, token="carbohydrate",
                        size="small")

ecology.connect(ax, atm, plants, bend=0.2, lw=1.6, text="Photosynthesis", text_offset=0.3, text_at=0.62)
ecology.connect(ax, plants, atm, bend=0.02, lw=1.6, text="Respiration", text_side=-1, text_at=0.42)
ecology.connect(ax, plants, animals, lw=1.6, text="Feeding", text_offset=0.3)
ecology.connect(ax, animals, atm, bend=-0.18, lw=1.6, text="Respiration")
ecology.connect(ax, plants, soil, bend=-0.06, lw=1.6, text="Litterfall", text_side=-1)
ecology.connect(ax, animals, soil, bend=0.1, lw=1.6, text="Death, excretion", text_side=-1)
ecology.connect(ax, soil, microbes, lw=1.6)
ecology.connect(ax, microbes, atm, lw=1.6, text="Decomposition", text_side=-1, text_at=0.5)
ecology.connect(ax, soil, fossil, bend=-0.18, lw=1.6, dashed=True, text="Burial (Myr)", text_side=-1)
ecology.connect(ax, fossil, atm, bend=0.1, lw=2.4, color=P.edge("negative"), text="Combustion")
ecology.connect(ax, atm, ocean, bend=0.15, lw=1.6, text="Dissolution", text_side=-1)
ecology.connect(ax, ocean, atm, bend=0.15, lw=1.6, text="Outgassing")

# human perturbation of the budget
x0, y0 = 0.5, 3.2
bio.label(ax, (x0, y0), "Human perturbation, 2013–2022", size="small", ha="left", bold=True)
bio.label(ax, (x0, y0 - 0.4), "GtC yr⁻¹, Global Carbon Budget 2023", size="tiny", ha="left", color=P.muted())
rows = [("Fossil CO₂ emissions", "9.6"), ("Land-use change", "1.3"), ("Atmospheric growth", "5.2"),
        ("Land sink", "3.3"), ("Ocean sink", "2.8")]
y = y0 - 0.85
for name, v in rows:
    bio.label(ax, (x0, y), name, size="tiny", ha="left")
    bio.label(ax, (x0 + 3.5, y), v, size="tiny", ha="right")
    y -= 0.36
