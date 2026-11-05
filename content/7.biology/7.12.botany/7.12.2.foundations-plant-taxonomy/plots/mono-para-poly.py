"""Monophyletic, paraphyletic and polyphyletic groups on one tree of the angiosperms (cladogram after
APG IV; branch lengths have no meaning). Eudicots (bar) are monophyletic: their common ancestor and all
its descendants, united by tricolpate pollen. The traditional "dicots" (dots) are paraphyletic: they
share the common ancestor of all angiosperms but exclude one group of its descendants, the monocots.
Cronquist's Nymphaeales, water lilies together with the lotus (stars), were polyphyletic: Nymphaea and
Nelumbo resemble each other as aquatic plants, but their closest relatives lie in different parts of
the tree, and the group's common ancestor is that of all angiosperms except Amborella. The square
marks a synapomorphy (tricolpate pollen) on the stem of the eudicots.
"""

import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(22, 12.2)
nw = ("(Amborella,(Nymphaea,(Illicium,((Magnolia,Chloranthus),(Monocots,(Ceratophyllum,"
      "(Ranunculus,(Nelumbo,(Saxifraga,(Rosa,Helianthus))))eud))))));")
text = {
    "Amborella": "Amborella",
    "Nymphaea": "Nymphaea (water lily)",
    "Illicium": "Illicium (star anise)",
    "Magnolia": "Magnolia (magnoliids)",
    "Chloranthus": "Chloranthus",
    "Monocots": "monocots (lilies, grasses, orchids)",
    "Ceratophyllum": "Ceratophyllum",
    "Ranunculus": "Ranunculus (buttercup)",
    "Nelumbo": "Nelumbo (lotus)",
    "Saxifraga": "Saxifraga",
    "Rosa": "Rosa (rosids)",
    "Helianthus": "Helianthus (asterids)",
}
italic = {k for k in text if k != "Monocots"}
dicots = ["Amborella", "Nymphaea", "Illicium", "Magnolia", "Chloranthus", "Ceratophyllum", "Ranunculus",
          "Nelumbo", "Saxifraga", "Rosa", "Helianthus"]
t = phylo.tree(ax, nw, origin=(1.0, 1.7), width=7.5, height=9.9, root_edge=0.4, tip_text=text,
               italic=lambda n: n in italic, label_size="small",
               icons={"Amborella": "phylopic/amborella", "Nymphaea": "phylopic/water-lily",
                      "Magnolia": "phylopic/magnolia", "Monocots": "phylopic/orchid",
                      "Rosa": "phylopic/rosaceae", "Helianthus": "phylopic/asteraceae"},
               icon_size=0.6, icon_color="plant",
               clades=[dict(node="eud", token="positive", style=["branch", "bar"],
                            label="eudicots (monophyletic)")],
               marks=[dict(node=n, kind="dot", token="highlight", at=1.0) for n in dicots]
               + [dict(node=n, kind="star", token="negative", at=0.55) for n in ("Nymphaea", "Nelumbo")]
               + [dict(node="eud", kind="duplication", token="positive", at=0.5)])
phylo.legend(ax, (1.2, 0.6), [("dot", "\"dicots\": paraphyletic (excludes the monocots)", "highlight")],
             size="tiny")
phylo.legend(ax, (9.6, 0.6), [("star", "water lilies + lotus: polyphyletic", "negative")], size="tiny")
phylo.legend(ax, (16.0, 0.6), [("duplication", "tricolpate pollen", "positive")], size="tiny")
