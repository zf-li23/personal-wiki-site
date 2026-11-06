# Subfamilies of Poaceae and the repeated origin of C4 photosynthesis (GPWG II 2012; Soreng et al. 2017).
# After three small early-diverging subfamilies, grasses split into the BOP clade (all C3) and the
# PACMAD clade. Dots mark subfamilies containing C4 lineages; C4 arose 22-24 times, all within PACMAD.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Anomochlooideae,(Pharoideae,(Puelioideae,((Oryzoideae,(Bambusoideae,Pooideae))BOP,"
          "(Panicoideae,(Aristidoideae,((Chloridoideae,Danthonioideae),(Micrairoideae,Arundinoideae))))PACMAD)BP)))Poaceae;")
fig, ax = bio.canvas(26, 11)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=9.5, height=9.4, label_size="normal", root_edge=0.5,
               clades=[dict(node="BOP", token="dna", style=("bar", "branch"), label="BOP (all C3)"),
                       dict(node="PACMAD", token="atp", style=("bar", "branch"), label="PACMAD")],
               icons={"Pooideae": "phylopic/wheat", "Panicoideae": "phylopic/maize"}, icon_size=1.1,
               icon_color="plant",
               marks=[dict(node=s, kind="dot", at=0.75, token="negative") for s in
                      ["Panicoideae", "Aristidoideae", "Chloridoideae", "Micrairoideae"]])
phylo.legend(ax, (20.0, 10.2), [("dot", "contains C4 lineages", "negative")])
