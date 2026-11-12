# Two hypotheses of chelicerate relationships. A: the traditional tree, in which the terrestrial
# arachnids form a clade (Arachnida) and the marine horseshoe crabs (Xiphosura) are their sister group.
# B: many phylogenomic analyses (e.g. Ballesteros and Sharma 2019) place Xiphosura among the arachnid
# orders, which would make Arachnida paraphyletic and imply either several invasions of land or a return
# to the sea; analyses that remove fast-evolving genes and taxa recover Arachnida (Lozano-Fernandez et al.
# 2019). Arachnopulmonata (scorpions plus the tetrapulmonates: spiders, whip spiders, whip scorpions) is
# supported in both. Sea spiders (Pycnogonida) are the sister group of all other chelicerates.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 10)
icons = {"Pycnogonida": "phylopic/sea-spider", "Xiphosura": "phylopic/horseshoe-crab",
         "Acariformes": "phylopic/mite", "Parasitiformes": "phylopic/tick", "Opiliones": "phylopic/harvestman",
         "Pseudoscorpiones": "phylopic/pseudoscorpion", "Scorpiones": "phylopic/scorpion", "Araneae": "phylopic/spider"}
a = "(Pycnogonida,(Xiphosura,(Opiliones,Acariformes,Parasitiformes,Pseudoscorpiones,(Scorpiones,Araneae)Arachnopulmonata)Arachnida)Euchelicerata);"
b = "(Pycnogonida,(Opiliones,Acariformes,Parasitiformes,Pseudoscorpiones,Xiphosura,(Scorpiones,Araneae)Arachnopulmonata)Euchelicerata);"
for nwk, x0, letter, title, cl in ((a, 0.8, "A", "Arachnida monophyletic", [dict(node="Arachnida", token="plant", style="bar", label="Arachnida")]),
                                   (b, 12.8, "B", "Xiphosura nested among arachnids", [])):
    bio.panel(ax, letter, (x0 - 0.5, 9.9))
    bio.label(ax, (x0 + 0.3, 9.6), title, size="normal", bold=True, ha="left")
    phylo.tree(ax, nwk, origin=(x0, 1.0), width=5.0, height=7.8, root_edge=0.4, icons=icons, icon_size=0.6,
               icon_color="animal", label_size="small",
               clades=cl + [dict(node="Arachnopulmonata", token="blood", style="branch")],
               marks=[dict(node="Arachnopulmonata", kind="trait", text="book lungs", at=0.5)])
