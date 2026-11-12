# Relationships of the main lineages of Lepidoptera and of Trichoptera, simplified from phylogenomic studies
# (Regier et al. 2013; Kawahara et al. 2019). The mandibulate Micropterigidae are the sister group of all
# other moths; the proboscis arose in Glossata; Ditrysia (separate copulatory and egg-laying openings in the
# female) contain about 98% of species. Butterflies (Papilionoidea, including skippers and the moth-
# butterflies Hedylidae) are one lineage among the moth superfamilies, so that "moths" are paraphyletic.
# Relationships among most apoditrysian superfamilies are left unresolved.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 12.5)
nwk = ("(Trichoptera,(Micropterigidae,(Agathiphagidae,(Heterobathmiidae,(Eriocraniidae,(Hepialoidea,"
       "(Nepticuloidea,(Adeloidea,(Tineoidea,(Gracillarioidea,(Yponomeutoidea,(Gelechioidea,Tortricoidea,"
       "Zygaenoidea,Pyraloidea,Papilionoidea,(Geometroidea,(Bombycoidea,Noctuoidea))Macroheterocera)Apoditrysia)))"
       "Ditrysia))))Glossata)))Lepidoptera)Amphiesmenoptera;")
t = phylo.tree(ax, nwk, origin=(0.2, 0.8), width=14.4, height=11.0, label_size="normal", root_edge=1.6,
               clades=[dict(node="Papilionoidea", token="highlight", style="band", label="butterflies"),
                       dict(node="Ditrysia", token="positive", style="bar", label="Ditrysia")],
               marks=[dict(node="Amphiesmenoptera", kind="trait", text="hairy wings;\nZW females", at=0.5, token="positive"),
                      dict(node="Lepidoptera", kind="trait", text="scales", at=0.5, token="positive"),
                      dict(node="Glossata", kind="trait", text="proboscis", at=0.5, token="enzyme"),
                      dict(node="Ditrysia", kind="trait", text="two female openings", at=0.5, token="positive")])
ys = [t.node(n).xy[1] for n in ("Micropterigidae", "Noctuoidea")]
xb = 20.6
ax.plot([xb, xb], [min(ys) - 0.2, max(ys) + 0.2], color=P.muted(), lw=1.4, ls=(0, (3, 2)))
bio.label(ax, (xb + 0.3, sum(ys) / 2), "\"moths\"\n(paraphyletic\nwithout\nbutterflies)", size="small", color=P.muted(), ha="left")
bio.label(ax, (23.6, 12.1), "Cladogram; branch lengths not to scale", size="tiny", color=P.muted(), ha="right")
