# Kruskal's algorithm on Example 3.7.1: edges examined in increasing order of weight
import matplotlib.pyplot as plt
import wikigraph as G

pos = {"a": (0, 1), "b": (1.5, 2), "c": (3, 2), "d": (4.5, 1), "e": (3, 0), "f": (1.5, 0)}
edges = [("a", "b", 4), ("a", "f", 2), ("b", "f", 5), ("b", "c", 6), ("c", "f", 1), ("c", "e", 3),
         ("e", "f", 8), ("c", "d", 7), ("d", "e", 9)]
order = sorted(edges, key=lambda e: e[2])[:7]

fig, axes = plt.subplots(2, 4, figsize=(11.0, 3.5))
for ax in axes.flat:
    ax.set_xlim(-0.4, 4.9)
    ax.set_ylim(-0.4, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
G.draw(axes[0, 0], pos, edges, weights=True)
axes[0, 0].set_title("weighted graph G", fontsize=G.FONT)
root = {v: v for v in pos}


def find(x):
    while root[x] != x:
        x = root[x]
    return x


tree = []
for ax, (u, v, w) in zip(axes.flat[1:], order):
    ok = find(u) != find(v)
    if ok:
        root[find(u)] = find(v)
        tree.append((u, v))
    hl = {e: G.BLUE for e in tree}
    if not ok:
        hl[(u, v)] = G.RED
    G.draw(ax, pos, edges, weights=True, highlight=hl, edge_color=G.GREY, dashed=[] if ok else [(u, v)])
    ax.set_title(f"{u}{v} ({w}): " + ("add" if ok else "reject, closes a cycle"), fontsize=G.FONT)
fig.subplots_adjust(0.01, 0.01, 0.99, 0.94, wspace=0.05, hspace=0.2)
