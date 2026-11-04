"""The microbial loop and the viral shunt in the surface ocean (schematic).

Phytoplankton (cyanobacteria and eukaryotic algae) fix CO2. Part of their production is eaten by
zooplankton (the classic food chain: diatoms, copepods, fish); a large part is released as dissolved
organic carbon (DOC) by exudation, sloppy feeding and cell lysis. Heterotrophic bacteria and archaea take up
the DOC, and are grazed by heterotrophic nanoflagellates, which are eaten by ciliates and these by
copepods: the microbial loop returns DOC to the food web and regenerates nutrients and CO2 by respiration at
each step. Viral lysis of bacteria (and of phytoplankton, not drawn) turns cells back into DOC (dashed) (the viral shunt),
which keeps carbon and nutrients in the microbial part of the web. Sinking particles (marine snow, faecal
pellets) export carbon to depth (the biological pump).
"""
import wikibio as bio
from wikibio import ecology as E

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)

phyto = E.node(ax, (4.2, 9.2), "Phytoplankton", icon="phylopic/diatom", icon_size=1.4, token="plant",
               sub="diatoms, cyanobacteria")
bio.icon(ax, "phylopic/cyanobacterium", at=(2.3, 9.4), height=1.1, color="plant")
cope = E.node(ax, (13.0, 9.2), "Copepods", icon="phylopic/copepod", icon_size=1.4, token="animal")
fish = E.node(ax, (19.5, 9.2), "Fish", icon="phylopic/herring", icon_size=1.2, token="animal")
doc = E.node(ax, (4.2, 4.6), "Dissolved organic carbon", token="metabolite", sub="DOC")
bact = E.node(ax, (10.6, 4.6), "Heterotrophic bacteria\nand archaea", token="bacterium")
hnf = E.node(ax, (16.2, 4.6), "Nanoflagellates", token="protein")
cil = E.node(ax, (17.6, 6.9), "Ciliates", token="protein")
vir = E.node(ax, (7.4, 1.6), "Viruses", token="virus")
co2 = E.node(ax, (20.0, 1.6), "CO₂ and nutrients", token="neutral", sub="respiration, excretion")

E.connect(ax, phyto, cope, text="classic food chain", text_side=1)
E.connect(ax, cope, fish)
E.connect(ax, phyto, doc, text="exudation, sloppy feeding", text_side=-1)
E.connect(ax, doc, bact, text="uptake", text_side=1)
E.connect(ax, bact, hnf, text="grazing", text_side=1)
E.connect(ax, hnf, cil)
E.connect(ax, cil, cope)
E.connect(ax, bact, vir, dashed=True, color=P.edge("virus"), text="lysis", text_side=-1)
E.connect(ax, vir, doc, dashed=True, color=P.edge("virus"), text="viral shunt", text_side=1)
for n in (bact, hnf):
    E.connect(ax, n, co2, kind="process", color=P.muted(), lw=0.9, margin=0.2)
bio.arrow(ax, (1.2, 7.6), (1.2, 0.6), kind="process", color=P.edge("highlight"), lw=1.4)
bio.label(ax, (1.45, 1.0), "sinking particles:\nbiological pump", size="tiny", ha="left", color=P.edge("highlight"))
bio.label(ax, (12.0, 11.6), "Surface ocean", size="small", bold=True)
bio.label(ax, (10.6, 6.1), "microbial loop", size="small", bold=True, color=P.edge("bacterium"))
