# Relationships of the eight ecdysozoan phyla. Scalidophora (introvert with scalids), Nematoida
# (nematodes and horsehair worms) and Panarthropoda (paired, clawed limbs) are well supported by
# morphology, but their mutual relationships are unresolved (polytomy) and Scalidophora is not always
# recovered by molecular data. Synapomorphies of Ecdysozoa: a molted three-layered cuticle and the loss of
# locomotory cilia.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(19, 11)
nwk = "((Priapulida,(Kinorhyncha,Loricifera))Scalidophora,(Nematoda,Nematomorpha)Nematoida,(Tardigrada,(Onychophora,Arthropoda))Panarthropoda)Ecdysozoa;"
t = phylo.tree(ax, nwk, origin=(1.0, 1.0), width=9.5, height=9.0, root_edge=0.6,
               icons={"Priapulida": "phylopic/priapulid", "Kinorhyncha": "phylopic/kinorhynch",
                      "Nematoda": "phylopic/c-elegans", "Nematomorpha": "phylopic/horsehair-worm",
                      "Tardigrada": "phylopic/tardigrade", "Onychophora": "phylopic/velvet-worm",
                      "Arthropoda": "phylopic/trilobite"},
               icon_size=0.75, icon_color="animal",
               clades=[dict(node="Scalidophora", token="rna", style="bar", label="Scalidophora"),
                       dict(node="Nematoida", token="dna", style="bar", label="Nematoida"),
                       dict(node="Panarthropoda", token="plant", style="bar", label="Panarthropoda")],
               marks=[dict(node="Ecdysozoa", kind="trait", text="molted cuticle,\nno motile cilia", at=0.5),
                      dict(node="Scalidophora", kind="trait", text="introvert with scalids"),
                      dict(node="Nematoida", kind="trait", text="only longitudinal muscle"),
                      dict(node="Panarthropoda", kind="trait", text="paired clawed limbs")])
