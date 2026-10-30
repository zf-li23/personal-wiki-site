# The searches of Example 5.1.1 after the first augmentation. From x4 the alternating tree
# reaches the unsaturated y4 (tree edges green, edges of the augmenting path not in M red); from x5 it stops with
# X0 = {x5, x2}, Y0 = {y1} and Gamma(X0) inside Y0, so x5 gets label 2.
import wikigraph as G

# the bipartite graph of Example 5.1.1
X = [f"x{i}" for i in range(1, 6)]
Y = [f"y{i}" for i in range(1, 6)]
ADJ = {"x1": ["y1", "y2"], "x2": ["y1"], "x3": ["y2", "y3", "y4", "y5"], "x4": ["y3"], "x5": ["y1"]}
EDGES = [(x, y) for x in X for y in ADJ[x]]
POS = {x: (1.1 * i, 1.8) for i, x in enumerate(X)} | {y: (1.1 * i, 0.0) for i, y in enumerate(Y)}
TEX = {v: f"${v[0]}_{v[1]}$" for v in X + Y}

M1 = [("x2", "y1"), ("x1", "y2"), ("x3", "y3")]
M2 = [("x2", "y1"), ("x1", "y2"), ("x4", "y3"), ("x3", "y4")]
tree4 = [("x4", "y3"), ("y3", "x3"), ("x3", "y2"), ("y2", "x1"), ("x1", "y1"), ("y1", "x2"), ("x3", "y4")]
path4 = [("x4", "y3"), ("y3", "x3"), ("x3", "y4")]
tree5 = [("x5", "y1"), ("y1", "x2")]


def key(e):
    return tuple(sorted(e))


def colours(matching, tree, path):
    out = {key(e): G.GREEN for e in tree}          # edges of the alternating tree
    out |= {key(e): G.RED for e in path}           # non-matching edges of the augmenting path
    out |= {key(e): G.BLUE for e in matching}      # matching edges
    return {tuple(e): c for e, c in out.items()}


fig, axes = G.panels(3, 4.4, 1.8, titles=["search from $x_4$: path $x_4y_3x_3y_4$",
                                           "search from $x_5$: $\\Gamma(X_0) = Y_0 = \\{y_1\\}$",
                                           "maximum matching, |M| = 4"])
G.draw(axes[0], POS, EDGES, highlight=colours(M1, tree4, path4), vertex_labels=TEX,
       vertex_color={"x4": G.AMBER, "y4": G.AMBER})
G.draw(axes[1], POS, EDGES, highlight=colours(M2, tree5, []), vertex_labels=TEX,
       vertex_color={"x5": G.AMBER, "x2": G.AMBER, "y1": G.AMBER})
G.draw(axes[2], POS, EDGES, highlight={e: G.BLUE for e in M2}, vertex_labels=TEX,
       vertex_color={"x5": G.GREY, "y5": G.GREY})
