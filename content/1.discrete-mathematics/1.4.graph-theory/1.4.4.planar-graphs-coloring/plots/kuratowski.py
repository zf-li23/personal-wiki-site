# The Petersen graph contains a subdivision of K3,3 (Example 4.3.1): branch vertices of the
# two parts in blue and red, subdivision vertices white, the two unused edges dashed.
import wikigraph as G

outer = G.circle(range(5), radius=1.8, center=(2.0, 1.9))
inner = G.circle(range(5, 10), radius=0.85, center=(2.0, 1.9))
pos = {**outer, **inner}
edges = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] \
    + [(i + 5, (i + 2) % 5 + 5) for i in range(5)]
unused = [(4, 9), (8, 5)]
fig, ax = G.canvas(4.0, 3.8)
part_a, part_b = [0, 2, 6], [1, 3, 7]
colours = {v: G.BLUE for v in part_a} | {v: G.RED for v in part_b}
G.draw(ax, pos, edges, dashed=unused, vertex_color=colours, labels=False,
       highlight={e: G.GREY for e in unused})
