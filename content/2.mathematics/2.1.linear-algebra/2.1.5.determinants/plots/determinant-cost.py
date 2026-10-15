import math
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 21)
# Multiplications: full (Leibniz) expansion, recursive cofactor expansion, Gaussian elimination
leibniz = np.array([math.factorial(int(k)) * (int(k) - 1) for k in n], dtype=float)
cofactor = np.zeros(n.size)
for i, k in enumerate(n):
    cofactor[i] = 0 if k == 1 else k * (cofactor[i - 1] + 1)
elimination = np.array([sum(j * j + j for j in range(1, k)) + (k - 1) for k in n], dtype=float)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.semilogy(n, np.maximum(leibniz, 1), "o-", markersize=4, label=r"full expansion, $(n-1)\cdot n!$")
ax.semilogy(n, np.maximum(cofactor, 1), "s-", markersize=4, label=r"cofactor expansion, $\approx (e-1)\cdot n!$")
ax.semilogy(n, np.maximum(elimination, 1), "^-", markersize=4, label=r"Gaussian elimination, $\approx n^3/3$")
ax.axhline(1e9, color="gray", linestyle="--", linewidth=1)
ax.text(1.2, 1.6e9, "about one second of work", color="gray", fontsize=9)
ax.set_xticks(range(0, 21, 2))
ax.set_xlabel("order n")
ax.set_ylabel("number of multiplications")
ax.set_title("Cost of computing an n x n determinant")
ax.legend(fontsize=9)
ax.grid(True, which="major", alpha=0.3)
fig.tight_layout()
