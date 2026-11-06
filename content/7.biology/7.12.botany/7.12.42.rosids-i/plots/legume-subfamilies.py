# Phylogeny of the six legume subfamilies (LPWG 2017) and the three traditional families. Coloured bars:
# traditional Caesalpiniaceae (paraphyletic, spread over five subfamilies), Mimosaceae (the mimosoid clade
# nested in Caesalpinioideae) and Papilionaceae. Dots: clades in which root nodules are widespread.
import wikibio as bio
from wikibio import phylo

NEWICK = ("(Polygalaceae,(Cercidoideae,(Detarioideae,(Duparquetioideae,(Dialioideae,"
          "((Caesalpinioids,Mimosoids)Caesalpinioideae,Papilionoideae))))))Fabales;")
fig, ax = bio.canvas(30, 12)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=11.0, height=10.0, label_size="normal", root_edge=0.4,
               tip_text={"Polygalaceae": "Polygalaceae and other Fabales",
                         "Caesalpinioids": "Caesalpinioideae: non-mimosoid genera",
                         "Mimosoids": "Caesalpinioideae: mimosoid clade"},
               clades=[dict(tips=["Cercidoideae"], token="petal", style="branch"),
                       dict(tips=["Detarioideae"], token="petal", style="branch"),
                       dict(tips=["Duparquetioideae"], token="petal", style="branch"),
                       dict(tips=["Dialioideae"], token="petal", style="branch"),
                       dict(tips=["Caesalpinioids"], token="petal", style="branch"),
                       dict(tips=["Mimosoids"], token="anther", style="branch"),
                       dict(tips=["Papilionoideae"], token="dna", style="branch")],
               marks=[dict(node=["Mimosoids"], kind="dot", at=0.5, token="positive", size=0.3),
                      dict(node=["Papilionoideae"], kind="dot", at=0.5, token="positive", size=0.3)])
for i, (tok, txt) in enumerate([("petal", "Traditional Caesalpiniaceae (paraphyletic)"),
                                ("anther", "Traditional Mimosaceae"),
                                ("dna", "Traditional Papilionaceae")]):
    phylo.marker(ax, (22.0, 11.0 - i * 0.9), "line", tok)
    bio.label(ax, (22.6, 11.0 - i * 0.9), txt, size="small", ha="left")
phylo.marker(ax, (22.0, 8.3), "dot", "positive", size=0.3)
bio.label(ax, (22.6, 8.3), "Root nodules widespread", size="small", ha="left")
