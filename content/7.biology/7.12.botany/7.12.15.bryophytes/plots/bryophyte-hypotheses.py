"""Changing hypotheses on land-plant phylogeny (simplified cladograms, Zygnematophyceae as outgroup).
A: liverworts diverge first; bryophytes paraphyletic, hornworts (or mosses) sister to vascular plants.
B: hornworts diverge first. C: current view: bryophytes monophyletic, liverworts + mosses (Setaphyta)
sister to hornworts, bryophytes sister to vascular plants. Green bar: bryophytes."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(33, 10.6)
TREES = [
    ("A", "Liverworts first (paraphyletic)", "(Zygnematophyceae,(Liverworts,(Mosses,(Hornworts,Vascular_plants))));", None),
    ("B", "Hornworts first (paraphyletic)", "(Zygnematophyceae,(Hornworts,(Liverworts,(Mosses,Vascular_plants))));", None),
    ("C", "Bryophytes monophyletic (current)", "(Zygnematophyceae,(((Liverworts,Mosses)Setaphyta,Hornworts)Bryophytes,Vascular_plants));",
     "Bryophytes"),
]
for k, (letter, title, nwk, clade) in enumerate(TREES):
    x0 = 0.6 + k * 11.0
    bio.panel(ax, letter, (x0 - 0.4, 10.4))
    bio.label(ax, (x0 + 4.6, 9.8), title, size="normal", bold=True)
    clades = [dict(node=clade, token="plant", style="bar", label=None)] if clade else None
    phylo.tree(ax, nwk, origin=(x0, 1.4), width=4.4, height=7.2, direction="right", root_edge=0.4, label_size="small",
               icons={"Liverworts": "phylopic/liverwort", "Mosses": "phylopic/moss", "Hornworts": "phylopic/hornwort",
                      "Vascular plants": "phylopic/fern"}, icon_color="plant", icon_size=0.7, clades=clades)
