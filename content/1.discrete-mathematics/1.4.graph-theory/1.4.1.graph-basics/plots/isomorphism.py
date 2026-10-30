import wikigraph as G

titles = ["$K_{3,3}$ as a hexagon", "$K_{3,3}$ in two rows", "$C_6$", "$2K_3$"]
fig, axes = G.panels(4, 2.4, 2.0, titles=titles)
names = [str(i) for i in range(1, 7)]
hexagon = G.circle(names, radius=1.0, center=(1.2, 1.0))
# vertices 1..6 around the hexagon; 1-2, 2-3, ... and the three long diagonals
K33 = [(names[i], names[(i + 1) % 6]) for i in range(6)] + [("1", "4"), ("2", "5"), ("3", "6")]
G.draw(axes[0], hexagon, K33)
rows = {"1": (0, 2.0), "3": (1.2, 2.0), "5": (2.4, 2.0), "2": (0, 0), "4": (1.2, 0), "6": (2.4, 0)}
G.draw(axes[1], rows, K33)
G.draw(axes[2], hexagon, [(names[i], names[(i + 1) % 6]) for i in range(6)])
tri = {"1": (0.0, 0.2), "2": (1.0, 0.2), "3": (0.5, 1.1), "4": (1.4, 1.0), "5": (2.4, 1.0), "6": (1.9, 1.9)}
G.draw(axes[3], tri, [("1", "2"), ("2", "3"), ("3", "1"), ("4", "5"), ("5", "6"), ("6", "4")])
