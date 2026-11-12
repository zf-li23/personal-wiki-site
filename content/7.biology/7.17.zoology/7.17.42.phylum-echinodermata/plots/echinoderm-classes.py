# The five living classes of echinoderms (after Telford et al. 2014; O'Hara et al. 2014) with characters mapped.
import wikibio as bio
from wikibio import phylo

NEWICK = "(Crinoidea,((Asteroidea,Ophiuroidea)Asterozoa,(Echinoidea,Holothuroidea)Echinozoa)Eleutherozoa)Echinodermata;"
TEXT = {"Crinoidea": "Crinoidea (sea lilies, feather stars; ~650)", "Asteroidea": "Asteroidea (sea stars; ~1,900)",
        "Ophiuroidea": "Ophiuroidea (brittle stars; ~2,100)", "Echinoidea": "Echinoidea (sea urchins; ~1,000)",
        "Holothuroidea": "Holothuroidea (sea cucumbers; ~1,700)"}
ICONS = {"Crinoidea": "phylopic/crinoid", "Asteroidea": "phylopic/starfish", "Ophiuroidea": "phylopic/brittle-star",
         "Echinoidea": "phylopic/sea-urchin", "Holothuroidea": "phylopic/sea-cucumber"}
CHARS = [("Echinodermata", "Pentaradial adult; stereom; water vascular system"),
         ("Crinoidea", "Mouth up; pinnulate arms; stalk; entoneural system dominant"),
         ("Eleutherozoa", "Mouth down; sieve-plate madreporite; robust tube feet"),
         ("Asterozoa", "Stellate body with arms"),
         ("Asteroidea", "Eversible stomach; papulae; suckered tube feet"),
         ("Ophiuroidea", "Arm vertebrae; disc set off from arms; no anus"),
         ("Echinozoa", "Peripharyngeal coelom; no arms"),
         ("Echinoidea", "Rigid test; Aristotle's lantern"),
         ("Holothuroidea", "Microscopic ossicles; feeding tentacles; respiratory trees")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.45, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(CHARS)]

fig, ax = bio.canvas(21.0, 10.6)
phylo.tree(ax, NEWICK, origin=(0.8, 3.8), width=8.0, height=6.2, root_edge=0.9, tip_text=TEXT, icons=ICONS,
           icon_size=0.95, icon_width=1.6, label_size="small",
           clades=[dict(node="Asterozoa", token="drug", style="bar", label="Asterozoa"),
                   dict(node="Echinozoa", token="dna", style="bar", label="Echinozoa")],
           marks=MARKS)
y = 2.9
for k, (_, txt) in enumerate(CHARS):
    col, row = divmod(k, 5)
    x0, yy = 0.9 + col * 10.2, y - row * 0.6
    phylo.marker(ax, (x0, yy), "trait", direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {txt}", size="small", ha="left")
