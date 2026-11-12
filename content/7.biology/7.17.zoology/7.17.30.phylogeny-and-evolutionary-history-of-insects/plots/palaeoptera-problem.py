# The Palaeoptera problem: three rooted hypotheses for Ephemeroptera, Odonata and Neoptera (outgroup Zygentoma),
# with a character cited in support of each; non-folding wings are ancestral in all three.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(27, 8.6)
ICONS = {"Ephemeroptera": "phylopic/mayfly", "Odonata": "phylopic/dragonfly", "Neoptera": "phylopic/grasshopper",
         "Zygentoma": "phylopic/silverfish"}
hyps = [
    ("A  Palaeoptera", "(Zygentoma,((Ephemeroptera,Odonata)X,Neoptera));", "intercalary\nveins"),
    ("B  Metapterygota", "(Zygentoma,(Ephemeroptera,(Odonata,Neoptera)X));", "loss of the\nsubimago"),
    ("C  Chiastomyaria", "(Zygentoma,(Odonata,(Ephemeroptera,Neoptera)X));", "direct sperm\ntransfer"),
]
for k, (title, nwk, trait) in enumerate(hyps):
    x0 = 0.6 + k * 9.0
    bio.label(ax, (x0 + 3.6, 8.0), title, size="small", bold=True)
    phylo.tree(ax, nwk, origin=(x0, 1.2), width=3.6, height=5.6, root_edge=0.4, icons=ICONS, icon_size=0.55,
               icon_width=1.1, icon_color="animal", label_size="small",
               marks=[dict(node="X", kind="trait", text=trait, token="positive", at=0.5, shift=(-0.3, -0.25), text_size="tiny")])
bio.label(ax, (13.5, 0.4), "Wing folding is a synapomorphy of Neoptera; the non-folding wing of mayflies and dragonflies is ancestral.",
          size="tiny", color=P.muted())
