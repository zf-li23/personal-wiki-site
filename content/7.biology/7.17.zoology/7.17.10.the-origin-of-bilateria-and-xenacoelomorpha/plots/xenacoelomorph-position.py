# Two hypotheses for the position of Xenacoelomorpha: A, sister to Nephrozoa (Cannon et al. 2016);
# B, sister to Ambulacraria within Deuterostomia (Xenambulacraria; Philippe et al. 2019).
import wikibio as bio
from wikibio import phylo

P = bio.P
A = "(Cnidaria,(Xenacoelomorpha,((Ambulacraria,Chordata)Deuterostomia,(Ecdysozoa,Spiralia)Protostomia)Nephrozoa)Bilateria);"
B = "(Cnidaria,(((Xenacoelomorpha,Ambulacraria)Xenambulacraria,Chordata)Deuterostomia,(Ecdysozoa,Spiralia)Protostomia)Bilateria);"
ICONS = {"Cnidaria": "phylopic/jellyfish", "Ambulacraria": "phylopic/starfish", "Chordata": "phylopic/zebrafish",
         "Ecdysozoa": "phylopic/drosophila", "Spiralia": "phylopic/snail"}
HL = [dict(tips=["Xenacoelomorpha"], token="highlight", style="branch")]

fig, ax = bio.canvas(25, 8.8)
bio.panel(ax, "A", (0.2, 8.6))
bio.label(ax, (5.2, 8.4), "Nephrozoa hypothesis", size="title", bold=True)
phylo.tree(ax, A, origin=(0.8, 1.6), width=6.4, height=6.0, root_edge=0.5, icons=ICONS, icon_size=0.6, icon_width=1.0,
           label_size="small", clades=HL,
           marks=[dict(node="Nephrozoa", kind="trait", text="1–3", at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom")])
bio.panel(ax, "B", (12.8, 8.6))
bio.label(ax, (17.8, 8.4), "Xenambulacraria hypothesis", size="title", bold=True)
phylo.tree(ax, B, origin=(13.4, 1.6), width=6.4, height=6.0, root_edge=0.5, icons=ICONS, icon_size=0.6, icon_width=1.0,
           label_size="small", clades=HL,
           marks=[dict(node="Bilateria", kind="trait", text="1–3", at=0.5, text_size="tiny", side=-1, offset=0.3, va="bottom"),
                  dict(node="Xenacoelomorpha", kind="loss", at=0.35)])
y = 0.7
phylo.marker(ax, (1.0, y), "trait", direction=(1, 0))
bio.label(ax, (1.35, y), "Gain: (1) anus, (2) nephridia, (3) centralized nervous system", size="small", ha="left")
phylo.marker(ax, (13.6, y), "loss", direction=(1, 0))
bio.label(ax, (13.95, y), "Loss of 1–3 in Xenacoelomorpha", size="small", ha="left")
