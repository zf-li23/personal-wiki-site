"""Repeated solutions to the same functional problems, mapped on a cladogram of the main lineages of the course.

Topology simplified from the tree of 7.17.6 and the class chapters (polytomies where relationships are unresolved
or irrelevant here). Each column is one functional design. A rounded bar spanning several rows marks one origin
shared by those lineages (homology at that level); separate dots in one column mark independent origins.
Hollow dots mark partial or regional states (regional endothermy of tunas). The short text gives the group in
which the design occurs. Assignments follow the chapters of this course: eyes 7.17.44 and 7.17.68, segmentation
7.17.3, tracheae and Malpighian tubules 7.17.20 and 7.17.44, circulation 7.17.44 and 7.17.65, flight 7.17.25 and
7.17.61, endothermy 7.17.50, hearts 7.17.65, tympanic ears 7.17.27 and 7.17.68, eusociality 7.17.38, jet
propulsion 7.17.9 and 7.17.14.
"""

from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio
from wikibio import phylo, quant

P = bio.P
NEWICK = ("(Cnidaria,((Flatworms,(((Gastropods,Bivalves),Cephalopods)Mollusca,Annelids,Nemerteans)),"
          "((Nematodes,(Onychophorans,(Chelicerates,(Myriapods,(Crustaceans,Insects))))),"
          "(Echinoderms,(Lancelets,(Teleosts,(Amphibians,(Mammals,(Lepidosaurs,(Turtles,"
          "(Crocodylians,(Pterosaurs,Birds)))))))))))Bilateria);")
NAME = {"Lepidosaurs": "Lizards and snakes", "Pterosaurs": "Pterosaurs (extinct)", "Chelicerates": "Chelicerates"}

# column title -> list of origins; an origin is (rows, text, partial)
COLS = [
    ("Camera eye", [(["Cnidaria"], "cubozoans"), (["Gastropods"], "heteropods"), (["Cephalopods"], "coleoids"),
                    (["Annelids"], "alciopids"), (["Chelicerates"], "spiders"),
                    (["Teleosts", "Birds"], "vertebrates")]),
    ("Compound eye", [(["Bivalves"], "ark clams"), (["Annelids"], "sabellids"),
                      (["Chelicerates", "Insects"], "arthropods")]),
    ("Segmentation", [(["Annelids"], "annelids"), (["Onychophorans", "Insects"], "panarthropods"),
                      (["Lancelets", "Birds"], "chordates")]),
    ("Tracheae", [(["Onychophorans"], ""), (["Chelicerates"], "arachnids"), (["Myriapods"], ""),
                  (["Crustaceans"], "woodlice"), (["Insects"], "")]),
    ("Malpighian tubules", [(["Chelicerates"], "endodermal"), (["Myriapods"], "ectodermal"),
                            (["Insects"], "ectodermal")]),
    ("Closed circulation", [(["Cephalopods"], ""), (["Annelids"], ""), (["Nemerteans"], ""),
                            (["Lancelets", "Birds"], "chordates")]),
    ("Powered flight", [(["Insects"], "wings"), (["Mammals"], "bats"), (["Pterosaurs"], ""), (["Birds"], "")]),
    ("Endothermy", [(["Teleosts"], "tunas", True), (["Mammals"], ""), (["Birds"], "")]),
    ("Divided ventricle", [(["Mammals"], ""), (["Crocodylians"], ""), (["Birds"], "")]),
    ("Tympanic ear", [(["Insects"], "20+ times"), (["Amphibians"], "frogs"), (["Mammals"], ""),
                      (["Lepidosaurs"], ""), (["Turtles"], ""), (["Crocodylians", "Birds"], "archosaurs")]),
    ("Eusociality", [(["Crustaceans"], "shrimps"), (["Insects"], "12+ times"), (["Mammals"], "mole-rats")]),
    ("Jet propulsion", [(["Cnidaria"], "medusae"), (["Bivalves"], "scallops"), (["Cephalopods"], ""),
                        (["Insects"], "naiads")]),
]
TOKENS = ["negative", "drug", "positive", "atp", "enzyme", "receptor", "dna", "highlight", "channel", "lipid_head",
          "metabolite", "bone"]

fig, ax = bio.canvas(31.0, 15.4)
t = phylo.tree(ax, NEWICK, origin=(0.5, 0.7), width=5.0, height=12.9, direction="right", root_edge=0.25,
               tip_text=NAME, label_size="small", align=True)
x0, cw = 9.6, 1.78
for j, (title, origins) in enumerate(COLS):
    xc = x0 + j * cw + cw / 2
    tok = TOKENS[j % len(TOKENS)]
    c = quant.line_color(tok)
    bio.label(ax, (xc, 14.45), title, size="tiny", bold=True, rotation=20, ha="left", va="bottom")
    for o in origins:
        rows, text = o[0], o[1]
        partial = len(o) > 2 and o[2]
        ys = [t.node(r).xy[1] for r in rows]
        ya, yb = max(ys), min(ys)
        if len(rows) > 1:
            ax.add_patch(FancyBboxPatch((xc - 0.17, yb - 0.17), 0.34, ya - yb + 0.34,
                                        boxstyle="round,pad=0,rounding_size=0.17", fc=P.fill(tok), ec=P.edge(tok),
                                        lw=0.8, zorder=6))
            ym = (ya + yb) / 2
        else:
            ax.add_patch(Circle((xc, ya), 0.17, fc="none" if partial else P.fill(tok), ec=P.edge(tok), lw=1.0, zorder=6))
            ym = ya
        if text:
            bio.label(ax, (xc + 0.26, ym), text, size="tiny", ha="left", color=c, zorder=7)
for j in range(len(COLS) + 1):
    x = x0 + j * cw
    ax.plot([x, x], [0.45, 14.2], color=P.muted(), lw=0.3, alpha=0.5, zorder=1)
bio.label(ax, (x0, 0.15), "Bar spanning several rows: one shared origin.   Separate dots in a column: independent "
          "origins.   Hollow dot: partial (regional endothermy).", size="tiny", ha="left", color=P.muted())
