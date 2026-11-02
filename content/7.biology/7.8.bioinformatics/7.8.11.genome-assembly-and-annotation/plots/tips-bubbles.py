# Abstract tip and bubble in a de Bruijn graph and the graph after simplification.
import wikigraph as G

fig, axes = G.panels(3, 5.0, 2.2, titles=["A  tip", "B  bubble", "C  simplified"])
main = {f"v{i}": (0.3 + 1.1 * i, 1.0) for i in range(0, 5)}

pa = dict(main)
pa.update({"t1": (2.5, 2.0), "t2": (3.5, 2.0)})
G.draw(axes[0], pa, [(f"v{i}", f"v{i+1}") for i in range(4)] + [("v2", "t1"), ("t1", "t2")],
       directed=True, highlight={("v2", "t1"): G.RED, ("t1", "t2"): G.RED}, dashed=[("v2", "t1"), ("t1", "t2")],
       labels=False)
G.caption(axes[0], (2.5, 0.1), "low-coverage dead end")

pb = {"v0": (0.3, 1.0), "v1": (1.4, 1.0), "p1": (2.5, 1.8), "p2": (2.5, 0.2), "v3": (3.6, 1.0), "v4": (4.7, 1.0)}
G.draw(axes[1], pb, [("v0", "v1"), ("v1", "p1"), ("p1", "v3"), ("v1", "p2"), ("p2", "v3"), ("v3", "v4")],
       directed=True, highlight={("v1", "p2"): G.RED, ("p2", "v3"): G.RED, ("v1", "p1"): G.BLUE, ("p1", "v3"): G.BLUE},
       dashed=[("v1", "p2"), ("p2", "v3")], labels=False)
G.caption(axes[1], (2.5, -0.35), "two parallel paths, same ends")

G.draw(axes[2], main, [(f"v{i}", f"v{i+1}") for i in range(4)], directed=True,
       highlight={(f"v{i}", f"v{i+1}"): G.BLUE for i in range(4)}, labels=False)
G.caption(axes[2], (2.5, 0.1), "one unitig")
