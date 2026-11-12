# Relationships of the paraneopteran orders and of the suborders of Hemiptera, simplified from
# phylogenomic studies (Misof et al. 2014; Johnson et al. 2018). The former order Homoptera (shaded:
# Sternorrhyncha, Auchenorrhyncha and Coleorrhyncha) is paraphyletic with respect to the true bugs
# (Heteroptera). Marks give characters of each clade.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 10.5)
nwk = ("(Psocodea,(Thysanoptera,(Sternorrhyncha,((Fulgoromorpha,Cicadomorpha)Auchenorrhyncha,"
       "(Coleorrhyncha,Heteroptera)Heteropterodea)Euhemiptera)Hemiptera)Condylognatha)Paraneoptera;")
t = phylo.tree(ax, nwk, origin=(0.6, 0.8), width=14.5, height=8.8, label_size="normal", root_edge=1.2,
               clades=[dict(node="Heteroptera", token="enzyme", style="band", label=""),
                       dict(node="Hemiptera", token="enzyme", style="bar", label="Hemiptera")],
               marks=[dict(node="Paraneoptera", kind="trait", text="cibarial pump; slender lacinia;\nno cerci; tarsi 3 or fewer",
                           at=0.5, token="positive"),
                      dict(node="Psocodea", kind="trait", text="lice arose within bark lice", at=0.55, token="positive"),
                      dict(node="Condylognatha", kind="trait", text="stylet mouthparts", at=0.5, token="positive"),
                      dict(node="Thysanoptera", kind="trait", text="right mandible lost;\nfringed wings", at=0.55, token="positive"),
                      dict(node="Hemiptera", kind="trait", text="labial beak sheathing\nfour stylets", at=0.5, token="positive"),
                      dict(node="Sternorrhyncha", kind="trait", text="beak between fore coxae", at=0.6, token="positive"),
                      dict(node="Heteroptera", kind="trait", text="hemelytra; scent glands", at=0.55, token="positive")])
bio.label(ax, (23.6, 10.1), "Cladogram; branch lengths not to scale", size="tiny", color=P.muted(), ha="right")
# the former Homoptera: a dashed bracket over the four tips that are not Heteroptera
ys = [t.node(n).xy[1] for n in ("Sternorrhyncha", "Fulgoromorpha", "Cicadomorpha", "Coleorrhyncha")]
xb = 21.0
ax.plot([xb, xb], [min(ys) - 0.2, max(ys) + 0.2], color=P.muted(), lw=1.4, ls=(0, (3, 2)))
bio.label(ax, (xb + 0.3, sum(ys) / 4), "former\n\"Homoptera\"\n(paraphyletic)", size="small", color=P.muted(), ha="left")
