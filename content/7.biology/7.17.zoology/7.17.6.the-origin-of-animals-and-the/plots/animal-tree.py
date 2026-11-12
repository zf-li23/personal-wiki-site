"""The animal tree of life used throughout this course (cladogram; branch lengths are meaningless).

Topology after Laumer et al. (2019, Proc. R. Soc. B 286: 20190831), Marletaz et al. (2019, Curr. Biol. 29:
312) for Gnathifera and Chaetognatha, Schultz et al. (2023, Nature 618: 110) for ctenophores as the sister
group of all other animals, and the summaries of Giribet & Edgecombe (2020) and Brusca et al. (2023).
Poorly supported or contested relationships are drawn as polytomies; the dashed line marks the alternative
placement of Xenacoelomorpha as sister group of Ambulacraria. Arthropoda is split into its subphyla
(Crustacea is paraphyletic with respect to Hexapoda), Chordata into its three subphyla. Numbers after the
tip names are the chapters of this course that treat the group.
"""

import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = (
    "(Choanoflagellata,(Ctenophora,(Porifera,(Placozoa,(Cnidaria,(Xenacoelomorpha,"
    "(((Echinodermata,Hemichordata)Ambulacraria,(Cephalochordata,(Urochordata,Vertebrata)Olfactores)Chordata)Deuterostomia,"
    "(((Priapulida,Kinorhyncha,Loricifera)Scalidophora,(Nematoda,Nematomorpha)Nematoida,"
    "(Tardigrada,(Onychophora,(Chelicerata,(Myriapoda,(Crustacea,Hexapoda)Pancrustacea)Mandibulata)Arthropoda))Panarthropoda)Ecdysozoa,"
    "((Chaetognatha,(Gnathostomulida,(Micrognathozoa,Rotifera)))Gnathifera,(Platyhelminthes,Gastrotricha)Rouphozoa,Dicyemida,"
    "((Entoprocta,Cycliophora),Mollusca,(Annelida,Nemertea),(Bryozoa,(Phoronida,Brachiopoda))Lophophorata)Lophotrochozoa)Spiralia)Protostomia)Nephrozoa)Bilateria)"
    "Planulozoa)ParaHoxozoa)Myriazoa)Metazoa);")
CH = {"Choanoflagellata": "", "Ctenophora": "8", "Porifera": "7", "Placozoa": "8", "Cnidaria": "9", "Xenacoelomorpha": "10",
      "Echinodermata": "42", "Hemichordata": "41", "Cephalochordata": "43", "Urochordata": "43", "Vertebrata": "44–67",
      "Priapulida": "17", "Kinorhyncha": "17", "Loricifera": "17", "Nematoda": "17", "Nematomorpha": "17",
      "Tardigrada": "18", "Onychophora": "18", "Chelicerata": "19", "Myriapoda": "20", "Crustacea": "21",
      "Hexapoda": "22–40", "Chaetognatha": "12", "Gnathostomulida": "12", "Micrognathozoa": "12", "Rotifera": "12",
      "Platyhelminthes": "11", "Gastrotricha": "11", "Dicyemida": "12", "Entoprocta": "16", "Cycliophora": "16",
      "Mollusca": "13–14", "Annelida": "15", "Nemertea": "16", "Bryozoa": "16", "Phoronida": "16", "Brachiopoda": "16"}
NAME = {"Choanoflagellata": "Choanoflagellates (outgroup)", "Crustacea": "Crustacea (paraphyletic)",
        "Rotifera": "Rotifera (incl. Acanthocephala)", "Annelida": "Annelida (incl. sipunculans)",
        "Dicyemida": "Dicyemida (position uncertain)", "Xenacoelomorpha": "Xenacoelomorpha"}
TEXT = {k: (NAME.get(k, k) + (f"   {v}" if v else "")) for k, v in CH.items()}
ICONS = {
    "Choanoflagellata": "phylopic/choanoflagellate", "Ctenophora": "phylopic/comb-jelly", "Porifera": "phylopic/sponge",
    "Placozoa": "phylopic/placozoan", "Cnidaria": "phylopic/jellyfish", "Echinodermata": "phylopic/starfish",
    "Cephalochordata": "phylopic/amphioxus", "Urochordata": "phylopic/ciona", "Vertebrata": "phylopic/zebrafish",
    "Nematoda": ("phylopic/c-elegans", {"rotate": 90}), "Tardigrada": "phylopic/tardigrade",
    "Onychophora": ("phylopic/velvet-worm", {"rotate": 90}), "Chelicerata": "phylopic/spider", "Myriapoda": "phylopic/centipede",
    "Crustacea": "phylopic/copepod", "Hexapoda": "phylopic/drosophila", "Platyhelminthes": "phylopic/planarian",
    "Mollusca": "phylopic/snail", "Annelida": "phylopic/earthworm",
}
KEY = [("Metazoa", "multicellularity, epithelia, collagen"), ("ParaHoxozoa", "Hox/ParaHox genes"),
       ("Bilateria", "bilateral symmetry, mesoderm"), ("Nephrozoa", "nephridia, through gut"),
       ("Deuterostomia", "pharyngeal slits"), ("Chordata", "notochord, dorsal nerve cord"),
       ("Ecdysozoa", "molted cuticle"), ("Panarthropoda", "paired segmental limbs"),
       ("Spiralia", "spiral cleavage"), ("Lophophorata", "lophophore")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.55, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(KEY)]

fig, ax = bio.canvas(24.0, 24.6)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.8), width=11.6, height=23.0, direction="right", root_edge=0.4,
               tip_text=TEXT, icons=ICONS, icon_size=0.62, icon_width=1.0, label_size="small",
               clades=[dict(node="Deuterostomia", token="dna", style="band", label="Deuterostomia"),
                       dict(node="Ecdysozoa", token="atp", style="band", label="Ecdysozoa"),
                       dict(node="Spiralia", token="positive", style="band", label="Spiralia"),
                       dict(node="Lophotrochozoa", token="positive", style="bar", label="Lophotrochozoa"),
                       dict(node="Gnathifera", token="positive", style="bar", label="Gnathifera")],
               marks=MARKS)
xen = t.node("Xenacoelomorpha")
amb = t.node("Ambulacraria")
a0 = (xen.xy[0] - 2.0, xen.xy[1] - 0.05)
bio.arrow(ax, a0, (amb.xy[0] + 0.2, amb.xy[1] + 0.1), kind="link", bend=0.15, dashed=True, color=P.muted(), lw=1.0)
bio.label(ax, (a0[0] - 0.2, a0[1] - 0.6), "alternative: sister to\nAmbulacraria", size="tiny", color=P.muted(), ha="right")
for name in ("Metazoa", "ParaHoxozoa", "Bilateria", "Nephrozoa", "Protostomia"):
    nd = t.node(name)
    bio.label(ax, (nd.xy[0] - 0.06, nd.xy[1] - 0.3), name, size="tiny", bold=True, ha="right", va="top", color=P.muted())
x0, y0 = 0.9, 7.2
bio.label(ax, (x0, y0 + 0.5), "Key characters", size="small", bold=True, ha="left")
for k, (_, text) in enumerate(KEY):
    yy = y0 - k * 0.42
    phylo.marker(ax, (x0 + 0.12, yy), "trait", size=0.14, direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {text}", size="tiny", ha="left")
bio.label(ax, (0.9, 2.2), "Numbers after names:\nchapters 7.17.n", size="tiny", ha="left", color=P.muted())
