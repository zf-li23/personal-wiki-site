"""The main line of plant evolution: a simplified cladogram from the Archaeplastida to the main angiosperm
clades (after APG IV, PPG I, Christenhusz et al. 2011 and One Thousand Plant Transcriptomes Initiative
2019; branch lengths are not to scale). Brown algae are an outside comparison with a secondary plastid.
Numbered marks: the six key novelties of the course (key below); stars: characters that arose more than
once (multicellularity, roots and leaves, heterospory). Bars: the chapters of the course."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Brown_algae,(Glaucophytes,(Red_algae,((Chlamydomonas,Ulva)Chlorophyta,(Zygnematophyceae,"
          "((Liverworts,Mosses,Hornworts)Bryophytes,(Lycophytes,(Ferns,((Cycads,Ginkgo,(Gnetales,Conifers))Gymno,"
          "(Amborella,(Water_lilies,(Magnoliids,(Monocots,Eudicots)Core)Mesa)ANAm)Angio)Seed)Euph)Vascular)Land)"
          "Strept)Green)Rhodo)Arch)Root;")
ICONS = {
    "Brown algae": "phylopic/kelp", "Red algae": "phylopic/porphyra", "Chlamydomonas": "phylopic/chlamydomonas",
    "Ulva": "phylopic/ulva", "Zygnematophyceae": "phylopic/zygnema", "Liverworts": "phylopic/liverwort",
    "Mosses": "phylopic/moss", "Hornworts": "phylopic/hornwort", "Lycophytes": "phylopic/clubmoss",
    "Ferns": "phylopic/fern", "Cycads": "phylopic/cycad", "Ginkgo": "phylopic/ginkgo", "Gnetales": "phylopic/gnetum",
    "Conifers": "phylopic/pine", "Amborella": "phylopic/amborella", "Water lilies": "phylopic/water-lily",
    "Magnoliids": "phylopic/magnolia", "Monocots": "phylopic/orchid", "Eudicots": "phylopic/asteraceae",
}
KEY = [
    ("Arch", "Plastid from a primary endosymbiosis of a cyanobacterium (two membranes)"),
    ("Red algae", "Multicellularity (independently also in brown and green algae)"),
    ("Land", "Embryo, multicellular sporophyte, jacketed gametangia, cuticle, sporopollenin"),
    ("Vascular", "Lignified xylem, phloem; branched, dominant sporophyte"),
    ("Seed", "Seed: retained megaspore, integument, pollen and pollen tube"),
    ("Angio", "Flower and fruit: closed carpel, double fertilization, triploid endosperm"),
]
STARS = [("Ulva", "green algae: multicellularity"), ("Lycophytes", "lycophytes: roots, microphylls, heterospory"),
         ("Ferns", "ferns: megaphylls, heterospory"), ("Euph", "euphyllophytes: roots")]

fig, ax = bio.canvas(30, 21)
TOP, BOT = 20.0, 5.2
t = phylo.tree(ax, NEWICK, origin=(0.8, BOT), width=12.0, height=TOP - BOT, direction="right", root_edge=0.4,
               label_size="small", italic={"Chlamydomonas", "Ulva", "Ginkgo", "Amborella"}, icons=ICONS,
               icon_color="plant", icon_size=0.62,
               clades=[dict(node="Green", token="chloroplast", style="bar", label="Green plants"),
                       dict(node="Land", token="plant", style="bar", label="Land plants"),
                       dict(node="Seed", token="ovule", style="bar", label="Seed plants")],
               marks=[dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="small", side=-1, offset=0.3,
                           va="bottom") for k, (n, _) in enumerate(KEY)] +
                     [dict(node=n, kind="star", at=0.55) for n, _ in STARS])

# chapter column
CH = {"Brown algae": "8", "Glaucophytes": "7", "Red algae": "7", "Chlamydomonas": "13", "Ulva": "13",
      "Zygnematophyceae": "14", "Liverworts": "15", "Mosses": "15", "Hornworts": "15", "Lycophytes": "16",
      "Ferns": "17", "Cycads": "25-26", "Ginkgo": "25-26", "Gnetales": "25-26", "Conifers": "25-26",
      "Amborella": "34", "Water lilies": "34", "Magnoliids": "35", "Monocots": "36-39", "Eudicots": "40-49"}
XC = 25.4
bio.label(ax, (XC, TOP + 0.75), "Chapter (7.12.x)", size="small", bold=True, ha="left")
for tip in t.tips():
    bio.label(ax, (XC, tip.xy[1]), CH[tip.name], size="small", ha="left", color=P.muted())

# key
bio.label(ax, (1.0, 4.3), "Key novelties", size="normal", bold=True, ha="left")
for k, (_, text) in enumerate(KEY):
    bio.label(ax, (1.0 + (k % 2) * 14.6, 3.5 - (k // 2) * 0.7), f"{k + 1}  {text}", size="small", ha="left")
bio.label(ax, (1.0, 1.1), "Stars, independent origins: " + "; ".join(s for _, s in STARS), size="small", ha="left",
          color=P.muted())
