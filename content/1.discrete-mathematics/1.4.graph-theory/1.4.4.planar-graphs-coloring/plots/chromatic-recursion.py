# Theorem 4.6.7 on the 4-cycle (Example 4.6.2): colorings of C4 split into those with
# v1, v3 colored differently (add the edge v1v3) and those with v1, v3 alike (merge them).
import wikigraph as G

TEX = {f"v{i}": f"$v_{i}$" for i in range(1, 5)} | {"v13": "$v_{13}$"}
sq = {"v1": (0, 0), "v2": (1.8, 0), "v3": (1.8, 1.8), "v4": (0, 1.8)}
c4 = [("v1", "v2"), ("v2", "v3"), ("v3", "v4"), ("v4", "v1")]
titles = ["$G = C_4$:  $t(t-1)(t^2-3t+3)$", "$G + (v_1, v_3)$:  $t(t-1)(t-2)^2$",
          "$v_1, v_3$ merged:  $t(t-1)^2$"]
fig, (a, b, c) = G.panels(3, 1.8, 1.8, titles=titles, scale=1.0, margin=0.7)
G.draw(a, sq, c4, vertex_labels=TEX)
G.draw(b, sq, c4 + [("v1", "v3")], highlight={("v1", "v3"): G.RED}, vertex_labels=TEX)
merged = {"v13": (0.2, 0.2), "v2": (1.8, 0.2), "v4": (0.2, 1.8)}
G.draw(c, merged, [("v13", "v2"), ("v13", "v4")], highlight={"v13": G.RED}, vertex_labels=TEX)
