import wikigraph as G

pos = {"a": (0, 1.0), "b": (1.4, 2.0), "c": (1.4, 0), "d": (2.8, 2.0), "e": (2.8, 0), "f": (4.2, 1.0)}
E = [("a", "b"), ("a", "c"), ("b", "c"), ("b", "d"), ("c", "e"), ("d", "e"), ("d", "f"), ("e", "f")]
adj = {v: sorted(u for e in E for u in e if v in e and u != v) for v in pos}

# BFS from a, neighbours in alphabetical order
layer, bfs_tree, queue = {"a": 0}, [], ["a"]
while queue:
    u = queue.pop(0)
    for v in adj[u]:
        if v not in layer:
            layer[v] = layer[u] + 1
            bfs_tree.append((u, v))
            queue.append(v)

# DFS from a
seen, dfs_tree = set(), []


def dfs(u):
    seen.add(u)
    for v in adj[u]:
        if v not in seen:
            dfs_tree.append((u, v))
            dfs(v)


dfs("a")
order = {}
for k, (u, v) in enumerate(dfs_tree):
    order.setdefault(u, 0)
    order[v] = k + 1

fig, axes = G.panels(3, 4.2, 2.0, margin=0.6, titles=["graph", "BFS from a: layers", "DFS from a: tree and back edges"])
G.draw(axes[0], pos, E)
shade = [G.BLUE, G.GREEN, G.AMBER, G.RED]
G.draw(axes[1], pos, E, dashed=[e for e in E if e not in bfs_tree and e[::-1] not in bfs_tree],
       highlight={**{e: G.BLUE for e in bfs_tree}, **{v: shade[layer[v]] for v in pos}},
       )
for v, (x, y) in pos.items():
    G.caption(axes[1], (x, y + (0.42 if y > 0.5 else -0.42)), f"layer {layer[v]}", size=8)
G.draw(axes[2], pos, E, dashed=[e for e in E if e not in dfs_tree and e[::-1] not in dfs_tree],
       highlight={e: G.RED for e in dfs_tree})
for v, (x, y) in pos.items():
    G.caption(axes[2], (x, y + (0.42 if y > 0.5 else -0.42)), f"#{order[v] + 1}", size=8)
