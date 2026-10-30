# A spanning tree T (blue) and its chords (dashed); a fundamental cycle and a fundamental cut set
import wikigraph as G

pos = {"v1": (0, 0), "v2": (2, 0), "v3": (2, 2), "v4": (0, 2), "v5": (0.9, 1.0)}
names = {v: f"$v_{v[1]}$" for v in pos}
edges = [("v1", "v2", "$e_1$"), ("v2", "v3", "$e_2$"), ("v3", "v4", "$e_3$"), ("v4", "v1", "$e_4$"),
         ("v1", "v5", "$e_5$"), ("v5", "v3", "$e_6$"), ("v2", "v5", "$e_7$")]
tree = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v1", "v5")]
chords = [("v4", "v1"), ("v5", "v3"), ("v2", "v5")]
fig, axes = G.panels(3, 2.0, 2.0, titles=["tree T and chords $e_4, e_6, e_7$", "fundamental cycle of $e_4$",
                                          "fundamental cut set of $e_2$"])
G.draw(axes[0], pos, edges, weights=True, highlight={e: G.BLUE for e in tree}, dashed=chords, vertex_labels=names)
cycle = [("v4", "v1"), ("v1", "v2"), ("v2", "v3"), ("v3", "v4")]
G.draw(axes[1], pos, edges, weights=True, highlight={e: G.RED for e in cycle}, dashed=chords, vertex_labels=names)
side = {"v3", "v4"}
cut = [("v2", "v3"), ("v4", "v1"), ("v5", "v3")]
G.draw(axes[2], pos, edges, weights=True, highlight={e: G.RED for e in cut}, dashed=chords, vertex_labels=names,
       vertex_color={v: G.AMBER for v in side})
