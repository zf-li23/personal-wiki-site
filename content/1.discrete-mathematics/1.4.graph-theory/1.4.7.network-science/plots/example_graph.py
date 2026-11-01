"""The example graph G0 of Section 7.1: two groups of four vertices joined by the edge 4-5. Each vertex
is coloured by its betweenness centrality (white = 0, dark red = 12.5) and annotated with its degree k
and local clustering coefficient C."""

from fractions import Fraction
import wikigraph as G

pos = {1: (0.0, 1.8), 2: (-0.9, 0.9), 3: (0.0, 0.0), 4: (1.3, 0.9),
       5: (3.1, 0.9), 6: (4.4, 1.8), 7: (4.4, 0.0), 8: (5.5, 0.9)}
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (5, 8), (6, 7), (7, 8)]
betweenness = {1: 2.5, 2: 0.0, 3: 2.5, 4: 12.0, 5: 12.5, 6: 0.0, 7: 0.5, 8: 0.0}

adj = {v: set() for v in pos}
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
notes = {}
for v in pos:
    k = len(adj[v])
    t = sum(1 for a in adj[v] for b in adj[v] if a < b and b in adj[a])
    c = Fraction(2 * t, k * (k - 1))
    notes[v] = (f"k={k}, C={c}", (0.0, -0.42) if v not in (1, 6) else (0.0, 0.42))
fig, ax = G.canvas(6.6, 2.4)
for v in pos:
    pos[v] = (pos[v][0] + 1.0, pos[v][1] + 0.3)
G.draw(ax, pos, edges, radius=0.22, vertex_color=G.colors(betweenness, cmap="Reds", vmin=0, vmax=14),
       vertex_notes=notes, highlight={(4, 5): G.RED})
