"""The four classes of the traditional phylum "Protozoa" (Chinese and older Western textbooks) and where their
representatives belong in the modern classification of eukaryotes (Adl et al. 2019; Burki et al. 2020).

Left: classes, defined by the organelles of locomotion (flagella, pseudopodia, none in the adult, cilia).
Middle: representative genera. Right: the supergroups and lineages to which they belong. Each traditional
class is spread over several supergroups, and some former protozoa are not protists at all: microsporidia
are fungi and myxosporeans are highly reduced parasitic cnidarians, that is, animals.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 15.6)
CLS = [("Flagellates\n(Mastigophora)", "dna", 12.6), ("Amoebae\n(Sarcodina)", "lipid", 7.8),
       ("Sporozoans\n(Sporozoa)", "negative", 4.5), ("Ciliates\n(Ciliata)", "positive", 1.6)]
GRP = {"Discoba": 14.6, "Metamonada": 13.2, "Archaeplastida": 11.8, "SAR: Alveolata": 9.0,
       "SAR: Stramenopiles": 7.0, "SAR: Rhizaria": 5.6, "Amoebozoa": 4.2, "Opisthokonta: Fungi": 2.8,
       "Opisthokonta: Choanozoa": 1.6, "Opisthokonta: Metazoa (Cnidaria)": 0.55}
GEN = [  # genus, class index, group, y
    ("Euglena", 0, "Discoba", 14.8), ("Trypanosoma, Leishmania", 0, "Discoba", 14.2),
    ("Giardia, Trichomonas", 0, "Metamonada", 13.6), ("Trichonympha", 0, "Metamonada", 13.0),
    ("Volvox, Chlamydomonas", 0, "Archaeplastida", 12.4), ("Noctiluca, Ceratium", 0, "SAR: Alveolata", 11.8),
    ("Choanoflagellates", 0, "Opisthokonta: Choanozoa", 11.2),
    ("Amoeba, Entamoeba", 1, "Amoebozoa", 9.6), ("Arcella, Difflugia", 1, "Amoebozoa", 9.0),
    ("Foraminifera", 1, "SAR: Rhizaria", 8.4), ("Radiolaria", 1, "SAR: Rhizaria", 7.8),
    ("Actinophrys", 1, "SAR: Stramenopiles", 7.2),
    ("Plasmodium, Eimeria", 2, "SAR: Alveolata", 5.6), ("Microsporidia", 2, "Opisthokonta: Fungi", 5.0),
    ("Myxosporidia", 2, "Opisthokonta: Metazoa (Cnidaria)", 4.4),
    ("Paramecium, Vorticella, Stentor", 3, "SAR: Alveolata", 2.2), ("Ichthyophthirius, Trichodina", 3, "SAR: Alveolata", 1.6),
]
for name, tok, y in CLS:
    bio.box(ax, (2.2, y), 3.6, 1.4, token=tok, text=name, size="small")
GTOK = {"Discoba": "neutral", "Metamonada": "neutral", "Archaeplastida": "plant", "SAR: Alveolata": "positive",
        "SAR: Stramenopiles": "positive", "SAR: Rhizaria": "positive", "Amoebozoa": "lipid",
        "Opisthokonta: Fungi": "dna", "Opisthokonta: Choanozoa": "dna", "Opisthokonta: Metazoa (Cnidaria)": "dna"}
for g, y in GRP.items():
    bio.box(ax, (21.6, y), 6.4, 0.9, token=GTOK[g], text=g, size="small")
for name, ci, g, y in GEN:
    tok, yc = CLS[ci][1], CLS[ci][2]
    bio.arrow(ax, (4.0, yc), (8.0, y), kind="link", color=P.edge(tok), lw=0.8)
    bio.label(ax, (8.2, y), name, size="small", ha="left", italic=name.split()[0] not in ("Foraminifera", "Radiolaria", "Choanoflagellates", "Microsporidia", "Myxosporidia"))
    bio.arrow(ax, (13.6, y), (18.4, GRP[g]), kind="process", color=P.muted(), lw=0.8)
bio.label(ax, (2.2, 15.3), "Traditional class", size="small", bold=True)
bio.label(ax, (10.0, 15.3), "Representatives", size="small", bold=True)
bio.label(ax, (21.6, 15.3), "Modern placement", size="small", bold=True)
