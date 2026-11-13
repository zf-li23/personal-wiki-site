"""The assembly of animal body plans along the tree of this course (cladogram; branch lengths are meaningless).

Topology as in the tree of 7.17.6 (ctenophores as the sister group of all other animals, Xenacoelomorpha as the
sister group of Nephrozoa), with the arthropods resolved to the main hexapod lineages after Misof et al. (2014)
and the vertebrates to the living classes and major clades (turtles as the sister group of archosaurs, birds
within archosaurs). Pterosaurs are omitted. Poorly resolved relationships are drawn as polytomies. Crustacea,
the wingless hexapods and the lobe-finned fishes are paraphyletic tip groups. Numbered bars mark the node at
which the main body-plan characters treated in the course arose; the key gives one or two characters per node.
Crossed bars mark well-known secondary losses or reversals.
"""

import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = (
    "(Choanoflagellata,(Ctenophora,(Porifera,(Placozoa,(Cnidaria,(Xenacoelomorpha,"
    "(((Gnathifera,Platyhelminthes,(Mollusca,Annelida,Nemertea,Lophophorata)Lophotrochozoa)Spiralia,"
    "((Nematoida,Scalidophora),(Tardigrada,(Onychophora,(Chelicerata,(Myriapoda,(Crustacea,"
    "(Wingless,(Palaeoptera,(Polyneoptera,(Paraneoptera,Holometabola)Eumetabola)Neoptera)Pterygota)Hexapoda)"
    "Pancrustacea)Mandibulata)Arthropoda))Panarthropoda)Ecdysozoa)Protostomia,"
    "((Echinodermata,Hemichordata)Ambulacraria,(Cephalochordata,(Tunicata,(Cyclostomata,(Chondrichthyes,"
    "(Actinopterygii,(Lobefins,(Lissamphibia,(Mammalia,(Lepidosauria,(Testudines,(Crocodylia,Aves)Archosauria))"
    "Sauropsida)Amniota)Tetrapoda)Sarcopterygii)Osteichthyes)Gnathostomata)Vertebrata)Olfactores)Chordata)"
    "Deuterostomia)Nephrozoa)Bilateria)Planulozoa)ParaHoxozoa)Myriazoa)Metazoa);")

NAME = {"Choanoflagellata": "Choanoflagellates (outgroup)", "Gnathifera": "Gnathifera (rotifers, arrow worms)",
        "Lophophorata": "Lophophorates", "Nematoida": "Nematodes, horsehair worms", "Scalidophora": "Priapulids and kin",
        "Crustacea": "Crustaceans (paraphyletic)", "Wingless": "Wingless hexapods", "Polyneoptera": "Polyneoptera",
        "Holometabola": "Holometabola", "Cyclostomata": "Cyclostomes", "Chondrichthyes": "Cartilaginous fishes",
        "Actinopterygii": "Ray-finned fishes", "Lobefins": "Coelacanths, lungfishes", "Lissamphibia": "Amphibians",
        "Mammalia": "Mammals", "Lepidosauria": "Lizards, snakes, tuatara", "Testudines": "Turtles",
        "Crocodylia": "Crocodylians", "Aves": "Birds"}
