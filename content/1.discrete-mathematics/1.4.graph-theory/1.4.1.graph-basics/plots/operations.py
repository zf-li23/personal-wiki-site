import wikigraph as G

pos = {"1": (0, 0), "2": (1.6, 0), "3": (1.6, 1.6), "4": (0, 1.6), "5": (0.8, 2.6)}
E1 = [("1", "2"), ("2", "3"), ("3", "4"), ("4", "1")]
E2 = [("1", "3"), ("2", "3"), ("3", "5"), ("4", "5")]
V1, V2 = {"1", "2", "3", "4"}, {"1", "2", "3", "4", "5"}
key = lambda e: frozenset(e)
s1, s2 = {key(e) for e in E1}, {key(e) for e in E2}
titles = ["$G_1$", "$G_2$", "$G_1 \\cup G_2$", "$G_1 \\cap G_2$", "$G_1 \\oplus G_2$"]
fig, axes = G.panels(5, 1.6, 2.6, titles=titles)
sel = lambda V: {k: pos[k] for k in sorted(V)}
G.draw(axes[0], sel(V1), E1, edge_color=G.BLUE)
G.draw(axes[1], sel(V2), E2, edge_color=G.RED)
G.draw(axes[2], sel(V1 | V2), E1 + [e for e in E2 if key(e) not in s1],
       highlight={e: G.GREEN for e in E1 if key(e) in s2})
G.draw(axes[3], sel(V1 & V2), [e for e in E1 if key(e) in s2], edge_color=G.GREEN)
G.draw(axes[4], sel(V1 | V2), [e for e in E1 if key(e) not in s2] + [e for e in E2 if key(e) not in s1])
