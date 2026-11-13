# Relationships of the living amniotes and some extinct groups (cladogram; daggers mark extinct groups),
# after Pough et al. (Vertebrate Life, 11th ed.), Crawford et al. 2015 and Simoes et al. 2022. Turtles are
# the sister group of archosaurs (Archelosauria) within the diapsid reptiles. Numbers of living species are
# rounded (Reptile Database 2024, IOC World Bird List 2024, Mammal Diversity Database 2024).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(((Caseasauria,(Sphenacodontia,Therapsida_and_mammals)S1)Synapsida,"
          "(Parareptilia,(Captorhinidae,(Ichthyosaurs_and_sauropterygians,"
          "(Lepidosauria,(Testudines,(Crocodylia,(Dinosaurs_and_pterosaurs,Aves)Avemetatarsalia)Archosauria)"
          "Archelosauria)Sauria)Diapsida)Eureptilia)Sauropsida)Amniota);")
TEXT = {"Caseasauria": "†Caseasauria", "Sphenacodontia": "†Sphenacodontia (Dimetrodon)",
        "Therapsida and mammals": "Therapsida: Mammalia (~6 700)",
        "Parareptilia": "†Parareptilia (mesosaurs, pareiasaurs)",
        "Captorhinidae": "†Captorhinidae",
        "Ichthyosaurs and sauropterygians": "†ichthyosaurs, sauropterygians",
        "Lepidosauria": "Lepidosauria: tuatara, squamates (~12 000)",
        "Testudines": "Testudines: turtles (~360)", "Crocodylia": "Crocodylia (~28)",
        "Dinosaurs and pterosaurs": "†pterosaurs, non-avian dinosaurs",
        "Aves": "Aves: birds (~11 000)"}
ICONS = {"Sphenacodontia": "phylopic/dimetrodon", "Therapsida and mammals": "phylopic/mouse",
         "Ichthyosaurs and sauropterygians": "phylopic/ichthyosaur", "Lepidosauria": "phylopic/lizard",
         "Testudines": "phylopic/turtle", "Crocodylia": "phylopic/crocodile",
         "Dinosaurs and pterosaurs": "phylopic/tyrannosaurus", "Aves": "phylopic/pigeon"}
MARKS = [dict(node="Amniota", kind="trait", text="amniotic egg, axis, astragalus", at=0.5, text_size="tiny",
              side=-1, offset=0.3, va="bottom"),
         dict(node="Synapsida", kind="trait", text="lower temporal fenestra", at=0.5, text_size="tiny", side=-1,
              offset=0.3, va="bottom"),
         dict(node="Diapsida", kind="trait", text="two temporal fenestrae", at=0.5, text_size="tiny", side=-1,
              offset=0.3, va="bottom"),
         dict(node="Archosauria", kind="trait", text="antorbital fenestra", at=0.5, text_size="tiny", side=-1,
              offset=0.3, va="bottom"),
         dict(node="Testudines", kind="loss", text="fenestrae closed", at=0.5, text_size="tiny", side=-1,
              offset=0.3, va="bottom")]
fig, ax = bio.canvas(26, 12)
t = phylo.tree(ax, NEWICK, origin=(0.6, 1.0), width=10.5, height=10.2, root_edge=0.6, icons=ICONS,
               icon_size=0.6, icon_width=1.4, icon_color="animal", label_size="small", tip_text=TEXT,
               clades=[dict(node="Synapsida", token="mrna", style="band", label="Synapsida"),
                       dict(node="Sauropsida", token="dna", style="band", label="Sauropsida")],
               marks=MARKS)
bio.label(ax, (0.6, 0.3), "Cladogram; † extinct; numbers are approximate counts of living species",
          size="tiny", color=P.muted(), ha="left")
