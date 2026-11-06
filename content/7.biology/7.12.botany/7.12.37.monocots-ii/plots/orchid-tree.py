# Relationships of the five orchid subfamilies (Chase et al. 2015; Givnish et al. 2015) with the
# approximate number of species and of fertile stamens. Bars mark the two independent reductions to a
# single fertile stamen (Vanilloideae; the common ancestor of Orchidoideae and Epidendroideae); the star
# marks the origin of the column and of dust seeds (orchids).
import wikibio as bio
from wikibio import phylo

P = bio.P
NEWICK = "(Apostasioideae,(Vanilloideae,(Cypripedioideae,(Orchidoideae,Epidendroideae)OE)COE)VCOE)Orchidaceae;"
fig, ax = bio.canvas(24, 9)
t = phylo.tree(ax, NEWICK, origin=(1.0, 1.0), width=9.0, height=6.6, label_size="normal", root_edge=0.6,
               icons={"Epidendroideae": "phylopic/orchid"}, icon_size=1.2, icon_color="petal",
               marks=[dict(node="Orchidaceae", kind="star", at=0.5, token="highlight", text="column, dust seeds"),
                      dict(node="Vanilloideae", kind="trait", at=0.55, token="negative", text="1 stamen"),
                      dict(node="OE", kind="trait", at=0.5, token="negative", text="1 stamen")])
ROWS = [("Apostasioideae", "~16 spp.", "3 or 2 stamens; powdery pollen"),
        ("Vanilloideae", "~250 spp.", "1 stamen; no pollinia"),
        ("Cypripedioideae", "~170 spp.", "2 stamens + shield staminode"),
        ("Orchidoideae", "~3600 spp.", "1 erect stamen; soft pollinia"),
        ("Epidendroideae", "~21000 spp.", "1 incumbent stamen; hard pollinia")]
ys = [t.node(name).xy[1] for name, _, _ in ROWS]
for i, (name, n, s) in enumerate(ROWS):
    y = ys[i] if ys else 7.6 - i * 1.65
    bio.label(ax, (15.2, y), n, size="small", ha="left")
    bio.label(ax, (17.6, y), s, size="small", ha="left")
