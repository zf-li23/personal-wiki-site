# Glycans in the Symbol Nomenclature for Glycans (SNFG). A: the symbol key: shape = class of monosaccharide
# (hexose circle, N-acetylhexosamine square, hexosamine divided square, hexuronate divided diamond,
# deoxyhexose triangle, pentose star, sialic acid diamond, muramic acid flat hexagon, ketohexose pentagon),
# colour = stereochemistry (gluco blue, manno green, galacto yellow, ido brown, ...). B: the three classes of
# N-glycans on Asn, all sharing the core Man3GlcNAc2: high-mannose (Man9GlcNAc2), hybrid, and complex
# (biantennary, disialylated, core-fucosylated). C: mucin-type O-glycan cores 1-4 on Ser/Thr. D: blood-group
# antigens H (type O), A and B, and sialyl Lewis x, the ligand of the selectins. Linkage labels give the
# anomeric configuration and the two carbons joined (b1-4 = beta, C-1 of the residue to C-4 of its parent).
import wikibio as bio
from wikibio import glycan as G

fig, ax = bio.canvas(25.0, 14.6)

# --- A: symbol key ----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 14.5))
bio.label(ax, (0.9, 14.15), "SNFG symbols", bold=True, ha="left")
key = ["Glc", "Man", "Gal", "GlcNAc", "GalNAc", "GlcN", "GlcA", "IdoA", "Fuc", "Xyl", "Neu5Ac", "Neu5Gc", "MurNAc", "Fru"]
G.legend(ax, (1.1, 13.3), key, cols=1, dy=0.86)

# --- B: N-glycans -------------------------------------------------------------------------------------
bio.panel(ax, "B", (4.2, 14.5))
bio.label(ax, (5.0, 14.15), "N-glycans (on Asn)", bold=True, ha="left")
for (kind, title), x in zip((("high-mannose", "High-mannose"), ("hybrid", "Hybrid"), ("complex", "Complex")), (10.4, 16.4, 23.4)):
    g = G.n_glycan(ax, (x, 10.6), kind=kind, step=1.05, row=0.95, size=0.46)
    x0, y0, x1, y1 = g.bounds()
    bio.label(ax, ((x0 + x1) / 2, 13.55), title, size="normal", ha="center")

# --- C: O-glycan cores ------------------------------------------------------------------------------------
bio.panel(ax, "C", (4.2, 7.0))
bio.label(ax, (5.0, 6.65), "O-glycan cores (on Ser/Thr)", bold=True, ha="left")
for k, core in enumerate((1, 2, 3, 4)):
    x = 6.9 + k * 2.9
    G.o_glycan(ax, (x, 4.6), core=core, direction="up", step=1.05, row=1.0, size=0.46)
    bio.label(ax, (x, 2.9), f"Core {core}", size="small")
G.o_glycan(ax, (6.9, 1.2), core="Tn", direction="right", step=1.05, size=0.46)
bio.label(ax, (7.9, 1.2), "Tn antigen", size="small", ha="left")

# --- D: blood groups and sialyl Lewis x ------------------------------------------------------------------
bio.panel(ax, "D", (17.0, 7.0))
bio.label(ax, (17.8, 6.65), "Blood-group and selectin ligands", bold=True, ha="left")
for k, (kind, name) in enumerate((("H", "H (type O)"), ("A", "A"), ("B", "B"))):
    y = 5.75 - k * 1.62
    G.abo(ax, (22.0, y), kind=kind, step=1.05, row=0.8, size=0.46, aglycone="R")
    bio.label(ax, (17.6, y), name, size="small", ha="left")
G.lewis(ax, (22.0, 0.85), kind="sLex", step=1.05, row=0.8, size=0.46, aglycone="R", labels="short")
bio.label(ax, (17.6, 0.85), "sialyl Lewis x", size="small", ha="left")
