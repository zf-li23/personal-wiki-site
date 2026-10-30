# kappa < lambda < delta (vertex connectivity, edge connectivity, minimum degree): two copies of K4 joined by the edges de and df
import wikigraph as G

pos = {"a": (0, 1.8), "b": (0, 0), "c": (1.2, 0), "d": (1.2, 1.8),
       "e": (2.8, 1.8), "f": (2.8, 0), "g": (4.0, 0), "h": (4.0, 1.8)}
k4 = lambda q: [(q[i], q[j]) for i in range(4) for j in range(i + 1, 4)]
edges = k4("abcd") + k4("efgh") + [("d", "e"), ("d", "f")]

fig, axes = G.panels(3, 4.0, 1.8, titles=[r"vertex cut $\{d\}$: $\kappa = 1$",
                                          r"edge cut $\{de, df\}$: $\lambda = 2$",
                                          r"minimum degree: $\delta = 3$"])
G.draw(axes[0], pos, edges, highlight={"d": G.RED}, vertex_color={"d": G.RED},
       dashed=[e for e in edges if "d" in e])
G.draw(axes[1], pos, edges, highlight={("d", "e"): G.BLUE, ("d", "f"): G.BLUE}, dashed=[("d", "e"), ("d", "f")])
G.draw(axes[2], pos, edges, highlight={"a": G.GREEN, ("a", "b"): G.GREEN, ("a", "c"): G.GREEN, ("a", "d"): G.GREEN})
