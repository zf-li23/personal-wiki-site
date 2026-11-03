"""Three pictures of the history of life. A: the scala naturae, a fixed linear ranking of beings.
B: Lamarck's hypothesis: life arises repeatedly by spontaneous generation (dots) and every lineage
climbs in complexity, so living species differ because they differ in age. C: Darwin's descent with
modification: one origin, lineages that split and diverge in form, many of which go extinct (crosses);
complexity need not increase. After the scheme of Futuyma and Kirkpatrick (2017), Fig. 1.5."""
import numpy as np
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(27.6, 10.5)

# A: the scala naturae
bio.panel(ax, "A", (0.3, 10.3))
RUNGS = ["God", "Angels", "Humans", "Animals", "Plants", "Minerals"]
TOKS = ["highlight", "antibody", "animal", "muscle", "plant", "neutral"]
for k, (name, tok) in enumerate(zip(RUNGS, TOKS)):
    y = 8.6 - 1.35 * k
    bio.box(ax, (3.6, y), 4.2, 0.95, tok, text=name, size="small")
    if k:
        bio.arrow(ax, (3.6, y + 0.5), (3.6, y + 0.85), kind="link", color=P.muted())
bio.arrow(ax, (6.3, 1.6), (6.3, 9.0), kind="process", color=P.muted())
bio.label(ax, (6.75, 5.3), "rank in a fixed, perfect order", size="tiny", color=P.muted(), rotation=90)
bio.label(ax, (3.6, 0.55), "Scala naturae (unchanging)", size="small", bold=True)

# B: Lamarck
bio.panel(ax, "B", (8.0, 10.3))
x0, y0, w, h = 8.8, 1.6, 7.6, 7.6
ax.plot([x0, x0 + w], [y0, y0], color=P.muted(), lw=0.9)
ax.plot([x0, x0], [y0, y0 + h], color=P.muted(), lw=0.9)
bio.label(ax, (x0 + w / 2, y0 - 0.45), "Time", size="small")
bio.label(ax, (x0 - 0.45, y0 + h / 2), "Complexity", size="small", rotation=90)
for k, t0 in enumerate(np.linspace(0.3, 6.6, 7)):
    xs = np.linspace(x0 + t0, x0 + w - 0.2, 30)
    ys = y0 + 0.25 + (xs - xs[0]) * 0.95
    ax.plot(xs, ys, color=bio.P.edge("dna"), lw=1.4)
    ax.plot([xs[0]], [ys[0]], "o", ms=5, color=bio.P.edge("negative"))
bio.label(ax, (x0 + w / 2, 0.55), "Lamarck: many origins, each lineage rises", size="small", bold=True)

# C: Darwin
bio.panel(ax, "C", (17.6, 10.3))
NEWICK = ("((((a:1.6,b:1.6):2.0,(c:2.3,X1:0.8):1.3):1.5,((d:2.6,X2:1.0):1.2,e:3.8):1.3):1.2,"
          "(((f:1.9,g:1.9):1.6,X3:1.2):1.8,(h:3.0,X4:1.4):2.3):1.0);")
t = phylo.tree(ax, NEWICK, origin=(18.4, 1.6), width=8.0, height=7.6, direction="up", scaled=True, tip_labels=False,
               root_edge=0.4)
for leaf in t.tips():
    x, y = leaf.xy
    if leaf.name.startswith("X"):
        bio.label(ax, (x, y + 0.15), "x", size="small", color=P.edge("negative"), bold=True)
    else:
        ax.plot([x], [y], "o", ms=3.5, color=P.ink())
root = t.root
rx, ry = root.xy
ax.plot([rx], [ry - 0.4], "o", ms=5, color=bio.P.edge("negative"))
bio.label(ax, (22.4, 1.15), "Form", size="small")
bio.arrow(ax, (27.0, 1.6), (27.0, 9.2), kind="process", color=P.muted())
bio.label(ax, (26.6, 5.3), "Time", size="small", rotation=90)
bio.label(ax, (22.4, 0.55), "Darwin: one origin, branching and divergence", size="small", bold=True)
