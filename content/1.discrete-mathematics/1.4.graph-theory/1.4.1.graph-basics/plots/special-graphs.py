import wikigraph as G

fig, axes = G.panels(4, 2.0, 2.0, titles=["$N_4$", "$K_3$", "$K_4$", "$K_5$"])
c = (1.0, 1.0)
for ax, k in zip(axes, [4, 3, 4, 5]):
    names = [str(i) for i in range(1, k + 1)]
    pos = G.circle(names, radius=0.95, center=c, start=90 if k != 4 else 45)
    edges = [] if ax is axes[0] else [(u, v) for i, u in enumerate(names) for v in names[i + 1:]]
    G.draw(ax, pos, edges, labels=False)
