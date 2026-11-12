# Relationships of the main lineages of Hymenoptera, simplified from phylogenomic studies (Peters et al.
# 2017; Branstetter et al. 2017; Blaimer et al. 2023). "Symphyta" (sawflies and wood wasps) are
# paraphyletic with respect to the parasitoid wood wasps (Orussidae) plus Apocrita; parasitoid Apocrita
# ("Parasitica") are paraphyletic with respect to the stinging wasps (Aculeata); ants are the sister group
# of Apoidea, and bees arose within the apoid wasps.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 12)
nwk = ("(Xyelidae,(Tenthredinoidea,(Pamphilioidea,(Cephidae,(Siricidae,(Orussidae,(("
       "Ichneumonoidea,(Chalcidoidea,Cynipoidea)Proctotrupomorpha),(Evanioidea,(Chrysidoidea,(Vespoidea,"
       "(Formicidae,(Sphecid_wasps,Bees)Apoidea)))Aculeata))Apocrita)Parasitoidida)))))Hymenoptera;")
nwk = nwk.replace("Sphecid_wasps", "'apoid wasps'")
t = phylo.tree(ax, nwk, origin=(0.6, 0.8), width=15.0, height=10.4, label_size="normal", root_edge=0.8,
               clades=[dict(node="Aculeata", token="enzyme", style="band", label="Aculeata"),
                       dict(node="Apocrita", token="positive", style="bar", label="Apocrita")],
               marks=[dict(node="Hymenoptera", kind="trait", text="hamuli; haplodiploidy", at=0.5, token="positive"),
                      dict(node="Parasitoidida", kind="trait", text="parasitoid larvae", at=0.5, token="positive"),
                      dict(node="Apocrita", kind="trait", text="wasp waist; legless larvae", at=0.5, token="positive"),
                      dict(node="Aculeata", kind="trait", text="ovipositor becomes a sting", at=0.5, token="highlight"),
                      dict(node="Bees", kind="trait", text="pollen diet;\nbranched hairs", at=0.5, token="positive")])
ys = [t.node(n).xy[1] for n in ("Xyelidae", "Siricidae")]
xb = 21.2
ax.plot([xb, xb], [min(ys) - 0.2, max(ys) + 0.2], color=P.muted(), lw=1.4, ls=(0, (3, 2)))
bio.label(ax, (xb + 0.3, sum(ys) / 2), "\"Symphyta\"\n(paraphyletic)", size="small", color=P.muted(), ha="left")
bio.label(ax, (23.6, 11.6), "Cladogram; branch lengths not to scale", size="tiny", color=P.muted(), ha="right")
