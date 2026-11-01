"""From a purified complex to binary edges. A: a hypothetical complex of six subunits with its five
direct contacts (the edges that a binary assay such as yeast two-hybrid could detect); the bait
(blue) touches only two of the others. B: the spoke model joins the bait to every co-purified
prey: 5 edges, 2 of them direct contacts. C: the matrix model joins every pair of co-purified
proteins: 15 edges, 5 of them direct contacts. Neither model is the set of physical contacts; both
say only that the proteins share a complex."""

import wikigraph as G

pos = G.circle(["B", "P1", "P2", "P3", "P4", "P5"], radius=1.2, center=(1.5, 1.4))
true = [("B", "P1"), ("B", "P5"), ("P1", "P2"), ("P2", "P3"), ("P3", "P4")]
spoke = [("B", p) for p in ["P1", "P2", "P3", "P4", "P5"]]
nodes = list(pos)
matrix = [(nodes[i], nodes[j]) for i in range(6) for j in range(i + 1, 6)]
ts = {frozenset(e) for e in true}
fig, axes = G.panels(3, 3, 2.8, titles=["A  Direct contacts", "B  Spoke model", "C  Matrix model"])
G.draw(axes[0], pos, true, vertex_color={"B": G.BLUE})
for ax, edges in [(axes[1], spoke), (axes[2], matrix)]:
    G.draw(ax, pos, edges, vertex_color={"B": G.BLUE}, edge_color=G.GREY,
           highlight={e: G.GREEN for e in edges if frozenset(e) in ts})
