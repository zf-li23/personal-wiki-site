# Phylogeny of Cnidaria (after Kayal et al. 2018; Chang et al. 2015) with key characters mapped.
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = ("((Octocorallia,(Ceriantharia,Hexacorallia))Anthozoa,"
          "((Polypodiozoa,Myxozoa)Endocnidozoa,(Hydrozoa,(Staurozoa,(Cubozoa,Scyphozoa)Rhopaliophora)Acraspeda)Medusozoa)MedEndo)Cnidaria;")
TEXT = {"Polypodiozoa": "Polypodiozoa (Polypodium)"}
ICONS = {"Hexacorallia": "phylopic/nematostella", "Hydrozoa": "phylopic/hydra", "Scyphozoa": "phylopic/jellyfish"}
CHARS = [("Cnidaria", "Cnidae; planula larva"),
         ("Anthozoa", "Actinopharynx, siphonoglyphs, mesenteries"),
         ("MedEndo", "Linear mitochondrial genome"),
         ("Medusozoa", "Medusa stage, cnidocil"),
         ("Hydrozoa", "Velum"),
         ("Rhopaliophora", "Rhopalia"),
         ("Scyphozoa", "Strobilation"),
         ("Endocnidozoa", "Parasitism; loss of nerves and gut")]
MARKS = [dict(node=n, kind="trait", text=str(k + 1), at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")
         for k, (n, _) in enumerate(CHARS)]
MARKS.append(dict(node="Staurozoa", kind="loss", at=0.5))

fig, ax = bio.canvas(19.0, 11.0)
t = phylo.tree(ax, NEWICK, origin=(0.8, 3.6), width=9.0, height=7.0, root_edge=0.8, tip_text=TEXT, icons=ICONS,
               icon_size=0.7, icon_width=1.1, label_size="small",
               clades=[dict(node="Anthozoa", token="positive", style="bar", label="Anthozoa"),
                       dict(node="Medusozoa", token="dna", style="bar", label="Medusozoa"),
                       dict(node="Endocnidozoa", token="negative", style="bar", label="Endocnidozoa")],
               marks=MARKS)
y = 2.9
for k, (_, txt) in enumerate(CHARS):
    col, row = divmod(k, 4)
    x0, yy = 1.0 + col * 8.6, y - row * 0.6
    phylo.marker(ax, (x0, yy), "trait", direction=(1, 0))
    bio.label(ax, (x0 + 0.35, yy), f"{k + 1}  {txt}", size="small", ha="left")
phylo.marker(ax, (9.6, 0.3), "loss", direction=(1, 0))
bio.label(ax, (9.95, 0.3), "Free-swimming medusa lost (sessile stauromedusa)", size="small", ha="left")
