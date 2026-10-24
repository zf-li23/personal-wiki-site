# Relationships of the major animal phyla (cladogram; choanoflagellates as outgroup), after current
# phylogenomic consensus: ctenophores as sister to all other animals (Schultz et al. 2023, Nature 618:110;
# the alternative, sponges first, is not excluded), Placozoa sister to Cnidaria + Bilateria, Xenacoelomorpha
# sister to Nephrozoa (alternatively sister to Ambulacraria, the "Xenambulacraria" hypothesis: dashed).
# Protostomes split into Ecdysozoa (moulting animals) and Spiralia (Lophotrochozoa in the wide sense).
# Numbered bars mark where key innovations arose (key, lower left).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Choanoflagellata,(Ctenophora,(Porifera,(Placozoa,(Cnidaria,(Xenacoelomorpha,"
          "((Echinodermata,Chordata)Deuterostomia,"
          "((Nematoda,(Tardigrada,(Onychophora,Arthropoda)Panarthropoda))Ecdysozoa,"
          "(Platyhelminthes,(Mollusca,Annelida)Lophotrochozoa)Spiralia)Protostomia)Nephrozoa)Bilateria)"
          "Planulozoa)ParaHoxozoa)Myriazoa)Metazoa);")

TEXT = {"Choanoflagellata": "Choanoflagellates", "Xenacoelomorpha": "Xenacoelomorpha (?)"}

ICONS = {
    "Choanoflagellata": "phylopic/choanoflagellate", "Ctenophora": "phylopic/comb-jelly", "Porifera": "phylopic/sponge",
    "Placozoa": "phylopic/placozoan", "Cnidaria": "phylopic/jellyfish", "Echinodermata": "phylopic/starfish",
    "Chordata": "phylopic/zebrafish", "Nematoda": ("phylopic/c-elegans", {"rotate": 90}), "Tardigrada": "phylopic/tardigrade",
    "Onychophora": ("phylopic/velvet-worm", {"rotate": 90}), "Arthropoda": "phylopic/drosophila", "Platyhelminthes": "phylopic/planarian",
    "Mollusca": "phylopic/snail", "Annelida": "phylopic/earthworm",
}

INNOVATIONS = [
    ("Metazoa", "Multicellularity, epithelia, collagen"),
    ("ParaHoxozoa", "Hox/ParaHox genes"),
    ("Bilateria", "Bilateral symmetry, mesoderm"),
    ("Nephrozoa", "Nephridia, through-gut (mouth and anus)"),
    ("Deuterostomia", "Pharyngeal gill slits"),
    ("Chordata", "Notochord, dorsal hollow nerve cord"),
    ("Ecdysozoa", "Cuticle moulted (ecdysis)"),
    ("Panarthropoda", "Paired segmental limbs"),
    ("Spiralia", "Spiral cleavage"),
    ("Mollusca", "Mantle, radula"),
    ("Annelida", "Segmented coelom, chaetae"),
]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.55, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(INNOVATIONS)]

fig, ax = bio.canvas(19.6, 15.2)
t = phylo.tree(ax, NEWICK, origin=(1.0, 0.8), width=11.2, height=13.6, direction="right", root_edge=0.5,
               tip_text=TEXT, icons=ICONS, icon_size=0.75, icon_width=1.25, label_size="small",
               clades=[dict(node="Deuterostomia", token="dna", style="band", label="Deuterostomia"),
                       dict(node="Ecdysozoa", token="atp", style="band", label="Ecdysozoa"),
                       dict(node="Spiralia", token="positive", style="band", label="Spiralia"),
                       dict(node="Lophotrochozoa", token="positive", style="bar", label="Lophotrochozoa")],
               marks=MARKS)

# uncertain placements
xen = t.node("Xenacoelomorpha")
ech = t.node("Echinodermata")
deu = t.node("Deuterostomia")
a0 = (xen.xy[0] - 1.8, xen.xy[1] - 0.06)
bio.arrow(ax, a0, (deu.xy[0] + 0.3, ech.xy[1] + 0.06), kind="link", bend=0.18, dashed=True, color=P.muted(), lw=1.0)
bio.label(ax, (a0[0] - 0.25, a0[1] - 0.45), "alternative: sister to\nAmbulacraria (Xenambulacraria)", size="tiny",
          color=P.muted(), ha="right", va="center")
for name, text in (("Metazoa", "Metazoa"), ("Bilateria", "Bilateria"), ("Nephrozoa", "Nephrozoa"),
                   ("Protostomia", "Protostomia")):
    nd = t.node(name)
    bio.label(ax, (nd.xy[0] - 0.06, nd.xy[1] - 0.32), text, size="tiny", bold=True, ha="right", va="top", color=P.muted())
root = t.node("Metazoa")
bio.label(ax, (root.xy[0] + 0.15, root.xy[1] + 0.25), "?", size="normal", bold=True, color=P.muted(), ha="left", va="bottom")

# key of innovations
x0, y0 = 0.9, 4.3
bio.label(ax, (x0, y0 + 0.45), "Key innovations", size="small", bold=True, ha="left")
for k, (_, text) in enumerate(INNOVATIONS):
    yy = y0 - k * 0.36
    phylo.marker(ax, (x0 + 0.12, yy), "trait", size=0.14, direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {text}", size="tiny", ha="left")
