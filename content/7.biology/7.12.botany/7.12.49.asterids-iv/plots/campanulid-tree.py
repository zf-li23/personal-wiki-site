# Relationships of the campanulids at order level (APG IV; Tank & Donoghue 2010; unresolved parts drawn as
# polytomies), with approximate species numbers. Marks: 1 campanulids (alternate leaves, inferior ovary,
# late sympetaly, polyacetylenes); 2 Aquifoliales (stipules, unisexual flowers, drupes); 3 Asterales (inulin,
# secondary pollen presentation); 4 Dipsacales (opposite leaves); 5 Apiales (umbels, epigynous disc,
# secretory canals).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = "(Aquifoliales,(Asterales,Escalloniales,Bruniales,(Apiales,(Paracryphiales,Dipsacales)ADP)))Campanulids;"
TXT = {"Aquifoliales": "Aquifoliales (c. 600 spp.)", "Asterales": "Asterales (c. 27 000; Asteraceae c. 25 000)",
       "Escalloniales": "Escalloniales (c. 130)", "Bruniales": "Bruniales (c. 80)", "Apiales": "Apiales (c. 5 500)",
       "Paracryphiales": "Paracryphiales (c. 35)", "Dipsacales": "Dipsacales (c. 1 100)"}
fig, ax = bio.canvas(28, 11)
phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=10.0, height=8.6, label_size="small", root_edge=0.5, tip_text=TXT,
           icons={"Asterales": "phylopic/asteraceae"},
           marks=[dict(node="Campanulids", kind="star", at=0.5, token="highlight", text="1"),
                  dict(node="Aquifoliales", kind="trait", at=0.5, token="plant", text="2"),
                  dict(node="Asterales", kind="trait", at=0.5, token="petal", text="3"),
                  dict(node="Dipsacales", kind="trait", at=0.5, token="rna", text="4"),
                  dict(node="Apiales", kind="trait", at=0.5, token="dna", text="5")])
KEY = ["1  Alternate leaves, inferior ovary, late sympetaly", "2  Stipules, unisexual flowers, drupes",
       "3  Inulin; secondary pollen presentation", "4  Opposite leaves", "5  Umbels, epigynous disc, secretory canals"]
for i, k in enumerate(KEY):
    bio.label(ax, (20.0, 9.6 - i * 0.8), k, size="small", ha="left")
