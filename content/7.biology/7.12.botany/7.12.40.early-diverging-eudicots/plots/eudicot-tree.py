# Backbone of the eudicots (APG IV; Soltis et al. 2018). Ranunculales, Proteales, Trochodendrales and
# Buxales diverge successively (early-diverging eudicots); the core eudicots comprise Gunnerales and the
# Pentapetalae (Dilleniales, superrosids, superasterids; the position of Dilleniales is unresolved and drawn
# as a polytomy). Marks: tricolpate pollen; the gamma whole-genome triplication; pentamerous flowers with
# a distinct calyx and corolla.
import wikibio as bio
from wikibio import phylo

NEWICK = ("(Monocots,((Ranunculales,(Proteales,(Trochodendrales,(Buxales,(Gunnerales,"
          "(Dilleniales,Superrosids,Superasterids)Pentapetalae)Core)B3)B2)B1)Eudicots)Mesangio)Root;")
fig, ax = bio.canvas(30, 13)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=12.5, height=11.0, label_size="normal", root_edge=0.5,
               tip_text={"Monocots": "Monocots (and other mesangiosperms)", "Superrosids": "Superrosids",
                         "Superasterids": "Superasterids"},
               clades=[dict(tips=["Ranunculales"], token="petal", style="branch"),
                       dict(tips=["Proteales"], token="petal", style="branch"),
                       dict(tips=["Trochodendrales"], token="petal", style="branch"),
                       dict(tips=["Buxales"], token="petal", style="branch"),
                       dict(node="Core", token="plant", style="bar", label="Core eudicots"),
                       dict(node="Pentapetalae", token="anther", style="branch")],
               marks=[dict(node="Eudicots", kind="star", at=0.5, token="highlight", text="1"),
                      dict(node="Core", kind="trait", at=0.5, token="dna", text="2"),
                      dict(node="Pentapetalae", kind="trait", at=0.5, token="petal", text="3")])
bio.label(ax, (19.0, 6.6), "Early-diverging eudicots (pink branches)", size="small", ha="left",
          color=bio.P.edge("petal"))
KEY = ["1  Tricolpate pollen",
       "2  Gamma whole-genome triplication; ellagic acid",
       "3  Flowers 5-merous; calyx and corolla in two whorls",
       "Position of Dilleniales unresolved"]
for i, k in enumerate(KEY):
    bio.label(ax, (19.0, 10.4 - i * 0.9), k, size="small", ha="left")
