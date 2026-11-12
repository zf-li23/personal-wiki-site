# Relationships of the main groups of ray-finned fishes (cladogram), after Pough et al. (Vertebrate Life,
# 11th ed.) and the phylogenomic classification of Betancur-R. et al. 2017; species numbers rounded, from
# Pough et al. and Fricke et al. (Eschmeyer's Catalog of Fishes).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Polypteriformes,(Acipenseriformes,((Lepisosteiformes,Amiiformes)Holostei,"
          "(Elopomorpha,(Osteoglossomorpha,((Clupeiformes,Ostariophysi)Otomorpha,"
          "(Protacanthopterygii,(Stomiiformes,(Gadiformes,Acanthopterygii)Acanthomorpha)N)Euteleostei)C)B)"
          "Teleostei)Neopterygii)Actinopteri)Actinopterygii;")
TEXT = {"Polypteriformes": "Polypteriformes, bichirs (12)",
        "Acipenseriformes": "Acipenseriformes, sturgeons, paddlefishes (27)",
        "Lepisosteiformes": "Lepisosteiformes, gars (7)", "Amiiformes": "Amiiformes, bowfins (2)",
        "Elopomorpha": "Elopomorpha, tarpons, eels (~1000)",
        "Osteoglossomorpha": "Osteoglossomorpha, bony-tongues (~250)",
        "Clupeiformes": "Clupeiformes, herrings, anchovies (~400)",
        "Ostariophysi": "Ostariophysi, carps, catfishes, tetras (~11 000)",
        "Protacanthopterygii": "Salmoniformes, Esociformes (~250)",
        "Stomiiformes": "Stomiiformes, dragonfishes (~450)",
        "Gadiformes": "Gadiformes, cods (~600)",
        "Acanthopterygii": "Acanthopterygii, spiny-finned fishes (~18 000)"}
ICONS = {"Polypteriformes": "phylopic/bichir", "Acipenseriformes": "phylopic/sturgeon",
         "Lepisosteiformes": "phylopic/gar", "Amiiformes": "phylopic/bowfin", "Elopomorpha": "phylopic/eel",
         "Clupeiformes": "phylopic/herring", "Ostariophysi": "phylopic/carp",
         "Protacanthopterygii": "phylopic/salmon", "Gadiformes": "phylopic/cod",
         "Acanthopterygii": "phylopic/tuna"}
MARKS = [dict(node="Teleostei", kind="duplication", text="3R", at=0.5, token="highlight"),
         dict(node="Ostariophysi", kind="trait", text="Weberian apparatus", at=0.5, text_size="tiny", side=1,
              offset=0.3, va="bottom"),
         dict(node="Acanthopterygii", kind="trait", text="fin spines, protrusible jaws", at=0.5,
              text_size="tiny", side=1, offset=0.3, va="bottom")]

fig, ax = bio.canvas(25, 12.5)
t = phylo.tree(ax, NEWICK, origin=(0.6, 1.0), width=9.0, height=10.8, root_edge=0.5, icons=ICONS,
               icon_size=0.55, icon_width=1.3, icon_color="animal", label_size="small", tip_text=TEXT,
               clades=[dict(node="Teleostei", token="dna", style="band", label="Teleostei")],
               marks=MARKS)
bio.label(ax, (0.6, 0.3), "Cladogram; numbers are approximate counts of living species", size="tiny",
          color=P.muted(), ha="left")
