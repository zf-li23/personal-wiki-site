# The two layers of plant innate immunity (after Jones and Dangl 2006 and later models).
# Left (PTI): the bacterial MAMP flg22 binds the LRR receptor kinase FLS2, which recruits the co-receptor BAK1;
# the receptor-like cytoplasmic kinase BIK1 is released and phosphorylates the NADPH oxidase RBOHD (apoplastic
# ROS burst) and Ca2+-permeable channels (CNGC2/4; OSCA1.3 in guard cells); Ca2+ activates CPKs, and a MAPK
# cascade (MPK3/6) activates WRKY transcription factors and defence genes.
# Right (ETI): a type III secretion system injects effectors; some suppress PTI (for example by targeting BIK1
# or the receptor complex: effector-triggered susceptibility); an intracellular NLR recognises one effector
# (directly or by guarding its target) and oligomerises into a resistosome, giving Ca2+ influx, transcription
# and often the hypersensitive response.
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(25.0, 13.0)
ym = 8.6
CB.sides(ax, (0.2, 24.8), ym, height=(4.0, 8.2), top="Apoplast", bottom="Plant cell cytoplasm", label_x=0.4)
bio.bilayer(ax, [(0.2, ym), (24.8, ym)])
ax.plot([12.4, 12.4], [0.5, 12.4], color=P.muted(), lw=0.8, ls=(0, (4, 4)), zorder=1)
bio.label(ax, (6.2, 12.25), "Layer 1: pattern-triggered immunity (PTI)", size="normal", bold=True)
bio.label(ax, (18.7, 12.25), "Layer 2: effector-triggered immunity (ETI)", size="normal", bold=True)

# bacterium, left
bac = bio.cell(ax, (3.2, 11.35), 1.5, 0.5, kind="bacterium")
bio.label(ax, (3.2, 11.35), "bacterium", size="tiny")
for k in range(3):
    bio.molecule(ax, (4.9 + 0.45 * k, 10.55 - 0.25 * k), token="highlight", r=0.13)
bio.label(ax, (5.9, 10.95), "flg22 (MAMP)", size="tiny", ha="left")

# FLS2 and BAK1
bio.receptor(ax, 5.6, ym, kind="rtk", token="receptor")
bio.receptor(ax, 6.4, ym, kind="rtk", token="enzyme")
bio.label(ax, (5.2, ym + 1.35), "FLS2", size="small", ha="right")
bio.label(ax, (6.85, ym + 1.35), "BAK1", size="small", ha="left")
bio.arrow(ax, (5.2, 10.2), (5.6, 9.55), kind="link")
# BIK1
bio.protein(ax, (6.9, ym - 1.75), 1.05, 0.65, "protein", text="BIK1")
bio.arrow(ax, (6.3, ym - 1.0), (6.7, ym - 1.4), kind="activation")
# RBOHD
CB.carrier(ax, 2.4, ym, open="out", token="lipid", width=1.2)
bio.label(ax, (2.4, ym - 1.0), "RBOHD", size="small", bold=True)
bio.arrow(ax, (6.35, ym - 1.85), (3.0, ym - 1.05), kind="activation", bend=-0.15)
bio.arrow(ax, (2.4, ym + 0.5), (2.4, ym + 1.0), kind="process")
bio.label(ax, (2.4, ym + 1.75), "O₂ → O₂•⁻ → H₂O₂", size="tiny")
bio.label(ax, (2.4, ym + 1.3), "ROS burst", size="tiny", bold=True)
# Ca channel
CB.channel(ax, 9.4, ym)
bio.label(ax, (9.4, ym + 1.65), "CNGC2/4", size="small", bold=True)
CB.flux(ax, 9.4, ym + 0.9, ym - 1.0, species=[("ca", 2)])
bio.arrow(ax, (7.45, ym - 1.6), (9.0, ym - 0.6), kind="activation")
# downstream
bio.box(ax, (9.6, 5.5), 2.0, 0.6, token="enzyme", text="CPKs", size="small")
bio.box(ax, (5.6, 5.5), 2.6, 0.6, token="protein", text="MAPK cascade", size="small")
bio.label(ax, (5.6, 4.95), "MPK3 / MPK6", size="tiny", color=P.muted())
bio.arrow(ax, (9.5, ym - 1.3), (9.6, 5.85), kind="activation")
bio.arrow(ax, (6.8, ym - 2.1), (5.9, 5.85), kind="activation")
# nucleus
bio.nucleus(ax, (7.4, 2.4), 1.6, pores=8, chromatin=False, nucleolus=False)
bio.label(ax, (7.4, 2.55), "WRKY TFs", size="small", bold=True)
bio.label(ax, (7.4, 2.0), "defence genes", size="tiny")
bio.arrow(ax, (5.8, 5.15), (6.6, 3.7), kind="activation")
bio.arrow(ax, (9.4, 5.15), (8.3, 3.7), kind="activation")
for i, t in enumerate(["callose deposition", "stomatal closure", "PR proteins, phytoalexins"]):
    bio.label(ax, (10.0, 2.9 - 0.55 * i), "• " + t, size="tiny", ha="left")

# ETI side: bacterium with T3SS
bio.cell(ax, (17.0, 11.1), 1.6, 0.55, kind="bacterium")
bio.label(ax, (17.0, 11.1), "pathogen", size="tiny")
ax.plot([17.0, 17.0], [10.55, ym - 0.3], color=P.edge("bacterium"), lw=3.2, solid_capstyle="round", zorder=12)
bio.label(ax, (17.25, 9.9), "type III secretion system", size="tiny", ha="left")
eff = [(16.2, 6.9), (17.0, 6.6), (17.8, 6.9)]
for e in eff:
    bio.molecule(ax, e, token="negative", r=0.2)
bio.label(ax, (18.25, 7.45), "effectors", size="small", ha="left")
bio.arrow(ax, (17.0, ym - 0.35), (17.0, 7.1), kind="process")
# effector suppresses PTI
bio.arrow(ax, (15.95, 6.85), (7.55, ym - 1.95), kind="inhibition", bend=0.12)
bio.label(ax, (12.4, 6.95), "suppression of PTI (ETS)", size="tiny", color=P.edge("negative"))
# NLR
bio.domains(ax, 18.9, 5.2, [("CC/TIR", 1.1, "receptor"), ("NB-ARC", 1.3, "enzyme"), ("LRR", 1.1, "protein")], height=0.5)
bio.label(ax, (20.65, 4.6), "NLR (R protein)", size="small", bold=True)
bio.arrow(ax, (18.0, 6.7), (19.8, 5.55), kind="link", dashed=True)
bio.label(ax, (19.35, 6.4), "recognition", size="tiny", ha="left")
# resistosome
for k in range(5):
    import math
    a = 2 * math.pi * k / 5
    bio.protein(ax, (21.6 + 0.55 * math.cos(a), 2.6 + 0.55 * math.sin(a)), 0.55, 0.55, "receptor")
bio.label(ax, (21.6, 1.45), "resistosome", size="small", bold=True)
bio.arrow(ax, (20.65, 4.85), (21.4, 3.35), kind="process")
bio.nucleus(ax, (16.4, 2.4), 1.35, pores=8, chromatin=False, nucleolus=False)
bio.label(ax, (16.4, 2.4), "transcription", size="tiny", bold=True)
bio.arrow(ax, (20.9, 2.5), (17.8, 2.5), kind="activation")
bio.label(ax, (23.1, 3.9), "Ca²⁺ influx", size="tiny")
bio.label(ax, (23.1, 3.5), "→ HR (cell death)", size="tiny")
