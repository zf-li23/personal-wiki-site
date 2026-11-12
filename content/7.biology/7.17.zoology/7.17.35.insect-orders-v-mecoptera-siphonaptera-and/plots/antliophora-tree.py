# Relationships of the antliophoran orders and of the main lineages of Diptera, simplified from phylogenomic
# studies (Wiegmann et al. 2011; Misof et al. 2014; Tihelka et al. 2020). Fleas are shown inside Mecoptera as
# the sister group of the southern family Nannochoristidae (Tihelka et al. 2020), a placement still debated;
# the lower dipteran lineages are left unresolved except that Bibionomorpha is the sister group of
# Brachycera (Wiegmann et al. 2011), so that "Nematocera" is a grade with respect to Brachycera, and Cyclorrhapha and Schizophora are nested clades.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 12)
nwk = ("(((Boreidae,(Panorpidae,Bittacidae)),(Nannochoristidae,Siphonaptera)),"
       "(Tipulomorpha,Psychodomorpha,Culicomorpha,(Bibionomorpha,"
       "((Tabanomorpha,Stratiomyomorpha),(Asiloidea,(Empidoidea,"
       "((Syrphidae,Phoridae),(Acalyptratae,Calyptratae)Schizophora)Cyclorrhapha)))Brachycera))Diptera)Antliophora;")
t = phylo.tree(ax, nwk, origin=(0.6, 0.8), width=14.5, height=10.4, label_size="normal", root_edge=0.8,
               clades=[dict(node="Siphonaptera", token="negative", style="band", label="fleas"),
                       dict(node="Brachycera", token="positive", style="bar", label="Brachycera"),
                       dict(node="Cyclorrhapha", token="enzyme", style="bar", label="Cyclorrhapha")],
               marks=[dict(node="Antliophora", kind="trait", text="sperm pump", at=0.5, token="positive"),
                      dict(node="Siphonaptera", kind="trait", text="wingless", at=0.5, token="negative"),
                      dict(node="Diptera", kind="trait", text="halteres;\nlegless larvae", at=0.5, token="positive"),
                      dict(node="Brachycera", kind="trait", text="short antennae", at=0.5, token="positive"),
                      dict(node="Cyclorrhapha", kind="trait", text="puparium", at=0.5, token="highlight"),
                      dict(node="Schizophora", kind="trait", text="ptilinum", at=0.5, token="highlight")])
ys = [t.node(n).xy[1] for n in ("Boreidae", "Nannochoristidae")]
xb = 20.0
ax.plot([xb, xb], [min(ys) - 0.2, max(ys) + 0.2], color=P.muted(), lw=1.4, ls=(0, (3, 2)))
bio.label(ax, (xb + 0.3, sum(ys) / 2), "\"Mecoptera\"\n(with fleas?)", size="small", color=P.muted(), ha="left")
ys = [t.node(n).xy[1] for n in ("Tipulomorpha", "Bibionomorpha")]
ax.plot([xb, xb], [min(ys) - 0.2, max(ys) + 0.2], color=P.muted(), lw=1.4, ls=(0, (3, 2)))
bio.label(ax, (xb + 0.3, sum(ys) / 2), "\"Nematocera\"\n(paraphyletic)", size="small", color=P.muted(), ha="left")
bio.label(ax, (23.6, 11.6), "Cladogram; branch lengths not to scale", size="tiny", color=P.muted(), ha="right")
