"""Traditional body-plan grades mapped onto the current animal phylogeny (cladogram after Laumer et al.
2019 and the summary in 7.17.6; the position of Xenacoelomorpha and the root are uncertain).

For each phylum the adult body cavity is shown as a small cross-section coloured by germ layer: none
(sponges, placozoans), diploblastic with only a gut, acoelomate, pseudocoelomate (blastocoelomate) or
coelomate; "hemocoel" marks phyla whose main body cavity is a blood space with the coelom reduced.
Acoelomate, blastocoelomate and coelomate phyla are interspersed on the tree: none of these grades is a
clade, and body cavities were gained, reduced or lost several times.
"""

import wikibio as bio
from wikibio import phylo
from wikibio import zoology as zoo

P = bio.P
NEWICK = ("(Porifera,Ctenophora,(Placozoa,(Cnidaria,(Xenacoelomorpha,"
          "((Echinodermata,Hemichordata),Chordata)Deuterostomia,"
          "((Nematoda,Priapulida,(Tardigrada,Arthropoda)),"
          "((Platyhelminthes,Gastrotricha),Rotifera,(Mollusca,Annelida,Brachiopoda,Nemertea)))Protostomia)Bilateria)));")
CAV = {"Porifera": None, "Ctenophora": "diploblast", "Placozoa": None, "Cnidaria": "diploblast",
       "Xenacoelomorpha": "acoelomate", "Echinodermata": "coelomate", "Hemichordata": "coelomate",
       "Chordata": "coelomate", "Nematoda": "pseudocoelomate", "Priapulida": "pseudocoelomate",
       "Tardigrada": "hemocoel", "Arthropoda": "hemocoel", "Platyhelminthes": "acoelomate",
       "Gastrotricha": "acoelomate", "Rotifera": "pseudocoelomate", "Mollusca": "hemocoel",
       "Annelida": "coelomate", "Brachiopoda": "coelomate", "Nemertea": "acoelomate"}
NOTE = {None: "no body cavity, no germ layers", "diploblast": "diploblastic: gut only", "acoelomate": "acoelomate",
        "pseudocoelomate": "blastocoelomate (pseudocoel)", "coelomate": "coelomate",
        "hemocoel": "hemocoel; coelom reduced"}
EXTRA = {"Nemertea": " (coelomic rhynchocoel)", "Mollusca": " (pericardium)", "Arthropoda": " (gonads, nephridia)"}
fig, ax = bio.canvas(22.0, 13.6)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.8), width=6.4, height=12.0, direction="right", root_edge=0.3,
               label_size="small", align=True,
               clades=[dict(node="Deuterostomia", token="dna", style="bar", label="Deuterostomia"),
                       dict(node="Protostomia", token="positive", style="bar", label="Protostomia")])
xc = 14.4
bio.label(ax, (xc, 13.3), "Adult body cavity", size="small", bold=True)
for name, kind in CAV.items():
    y = t.node(name).xy[1]
    if kind in (None, "hemocoel"):
        pass
    else:
        zoo.body_plan(ax, (xc, y), 0.25, kind, zorder=8)
    bio.label(ax, (xc + 0.55, y), NOTE[kind] + EXTRA.get(name, ""), size="tiny", ha="left")
zoo.germ_layer_legend(ax, (12.0, 0.3), cavities=(), step=2.6)
