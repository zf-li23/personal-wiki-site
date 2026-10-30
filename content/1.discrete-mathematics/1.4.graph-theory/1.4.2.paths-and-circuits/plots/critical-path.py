import wikigraph as G

# PT graph: vertices are tasks, an arc u -> v carries the duration of u
dur = {"s": 0, "A": 3, "B": 2, "C": 4, "D": 2, "E": 3, "t": 0}
arcs = [("s", "A"), ("s", "B"), ("A", "C"), ("A", "D"), ("B", "D"), ("C", "E"), ("D", "E"), ("E", "t")]
order = ["s", "A", "B", "C", "D", "E", "t"]  # a topological order
early = {"s": 0}
for v in order[1:]:
    early[v] = max(early[u] + dur[u] for u, x in arcs if x == v)
tail = {"t": 0}  # longest path from v to t
for v in reversed(order[:-1]):
    tail[v] = max(dur[v] + tail[x] for u, x in arcs if u == v)
late = {v: early["t"] - tail[v] for v in order}
critical = [v for v in order if early[v] == late[v]]

pos = {"s": (0, 1.0), "A": (1.5, 2.0), "B": (1.5, 0), "C": (3.0, 2.0), "D": (3.0, 0), "E": (4.5, 1.0),
       "t": (6.0, 1.0)}
fig, ax = G.canvas(6.0, 2.0, margin=0.8)
hl = {(u, v): G.RED for u, v in arcs if u in critical and v in critical and early[v] == early[u] + dur[u]}
hl.update({v: G.RED for v in critical})
G.draw(ax, pos, [(u, v, dur[u]) for u, v in arcs], directed=True, weights=True, highlight=hl)
for v, (x, y) in pos.items():
    G.caption(ax, (x, y + 0.45 if y > 0.5 else y - 0.45), f"[{early[v]}, {late[v]}]", size=9)
G.caption(ax, (3.0, -0.95), "[earliest start, latest start]; critical path in red, length " + str(early["t"]),
          size=9)
