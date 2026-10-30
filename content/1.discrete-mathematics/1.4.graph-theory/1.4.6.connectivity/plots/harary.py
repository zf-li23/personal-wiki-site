# Harary graphs H(k, 8): k-connected with the fewest possible edges, ceil(8k/2)
import wikigraph as G


def harary(k, n):
    edges = {tuple(sorted((i, (i + j) % n))) for i in range(n) for j in range(1, k // 2 + 1)}
    if k % 2:
        if n % 2 == 0:
            edges |= {(i, i + n // 2) for i in range(n // 2)}
        else:
            edges |= {tuple(sorted((i, (i + (n - 1) // 2) % n))) for i in range((n + 1) // 2)}
    return sorted(edges)


n = 8
ks = [2, 3, 4, 5]
fig, axes = G.panels(len(ks), 2.4, 2.4, scale=0.75,
                     titles=[f"H({k}, {n}): {len(harary(k, n))} edges" for k in ks])
pos = G.circle(range(n), radius=1.1, center=(1.2, 1.2))
for k, ax in zip(ks, axes):
    base = harary(k - k % 2, n)
    G.draw(ax, pos, harary(k, n), labels=False, radius=0.13,
           highlight={e: G.RED for e in harary(k, n) if e not in base})
