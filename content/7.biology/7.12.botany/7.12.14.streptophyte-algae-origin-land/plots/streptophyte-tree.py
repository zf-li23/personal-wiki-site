"""Phylogeny of the streptophytes and the stepwise origin of land-plant characters (simplified
cladogram after One Thousand Plant Transcriptomes Initiative 2019 and Puttick et al. 2018).
Numbered marks: origins of characters (key below); x: loss in the Zygnematophyceae."""
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("(Chlorophyta,((Mesostigmatophyceae,Chlorokybophyceae),(Klebsormidiophyceae,(Charophyceae,"
          "(Coleochaetophyceae,(Zygnematophyceae,(((Liverworts,Mosses),Hornworts)Bryophytes,Vascular_plants)"
          "Land_plants)ZL)CZL)Phragmoplastophyta)KP)Streptophyta);")
KEY = [
    ("Streptophyta", "Asymmetrical flagellar apparatus with a multilayered structure; glycolate oxidase; open mitosis"),
    ("KP", "Spindle persists at telophase"),
    ("Phragmoplastophyta", "Phragmoplast and cell plate; rosette cellulose synthase"),
    ("CZL", "Apical growth; plasmodesmata; oogamy, egg retained on the parent (lost in Zygnematophyceae: x)"),
    ("Land plants", "Embryo; multicellular sporophyte, gametangia and sporangia; cuticle; sporopollenin spore wall"),
    ("Vascular plants", "Lignified xylem and phloem; branched, independent sporophyte"),
]
fig, ax = bio.canvas(24, 16.4)
t = phylo.tree(ax, NEWICK, origin=(1.0, 4.8), width=11.6, height=10.8, direction="right", root_edge=0.6, label_size="small",
               icons={"Charophyceae": "phylopic/chara", "Coleochaetophyceae": "phylopic/coleochaete",
                      "Zygnematophyceae": "phylopic/zygnema", "Liverworts": "phylopic/liverwort", "Mosses": "phylopic/moss",
                      "Hornworts": "phylopic/hornwort", "Vascular plants": "phylopic/fern"},
               icon_color="plant", icon_size=0.75,
               clades=[dict(node="Land plants", token="plant", style="bar", label="Land plants"),
                       dict(node="Bryophytes", token="chloroplast", style="bar", label="Bryophytes")],
               marks=[dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="small", side=-1, offset=0.28, va="bottom")
                      for k, (n, _) in enumerate(KEY)] +
                     [dict(node="Zygnematophyceae", kind="loss", text="x", at=0.5, text_size="small", side=-1, offset=0.28,
                           va="bottom")])
bio.label(ax, (7.5, 16.0), "Streptophytes: charophyte algae and land plants", size="normal", bold=True)
for k, (_, text) in enumerate(KEY):
    bio.label(ax, (1.2, 3.8 - k * 0.55), f"{k + 1}  {text}", size="small", ha="left")
