# Independent colonizations of land by panarthropods (stars) and the land adaptations of each lineage,
# mapped on the phylogeny of BG 4e. Onychophorans, arachnids (once or more; see 7.17.19), myriapods,
# hexapods and, within Malacostraca, woodlice and land crabs each moved onto land separately; their
# tracheae and Malpighian tubules are convergent (tracheae of four kinds; tubules endodermal in arachnids,
# ectodermal in myriapods and hexapods).
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(22, 10.5)
nwk = ("(Onychophora,((Pycnogonida,Xiphosura,Arachnida)Chelicerata,(Myriapoda,('Other crustaceans',Malacostraca,"
       "(Remipedia,Hexapoda))Pancrustacea)Mandibulata)Arthropoda);")
t = phylo.tree(ax, nwk, origin=(0.8, 1.0), width=7.5, height=8.4, root_edge=0.4, label_size="small",
               icons={"Onychophora": "phylopic/velvet-worm", "Pycnogonida": "phylopic/sea-spider",
                      "Xiphosura": "phylopic/horseshoe-crab", "Arachnida": "phylopic/scorpion",
                      "Myriapoda": "phylopic/centipede", "Other crustaceans": "phylopic/copepod",
                      "Malacostraca": "phylopic/woodlouse", "Remipedia": "phylopic/remipede", "Hexapoda": "phylopic/honey-bee"},
               icon_size=0.6, icon_color="animal",
               marks=[dict(node=n, kind="star", token="highlight", at=0.6) for n in
                      ("Onychophora", "Arachnida", "Myriapoda", "Malacostraca", "Hexapoda")])
notes = {"Onychophora": "unbranched tracheae, many open spiracles; nephridia",
         "Pycnogonida": "marine",
         "Xiphosura": "marine (book gills)",
         "Arachnida": "book lungs, sieve and tube tracheae; endodermal Malpighian tubules; guanine",
         "Myriapoda": "tracheae; ectodermal Malpighian tubules; little wax",
         "Other crustaceans": "aquatic; gills; antennal or maxillary glands",
         "Malacostraca": "woodlice: pleopodal lungs; land crabs: branchial chambers",
         "Remipedia": "marine caves",
         "Hexapoda": "tracheae with closable spiracles; ectodermal Malpighian tubules; wax layer"}
for tip, txt in notes.items():
    x, y = t.node(tip).xy
    bio.label(ax, (13.0, y), txt, size="tiny", ha="left")
phylo.legend(ax, (1.2, 0.4), [("star", "colonization of land", "highlight")])
