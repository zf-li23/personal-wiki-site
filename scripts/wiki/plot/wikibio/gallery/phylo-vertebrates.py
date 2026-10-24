# Vertebrate cladogram: a slanted cladogram with derived characters on the branches where they arose
# and PhyloPic silhouettes on the tips (turtles as the sister group of archosaurs).
import wikibio as bio
from wikibio import phylo

NEWICK = ("(Lamprey,(Shark,(Zebrafish,(Coelacanth,(Lungfish,(Frog,(Mouse,(Lizard,(Turtle,"
          "(Crocodile,Chicken))))))))));")

TEXT = {"Lamprey": "Lampreys", "Shark": "Sharks", "Zebrafish": "Ray-finned\nfishes", "Coelacanth": "Coelacanths",
        "Lungfish": "Lungfishes", "Frog": "Amphibians", "Mouse": "Mammals", "Lizard": "Lizards,\nsnakes",
        "Turtle": "Turtles", "Crocodile": "Crocodilians", "Chicken": "Birds"}

ICONS = {
    "Lamprey": "phylopic/lamprey", "Shark": "phylopic/great-white-shark", "Zebrafish": "phylopic/zebrafish",
    "Coelacanth": "phylopic/coelacanth", "Lungfish": "phylopic/lungfish", "Frog": "phylopic/xenopus",
    "Mouse": "phylopic/mouse", "Lizard": "phylopic/anole", "Turtle": "phylopic/green-turtle",
    "Crocodile": ("phylopic/nile-crocodile", {"rotate": -90}), "Chicken": "phylopic/chicken",
}

MARKS = [
    dict(node=["Lamprey", "Chicken"], kind="trait", at=0.45, text="Vertebral column, cranium"),
    dict(node=["Shark", "Chicken"], kind="trait", text="Jaws"),
    dict(node=["Zebrafish", "Chicken"], kind="trait", text="Bony skeleton"),
    dict(node=["Coelacanth", "Chicken"], kind="trait", text="Lobed fins"),
    dict(node=["Frog", "Chicken"], kind="trait", text="Four limbs with digits"),
    dict(node=["Mouse", "Chicken"], kind="trait", text="Amniotic egg"),
    dict(node="Mouse", kind="trait", at=0.6, text="Hair", side=-1, offset=0.22, va="bottom", ha="left"),
    dict(node="Chicken", kind="trait", at=0.6, text="Feathers"),
]

fig, ax = bio.canvas(20, 12.2)
t = phylo.tree(ax, NEWICK, origin=(1.3, 0.6), width=17.4, height=7.4, layout="slanted", direction="up", root_edge=1.2,
               tip_text=TEXT, icons=ICONS, icon_size=1.0, icon_width=1.45, label_size="small",
               clades=[dict(tips=["Mouse", "Chicken"], token="animal", style="band", label="Amniota"),
                       dict(tips=["Frog", "Chicken"], token="positive", style="bar", label="Tetrapoda"),
                       dict(tips=["Shark", "Chicken"], token="dna", style="bar", label="Gnathostomata")],
               marks=MARKS)
