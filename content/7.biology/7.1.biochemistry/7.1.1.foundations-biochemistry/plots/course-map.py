# Course map: the structural hierarchy of the cell (monomeric units -> macromolecules ->
# supramolecular complexes -> cell), with the chapters of the course placed under the level they
# deal with, and the two threads of the course: Part I (structure) and Part II (metabolism).
import numpy as np
import wikibio as bio

fig, ax = bio.canvas(21, 11.4)
cols = [2.6, 7.9, 13.2, 18.4]
titles = ["Monomeric units", "Macromolecules", "Supramolecular\ncomplexes", "Cells and organelles"]
for x, t in zip(cols, titles):
    bio.label(ax, (x, 10.7), t, size="normal", bold=True)
for x0, x1 in zip(cols[:-1], cols[1:]):
    bio.arrow(ax, (x0 + 1.9, 8.4), (x1 - 1.9, 8.4), kind="process")

# monomeric units
y = 8.4
bio.molecule(ax, (1.6, 9.2), "protein", "aa", r=0.34)
bio.molecule(ax, (3.5, 9.2), "dna", "nt", r=0.34)
bio.molecule(ax, (1.6, 7.6), "carbohydrate", "sugar", r=0.42, size="tiny")
bio.molecule(ax, (3.5, 7.6), "lipid", "FA", r=0.34)
bio.molecule(ax, (2.55, 8.4), "h", "H$_2$O", r=0.3, size="tiny")

# macromolecules
bio.protein(ax, (6.9, 9.2), 1.5, 1.0, "protein", text="protein")
bio.dna(ax, (7.4, 7.55), (9.6, 7.55), style="helix", width=0.5, ends=False)
for i in range(6):
    bio.molecule(ax, (8.0 + 0.32 * i, 9.25 + 0.1 * np.sin(i)), "carbohydrate", r=0.15)
bio.label(ax, (8.8, 9.75), "polysaccharide", size="tiny")
bio.label(ax, (6.6, 7.55), "DNA", size="tiny")

# supramolecular complexes
bio.bilayer(ax, [(11.7, 7.5), (14.8, 7.5)])
bio.protein(ax, (13.9, 7.5), 0.7, 1.3, "receptor", wobble=0.05)
bio.ribosome(ax, (12.3, 9.25), size=0.9)
bio.label(ax, (12.3, 9.95), "ribosome", size="tiny")
bio.label(ax, (14.0, 9.1), "membrane", size="tiny")

# cell
bio.cell(ax, (18.4, 8.4), 2.0, 1.45, kind="animal")
bio.nucleus(ax, (17.9, 8.6), 0.65)
bio.mitochondrion(ax, (19.4, 7.9), 1.0, 0.42, angle=25, cristae=4)

chapters = [
    ["7.1.2  Water, weak interactions", "7.1.3  Amino acids, peptides"],
    ["7.1.4  Working with proteins", "7.1.5–7.1.6  Structure, folding", "7.1.7  Protein function",
     "7.1.8–7.1.9  Enzymes", "7.1.10  Carbohydrates", "7.1.11  Nucleic acids"],
    ["7.1.12  Lipids", "7.1.13  Membranes, transport", "7.1.14–7.1.15  Signaling"],
    ["7.1.16–7.1.17  Bioenergetics, logic", "7.1.18–7.1.22  Fuel pathways", "7.1.23–7.1.24  ATP synthesis",
     "7.1.25–7.1.28  Biosynthesis", "7.1.29  Integration", "7.1.30  Summary"],
]
for x, chs in zip(cols, chapters):
    for k, c in enumerate(chs):
        bio.label(ax, (x - 2.2, 5.9 - 0.52 * k), c, size="tiny", ha="left")

bio.box(ax, (7.9, 1.75), 13.6, 0.85, "protein", text="Part I  Structure: chemical properties  →  structure  →  function",
        size="small")
bio.box(ax, (18.4, 1.75), 5.0, 0.85, "atp", text="Part II  Metabolism", size="small")
bio.label(ax, (18.4, 0.85), "energy balance + feedback control", size="tiny")
bio.label(ax, (7.9, 0.85), "weak interactions and side-chain chemistry decide shape; shape decides binding, catalysis, signaling",
          size="tiny")
