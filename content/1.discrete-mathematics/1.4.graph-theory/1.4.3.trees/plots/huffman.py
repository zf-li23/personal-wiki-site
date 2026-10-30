# Huffman tree for the weights 2, 3, 5, 7, 11; internal vertices carry the merged weights, edges the code bits
import wikigraph as G

pos = {"r": (3.0, 4.0), "11": (4.6, 3.0), "s": (1.8, 3.0), "7": (3.0, 2.0), "t": (0.8, 2.0),
       "5": (1.8, 1.0), "u": (0, 1.0), "2": (-0.6, 0), "3": (0.6, 0)}
labels = {"r": "28", "s": "17", "t": "10", "u": "5"}
edges = [("r", "s", "0"), ("r", "11", "1"), ("s", "t", "0"), ("s", "7", "1"), ("t", "u", "0"), ("t", "5", "1"),
         ("u", "2", "0"), ("u", "3", "1")]
leaves = ["11", "7", "5", "2", "3"]
codes = {"11": "1", "7": "01", "5": "001", "2": "0000", "3": "0001"}
fig, ax = G.canvas(6.4, 4.4)
for k in ("r", "s", "t", "u", "11", "7", "5", "2", "3"):
    x, y = pos[k]
    pos[k] = (x + 1.0, y + 0.4)
G.draw(ax, pos, edges, weights=True, vertex_labels=labels, vertex_color={v: G.GREEN for v in leaves}, radius=0.28)
for v in leaves:
    x, y = pos[v]
    G.caption(ax, (x, y - 0.5), codes[v], size=G.FONT - 1)
G.caption(ax, (4.7, 0.3), "WPL = 2*4 + 3*4 + 5*3 + 7*2 + 11*1 = 60", size=G.FONT - 1)
