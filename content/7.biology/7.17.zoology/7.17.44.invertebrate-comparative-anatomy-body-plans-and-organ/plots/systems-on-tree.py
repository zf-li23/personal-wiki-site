"""Organ systems of the animal phyla mapped onto the animal tree (cladogram after 7.17.6: ctenophores
as the sister group of all other animals, Xenacoelomorpha as the sister group of Nephrozoa; polytomies
mark unresolved nodes).

Each row is a phylum (or a chordate subphylum), each column an organ system; the cell gives the adult
state of the phylum in a few words, coloured by kind of state so that identical states line up as
colour bands. Variation within phyla is summarized ("open / closed" for molluscs, whose cephalopods
are closed). Reading down a column shows which states are confined to one clade (dorsal hollow nerve
cord, molted cuticle, compound eyes) and which are scattered across the tree (closed circulation,
camera eyes, protonephridia), the pattern expected of homology and of convergence respectively.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import phylo, quant

P = bio.P
NEWICK = ("(Ctenophora,(Porifera,(Placozoa,(Cnidaria,(Xenacoelomorpha,"
          "(((Echinodermata,Hemichordata)Ambulacraria,(Cephalochordata,(Tunicata,Vertebrata))Chordata)Deuterostomia,"
          "((Priapulida,Nematoda,(Tardigrada,(Onychophora,Arthropoda)))Ecdysozoa,"
          "(Rotifera,(Platyhelminthes,(Mollusca,Annelida,Nemertea,(Brachiopoda,Bryozoa)))))Spiralia)"
          "Protostomia)Nephrozoa))));")

# column -> {phylum: (text, kind)}; kinds map to colour tokens below
NONE = "none"
COLS = [
    ("Skeleton", {
        "Ctenophora": ("mesoglea", "gel"), "Porifera": ("spicules", "mineral"), "Placozoa": ("none", NONE),
        "Cnidaria": ("hydrostatic", "hydro"), "Xenacoelomorpha": ("hydrostatic", "hydro"),
        "Echinodermata": ("stereom ossicles", "mineral"), "Hemichordata": ("hydrostatic", "hydro"),
        "Cephalochordata": ("notochord", "rod"), "Tunicata": ("tunic", "gel"), "Vertebrata": ("bone, cartilage", "mineral"),
        "Priapulida": ("hydrostatic", "hydro"), "Nematoda": ("hydrostatic", "hydro"), "Tardigrada": ("hydrostatic", "hydro"),
        "Onychophora": ("hydrostatic", "hydro"), "Arthropoda": ("exoskeleton", "exo"), "Rotifera": ("intracell. lamina", "gel"),
        "Platyhelminthes": ("parenchyma", "hydro"), "Mollusca": ("shell", "mineral"), "Annelida": ("septate coelom", "hydro"),
        "Nemertea": ("hydrostatic", "hydro"), "Brachiopoda": ("shell", "mineral"), "Bryozoa": ("zooecium", "mineral")}),
    ("Gut", {
        "Ctenophora": ("anal pores", "partial"), "Porifera": ("none", NONE), "Placozoa": ("none", NONE),
        "Cnidaria": ("blind sac", "blind"), "Xenacoelomorpha": ("blind sac", "blind"), "Echinodermata": ("through", "through"),
        "Hemichordata": ("through", "through"), "Cephalochordata": ("through", "through"), "Tunicata": ("through, U", "through"),
        "Vertebrata": ("through", "through"), "Priapulida": ("through", "through"), "Nematoda": ("through", "through"),
        "Tardigrada": ("through", "through"), "Onychophora": ("through", "through"), "Arthropoda": ("through", "through"),
        "Rotifera": ("through", "through"), "Platyhelminthes": ("blind sac", "blind"), "Mollusca": ("through", "through"),
        "Annelida": ("through", "through"), "Nemertea": ("through", "through"), "Brachiopoda": ("U, often blind", "partial"),
        "Bryozoa": ("through, U", "through")}),
    ("Gas exchange", {
        "Ctenophora": ("surface", NONE), "Porifera": ("water canals", NONE), "Placozoa": ("surface", NONE),
        "Cnidaria": ("surface", NONE), "Xenacoelomorpha": ("surface", NONE), "Echinodermata": ("tube feet, papulae", "gill"),
        "Hemichordata": ("pharynx, surface", "gill"), "Cephalochordata": ("surface", NONE), "Tunicata": ("pharynx", "gill"),
        "Vertebrata": ("gills, lungs", "lung"), "Priapulida": ("surface", NONE), "Nematoda": ("surface", NONE),
        "Tardigrada": ("surface", NONE), "Onychophora": ("tracheae", "lung"), "Arthropoda": ("gills, tracheae", "lung"),
        "Rotifera": ("surface", NONE), "Platyhelminthes": ("surface", NONE), "Mollusca": ("ctenidia, lung", "gill"),
        "Annelida": ("surface, gills", "gill"), "Nemertea": ("surface", NONE), "Brachiopoda": ("lophophore, mantle", "gill"),
        "Bryozoa": ("lophophore", NONE)}),
    ("Circulation", {
        "Ctenophora": ("none", NONE), "Porifera": ("none", NONE), "Placozoa": ("none", NONE), "Cnidaria": ("none", NONE),
        "Xenacoelomorpha": ("none", NONE), "Echinodermata": ("hemal sinuses", "open"), "Hemichordata": ("open", "open"),
        "Cephalochordata": ("closed, no heart", "closed"), "Tunicata": ("open, reversing", "open"), "Vertebrata": ("closed", "closed"),
        "Priapulida": ("none", NONE), "Nematoda": ("none", NONE), "Tardigrada": ("none", NONE), "Onychophora": ("open", "open"),
        "Arthropoda": ("open", "open"), "Rotifera": ("none", NONE), "Platyhelminthes": ("none", NONE),
        "Mollusca": ("open / closed", "open"), "Annelida": ("closed", "closed"), "Nemertea": ("closed", "closed"),
        "Brachiopoda": ("open", "open"), "Bryozoa": ("none", NONE)}),
    ("Excretion", {
        "Ctenophora": ("none", NONE), "Porifera": ("none", NONE), "Placozoa": ("none", NONE), "Cnidaria": ("none", NONE),
        "Xenacoelomorpha": ("none", NONE), "Echinodermata": ("none", NONE), "Hemichordata": ("glomerulus", "filter"),
        "Cephalochordata": ("cyrtopodocytes", "proto"), "Tunicata": ("renal sac", "other"), "Vertebrata": ("nephrons", "filter"),
        "Priapulida": ("protonephridia", "proto"), "Nematoda": ("renette canals", "other"), "Tardigrada": ("Malpighian", "malp"),
        "Onychophora": ("nephridia", "filter"), "Arthropoda": ("glands, Malpighian", "malp"), "Rotifera": ("protonephridia", "proto"),
        "Platyhelminthes": ("protonephridia", "proto"), "Mollusca": ("metanephridia", "filter"),
        "Annelida": ("metanephridia", "filter"), "Nemertea": ("protonephridia", "proto"),
        "Brachiopoda": ("metanephridia", "filter"), "Bryozoa": ("none", NONE)}),
    ("Nervous system", {
        "Ctenophora": ("nerve net", "net"), "Porifera": ("none", NONE), "Placozoa": ("none", NONE), "Cnidaria": ("nerve net", "net"),
        "Xenacoelomorpha": ("net, cords", "net"), "Echinodermata": ("ring, radial", "ring"), "Hemichordata": ("net, cords", "net"),
        "Cephalochordata": ("dorsal tube", "dorsal"), "Tunicata": ("dorsal tube (larva)", "dorsal"), "Vertebrata": ("dorsal tube", "dorsal"),
        "Priapulida": ("ring, ventral cord", "ring"), "Nematoda": ("ring, cords", "ring"), "Tardigrada": ("ventral ganglia", "ventral"),
        "Onychophora": ("ventral cords", "ventral"), "Arthropoda": ("ventral ganglia", "ventral"), "Rotifera": ("ganglion, cords", "cords"),
        "Platyhelminthes": ("orthogon", "cords"), "Mollusca": ("ganglia, 4 cords", "cords"), "Annelida": ("ventral ganglia", "ventral"),
        "Nemertea": ("lateral cords", "cords"), "Brachiopoda": ("circumenteric ring", "ring"), "Bryozoa": ("ganglion", "cords")}),
    ("Eyes", {
        "Ctenophora": ("none", NONE), "Porifera": ("none", NONE), "Placozoa": ("none", NONE), "Cnidaria": ("cups, lens eyes", "lens"),
        "Xenacoelomorpha": ("eyespots", "cup"), "Echinodermata": ("arm-tip cups", "cup"), "Hemichordata": ("larval eyespots", "cup"),
        "Cephalochordata": ("frontal eye", "cup"), "Tunicata": ("larval ocellus", "cup"), "Vertebrata": ("camera eyes", "lens"),
        "Priapulida": ("none", NONE), "Nematoda": ("none / ocelli", NONE), "Tardigrada": ("eyespots", "cup"),
        "Onychophora": ("lens ocelli", "lens"), "Arthropoda": ("compound, ocelli", "compound"), "Rotifera": ("eyespots", "cup"),
        "Platyhelminthes": ("pigment cups", "cup"), "Mollusca": ("cups to camera", "lens"), "Annelida": ("cups to lens", "lens"),
        "Nemertea": ("pigment cups", "cup"), "Brachiopoda": ("larval eyespots", "cup"), "Bryozoa": ("larval eyespots", "cup")}),
]
TOKEN = {NONE: "neutral", "gel": "lipid_tail", "mineral": "bone", "hydro": "channel", "rod": "metabolite", "exo": "drug",
         "blind": "highlight", "partial": "lipid_head", "through": "positive",
         "gill": "channel", "lung": "positive",
         "open": "receptor", "closed": "negative",
         "proto": "enzyme", "filter": "channel", "malp": "positive", "other": "lipid_tail",
         "net": "highlight", "ring": "receptor", "cords": "enzyme", "ventral": "drug", "dorsal": "dna",
         "cup": "highlight", "lens": "negative", "compound": "drug"}

fig, ax = bio.canvas(29.8, 15.6)
t = phylo.tree(ax, NEWICK, origin=(0.5, 0.7), width=5.4, height=13.2, direction="right", root_edge=0.25,
               label_size="small", align=True)
for clade, tips, tok in (("Deuterostomia", ("Echinodermata", "Vertebrata"), "dna"),
                         ("Ecdysozoa", ("Priapulida", "Arthropoda"), "drug"),
                         ("Spiralia", ("Rotifera", "Bryozoa"), "positive")):
    ya, yb = (t.node(n).xy[1] for n in tips)
    c = quant.line_color(tok)
    ax.plot([8.75, 8.75], [ya + 0.25, yb - 0.25], color=c, lw=2.2, solid_capstyle="round", zorder=5)
    bio.label(ax, (9.05, (ya + yb) / 2), clade, size="tiny", bold=True, color=c, rotation=90)
x0, cw, ch = 9.45, 2.88, 0.5
for j, (title, cells) in enumerate(COLS):
    xc = x0 + j * cw + cw / 2
    bio.label(ax, (xc, 14.55), title, size="small", bold=True)
    for name, (text, kind) in cells.items():
        y = t.node(name).xy[1]
        tok = TOKEN[kind]
        ax.add_patch(FancyBboxPatch((xc - cw / 2 + 0.07, y - ch / 2), cw - 0.14, ch,
                                    boxstyle="round,pad=0,rounding_size=0.1",
                                    fc=P.light(tok) if kind != NONE else P.light("neutral"),
                                    ec=P.edge(tok), lw=0.5, zorder=4))
        bio.label(ax, (xc, y), text, size="tiny", color=P.muted() if kind == NONE else P.on_fill(), zorder=6)
bio.label(ax, (x0 + 3.5 * cw, 0.2), "Cell colours group identical states; grey = absent or surface only. "
          "Adult states; variation within a phylum summarized.", size="tiny", color=P.muted())
