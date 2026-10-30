# Proof of Euler's formula: start from a spanning tree (one face) and add the chords back;
# each chord closes a cycle and splits one face into two.
import wikigraph as G

TEX = {f"v{i}": f"$v_{i}$" for i in range(1, 6)}

pos = {"v1": (0, 0), "v2": (2.2, 0), "v3": (2.2, 2.2), "v4": (0, 2.2), "v5": (3.4, 3.0)}
tree = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v3", "v5")]
chords = [("v4", "v1"), ("v1", "v3")]
titles = ["spanning tree: d = 1", "add chord $v_4v_1$: d = 2", "add chord $v_1v_3$: d = 3"]
fig, axes = G.panels(3, 3.6, 3.2, titles=titles)
for k, ax in enumerate(axes):
    added = chords[:k]
    hl = {e: G.BLUE for e in tree}
    if k:
        hl[added[-1]] = G.RED
    G.draw(ax, pos, tree + added, highlight=hl, vertex_labels=TEX)
labels = [[("$f_0$", (1.0, 1.1))],
          [("$f_1$", (1.1, 1.1)), ("$f_0$", (3.0, 0.8))],
          [("$f_1$", (1.5, 0.65)), ("$f_2$", (0.7, 1.55)), ("$f_0$", (3.0, 0.8))]]
for ax, items in zip(axes, labels):
    for text, xy in items:
        ax.text(*xy, text, fontsize=12, color=G.GREEN, ha="center", va="center")
