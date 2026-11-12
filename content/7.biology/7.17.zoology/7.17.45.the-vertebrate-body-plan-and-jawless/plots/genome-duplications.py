# Whole-genome duplications in vertebrate history and the number of Hox clusters in living groups.
# Placement of the duplications after Marletaz et al. 2024 (Nature) and Yu et al. 2024 (Nat. Ecol. Evol.):
# 1R before the cyclostome-gnathostome split, 2R in the gnathostome stem, an independent triplication (CR)
# in cyclostomes, and the teleost-specific 3R. Hox cluster numbers: amphioxus 1; lampreys at least 6;
# hagfishes 6 or more (counts uncertain); elasmobranchs 3 (HoxC lost); chimaeras, coelacanth, tetrapods 4;
# zebrafish 7 (one of eight lost after 3R); salmonids up to 13 after a further duplication.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Amphioxus,((Hagfishes,Lampreys)Cyclostomata,((Sharks_and_rays,Chimaeras)Chondrichthyes,"
          "((Gar,Teleosts)Actinopterygii,Tetrapods)Osteichthyes)Gnathostomata)Vertebrata);")
ICONS = {"Amphioxus": "phylopic/amphioxus", "Hagfishes": ("phylopic/hagfish", {"rotate": 90}),
         "Lampreys": "phylopic/lamprey", "Sharks and rays": "phylopic/great-white-shark",
         "Chimaeras": "phylopic/chimaera", "Gar": "phylopic/gar", "Teleosts": "phylopic/zebrafish",
         "Tetrapods": "phylopic/frog"}
HOX = {"Amphioxus": "1", "Hagfishes": "6+", "Lampreys": "6+", "Sharks and rays": "3 (HoxC lost)",
       "Chimaeras": "4", "Gar": "4", "Teleosts": "7-8 (13 in salmonids)", "Tetrapods": "4"}
MARKS = [dict(node="Vertebrata", kind="duplication", text="1R", at=0.5, token="highlight"),
         dict(node="Gnathostomata", kind="duplication", text="2R", at=0.5, token="highlight"),
         dict(node="Cyclostomata", kind="duplication", text="CR (triplication)", at=0.5, token="negative"),
         dict(node="Teleosts", kind="duplication", text="3R", at=0.4, token="highlight")]

fig, ax = bio.canvas(20, 10)
t = phylo.tree(ax, NEWICK, origin=(0.6, 1.2), width=8.0, height=7.6, root_edge=0.6, icons=ICONS,
               icon_size=0.6, icon_width=1.3, icon_color="animal", label_size="small", marks=MARKS)
bio.label(ax, (16.6, 9.4), "Hox clusters", size="small", bold=True)
for n in t.tips():
    bio.label(ax, (15.2, n.xy[1]), HOX[n.name], size="small", ha="left")
bio.label(ax, (0.6, 0.35), "Squares: whole-genome duplications (placement after 2024 hagfish genome studies)",
          size="tiny", color=P.muted(), ha="left")
