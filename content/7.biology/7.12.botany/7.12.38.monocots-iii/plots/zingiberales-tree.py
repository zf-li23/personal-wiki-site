# Relationships of the eight families of Zingiberales (Kress et al. 2001; Sass et al. 2016) with the
# number of fertile stamens. The "banana group" (Musaceae, Strelitziaceae, Lowiaceae, Heliconiaceae) is a
# grade with five fertile stamens; the "ginger group" is a clade with one fertile stamen (half a stamen,
# one theca, in Cannaceae and Marantaceae) and petaloid staminodes. Bars mark the reductions.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Musaceae,((Strelitziaceae,Lowiaceae),(Heliconiaceae,((Cannaceae,Marantaceae)CM,"
          "(Costaceae,Zingiberaceae)CZ)Ginger)HG)Rest)Zingiberales;")
fig, ax = bio.canvas(24, 9.5)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=8.5, height=7.6, label_size="normal", root_edge=0.6,
               clades=[dict(node="Ginger", token="atp", style=("branch",), label=None)],
               marks=[dict(node="Ginger", kind="trait", at=0.5, token="negative", text="1 stamen"),
                      dict(node="CM", kind="trait", at=0.5, token="negative", text="1/2 stamen")])
ROWS = {"Musaceae": "5 + 1 staminode", "Strelitziaceae": "5", "Lowiaceae": "5", "Heliconiaceae": "5 + 1 staminode",
        "Cannaceae": "1/2; petaloid staminodes", "Marantaceae": "1/2; staminodes form a trigger",
        "Costaceae": "1; labellum of 5 staminodes", "Zingiberaceae": "1; labellum of 2 staminodes"}
bio.label(ax, (14.6, 9.0), "Fertile stamens", size="small", ha="left", bold=True)
for name, s in ROWS.items():
    bio.label(ax, (14.6, t.node(name).xy[1]), s, size="small", ha="left")
