import wikigraph as G

titles = ["Eulerian, not Hamiltonian", "Hamiltonian, not Eulerian", "both: $K_5$"]
fig, axes = G.panels(3, 3.0, 2.0, titles=titles)
# bowtie: two triangles sharing c; an Euler circuit c a b c d e c, edges numbered in order
bow = {"a": (0, 2.0), "b": (0, 0), "c": (1.5, 1.0), "d": (3.0, 2.0), "e": (3.0, 0)}
tour = "cabcdec"
G.draw(axes[0], bow, [(tour[k], tour[k + 1], k + 1) for k in range(6)], weights=True,
       highlight={(tour[k], tour[k + 1]): G.BLUE for k in range(6)})
# K4: every degree is 3 (odd), a Hamiltonian cycle a b c d a in red
sq = {"a": (0.5, 2.0), "b": (2.5, 2.0), "c": (2.5, 0), "d": (0.5, 0)}
G.draw(axes[1], sq, [("a", "b"), ("b", "c"), ("c", "d"), ("d", "a"), ("a", "c"), ("b", "d")],
       highlight={("a", "b"): G.RED, ("b", "c"): G.RED, ("c", "d"): G.RED, ("d", "a"): G.RED})
names = list("abcde")
k5 = G.circle(names, radius=1.0, center=(1.5, 1.0))
outer = {(names[i], names[(i + 1) % 5]): G.RED for i in range(5)}
G.draw(axes[2], k5, [(u, v) for i, u in enumerate(names) for v in names[i + 1:]], highlight=outer)
