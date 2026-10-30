# A 3-wide container in the cube Q3 between x = 000 and y = 011: lengths 2, 2, 4
import wikigraph as G

pos = {"000": (0, 0), "100": (2.2, 0), "010": (0, 2.2), "110": (2.2, 2.2),
       "001": (1.0, 0.8), "101": (3.2, 0.8), "011": (1.0, 3.0), "111": (3.2, 3.0)}
edges = [(u, v) for u in pos for v in pos if u < v and sum(a != b for a, b in zip(u, v)) == 1]
paths = [("000", "001", "011"), ("000", "010", "011"), ("000", "100", "101", "111", "011")]
hl = {}
for p, colour in zip(paths, (G.BLUE, G.GREEN, G.AMBER)):
    for u, v in zip(p, p[1:]):
        hl[(u, v)] = colour
fig, ax = G.canvas(3.2, 3.0)
G.draw(ax, pos, edges, highlight=hl, radius=0.3, vertex_color={"000": G.VIOLET, "011": G.VIOLET})
