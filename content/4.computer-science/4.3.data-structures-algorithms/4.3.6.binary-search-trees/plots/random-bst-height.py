"""Height and average depth of random BSTs under two models of randomness."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def bst_by_permutation(n):
    """Insert a random permutation of 0..n-1; return (height, average depth)."""
    keys = rng.permutation(n)
    lc = np.full(n, -1)
    rc = np.full(n, -1)
    depth = np.zeros(n, dtype=int)
    root = keys[0]
    for k in keys[1:]:
        v, d = root, 0
        while True:
            d += 1
            side = lc if k < v else rc
            if side[v] < 0:
                side[v] = k
                depth[k] = d
                break
            v = side[v]
    return depth.max(), depth.mean()


def bst_by_shape(n):
    """Uniformly random binary tree with n internal nodes (Remy's algorithm).

    Every such tree is equally likely; as a BST its keys are fixed by the inorder.
    Returns (height, average depth) of the internal nodes.
    """
    size = 2 * n + 1
    parent = np.full(size, -1)
    child = np.full((size, 2), -1)
    nodes = 1                                      # node 0: a single external node
    for _ in range(n):
        x = rng.integers(nodes)                    # any existing node, internal or external
        side = rng.integers(2)
        new_int, new_ext = nodes, nodes + 1
        nodes += 2
        p = parent[x]                              # new internal node takes x's place
        if p >= 0:
            child[p, 0 if child[p, 0] == x else 1] = new_int
        parent[new_int] = p
        child[new_int, side] = x
        child[new_int, 1 - side] = new_ext
        parent[x] = parent[new_ext] = new_int
    root = int(np.flatnonzero(parent[:nodes] < 0)[0])
    depths, frontier, d = [], [root], 0
    while frontier:                                # level by level over internal nodes
        internal = [v for v in frontier if child[v, 0] >= 0]
        depths += [d] * len(internal)
        frontier = [c for v in internal for c in child[v]]
        d += 1
    return max(depths), float(np.mean(depths))


ns = np.array([2 ** k for k in range(4, 13)])
trials = 20
perm = np.array([[bst_by_permutation(n) for _ in range(trials)] for n in ns]).mean(axis=1)
shape = np.array([[bst_by_shape(n) for _ in range(trials)] for n in ns]).mean(axis=1)

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(ns, shape[:, 0], "s-", color="C3", label="random shape: height")
ax.plot(ns, 2 * np.sqrt(np.pi * ns), ":", color="C3", label=r"$2\sqrt{\pi n}$")
ax.plot(ns, perm[:, 0], "o-", color="C0", label="random insertion order: height")
ax.plot(ns, perm[:, 1], "^-", color="C2", label="random insertion order: average depth")
harmonic = np.array([np.sum(1.0 / np.arange(1, n + 1)) for n in ns])
ax.plot(ns, 2 * (1 + 1 / ns) * harmonic - 4, ":", color="C2",
        label=r"exact mean $2(1+1/n)H_n-4$")
ax.plot(ns, np.log2(ns), "--", color="0.5", label=r"$\log_2 n$ (ideal)")
ax.set_xscale("log", base=2)
ax.set_yscale("log")
ax.set_xlabel("number of keys n")
ax.set_ylabel("edges from the root")
ax.set_title(f"Random BSTs (mean of {trials} trials)")
ax.legend(fontsize=8)
fig.tight_layout()
