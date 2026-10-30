# The plane graph G of Example 4.1.1 (black) and its dual G* (red): one dual vertex per face,
# one dual edge crossing each edge of G; the cut edge v3v5 gives a loop at f0.
import numpy as np
import wikigraph as G

TEX = {f"v{i}": f"$v_{i}$" for i in range(1, 6)}
pos = {"v1": (0, 0), "v2": (2.2, 0), "v3": (2.2, 2.2), "v4": (0, 2.2), "v5": (3.5, 3.0)}
edges = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v1"), ("v1", "v3"), ("v3", "v5")]
dual = {"f1": (1.5, 0.7), "f2": (0.7, 1.5), "f0": (3.7, 1.0)}
# each dual edge is a smooth curve through waypoints; the middle waypoint lies on the primal edge
routes = [
    ["f1", (1.1, 1.1), "f2"],                                                   # crosses v1v3
    ["f1", (2.2, 1.0), "f0"],                                                   # crosses v2v3
    ["f1", (1.1, 0.0), (2.4, -0.5), "f0"],                                      # crosses v1v2
    ["f2", (0.0, 1.0), (-0.6, -0.5), (1.2, -1.05), (3.3, -0.75), "f0"],         # crosses v4v1
    ["f2", (1.0, 2.2), (1.7, 3.2), (3.3, 4.0), (4.55, 3.3), (4.5, 1.7), "f0"],  # crosses v3v4
    ["f0", (3.3, 1.9), (2.85, 2.6), (3.2, 3.55), (4.05, 3.2), (4.0, 1.9), "f0"],  # loop across v3v5
]


def spline(points, k=24):
    """Catmull-Rom curve through the given points."""
    p = np.array([points[0]] + points + [points[-1]], dtype=float)
    out = []
    for i in range(1, len(p) - 2):
        t = np.linspace(0, 1, k, endpoint=False)[:, None]
        a, b, c, d = p[i - 1], p[i], p[i + 1], p[i + 2]
        out.append(0.5 * ((2 * b) + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t ** 2
                          + (-a + 3 * b - 3 * c + d) * t ** 3))
    out.append(p[-2][None, :])
    return np.vstack(out)


fig, ax = G.canvas(5.6, 5.4, scale=0.8)
ax.set_xlim(-1.0, 5.0)
ax.set_ylim(-1.4, 4.4)
G.draw(ax, pos, edges, vertex_labels=TEX)
for route in routes:
    pts = [dual[p] if isinstance(p, str) else p for p in route]
    xy = spline(pts)
    far = np.ones(len(xy), dtype=bool)
    for name in (route[0], route[-1]):
        far &= np.hypot(*(xy - np.array(dual[name])).T) > G.RADIUS
    ax.plot(xy[far, 0], xy[far, 1], color=G.RED, lw=G.EDGE, ls="--", zorder=1)
G.draw(ax, dual, [], vertex_color={f: G.RED for f in dual},
       vertex_labels={f: f"$f_{f[1]}^*$" for f in dual})
