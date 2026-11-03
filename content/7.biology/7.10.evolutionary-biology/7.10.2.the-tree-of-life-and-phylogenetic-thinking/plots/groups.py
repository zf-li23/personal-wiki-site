"""Monophyletic, paraphyletic and polyphyletic groups on one tree of amniotes, and crown and stem
groups. A: Archosauria (crocodiles and birds) is monophyletic: an ancestor and all its descendants.
The traditional class Reptilia (lizards and snakes, turtles, crocodiles, without birds) is
paraphyletic: it omits some descendants of its common ancestor. "Warm-blooded animals" (birds and
mammals) is polyphyletic: endothermy evolved twice, and the group excludes the common ancestor's
other descendants. B: the crown group Aves is the most recent common ancestor of living birds and all
its descendants; extinct relatives that branched off the lineage below it (Archaeopteryx, non-avian
dinosaurs such as Tyrannosaurus) form the stem group; crown plus stem is the total group."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(26, 10.4)

bio.panel(ax, "A", (0.2, 10.2))
NW = "(Mammals,((Lizards_and_snakes,Turtles),(Crocodiles,Birds)Archosauria)Reptiles)Amniota;"
ICONS = {"Mammals": "phylopic/mouse", "Lizards and snakes": "phylopic/lizard", "Turtles": "phylopic/turtle",
         "Crocodiles": "phylopic/crocodile", "Birds": "phylopic/pigeon"}
t = phylo.tree(ax, NW, origin=(1.4, 2.2), width=10.0, height=5.2, direction="up", icons=ICONS, icon_size=0.7,
               label_size="small", root_edge=0.4,
               clades=[dict(node="Archosauria", token="positive", style="branch")])
xs = {n.name: n.xy[0] for n in t.tips()}
y0 = 1.2
def bar(names, y, tok, text):
    a, b = min(xs[n] for n in names), max(xs[n] for n in names)
    ax.plot([a - 0.5, b + 0.5], [y, y], color=P.edge(tok), lw=4, solid_capstyle="round")
    bio.label(ax, ((a + b) / 2, y - 0.35), text, size="tiny", va="top")
bar(["Crocodiles", "Birds"], 1.25, "positive", "Archosauria: monophyletic")
a, b = xs["Lizards and snakes"], xs["Crocodiles"]
ax.plot([a - 0.5, b + 0.5], [0.15, 0.15], color=P.edge("highlight"), lw=4, solid_capstyle="round")
bio.label(ax, (a - 0.6, 0.15), "Traditional Reptilia:\nparaphyletic", size="tiny", ha="right")
for n in ("Mammals", "Birds"):
    bio.label(ax, (xs[n], 9.5), "warm-blooded", size="tiny", color=P.edge("negative"), bold=True)
ax.plot([xs["Mammals"], xs["Birds"]], [9.9, 9.9], color=P.edge("negative"), lw=1.0, ls=(0, (3, 2)))
bio.label(ax, ((xs["Mammals"] + xs["Birds"]) / 2, 10.15), "'warm-blooded animals': polyphyletic", size="tiny",
          color=P.edge("negative"))

bio.panel(ax, "B", (13.4, 10.2))
NB = "(Crocodiles:10,((Tyrannosaurus:4.5,(Archaeopteryx:3.0,((Pigeon:2.0,Chicken:2.0):1.5,Penguin:3.5)Crown:1.5):3.0):2.5)):1;"
ICB = {"Crocodiles": "phylopic/crocodile", "Tyrannosaurus": "phylopic/tyrannosaurus",
       "Archaeopteryx": "phylopic/archaeopteryx", "Pigeon": "phylopic/pigeon", "Chicken": "phylopic/chicken",
       "Penguin": "phylopic/penguin"}
tb = phylo.tree(ax, NB, origin=(14.4, 2.2), width=10.5, height=6.0, direction="up", scaled=True, icons=ICB,
                icon_size=0.7, italic={"Tyrannosaurus", "Archaeopteryx"}, label_size="small",
                clades=[dict(node="Crown", token="dna", style="branch")])
for name in ("Tyrannosaurus", "Archaeopteryx"):
    x, y = tb.node(name).xy
    bio.label(ax, (x, y), "x", size="small", bold=True, color=P.edge("negative"))
cx = [tb.node(n).xy[0] for n in ("Pigeon", "Chicken", "Penguin")]
ax.plot([min(cx) - 0.5, max(cx) + 0.5], [1.25, 1.25], color=P.edge("dna"), lw=4, solid_capstyle="round")
bio.label(ax, ((min(cx) + max(cx)) / 2, 0.9), "crown group Aves", size="tiny", va="top")
sx = [tb.node(n).xy[0] for n in ("Tyrannosaurus", "Archaeopteryx")]
ax.plot([min(sx) - 0.5, max(sx) + 0.3], [1.25, 1.25], color=P.edge("highlight"), lw=4, solid_capstyle="round")
bio.label(ax, ((min(sx) + max(sx)) / 2, 0.9), "stem group", size="tiny", va="top")
ax.plot([min(sx) - 0.5, max(cx) + 0.5], [0.25, 0.25], color=P.muted(), lw=1.2)
bio.label(ax, ((min(sx) + max(cx)) / 2, 0.1), "total group (crown + stem)", size="tiny", va="top", color=P.muted())
bio.label(ax, (14.4, 9.9), "x: extinct taxon", size="tiny", ha="left", color=P.muted())
