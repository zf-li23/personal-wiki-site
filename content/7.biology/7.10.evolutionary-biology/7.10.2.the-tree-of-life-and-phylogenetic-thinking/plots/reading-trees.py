"""How to read a phylogenetic tree. A: the parts of a rooted tree of human, chimpanzee and bonobo,
with an extinct lineage F (after Futuyma and Kirkpatrick 2017, Fig. 2.6). B: four drawings of the same
tree; rotating the branches about a node, changing the direction of time or drawing the branches
slanted changes nothing, because relationships are given by the order of branching, not by the order
of the tips. C: a different tree, in which 1 and 2, not 2 and 3, are sister taxa. D: relationship is not
similarity: crocodiles look more like lizards, but share a more recent common ancestor with birds; the
bird lineage has changed more (bars: character changes)."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(30, 9.6)

# A: anatomy
bio.panel(ax, "A", (0.2, 9.4))
t = phylo.tree(ax, "((Human:4,(Chimpanzee:2,Bonobo:2)D:2)E:1.2,F:2.2)R;", origin=(2.0, 1.6), width=4.8, height=6.0,
               direction="up", scaled=True, root_edge=0.8, label_size="small")
f = t.node("F")
bio.label(ax, (f.xy[0], f.xy[1]), "x", size="small", bold=True, color=P.edge("negative"))
d, e, r = t.node("D"), t.node("E"), t.node("R")
bio.callout(ax, d.xy, (d.xy[0] + 1.9, d.xy[1] + 0.4), "Internal node D:\nMRCA of the\nsister species", size="tiny")
bio.callout(ax, e.xy, (e.xy[0] - 1.0, e.xy[1] - 0.9), "Node E", size="tiny")
bio.callout(ax, (r.xy[0], r.xy[1] - 0.5), (r.xy[0] + 1.6, r.xy[1] - 0.6), "Root", size="tiny")
hx = t.node("Human").xy
bio.callout(ax, (hx[0], hx[1] - 2.0), (hx[0] - 0.3, hx[1] - 1.0), "Branch\n(lineage)", size="tiny")
bio.arrow(ax, (0.75, 1.6), (0.75, 8.0), kind="process", color=P.muted())
bio.label(ax, (0.4, 4.8), "Time", size="tiny", rotation=90, color=P.muted())

# B: equivalent drawings
bio.panel(ax, "B", (8.0, 9.4))
bio.label(ax, (13.6, 9.0), "All the same tree: 2 and 3 are sister taxa", size="small", bold=True)
phylo.tree(ax, "(1,(2,3));", origin=(8.6, 5.3), width=2.4, height=2.8, direction="up")
phylo.tree(ax, "(1,(3,2));", origin=(12.0, 5.3), width=2.4, height=2.8, direction="up")
phylo.tree(ax, "((3,2),1);", origin=(15.4, 5.3), width=2.4, height=2.8, direction="up")
phylo.tree(ax, "(1,(2,3));", origin=(8.8, 1.0), width=2.8, height=2.6, layout="slanted", direction="right")
phylo.tree(ax, "((2,3),1);", origin=(13.8, 1.0), width=2.8, height=2.6, layout="slanted", direction="up")
bio.label(ax, (13.6, 4.55), "rotated about a node; time to the right; slanted branches", size="tiny", color=P.muted())

# C: a different tree
bio.panel(ax, "C", (19.0, 9.4))
phylo.tree(ax, "((1,2),3);", origin=(19.6, 5.3), width=2.4, height=2.8, direction="up")
bio.label(ax, (20.8, 4.55), "A different tree:\n1 and 2 are sisters", size="tiny", color=P.muted())

# D: similarity versus relationship
bio.panel(ax, "D", (23.4, 9.4))
td = phylo.tree(ax, "(Lizard,(Crocodile,Bird)Archosauria)Root;", origin=(24.2, 1.6), width=5.2, height=6.0,
                direction="up", label_size="small",
                marks=[dict(node="Bird", kind="trait", at=a, token="highlight") for a in (0.2, 0.4, 0.6, 0.8)]
                + [dict(node="Crocodile", kind="trait", at=0.5, token="highlight"),
                   dict(node="Lizard", kind="trait", at=0.6, token="highlight")])
bio.label(ax, (26.8, 0.7), "Closest relatives: crocodiles and birds", size="tiny", color=P.muted())
