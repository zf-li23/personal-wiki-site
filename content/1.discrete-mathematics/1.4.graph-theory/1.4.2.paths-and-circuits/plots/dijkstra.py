import math
import matplotlib.pyplot as plt
import wikigraph as G

pos = {1: (0, 1.2), 2: (1.4, 0), 3: (1.7, 1.4), 4: (3.4, 0.2), 5: (3.6, 2.3), 6: (1.5, 2.8)}
E = [(1, 2, 7), (1, 3, 9), (1, 6, 14), (2, 3, 10), (2, 4, 15), (3, 4, 11), (3, 6, 2), (4, 5, 6), (5, 6, 9)]
w = {}
for u, v, c in E:
    w[(u, v)] = w[(v, u)] = c

pi = {v: math.inf for v in pos}
pred = {}
pi[1] = 0
permanent = []
states = []
while len(permanent) < len(pos):
    u = min((v for v in pos if v not in permanent), key=lambda v: (pi[v], v))
    permanent.append(u)
    for v in pos:
        if v not in permanent and (u, v) in w and pi[u] + w[(u, v)] < pi[v]:
            pi[v] = pi[u] + w[(u, v)]
            pred[v] = u
    states.append((list(permanent), dict(pi), dict(pred)))

names = {v: f"$v_{v}$" for v in pos}
fig, axes = plt.subplots(2, 3, figsize=(9.6, 6.0))
for step, ax in enumerate(axes.flat):
    perm, lab, pr = states[step]
    ax.set_xlim(-0.6, 4.2)
    ax.set_ylim(-0.6, 3.4)
    ax.set_aspect("equal")
    ax.axis("off")
    tree = {(pr[v], v): G.BLUE for v in pr}
    hl = dict(tree)
    hl[perm[-1]] = G.RED
    G.draw(ax, pos, E, weights=True, highlight=hl, edge_color=G.GREY, vertex_labels=names,
           vertex_color={v: G.BLUE for v in perm[:-1]} | {perm[-1]: G.RED})
    for v, (x, y) in pos.items():
        text = "$\\infty$" if lab[v] == math.inf else str(lab[v])
        if v not in perm:
            text = f"({text})"
        dx, dy = {2: (0, -0.38), 4: (0, -0.38), 3: (0.42, 0.22)}.get(v, (0, 0.36))
        ax.text(x + dx, y + dy, text, ha="center", va="center",
                fontsize=9, color=G.RED if v == perm[-1] else G.INK)
    ax.set_title(f"step {step + 1}: $v_{perm[-1]}$ becomes permanent", fontsize=10)
fig.subplots_adjust(0.01, 0.01, 0.99, 0.95, wspace=0.05, hspace=0.12)
