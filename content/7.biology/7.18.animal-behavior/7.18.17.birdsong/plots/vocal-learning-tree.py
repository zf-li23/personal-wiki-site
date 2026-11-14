# Vocal learning mapped on the phylogeny of modern birds (topology after Jarvis et al. 2014 and Prum et al. 2015,
# simplified; not to scale). Parrots are the sister group of passerines, and falcons the sister of both.
# Vocal learners (bands): hummingbirds, parrots, oscine songbirds; within the suboscines at least the
# bellbirds (Procnias) learn (Kroodsma et al. 2013). Two equally parsimonious scenarios: (1) three
# independent gains (hummingbirds, parrots, oscines); (2) two gains (hummingbirds; the common ancestor of
# parrots and passerines) and losses in suboscines and New Zealand wrens (Acanthisitti).
import wikibio as bio
from wikibio import phylo

P = bio.P
PASS = "(NZ_wrens,(Suboscines,Oscines)Eupasseres)Passeriformes"
TELL = "((Owls,(Eagles,Woodpeckers)),(Falcons,(Parrots," + PASS + ")Psittacopasserae)Australaves)Telluraves"
NEOAVES = "(Pigeons,((Nightjars,(Swifts,Hummingbirds)Apodiformes)Strisores,(Cranes,(Herons," + TELL + "))))Neoaves"
NEWICK = "((Ostrich,Chicken)," + NEOAVES + ")Neornithes;"
ICONS = {"Ostrich": "phylopic/ostrich", "Chicken": "phylopic/chicken", "Pigeons": "phylopic/pigeon",
         "Nightjars": "phylopic/nightjar", "Swifts": "phylopic/swift", "Hummingbirds": "phylopic/hummingbird",
         "Cranes": "phylopic/crane", "Herons": "phylopic/heron", "Owls": "phylopic/owl", "Eagles": "phylopic/eagle",
         "Woodpeckers": "phylopic/woodpecker", "Falcons": "phylopic/falcon", "Parrots": "phylopic/parrot",
         "Suboscines": "phylopic/sparrow", "Oscines": "phylopic/zebra-finch"}
TEXT = {"NZ wrens": "New Zealand wrens", "Suboscines": "Suboscines (bellbirds learn)", "Oscines": "Oscine songbirds"}
MARKS = [
    dict(node="Hummingbirds", kind="trait", at=0.5, text="gain", side=1, text_size="tiny"),
    dict(node="Parrots", kind="trait", at=0.5, text="gain (1)", side=1, text_size="tiny"),
    dict(node="Oscines", kind="trait", at=0.5, text="gain (1)", side=1, text_size="tiny"),
    dict(node="Psittacopasserae", kind="trait", at=0.5, text="gain (2)", side=-1, text_size="tiny"),
    dict(node="Suboscines", kind="loss", at=0.5, text="loss (2)", side=1, text_size="tiny"),
    dict(node="NZ wrens", kind="loss", at=0.5, text="loss (2)", side=1, text_size="tiny"),
]
fig, ax = bio.canvas(21, 12.6)
t = phylo.tree(ax, NEWICK, origin=(0.8, 1.6), width=10.0, height=10.4, direction="right", root_edge=0.3,
               tip_text=TEXT, icons=ICONS, icon_size=0.55, icon_width=0.9, label_size="small", marks=MARKS,
               clades=[dict(tips=["Hummingbirds"], token="highlight", style="band"),
                       dict(tips=["Parrots"], token="highlight", style="band"),
                       dict(tips=["Oscines"], token="highlight", style="band")])
x0, y0 = 0.8, 0.8
phylo.marker(ax, (x0 + 0.12, y0), "trait", size=0.14, direction=(1, 0))
bio.label(ax, (x0 + 0.4, y0), "gain of vocal learning", size="tiny", ha="left")
phylo.marker(ax, (x0 + 5.2, y0), "loss", size=0.14, direction=(1, 0))
bio.label(ax, (x0 + 5.5, y0), "loss", size="tiny", ha="left")
bio.label(ax, (x0 + 7.6, y0), "(1) three gains   (2) two gains, two losses   shaded: vocal learners", size="tiny", ha="left")