ICONS = {
    "Choanoflagellata": "phylopic/choanoflagellate", "Ctenophora": "phylopic/comb-jelly", "Porifera": "phylopic/sponge",
    "Placozoa": "phylopic/placozoan", "Cnidaria": "phylopic/jellyfish", "Platyhelminthes": "phylopic/planarian",
    "Mollusca": "phylopic/snail", "Annelida": "phylopic/earthworm", "Nemertea": "phylopic/ribbon-worm",
    "Lophophorata": "phylopic/lingula", "Nematoida": ("phylopic/c-elegans", {"rotate": 90}),
    "Scalidophora": "phylopic/priapulid", "Tardigrada": "phylopic/tardigrade",
    "Onychophora": ("phylopic/velvet-worm", {"rotate": 90}), "Chelicerata": "phylopic/spider",
    "Myriapoda": "phylopic/centipede", "Crustacea": "phylopic/crab", "Wingless": "phylopic/silverfish",
    "Palaeoptera": "phylopic/dragonfly", "Polyneoptera": "phylopic/grasshopper", "Paraneoptera": "phylopic/cicada",
    "Holometabola": "phylopic/beetle", "Echinodermata": "phylopic/starfish", "Hemichordata": "phylopic/acorn-worm",
    "Cephalochordata": "phylopic/amphioxus", "Tunicata": "phylopic/ciona", "Cyclostomata": "phylopic/lamprey",
    "Chondrichthyes": "phylopic/dogfish", "Actinopterygii": "phylopic/carp", "Lobefins": "phylopic/coelacanth",
    "Lissamphibia": "phylopic/frog", "Mammalia": "phylopic/rabbit", "Lepidosauria": "phylopic/lizard",
    "Testudines": "phylopic/turtle", "Crocodylia": "phylopic/crocodile", "Aves": "phylopic/pigeon",
}
KEY = [
    ("Metazoa", "multicellularity, epithelia on collagen, flagellated sperm"),
    ("ParaHoxozoa", "Hox and ParaHox genes"),
    ("Planulozoa", "Wnt-patterned axis, ciliated larva with apical organ"),
    ("Bilateria", "bilateral symmetry, mesoderm, cephalization"),
    ("Nephrozoa", "through gut, nephridia"),
    ("Spiralia", "spiral cleavage with 4d mesoderm"),
    ("Ecdysozoa", "molted cuticle, no locomotory cilia"),
    ("Panarthropoda", "paired clawed limbs, hemocoel, segments"),
    ("Arthropoda", "jointed exoskeleton, tagmata, compound eyes"),
    ("Pterygota", "wings"),
    ("Neoptera", "wing folding"),
    ("Holometabola", "pupa, imaginal discs"),
    ("Deuterostomia", "pharyngeal slits"),
    ("Chordata", "notochord, dorsal hollow nerve cord, endostyle"),
    ("Vertebrata", "neural crest, placodes, cranium, mineralized tissues"),
    ("Gnathostomata", "jaws, paired fins, second genome duplication"),
    ("Osteichthyes", "endochondral bone, lungs, marginal jaw bones"),
    ("Tetrapoda", "limbs with digits"),
    ("Amniota", "amniotic egg, waterproof keratinized skin"),
    ("Mammalia", "hair, mammary glands, three ear ossicles"),
    ("Aves", "flight; feathers and endothermy arose in the dinosaur stem"),
]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.55, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(KEY)]
LOSSES = [("Platyhelminthes", "a"), ("Echinodermata", "b"), ("Annelida", "c")]
LOSS_TEXT = {"a": "flatworms: anus and coelom lost or never present",
             "b": "echinoderms: pentaradial adults, slits lost",
             "c": "sipunculans, echiurans: segmentation lost"}
MARKS += [dict(node=n, kind="loss", text=t, at=0.25, text_size="tiny", side=-1, offset=0.3, va="bottom")
          for n, t in LOSSES]

fig, ax = bio.canvas(30.6, 27.0)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.8), width=12.6, height=25.4, direction="right", root_edge=0.4,
               tip_text=NAME, icons=ICONS, icon_size=0.58, icon_width=0.95, label_size="small",
               clades=[dict(node="Spiralia", token="positive", style="band", label="Spiralia"),
                       dict(node="Ecdysozoa", token="atp", style="band", label="Ecdysozoa"),
                       dict(node="Deuterostomia", token="dna", style="band", label="Deuterostomia")],
               marks=MARKS)
for name in ("Metazoa", "Bilateria", "Nephrozoa", "Protostomia", "Vertebrata", "Amniota"):
    nd = t.node(name)
    bio.label(ax, (nd.xy[0] - 0.06, nd.xy[1] - 0.3), name, size="tiny", bold=True, ha="right", va="top", color=P.muted())

x0, y0 = 21.0, 21.4
bio.label(ax, (x0, y0 + 0.55), "Innovations at the nodes", size="small", bold=True, ha="left")
for k, (_, text) in enumerate(KEY):
    yy = y0 - k * 0.4
    phylo.marker(ax, (x0 + 0.12, yy), "trait", size=0.14, direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {text}", size="tiny", ha="left")
yy = y0 - len(KEY) * 0.4 - 0.25
for code in ("a", "b", "c"):
    phylo.marker(ax, (x0 + 0.12, yy), "loss", size=0.14, direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{code}  {LOSS_TEXT[code]}", size="tiny", ha="left")
    yy -= 0.4
