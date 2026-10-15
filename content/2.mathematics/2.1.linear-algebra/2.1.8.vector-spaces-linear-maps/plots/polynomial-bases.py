import numpy as np
import matplotlib.pyplot as plt

# Three bases of the space of polynomials of degree < 4, drawn on [0, 1]
x = np.linspace(0, 1, 400)
nodes = np.array([0.0, 1 / 3, 2 / 3, 1.0])
x0 = 0.5
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

fig, axes = plt.subplots(1, 3, figsize=(16, 4.6), sharey=True)

ax = axes[0]
for k in range(4):
    ax.plot(x, x**k, color=colors[k], lw=2, label=f"x^{k}")
ax.set_title("Monomial basis 1, x, x^2, x^3")

ax = axes[1]
for k in range(4):
    ax.plot(x, (x - x0) ** k, color=colors[k], lw=2, label=f"(x - 1/2)^{k}")
ax.set_title("Shifted basis (x - x0)^k, x0 = 1/2")

ax = axes[2]
for i in range(4):
    Li = np.ones_like(x)
    for j in range(4):
        if j != i:
            Li *= (x - nodes[j]) / (nodes[i] - nodes[j])
    ax.plot(x, Li, color=colors[i], lw=2, label=f"L{i}")
ax.plot(nodes, np.zeros(4), "o", color="gray", ms=7)
ax.plot(nodes, np.ones(4), "o", color="gray", ms=7, mfc="none")
ax.set_title("Lagrange basis on nodes 0, 1/3, 2/3, 1")

for ax in axes:
    ax.axhline(0, color="gray", lw=0.6)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.legend(loc="upper left", fontsize=9)
axes[0].set_ylim(-0.6, 1.15)
fig.tight_layout()
