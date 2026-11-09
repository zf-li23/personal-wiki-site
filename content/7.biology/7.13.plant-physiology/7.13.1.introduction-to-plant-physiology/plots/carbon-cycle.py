# The global carbon cycle and the role of plants (fluxes in Pg C per year, stocks in Pg C).
# Gross and net primary production: terrestrial GPP about 120 (Beer et al. 2010); NPP about 56 on land and
# 49 in the ocean (Field et al. 1998). Anthropogenic perturbation, 2013-2022 decadal means of the Global
# Carbon Budget 2023 (Friedlingstein et al. 2023): fossil CO2 emissions 9.6, land-use change 1.3, growth of
# atmospheric CO2 5.2, ocean sink 2.8, land sink 3.3. Atmospheric stock about 880 Pg C in 2022 (2.12 Pg C per
# ppm of CO2; about 590 Pg C before industrialization).
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 12.0)
bio.box(ax, (11.0, 10.2), 7.4, 1.6, "neutral", text="Atmosphere ≈ 880 Pg C (≈ 417 ppm CO₂)", size="small")
bio.box(ax, (4.2, 3.2), 6.6, 2.0, "plant", text="Land: vegetation and soils", size="small")
bio.box(ax, (17.8, 3.2), 6.6, 2.0, "channel", text="Ocean", size="small")
bio.box(ax, (11.0, 1.0), 4.6, 1.2, "animal", text="Fossil carbon", size="small")


def flow(a, b, txt, at, tok, kind="process", bend=0.0):
    bio.arrow(ax, a, b, kind=kind, color=P.edge(tok), lw=1.6, bend=bend)
    bio.label(ax, at, txt, size="tiny", ha="center")


flow((7.9, 9.35), (2.4, 4.3), "photosynthesis\nGPP ≈ 120", (3.4, 7.3), "plant")
flow((4.4, 4.3), (8.9, 9.35), "", (0, 0), "neutral")
bio.label(ax, (6.35, 5.5), "respiration,\ndecay", size="tiny", color=P.edge("neutral"))
flow((6.6, 4.3), (9.9, 9.35), "", (0, 0), "negative")
bio.label(ax, (9.3, 7.1), "land use\n1.3", size="tiny", color=P.edge("negative"))
bio.label(ax, (4.2, 2.6), "NPP ≈ 56; net sink 3.3", size="tiny", color=P.on_fill())
flow((13.6, 9.35), (17.0, 4.3), "net uptake 2.8", (16.6, 7.1), "channel")
bio.label(ax, (17.8, 2.6), "phytoplankton NPP ≈ 49", size="tiny", color=P.on_fill())
flow((11.0, 1.65), (11.0, 9.35), "fossil\n9.6", (11.7, 5.6), "negative")
bio.label(ax, (11.0, 11.5), "atmospheric increase +5.2 per year", size="tiny", bold=True)
bio.label(ax, (11.0, 0.15), "fluxes in Pg C yr⁻¹ (1 Pg = 10¹⁵ g); decadal means 2013–2022", size="tiny", color=P.muted())
