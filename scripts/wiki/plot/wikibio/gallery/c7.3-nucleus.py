# The nucleus module: envelope section with NPCs, ER continuity, lamina and a LINC complex; NPC face view;
# karyopherins, Ran and cargo; chromosome territories with a tripartite nucleolus; polytene and lampbrush chromosomes
import wikibio as bio
from wikibio import nuclear as N

fig, ax = bio.canvas(16, 8.6)
bio.panel(ax, "A", (0.1, 8.5))
env = N.envelope(ax, 0.3, 10.3, 5.2, gap=0.5, pores=[3.6, 7.6], pore_width=1.4, er=1.4, er_height=1.7, tint=(2.6, 2.4))
N.linc(ax, 5.6, env, reach=1.2)
p = env["pores"][1]
bio.callout(ax, p["filaments"][-1], (9.0, 7.6), "Cytoplasmic filaments")
bio.callout(ax, p["basket"], (9.4, 3.2), "Nuclear basket")
bio.callout(ax, (7.6, 5.2), (9.5, 4.3), "FG mesh")
bio.callout(ax, (5.0, 5.2), (5.0, 6.9), "Perinuclear space")
bio.callout(ax, (5.66, 6.7), (6.6, 7.6), "LINC (nesprin)")
bio.callout(ax, (1.4, 6.8), (2.2, 7.9), "ER")
bio.callout(ax, (2.3, 4.45), (2.3, 3.4), "Lamina")

bio.panel(ax, "B", (10.8, 8.5))
N.pore_top(ax, (13.2, 6.5), 1.1)
bio.label(ax, (13.2, 4.8), "NPC face view (eightfold)", size="small")
imp = N.karyopherin(ax, (11.8, 2.8), 0.5, kind="importin", angle=0, text="Importin β")
N.cargo(ax, (12.2, 2.8), 0.22, signal="NLS", angle=180)
N.karyopherin(ax, (14.4, 2.8), 0.5, kind="exportin", angle=0, text="Exportin")
N.ran(ax, (14.75, 3.05), "GTP")
N.cargo(ax, (14.75, 2.55), 0.18, signal="NES", angle=180)
N.ran(ax, (12.4, 1.0), "GDP")
bio.label(ax, (12.8, 1.0), "Ran·GDP", size="tiny", ha="left")
N.ran(ax, (14.0, 1.0), "GTP")
bio.label(ax, (14.4, 1.0), "Ran·GTP", size="tiny", ha="left")

fig2, ax2 = bio.canvas(16, 7.4)
bio.panel(ax2, "C", (0.1, 7.3))
t = N.territories(ax2, (3.8, 3.7), 3.3, 2.9, n=14, seed=3, highlight={2: "dna", 9: "receptor"}, nucleoli=[(4.6, 3.2, 0.8)])
N.nucleolus(ax2, (4.6, 3.2), 0.8, units=3)
bio.panel(ax2, "D", (8.0, 7.3))
nl = N.nucleolus(ax2, (10.0, 4.5), 1.8, units=4, seed=7)
u = nl["units"][0]
bio.callout(ax2, u[0], (12.8, 6.6), "Fibrillar centre")
bio.callout(ax2, (u[0][0] + u[2] * 0.9, u[0][1]), (12.8, 6.0), "Dense fibrillar component")
bio.callout(ax2, (11.5, 3.4), (12.8, 2.8), "Granular component")
bio.panel(ax2, "E", (8.0, 2.4))
N.polytene(ax2, 8.4, 15.6, 1.75, 0.55, puff=0.55, puff_width=1.0)
N.lampbrush(ax2, 8.6, 15.4, 0.6, loops=6, loop_height=0.45)
