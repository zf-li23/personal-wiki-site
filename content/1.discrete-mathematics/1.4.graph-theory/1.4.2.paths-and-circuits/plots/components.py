import matplotlib.pyplot as plt
import numpy as np
import wikigraph as G

pos = {"1": (0, 0), "2": (1.2, 0), "3": (0.6, 1.0), "4": (2.4, 0.5), "5": (3.6, 0.5), "6": (3.0, 1.5),
       "7": (4.6, 0), "8": (4.6, 1.2)}
E = [("1", "2"), ("2", "3"), ("3", "1"), ("4", "5"), ("5", "6"), ("6", "4"), ("7", "8")]
parts = [("1", "2", "3"), ("4", "5", "6"), ("7", "8")]
colours = [G.BLUE, G.RED, G.GREEN]
fig, (ax, mx) = plt.subplots(1, 2, figsize=(8.4, 2.8), gridspec_kw={"width_ratios": [1.5, 1]})
ax.set_xlim(-0.4, 5.0)
ax.set_ylim(-0.6, 1.9)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("three connected components", fontsize=10)
hl = {}
for part, c in zip(parts, colours):
    hl.update({v: c for v in part})
    hl.update({e: c for e in E if e[0] in part})
G.draw(ax, pos, E, highlight=hl)
# adjacency matrix in this numbering: block diagonal
A = np.zeros((8, 8))
for u, v in E:
    A[int(u) - 1, int(v) - 1] = A[int(v) - 1, int(u) - 1] = 1
mx.imshow(A, cmap="Greys", vmin=0, vmax=1.6)
start = 0
for part, c in zip(parts, colours):
    k = len(part)
    mx.add_patch(plt.Rectangle((start - 0.5, start - 0.5), k, k, fill=False, edgecolor=c, lw=2))
    start += k
mx.set_xticks(range(8), [str(i) for i in range(1, 9)])
mx.set_yticks(range(8), [str(i) for i in range(1, 9)])
mx.tick_params(length=0, labelsize=9)
mx.set_title("adjacency matrix", fontsize=10)
fig.tight_layout()
