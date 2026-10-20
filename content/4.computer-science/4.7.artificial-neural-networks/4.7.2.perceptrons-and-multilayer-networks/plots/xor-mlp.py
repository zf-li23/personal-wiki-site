"""XOR with a perceptron and with a multilayer perceptron. Left: the four XOR
points; no line separates the classes. Middle: decision regions of a 2-4-1 MLP
(tanh hidden layer, sigmoid output) trained by gradient descent on the
cross-entropy loss. Right: the training loss against the number of epochs."""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)

rng = np.random.default_rng(3)
W1 = rng.normal(0, 1, (4, 2))
b1 = np.zeros(4)
w2 = rng.normal(0, 1, 4)
b2 = 0.0
eta, losses = 0.5, []
for epoch in range(3000):
    H = np.tanh(X @ W1.T + b1)
    p = 1 / (1 + np.exp(-(H @ w2 + b2)))
    losses.append(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))
    d_out = (p - y) / len(X)               # dE/dz at the sigmoid output
    d_hid = np.outer(d_out, w2) * (1 - H ** 2)
    w2 -= eta * H.T @ d_out
    b2 -= eta * d_out.sum()
    W1 -= eta * d_hid.T @ X
    b1 -= eta * d_hid.sum(axis=0)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.9))
for ax in axes[:2]:
    ax.scatter(X[y == 0, 0], X[y == 0, 1], s=90, marker="o", color="C0", zorder=3, label="class 0")
    ax.scatter(X[y == 1, 0], X[y == 1, 1], s=110, marker="X", color="C3", zorder=3, label="class 1")
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
axes[0].set_title("XOR: not linearly separable", fontsize=10)
axes[0].legend(fontsize=8, loc="upper center", ncol=2)
g = np.linspace(-0.5, 1.5, 300)
G1, G2 = np.meshgrid(g, g)
P = np.c_[G1.ravel(), G2.ravel()]
prob = 1 / (1 + np.exp(-(np.tanh(P @ W1.T + b1) @ w2 + b2)))
cs = axes[1].contourf(G1, G2, prob.reshape(G1.shape), levels=np.linspace(0, 1, 11), cmap="RdBu_r", alpha=0.55)
axes[1].contour(G1, G2, prob.reshape(G1.shape), levels=[0.5], colors="k", linewidths=1.5)
fig.colorbar(cs, ax=axes[1], fraction=0.046, label="P(class 1)")
axes[1].set_title("2-4-1 MLP: decision boundary P = 0.5", fontsize=10)
axes[2].plot(losses, color="C0")
axes[2].set_yscale("log")
axes[2].set_xlabel("epoch")
axes[2].set_ylabel("cross-entropy loss")
axes[2].set_title("training loss", fontsize=10)
axes[2].grid(alpha=0.3)
fig.tight_layout()
