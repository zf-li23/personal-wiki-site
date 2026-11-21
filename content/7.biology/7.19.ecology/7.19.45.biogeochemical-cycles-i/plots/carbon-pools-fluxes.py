# The global carbon cycle as pools (boxes, Pg C) and fluxes (arrows, Pg C per year).
# Rounded values after IPCC AR6 (Canadell et al. 2021) and the Global Carbon Budget 2024
# (Friedlingstein et al. 2024; anthropogenic fluxes are means for 2014-2023).
# Natural gross fluxes in the ink color, anthropogenic perturbations in red.
import wikibio as bio
from wikibio import ecology as eco

P = bio.P
fig, ax = bio.canvas(16, 9.9)
red = P.edge("negative")

eco.node(ax, (8, 8.3), "Atmosphere", token="extracellular", sub="590 preindustrial + 280 added", w=5.4)
eco.node(ax, (2.4, 5.4), "Vegetation", token="plant", sub="450", w=2.8)
eco.node(ax, (2.4, 2.9), "Soils and litter", token="lipid_tail", sub="1700", w=2.8)
eco.node(ax, (2.4, 0.9), "Permafrost", token="neutral", sub="1400", w=2.8)
eco.node(ax, (8, 2.0), "Fossil fuels", token="lipid", sub="about 1000 in reserves", w=3.4)
eco.node(ax, (12.3, 5.4), "Surface ocean", token="dna", sub="900", w=2.9)
eco.node(ax, (15.05, 5.4), "Marine biota", token="chloroplast", sub="3", w=1.9, size="small")
eco.node(ax, (12.3, 2.9), "Deep ocean", token="dna", sub="37 000 + 700 organic", w=3.6)
eco.node(ax, (12.3, 0.9), "Sediments", token="neutral", sub="1750", w=2.8)

lab = lambda xy, t, **k: bio.label(ax, xy, t, size="small", **k)
# land-atmosphere
bio.arrow(ax, (2.0, 6.0), (5.2, 7.75))
lab((2.3, 7.15), "photosynthesis ~120", ha="left")
bio.arrow(ax, (5.6, 7.75), (2.9, 6.0))
lab((4.85, 6.35), "respiration, fire ~117", ha="left")
bio.arrow(ax, (2.4, 4.85), (2.4, 3.5))
lab((2.55, 4.15), "litter ~60", ha="left")
bio.arrow(ax, (3.85, 3.2), (6.2, 7.75), bend=-0.08)
lab((5.0, 4.6), "decomposition ~60", ha="left")
# ocean-atmosphere
bio.arrow(ax, (10.4, 7.75), (11.9, 6.0))
lab((11.5, 7.15), "dissolution ~80", ha="left")
bio.arrow(ax, (12.6, 6.0), (11.0, 7.75))
lab((11.95, 6.6), "outgassing ~77", ha="left")
bio.arrow(ax, (13.78, 5.4), (14.08, 5.4))
bio.arrow(ax, (12.0, 4.85), (12.0, 3.5))
bio.arrow(ax, (12.6, 3.5), (12.6, 4.85))
lab((12.75, 4.15), "mixing, pumps ~90", ha="left")
bio.arrow(ax, (12.3, 2.35), (12.3, 1.5))
lab((12.45, 1.92), "burial 0.2", ha="left")
bio.arrow(ax, (3.85, 2.75), (10.8, 4.95), bend=-0.03, color=P.muted())
lab((9.15, 3.85), "rivers ~0.8", ha="left", color=P.muted())
# anthropogenic
bio.arrow(ax, (8.0, 2.6), (8.0, 7.75), color=red, lw=2.4)
lab((8.15, 6.4), "fossil CO$_2$ 9.7", ha="left", color=red)
lab((8, 9.7), "Human perturbation, 2014-2023: emissions 9.7 (fossil) + 1.1 (land-use change)", color=red)
lab((8, 9.25), "growth in the atmosphere 5.2, ocean sink 2.9, land sink 3.2", color=red)
lab((8, 0.1), "Pools in Pg C; fluxes in Pg C per year (1 Pg = 10$^{15}$ g)", color=P.muted())
