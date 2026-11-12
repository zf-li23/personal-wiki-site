# Relationships of early jawed vertebrates and of the living chondrichthyans (cladogram). Placoderms are
# drawn as a paraphyletic series on the gnathostome stem (antiarchs, arthrodires, ptyctodonts, then the
# "maxillate placoderms" Entelognathus and Qilinyu), acanthodians as stem chondrichthyans, after Zhu et al.
# 2013, 2016 and Pough et al. (Vertebrate Life, 11th ed.). Batoids are the sister group of all sharks.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Osteostracans,(Antiarchs,(Arthrodires,(Ptyctodonts,(Entelognathus_and_Qilinyu,"
          "(('Acanthodians (stem)',(Chimaeras,((Galeomorph_sharks,Squalomorph_sharks)Selachii,"
          "Batoids)Elasmobranchii)Chondrichthyes)CH,Osteichthyes)Crown)M)P)A)G);")
ICONS = {"Osteostracans": "phylopic/osteostracan", "Arthrodires": "phylopic/placoderm",
         "Chimaeras": "phylopic/chimaera", "Galeomorph sharks": "phylopic/great-white-shark",
         "Squalomorph sharks": "phylopic/dogfish", "Batoids": "phylopic/stingray",
         "Osteichthyes": "phylopic/zebrafish"}
TEXT = {"Entelognathus and Qilinyu": "Entelognathus, Qilinyu (maxillate placoderms)",
        "Antiarchs": "Antiarchs (placoderm)", "Arthrodires": "Arthrodires (placoderm)",
        "Ptyctodonts": "Ptyctodonts (placoderm)", "Batoids": "Batoids (skates and rays)",
        "Chimaeras": "Holocephali (chimaeras)", "Osteichthyes": "Osteichthyes (bony fishes)"}
MARKS = [dict(node="G", kind="trait", text="jaws, teeth, pelvic fins, 3 semicircular canals", at=0.5,
              text_size="tiny", side=1, offset=0.3, va="bottom"),
         dict(node="M", kind="trait", text="maxilla, premaxilla, dentary", at=0.5, text_size="tiny", side=-1,
              offset=0.3, va="top"),
         dict(node="Chondrichthyes", kind="trait", text="prismatic calcified cartilage, claspers", at=0.5, text_size="tiny",
              side=1, offset=0.3, va="bottom"),
         dict(node="Osteichthyes", kind="trait", text="endochondral bone, lepidotrichia", at=0.5,
              text_size="tiny", side=1, offset=0.3, va="bottom")]

fig, ax = bio.canvas(24, 12)
t = phylo.tree(ax, NEWICK, origin=(0.6, 1.2), width=12.5, height=10.2, root_edge=0.5, icons=ICONS,
               icon_size=0.6, icon_width=1.4, icon_color="animal", label_size="small", tip_text=TEXT,
               clades=[dict(node="Chondrichthyes", token="dna", style="band", label="Chondrichthyes")],
               italic={"Entelognathus and Qilinyu"}, marks=MARKS)
bio.label(ax, (0.6, 0.35), "Cladogram; positions of acanthodians and of some placoderm groups are debated",
          size="tiny", color=P.muted(), ha="left")
