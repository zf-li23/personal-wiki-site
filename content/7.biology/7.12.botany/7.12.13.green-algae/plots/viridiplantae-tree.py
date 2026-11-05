"""Phylogeny of the green plants (simplified cladogram after Leliaert et al. 2012 and One Thousand Plant
Transcriptomes Initiative 2019; the order among the core chlorophyte classes and among the early
prasinophyte lineages, the three classes at the top, is not fully resolved). Numbered marks: origins of characters (key below)."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Palmophyllophyceae,(Mamiellophyceae,(Pyramimonadophyceae,(Chlorodendrophyceae,(Trebouxiophyceae,"
          "(Ulvophyceae,Chlorophyceae)))Core_chlorophytes)))Chlorophyta,((Mesostigmatophyceae,Chlorokybophyceae),"
          "(Klebsormidiophyceae,(Charophyceae,(Coleochaetophyceae,(Zygnematophyceae,Land_plants)))Phragmoplastophyta))"
          "Streptophyta)Viridiplantae;")
KEY = [
    ("Viridiplantae", "Chlorophyll b; starch stored inside the plastid; no phycobilisomes"),
    ("Chlorophyta", "Cruciate, symmetrical flagellar roots (X-2-X-2)"),
    ("Chlorophyceae", "Phycoplast (also in Trebouxiophyceae)"),
    ("Streptophyta", "Asymmetrical flagellar apparatus with a multilayered structure; glycolate oxidase"),
    ("Phragmoplastophyta", "Phragmoplast and cell plate; rosette cellulose synthase"),
    ("Land plants", "Embryo, multicellular sporophyte, cuticle, sporopollenin-walled spores"),
]

fig, ax = bio.canvas(21, 17.6)
t = phylo.tree(ax, NEWICK, origin=(1.0, 4.6), width=11.0, height=12.4, direction="right", root_edge=0.6,
               label_size="small", icons={
                   "Chlorophyceae": "phylopic/volvox", "Ulvophyceae": "phylopic/ulva", "Charophyceae": "phylopic/chara",
                   "Coleochaetophyceae": "phylopic/coleochaete", "Zygnematophyceae": "phylopic/zygnema",
                   "Land plants": "phylopic/moss"},
               icon_color="plant", icon_size=0.75,
               clades=[dict(node="Chlorophyta", token="chloroplast", style="bar", label="Chlorophyta"),
                       dict(node="Streptophyta", token="plant", style="bar", label="Streptophyta")],
               marks=[dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="small", side=-1, offset=0.28, va="bottom")
                      for k, (n, _) in enumerate(KEY)] +
                     [dict(node="Trebouxiophyceae", kind="trait", text="3", at=0.5, text_size="small", side=-1, offset=0.28,
                           va="bottom")])
bio.label(ax, (8.0, 17.2), "Green plants (Viridiplantae)", size="normal", bold=True)
y = 3.6
for k, (_, text) in enumerate(KEY):
    bio.label(ax, (1.2, y - k * 0.55), f"{k + 1}  {text}", size="small", ha="left")
