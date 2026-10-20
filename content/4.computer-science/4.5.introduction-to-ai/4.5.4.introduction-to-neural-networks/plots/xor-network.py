"""A 2-3-1 sigmoid network trained by backpropagation on XOR: output surface and training loss."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
t = np.array([0, 1, 1, 0], dtype=float)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


W1, b1 = rng.uniform(-1, 1, (3, 2)), np.zeros(3)
W2, b2 = rng.uniform(-1, 1, 3), 0.0
eta, epochs = 0.5, 6000
losses = []
for epoch in range(epochs):
    for i in rng.permutation(4):
        h = sigmoid(W1 @ X[i] + b1)
        o = sigmoid(W2 @ h + b2)
        d_o = (t[i] - o) * o * (1 - o)
        d_h = h * (1 - h) * W2 * d_o
        W2 += eta * d_o * h
        b2 += eta * d_o
        W1 += eta * np.outer(d_h, X[i])
        b1 += eta * d_h
    out = sigmoid(sigmoid(X @ W1.T + b1) @ W2 + b2)
    losses.append(0.5 * np.sum((t - out) ** 2))

g = np.linspace(-0.5, 1.5, 201)
gx, gy = np.meshgrid(g, g)
grid = np.c_[gx.ravel(), gy.ravel()]
surface = sigmoid(sigmoid(grid @ W1.T + b1) @ W2 + b2).reshape(gx.shape)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
cs = axes[0].contourf(gx, gy, surface, levels=np.linspace(0, 1, 11), cmap="RdBu_r", alpha=0.8)
axes[0].contour(gx, gy, surface, levels=[0.5], colors="black", linewidths=1.5)
for k, marker in [(0, "o"), (1, "s")]:
    m = t == k
    axes[0].scatter(X[m, 0], X[m, 1], s=90, marker=marker, edgecolor="black",
                    color="white", label=f"target {k}", zorder=3)
fig.colorbar(cs, ax=axes[0], label="network output")
axes[0].set_xlabel("x_1")
axes[0].set_ylabel("x_2")
axes[0].set_title("output surface, boundary o = 0.5")
axes[0].legend(loc="upper center", fontsize=8)
axes[0].set_aspect("equal")
axes[1].plot(np.arange(1, epochs + 1), losses)
axes[1].set_yscale("log")
axes[1].set_xlabel("epoch")
axes[1].set_ylabel("sum of squared errors E")
axes[1].set_title("training loss (SGD, learning rate 0.5)")
axes[1].grid(alpha=0.3)
fig.tight_layout()
