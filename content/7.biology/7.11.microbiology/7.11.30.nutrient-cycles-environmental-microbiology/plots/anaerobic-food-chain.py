"""The anaerobic food chain: how organic polymers are mineralized to methane and CO2 (schematic).

Without O2 and other external electron acceptors, no single organism mineralizes a polymer. Hydrolytic
bacteria (and fungi in oxic zones) break polymers into monomers with extracellular enzymes; primary
fermenters convert the monomers to acetate, H2 and CO2, and to more reduced products (propionate, butyrate,
lactate, alcohols); syntrophs oxidize these to acetate and H2, which is only possible while hydrogenotrophic
partners keep the H2 partial pressure low (interspecies hydrogen transfer, dashed arrow); acetogens make
acetate from H2 and CO2; methanogens convert acetate (acetoclastic, about two thirds of the methane in
freshwater sediments and digesters) and H2 + CO2 (hydrogenotrophic, about one third) to CH4. Where sulfate is
available (marine sediments), sulfate reducers take the place of syntrophs and methanogens and oxidize the
same intermediates to CO2. Methane that diffuses upward is largely oxidized by anaerobic (AOM, with sulfate)
and aerobic methanotrophs before it reaches the atmosphere.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 15.0)


def node(xy, text, tok, w=4.6, h=1.2, size="small"):
    bio.box(ax, xy, w, h, token=tok, text=text, size=size)
    return xy


def step(a, b, text=None, side=1, dashed=False, color=None, off=0.25):
    bio.arrow(ax, a, b, kind="process", dashed=dashed, color=color)
    if text:
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        bio.label(ax, (mx + side * off, my), text, size="tiny", ha="left" if side > 0 else "right",
                  color=color or P.muted())


poly = node((8.0, 13.6), "polysaccharides, proteins,\nlipids, nucleic acids", "carbohydrate", w=6.0)
mono = node((8.0, 10.9), "sugars, amino acids,\nfatty acids, bases", "metabolite", w=5.2)
red = node((3.6, 7.9), "propionate, butyrate,\nlactate, alcohols", "lipid", w=4.8)
ace = node((8.6, 5.0), "acetate", "atp", w=3.0)
h2 = node((13.4, 5.0), "H₂ + CO₂", "enzyme", w=3.0)
ch4 = node((10.9, 1.6), "CH₄ + CO₂", "neutral", w=3.6)
step((8.0, 13.0), (8.0, 11.55), "1  hydrolysis (extracellular enzymes)")
step((8.0, 10.3), (4.6, 8.55), "2  fermentation", side=-1, off=0.4)
step((8.4, 10.3), (8.6, 5.65))
step((9.0, 10.3), (12.8, 5.65), "2  fermentation", off=0.3)
step((4.4, 7.3), (7.6, 5.6))
bio.label(ax, (5.3, 6.0), "3  syntrophic\n    oxidation", size="tiny", ha="right", color=P.muted())
step((4.9, 7.3), (12.4, 5.62))
bio.arrow(ax, (12.3, 5.5), (5.6, 7.3), kind="activation", dashed=True, color=P.edge("enzyme"), bend=-0.25)
bio.label(ax, (3.4, 4.6), "dashed: H₂ consumers keep p(H₂)\nlow enough for syntrophs\n(interspecies H₂ transfer)", size="tiny", color=P.edge("enzyme"))
step((12.0, 4.6), (10.2, 4.6), None)
bio.label(ax, (11.1, 4.25), "acetogens", size="tiny", color=P.muted())
step((8.6, 4.4), (10.3, 2.2), "4  acetoclastic\n    methanogens (~⅔)", side=-1, off=0.4)
step((13.4, 4.4), (11.5, 2.2), "4  hydrogenotrophic\n    methanogens (~⅓)", off=0.3)

# sulfate branch -------------------------------------------------------------------------------------
bio.box(ax, (20.0, 6.4), 6.2, 3.4, token="extracellular")
bio.label(ax, (20.0, 7.6), "With sulfate (marine sediments)", size="small", bold=True)
bio.label(ax, (20.0, 6.3), "sulfate reducers oxidize\nfatty acids, acetate and H₂\ncompletely to CO₂;\nmethanogens are outcompeted", size="tiny")
step((14.9, 5.6), (16.8, 6.2), None, color=P.muted())

# fate of methane ---------------------------------------------------------------------------------
bio.box(ax, (20.0, 1.9), 6.2, 2.4, token="extracellular")
bio.label(ax, (20.0, 2.6), "The microbial methane filter", size="small", bold=True)
bio.label(ax, (20.0, 1.6), "AOM (ANME + sulfate reducers)\nand aerobic methanotrophs\noxidize most CH₄ to CO₂", size="tiny")
step((12.8, 1.6), (16.8, 1.8), None, color=P.muted())
bio.label(ax, (1.0, 14.6), "Anoxic habitat: wetland, rice paddy, lake sediment, digester, rumen", size="small",
          ha="left", color=P.muted())
