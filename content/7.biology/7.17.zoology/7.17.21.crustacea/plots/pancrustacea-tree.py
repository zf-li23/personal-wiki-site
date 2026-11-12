# Relationships of the crustacean lineages and the hexapods (Pancrustacea), following the classification
# of BG 4e and phylogenomic analyses. Oligostraca (ostracods, mystacocarids, fish lice, tongue worms) are
# the sister group of Altocrustacea, which divides into Multicrustacea (Malacostraca, copepods and
# thecostracans) and Allotriocarida (branchiopods, cephalocarids, remipedes and hexapods). The hexapods
# arose within the crustaceans, which are therefore paraphyletic; the remipedes (possibly with the
# cephalocarids) are their closest living relatives.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(20, 12)
nwk = ("(((Ostracoda,Mystacocarida,(Branchiura,Pentastomida)Ichthyostraca)Oligostraca,"
       "((Malacostraca,(Copepoda,Thecostraca))Multicrustacea,(Branchiopoda,(Cephalocarida,(Remipedia,Hexapoda)))Allotriocarida)Altocrustacea)Pancrustacea);")
t = phylo.tree(ax, nwk, origin=(0.8, 1.0), width=8.5, height=10.0, root_edge=0.4, label_size="small",
               icons={"Malacostraca": "phylopic/crab",
                      "Copepoda": "phylopic/copepod", "Thecostraca": "phylopic/barnacle", "Branchiopoda": "phylopic/daphnia",
                      "Remipedia": "phylopic/remipede", "Hexapoda": "phylopic/honey-bee"},
               icon_size=0.7, icon_color="animal",
               clades=[dict(node="Oligostraca", token="rna", style="bar", label="Oligostraca"),
                       dict(node="Multicrustacea", token="dna", style="bar", label="Multicrustacea"),
                       dict(node="Allotriocarida", token="plant", style="bar", label="Allotriocarida")],
               marks=[dict(node="Hexapoda", kind="trait", text="six legs, tracheae, on land", at=0.5)])
bio.label(ax, (10.5, 0.12), "Crustacea in the traditional sense = Pancrustacea minus Hexapoda (paraphyletic)", size="tiny", color=P.muted())
