# A matching M (blue), an augmenting path P from x2 to y3 (edges of M blue, others red),
# and the larger matching M xor P obtained by swapping the roles of the edges on P.
import wikigraph as G

# the bipartite graph of Example 5.1.1
X = [f"x{i}" for i in range(1, 6)]
Y = [f"y{i}" for i in range(1, 6)]
ADJ = {"x1": ["y1", "y2"], "x2": ["y1"], "x3": ["y2", "y3", "y4", "y5"], "x4": ["y3"], "x5": ["y1"]}
EDGES = [(x, y) for x in X for y in ADJ[x]]
POS = {x: (1.1 * i, 1.8) for i, x in enumerate(X)} | {y: (1.1 * i, 0.0) for i, y in enumerate(Y)}
TEX = {v: f"${v[0]}_{v[1]}$" for v in X + Y}

M = [("x1", "y1"), ("x3", "y2")]
P = ["x2", "y1", "x1", "y2", "x3", "y3"]
path = list(zip(P, P[1:]))
new = [e for e in M if e not in path and e[::-1] not in path] + \
      [e for e in path if e not in M and e[::-1] not in M]


def unsaturated(matching):
    hit = {v for e in matching for v in e}
    return {v: G.GREY for v in POS if v not in hit}


fig, axes = G.panels(3, 4.4, 1.8, titles=["matching M", "augmenting path P", "$M \\oplus P$"])
G.draw(axes[0], POS, EDGES, highlight={e: G.BLUE for e in M}, vertex_color=unsaturated(M), vertex_labels=TEX)
G.draw(axes[1], POS, EDGES, vertex_color=unsaturated(M), vertex_labels=TEX,
       highlight={e: (G.BLUE if e in M or e[::-1] in M else G.RED) for e in path})
G.draw(axes[2], POS, EDGES, highlight={e: G.BLUE for e in new}, vertex_color=unsaturated(new), vertex_labels=TEX)
