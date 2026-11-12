# Relationships of the hexapods (cladogram; consensus of phylogenomic studies such as Misof et al. 2014,
# with the relationships among the three entognathan orders (unresolved here), the monophyly of Entognatha and of Palaeoptera still debated). Marks give
# the characters that diagnose each clade.
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(24, 11)
nwk = ("((Collembola,Protura,Diplura)Entognatha,(Archaeognatha,(Zygentoma,((Ephemeroptera,Odonata)Palaeoptera,"
       "(Polyneoptera,(Paraneoptera,Holometabola)Eumetabola)Neoptera)Pterygota)Dicondylia)Insecta)Hexapoda;")
t = phylo.tree(ax, nwk, origin=(0.6, 0.8), width=16.5, height=9.4, label_size="normal", root_edge=1.5,
               clades=[dict(node="Entognatha", token="neutral", style="band", label="Entognatha"),
                       dict(node="Pterygota", token="enzyme", style="band", label="Pterygota")],
               marks=[dict(node="Hexapoda", kind="trait", text="3-segmented thorax;\nlabium; tentorium", at=0.45, token="positive"),
                      dict(node="Entognatha", kind="trait", text="mouthparts in a\nhead pocket", token="neutral"),
                      dict(node="Insecta", kind="trait", text="unmuscled flagellum;\nJohnston's organ", token="positive", at=0.4, shift=(-0.25, 0)),
                      dict(node="Dicondylia", kind="trait", text="dicondylic mandible", token="positive"),
                      dict(node="Pterygota", kind="trait", text="wings; adults do not molt", token="positive"),
                      dict(node="Neoptera", kind="trait", text="wing folding", token="positive"),
                      dict(node="Holometabola", kind="trait", text="pupa", token="positive", at=0.6)])
bio.label(ax, (23.6, 0.5), "Cladogram; branch lengths not to scale", size="tiny", color=P.muted(), ha="right")
