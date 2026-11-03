"""Rooting the tree of life with ancient paralogs (after Barton et al. 2007, Fig. 5.20): a duplication before
LUCA gave EF-Tu and EF-G; each paralog subtree contains Bacteria, Archaea and Eukarya and roots the other."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(16, 9)
NW = "((Bacteria_Tu,(Archaea_Tu,Eukarya_Tu)ae_Tu)EF_Tu,(Bacteria_G,(Archaea_G,Eukarya_G)ae_G)EF_G)Dup;"
TXT = {"Bacteria Tu": "Bacteria (EF-Tu)", "Archaea Tu": "Archaea (EF-Tu)", "Eukarya Tu": "Eukarya (EF-Tu)",
       "Bacteria G": "Bacteria (EF-G)", "Archaea G": "Archaea (EF-G)", "Eukarya G": "Eukarya (EF-G)"}
t = phylo.tree(ax, NW, origin=(1.5, 1.0), width=8.0, height=7.0, root_edge=0.6, tip_text=TXT, label_size="small",
               clades=[dict(tips=["Bacteria Tu"], token="positive", style="branch"),
                       dict(tips=["Bacteria G"], token="positive", style="branch"),
                       dict(node="ae Tu", token="rna", style="branch"),
                       dict(node="ae G", token="rna", style="branch")],
               marks=[dict(node="Dup", kind="duplication", at=1.0, size=0.32)])
x, y = t.node("Dup").xy
bio.label(ax, (x - 0.2, y - 0.6), "duplication\nbefore LUCA", size="tiny", ha="center", va="top", color=P.muted())
for name, text in (("EF Tu", "root of the\nEF-Tu subtree"), ("EF G", "root of the\nEF-G subtree")):
    nx, ny = t.node(name).xy
    ax.plot([nx], [ny], "o", ms=6, color=P.edge("negative"), zorder=14)
    bio.label(ax, (nx - 0.25, ny + (0.55 if name == "EF Tu" else -0.55)), text, size="tiny", ha="right",
              color=P.muted())
bio.label(ax, (8.0, 0.4), "green: Bacteria   orange: Archaea + Eukarya", size="tiny", color=P.muted())
