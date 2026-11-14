# Losses and a regain of sweet and umami taste receptor genes mapped on a cladogram (topology only).
# Sweet = T1R2 + T1R3 (Tas1r2), umami = T1R1 + T1R3 (Tas1r1). Sources: Li et al. 2005 (cat Tas1r2
# pseudogene); Li et al. 2010, Zhao et al. 2010 (giant panda Tas1r1 pseudogene); Jiang et al. 2012
# (sea lion and bottlenose dolphin: Tas1r2 and Tas1r1 pseudogenes); chicken genome (no Tas1r2);
# Baldwin et al. 2014 (hummingbird T1R1-T1R3 retuned to sugars).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Human,Mouse)Euarchontoglires,(Dolphin,(Cat,(Dog,(Panda,Sea_lion)Arctoidea)Caniformia)Carnivora)"
          "Laurasiatheria)Mammals,(Chicken,Hummingbird)Birds)Amniotes;")
ICONS = {"Human": "phylopic/human", "Mouse": "phylopic/mouse", "Dolphin": "phylopic/dolphin",
         "Cat": "phylopic/tiger", "Dog": "phylopic/wolf", "Panda": "phylopic/giant-panda",
         "Sea lion": "phylopic/harbour-seal", "Chicken": "phylopic/chicken",
         "Hummingbird": "phylopic/hummingbird"}
TEXT = {"Human": "Human (omnivore)", "Mouse": "Mouse (omnivore)", "Dolphin": "Bottlenose dolphin (fish, swallowed whole)",
        "Cat": "Cat (obligate carnivore)", "Dog": "Dog (omnivorous carnivore)", "Panda": "Giant panda (bamboo)",
        "Sea lion": "Sea lion (fish, swallowed whole)", "Chicken": "Chicken (seeds, insects)",
        "Hummingbird": "Hummingbird (nectar)"}
MARKS = [
    dict(node="Cat", kind="loss", at=0.5, text="sweet", side=1, text_size="tiny"),
    dict(node="Panda", kind="loss", at=0.5, text="umami", side=1, text_size="tiny"),
    dict(node="Sea lion", kind="loss", at=0.5, text="sweet, umami", side=1, text_size="tiny"),
    dict(node="Dolphin", kind="loss", at=0.5, text="sweet, umami", side=1, text_size="tiny"),
    dict(node="Birds", kind="loss", at=0.5, text="sweet (Tas1r2 gene lost)", side=1, text_size="tiny"),
    dict(node="Hummingbird", kind="trait", at=0.5, text="sugar sensing regained", side=1, text_size="tiny"),
]
fig, ax = bio.canvas(19, 10.4)
t = phylo.tree(ax, NEWICK, origin=(0.8, 1.6), width=8.6, height=8.0, direction="right", root_edge=0.3,
               tip_text=TEXT, icons=ICONS, icon_size=0.6, icon_width=1.0, label_size="small", marks=MARKS,
               clades=[dict(node="Carnivora", token="drug", style="band", label="Carnivora")])
x0, y0 = 0.8, 0.8
phylo.marker(ax, (x0 + 0.12, y0), "loss", size=0.14, direction=(1, 0))
bio.label(ax, (x0 + 0.4, y0), "loss of a functional receptor gene (pseudogene or deletion)", size="tiny", ha="left")
phylo.marker(ax, (x0 + 10.2, y0), "trait", size=0.14, direction=(1, 0))
bio.label(ax, (x0 + 10.5, y0), "gain of a function", size="tiny", ha="left")
