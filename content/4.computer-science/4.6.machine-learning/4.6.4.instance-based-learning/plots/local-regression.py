"""Instance-based regression on noisy samples of a smooth function: k-nearest-
neighbor averages, a kernel-weighted average (Nadaraya-Watson) and locally
weighted linear regression, all with a Gaussian kernel of width K_w where
applicable. Local linear fits remove the bias of the kernel average near the
ends of the data."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 60
x = np.sort(rng.uniform(0, 10, n))
f = lambda t: np.sin(t) + 0.3 * t
y = f(x) + rng.normal(0, 0.35, n)
xq = np.linspace(0, 10, 400)


def knn_regress(k):
    d = np.abs(xq[:, None] - x[None, :])
    nn = np.argsort(d, axis=1)[:, :k]
    return y[nn].mean(axis=1)


def kernel_weights(kw):
    return np.exp(-((xq[:, None] - x[None, :]) ** 2) / kw ** 2)


def nadaraya_watson(kw):
    w = kernel_weights(kw)
    return (w @ y) / w.sum(axis=1)


def local_linear(kw):
    w = kernel_weights(kw)
    out = np.empty_like(xq)
    A = np.c_[np.ones(n), x]
    for j, (q, wj) in enumerate(zip(xq, w)):
        beta = np.linalg.solve(A.T @ (wj[:, None] * A), A.T @ (wj * y))   # weighted least squares
        out[j] = beta[0] + beta[1] * q
    return out


panels = [
    ("k-NN average", [("k = 1", knn_regress(1)), ("k = 9", knn_regress(9))]),
    ("Kernel regression", [("K_w = 0.3", nadaraya_watson(0.3)), ("K_w = 1.2", nadaraya_watson(1.2))]),
    ("Locally weighted linear regression", [("K_w = 0.6", local_linear(0.6)), ("K_w = 1.2", local_linear(1.2))]),
]
fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
for ax, (title, fits) in zip(axes, panels):
    ax.scatter(x, y, s=12, color="gray", label="training data")
    ax.plot(xq, f(xq), linestyle="--", color="black", linewidth=1, label="true function")
    for label, yhat in fits:
        ax.plot(xq, yhat, label=label)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.legend(loc="upper left", fontsize=8)
axes[0].set_ylabel("y")
fig.tight_layout()
