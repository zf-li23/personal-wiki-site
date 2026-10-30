# Encoding a labeled tree as its Pruefer sequence: delete the smallest leaf (red), record its neighbour (blue)
import matplotlib.pyplot as plt
import wikigraph as G

pos = {"1": (0, 2), "2": (0, 0), "5": (1, 1), "3": (2.2, 1), "6": (3.2, 2), "4": (4.2, 2), "7": (3.2, 0)}
edges = [("1", "5"), ("2", "5"), ("5", "3"), ("3", "6"), ("6", "4"), ("3", "7")]

fig, axes = plt.subplots(2, 3, figsize=(9.6, 4.6))
seq = []
alive = dict(pos)
cur = list(edges)
for k, ax in enumerate(axes.flat):
    ax.set_xlim(-0.4, 4.6)
    ax.set_ylim(-0.4, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")
    deg = {v: sum(v in e for e in cur) for v in alive}
    if k < 5:
        leaf = min((v for v in alive if deg[v] == 1), key=int)
        (nb,) = [u if w == leaf else w for u, w in cur if leaf in (u, w)]
        G.draw(ax, alive, cur, highlight={leaf: G.RED, (leaf, nb): G.RED, nb: G.BLUE},
               vertex_color={leaf: G.RED, nb: G.BLUE})
        seq.append(nb)
        ax.set_title(f"step {k + 1}: delete leaf {leaf}, write {nb}", fontsize=G.FONT)
        G.caption(ax, (2.1, -0.3), "sequence: (" + ", ".join(seq) + ")", size=G.FONT - 1)
        cur = [e for e in cur if leaf not in e]
        del alive[leaf]
    else:
        G.draw(ax, alive, cur)
        ax.set_title("two vertices remain: stop", fontsize=G.FONT)
        G.caption(ax, (2.1, -0.3), "Pruefer sequence (" + ", ".join(seq) + ")", size=G.FONT - 1)
fig.subplots_adjust(0.01, 0.02, 0.99, 0.93, wspace=0.05, hspace=0.25)
