import wikigraph as G

pos = {"a": (0, 0), "b": (1.4, 0), "c": (2.8, 0), "d": (0, 1.6), "e": (1.4, 1.6), "f": (2.8, 1.6)}
E = [("a", "b"), ("b", "c"), ("d", "e"), ("e", "f"), ("a", "d"), ("b", "e"), ("c", "f"), ("a", "e"), ("e", "c")]
titles = ["G", "a subgraph", "a spanning subgraph", "induced by {a, b, d, e}"]
fig, axes = G.panels(4, 2.8, 1.6, titles=titles)
G.draw(axes[0], pos, E)
sub = {k: pos[k] for k in "abef"}
G.draw(axes[1], sub, [("a", "b"), ("e", "f")])
G.draw(axes[2], pos, [("a", "b"), ("b", "c"), ("e", "f"), ("a", "d"), ("e", "c")])
# induced subgraph: every edge of G with both ends in the chosen set
S = set("abde")
G.draw(axes[3], {k: pos[k] for k in S}, [e for e in E if set(e) <= S], highlight={v: G.BLUE for v in S})
