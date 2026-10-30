import matplotlib.pyplot as plt
import wikigraph as G

pos = {"a": (0, 0), "b": (1.6, 0), "c": (3.2, 0), "d": (0, 1.6), "e": (1.6, 1.6), "f": (3.2, 1.6)}
E = [("a", "b"), ("b", "c"), ("a", "d"), ("d", "e"), ("e", "f"), ("c", "f"), ("b", "e"), ("a", "e"), ("c", "e")]
cases = [
    ("walk  a b e b c", "abebc", G.BLUE),
    ("trail  d e b a e f", "debaef", G.BLUE),
    ("path  d a b c f", "dabcf", G.BLUE),
    ("closed walk  a b e b a", "abeba", G.RED),
    ("circuit  a b e c f e d a", "abecfeda", G.RED),
    ("cycle  a b e d a", "abeda", G.RED),
]
fig, axes = plt.subplots(2, 3, figsize=(9.0, 5.0))
for ax, (title, seq, colour) in zip(axes.flat, cases):
    ax.set_xlim(-0.5, 3.7)
    ax.set_ylim(-0.5, 2.1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=10)
    # number the steps of the sequence on the edges it uses
    steps = {}
    for k in range(len(seq) - 1):
        steps.setdefault(frozenset(seq[k:k + 2]), []).append(str(k + 1))
    edges = [(u, v, ",".join(steps[frozenset((u, v))])) if frozenset((u, v)) in steps else (u, v) for u, v in E]
    hl = {(u, v): colour for u, v in E if frozenset((u, v)) in steps}
    hl[seq[0]] = colour
    hl[seq[-1]] = colour
    G.draw(ax, pos, edges, weights=True, highlight=hl, edge_color=G.GREY)
fig.subplots_adjust(0.01, 0.01, 0.99, 0.95, wspace=0.05, hspace=0.15)
