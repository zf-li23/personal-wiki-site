import wikigraph as G

fig, axes = G.panels(4, 2.0, 2.0, titles=["$P_4$", "its complement", "$C_5$", "its complement"])
pos = {"a": (0, 2.0), "b": (2.0, 2.0), "c": (0, 0), "d": (2.0, 0)}
P4 = [("a", "b"), ("b", "c"), ("c", "d")]
G.draw(axes[0], pos, P4)
G.draw(axes[1], pos, [("a", "c"), ("a", "d"), ("b", "d")], edge_color=G.BLUE)
names = list("12345")
cp = G.circle(names, radius=1.0, center=(1.0, 1.0))
C5 = [(names[i], names[(i + 1) % 5]) for i in range(5)]
G.draw(axes[2], cp, C5)
G.draw(axes[3], cp, [(names[i], names[(i + 2) % 5]) for i in range(5)], edge_color=G.BLUE)
