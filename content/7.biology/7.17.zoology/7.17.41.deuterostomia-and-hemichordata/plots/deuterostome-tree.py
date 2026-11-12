# Phylogeny of Deuterostomia (after Cannon et al. 2014; Simakov et al. 2015) with key characters mapped.
import wikibio as bio
from wikibio import phylo

NEWICK = ("((Echinodermata,(Enteropneusta,Pterobranchia)Hemichordata)Ambulacraria,"
          "(Cephalochordata,(Tunicata,Vertebrata)Olfactores)Chordata)Deuterostomia;")
TEXT = {"Enteropneusta": "Enteropneusta (acorn worms)", "Pterobranchia": "Pterobranchia",
        "Cephalochordata": "Cephalochordata (lancelets)", "Tunicata": "Tunicata"}
ICONS = {"Echinodermata": "phylopic/starfish", "Enteropneusta": "phylopic/acorn-worm",
         "Pterobranchia": "phylopic/pterobranch", "Cephalochordata": "phylopic/amphioxus",
         "Tunicata": "phylopic/ciona", "Vertebrata": "phylopic/lamprey"}
CHARS = [("Deuterostomia", "Pharyngeal slits; pharyngeal gene cluster"),
         ("Ambulacraria", "Dipleurula larva; axial complex; tripartite coelom"),
         ("Echinodermata", "Pentaradial adult; water vascular system; stereom"),
         ("Hemichordata", "Proboscis, collar, trunk; stomochord; glomerulus"),
         ("Pterobranchia", "Tentaculate arms; secreted tubes"),
         ("Chordata", "Notochord; dorsal hollow nerve cord; endostyle; tail"),
         ("Tunicata", "Cellulose tunic"),
         ("Vertebrata", "Neural crest; placodes; cranium")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.45, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(CHARS)]
MARKS.append(dict(node="Echinodermata", kind="loss", at=0.75))

fig, ax = bio.canvas(20.0, 10.6)
phylo.tree(ax, NEWICK, origin=(0.8, 3.6), width=9.0, height=6.4, root_edge=0.9, tip_text=TEXT, icons=ICONS,
           icon_size=0.75, icon_width=1.5, label_size="small",
           clades=[dict(node="Ambulacraria", token="positive", style="bar", label="Ambulacraria"),
                   dict(node="Chordata", token="dna", style="bar", label="Chordata")],
           marks=MARKS)
y = 2.8
for k, (_, txt) in enumerate(CHARS):
    col, row = divmod(k, 4)
    x0, yy = 0.9 + col * 9.6, y - row * 0.6
    phylo.marker(ax, (x0, yy), "trait", direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {txt}", size="small", ha="left")
phylo.marker(ax, (0.9, 0.2), "loss", direction=(1, 0))
bio.label(ax, (1.25, 0.2), "Pharyngeal slits lost (crown-group echinoderms)", size="small", ha="left")
