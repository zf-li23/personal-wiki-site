"""Glycoconjugate oligosaccharides drawn in the Symbol Nomenclature for Glycans (SNFG).
A: symbol key. B: N-linked glycans on Asn (high-mannose Man9GlcNAc2 and a complex biantennary,
disialylated, core-fucosylated glycan); both share the core Man3GlcNAc2. C: an O-linked mucin core 1
glycan with sialic acids on Ser/Thr, and the tetrasaccharide linker by which glycosaminoglycans
(here chondroitin sulfate repeats) are attached to the core protein of a proteoglycan.
D: blood-group antigens H, A and B on a type 2 chain, sialyl Lewis x, the ligand of the selectins."""

import wikibio as bio
from wikibio import glycan as G

fig, ax = bio.canvas(24.5, 13.6)
S = dict(step=1.05, row=0.95, size=0.46)

bio.panel(ax, "A", (0.1, 13.5))
bio.label(ax, (0.9, 13.15), "Symbols", bold=True, ha="left")
G.legend(ax, (1.1, 12.3), ["Glc", "Gal", "Man", "GlcNAc", "GalNAc", "Fuc", "Neu5Ac", "Xyl", "GlcA"], dy=0.9)

bio.panel(ax, "B", (4.0, 13.5))
bio.label(ax, (4.8, 13.15), "N-linked (Asn–X–Ser/Thr)", bold=True, ha="left")
g = G.n_glycan(ax, (10.6, 10.2), kind="high-mannose", **S)
bio.label(ax, (7.3, 12.45), "High-mannose", size="normal")
g = G.n_glycan(ax, (22.9, 10.2), kind="complex", **S)
bio.label(ax, (18.4, 12.45), "Complex (sialylated)", size="normal")
bio.label(ax, (23.35, 9.35), "core Fuc", size="tiny", color=bio.P.muted(), ha="left")

bio.panel(ax, "C", (4.0, 7.2))
bio.label(ax, (4.8, 6.85), "O-linked and proteoglycan linkage", bold=True, ha="left")
G.draw(ax, "Neu5Ac(a2-3)Gal(b1-3)[Neu5Ac(a2-6)]GalNAc(a1-", at=(8.6, 5.0), aglycone="Ser/Thr", **S)
bio.label(ax, (6.9, 3.6), "Sialylated core 1 (mucins)", size="small")
G.draw(ax, "GalNAc(b1-4)GlcA(b1-3)GalNAc(b1-4)GlcA(b1-3)Gal(b1-3)Gal(b1-4)Xyl(b1-", at=(14.0, 2.1), aglycone="Ser",
       labels="short", **S)
bio.label(ax, (8.75, 1.05), "chondroitin repeats", size="small")
bio.label(ax, (12.4, 1.05), "tetrasaccharide linker", size="small")
ax.plot([7.4, 10.15], [1.45, 1.45], color=bio.P.muted(), lw=0.8)
ax.plot([10.55, 14.3], [1.45, 1.45], color=bio.P.muted(), lw=0.8)

bio.panel(ax, "D", (16.0, 7.2))
bio.label(ax, (16.8, 6.85), "Recognition determinants", bold=True, ha="left")
rows = [("H", "H (group O)"), ("A", "A"), ("B", "B")]
for k, (kind, name) in enumerate(rows):
    y = 5.9 - k * 1.55
    G.abo(ax, (22.6, y), kind=kind, row=0.75, step=1.05, size=0.46, labels="short")
    bio.label(ax, (16.4, y), name, size="small", ha="left")
G.lewis(ax, (22.6, 1.05), kind="sLex", row=0.75, step=1.05, size=0.46, labels="short")
bio.label(ax, (16.4, 1.05), "sialyl Lewis x", size="small", ha="left")
