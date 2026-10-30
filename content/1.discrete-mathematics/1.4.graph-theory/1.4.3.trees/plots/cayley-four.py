# The 16 labeled trees on the vertex set {1, 2, 3, 4}: 4 stars and 12 paths (Cayley: 4^2 = 16)
from itertools import combinations

import matplotlib.pyplot as plt
import wikigraph as G

pos = {"1": (0, 1), "2": (1, 1), "3": (1, 0), "4": (0, 0)}
pairs = list(combinations(pos, 2))


def is_tree(es):
    comp = {v: v for v in pos}
    for u, v in es:
        a, b = comp[u], comp[v]
        if a == b:
            return False
        comp = {x: (a if c == b else c) for x, c in comp.items()}
    return True


trees = [t for t in combinations(pairs, 3) if is_tree(t)]
trees.sort(key=lambda t: max(sum(v in e for e in t) for v in pos) < 3)  # stars first
fig, axes = plt.subplots(2, 8, figsize=(10.5, 3.0))
for k, (ax, t) in enumerate(zip(axes.flat, trees)):
    ax.set_xlim(-0.35, 1.35)
    ax.set_ylim(-0.35, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    star = max(sum(v in e for e in t) for v in pos) == 3
    G.draw(ax, pos, list(t), highlight={e: (G.AMBER if star else G.BLUE) for e in t}, radius=0.17)
    ax.set_title("star" if star else "path", fontsize=G.FONT - 1)
fig.subplots_adjust(0.01, 0.01, 0.99, 0.9, wspace=0.1, hspace=0.3)
