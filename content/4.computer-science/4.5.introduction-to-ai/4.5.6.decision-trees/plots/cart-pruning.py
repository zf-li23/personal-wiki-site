"""CART classification tree on two-dimensional data: the full tree, the tree chosen by
cost-complexity pruning on a validation set, and the error along the pruning sequence."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def make_data(n):
    X = rng.uniform(-1, 1, (n, 2))
    p = 1 / (1 + np.exp(-6 * (X[:, 1] - 0.5 * np.sin(3 * X[:, 0]))))   # smooth true boundary
    y = (rng.random(n) < p).astype(int)
    return X, y


Xtr, ytr = make_data(300)
Xva, yva = make_data(2000)


def gini(y):
    if len(y) == 0:
        return 0.0
    p = y.mean()
    return 2 * p * (1 - p)


def grow(X, y, min_leaf=1):
    """Grow a full binary tree with Gini splits; a node is a dict."""
    node = {"n": len(y), "label": int(round(y.mean() + 1e-9)) if len(y) else 0,
            "err": min(y.sum(), len(y) - y.sum())}
    if node["err"] == 0 or len(y) < 2 * min_leaf:
        return node
    best = None
    for j in range(X.shape[1]):
        order = np.argsort(X[:, j])
        xs, ys = X[order, j], y[order]
        c1 = np.cumsum(ys)
        for k in range(min_leaf, len(y) - min_leaf + 1):
            if xs[k - 1] == xs[k]:                     # no threshold between equal values
                continue
            nl, nr = k, len(y) - k
            pl, pr = c1[k - 1] / nl, (c1[-1] - c1[k - 1]) / nr
            score = nl * 2 * pl * (1 - pl) + nr * 2 * pr * (1 - pr)
            if best is None or score < best[0]:
                best = (score, j, (xs[k - 1] + xs[k]) / 2)
    if best is None:
        return node
    _, j, thr = best
    m = X[:, j] <= thr
    node.update(feature=j, threshold=thr, left=grow(X[m], y[m], min_leaf), right=grow(X[~m], y[~m], min_leaf))
    return node


def leaves(node):
    return 1 if "left" not in node else leaves(node["left"]) + leaves(node["right"])


def subtree_err(node):
    return node["err"] if "left" not in node else subtree_err(node["left"]) + subtree_err(node["right"])


def predict(node, X):
    out = np.empty(len(X), dtype=int)
    for i, x in enumerate(X):
        t = node
        while "left" in t:
            t = t["left"] if x[t["feature"]] <= t["threshold"] else t["right"]
        out[i] = t["label"]
    return out


def weakest_link(node):
    """Return (alpha, node) minimizing g(t) = (R(t) - R(T_t)) / (|T_t| - 1) over internal nodes."""
    if "left" not in node:
        return (np.inf, None)
    here = ((node["err"] - subtree_err(node)) / (leaves(node) - 1), node)
    return min([here, weakest_link(node["left"]), weakest_link(node["right"])], key=lambda t: t[0])


def copy(node):
    c = dict(node)
    if "left" in node:
        c["left"], c["right"] = copy(node["left"]), copy(node["right"])
    return c


tree = grow(Xtr, ytr)
sequence = [copy(tree)]
while "left" in tree:
    _, t = weakest_link(tree)
    for key in ("feature", "threshold", "left", "right"):
        del t[key]                                    # collapse the weakest link into a leaf
    sequence.append(copy(tree))

sizes = [leaves(t) for t in sequence]
train_err = [np.mean(predict(t, Xtr) != ytr) for t in sequence]
val_err = [np.mean(predict(t, Xva) != yva) for t in sequence]
best = int(np.argmin(val_err))

g = np.linspace(-1, 1, 161)
gx, gy = np.meshgrid(g, g)
grid = np.c_[gx.ravel(), gy.ravel()]
fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))
for ax, t, title in [(axes[0], sequence[0], f"full tree: {sizes[0]} leaves"),
                     (axes[1], sequence[best], f"pruned tree: {sizes[best]} leaves")]:
    z = predict(t, grid).reshape(gx.shape)
    ax.contourf(gx, gy, z, levels=[-0.5, 0.5, 1.5], colors=["C1", "C0"], alpha=0.2)
    ax.scatter(Xtr[ytr == 1, 0], Xtr[ytr == 1, 1], s=10, color="C0")
    ax.scatter(Xtr[ytr == 0, 0], Xtr[ytr == 0, 1], s=10, color="C1", marker="s")
    ax.plot(g, 0.5 * np.sin(3 * g), color="black", linestyle="--", linewidth=1, label="true boundary")
    ax.set_title(title)
    ax.set_xlabel("x_1")
    ax.set_ylabel("x_2")
    ax.set_aspect("equal")
    ax.legend(loc="lower right", fontsize=8)
axes[2].plot(sizes, train_err, marker=".", label="training error")
axes[2].plot(sizes, val_err, marker=".", label="validation error")
axes[2].axvline(sizes[best], color="gray", linestyle=":")
axes[2].set_xscale("log")
axes[2].set_xlabel("number of leaves along the pruning sequence")
axes[2].set_ylabel("misclassification rate")
axes[2].set_title("cost-complexity pruning")
axes[2].legend()
axes[2].grid(alpha=0.3)
fig.tight_layout()
