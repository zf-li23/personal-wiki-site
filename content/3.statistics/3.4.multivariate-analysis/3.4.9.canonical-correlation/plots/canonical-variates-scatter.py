"""Sample canonical variates for simulated data with two sets of variables (p = 2, q = 3)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 300
z = rng.standard_normal((n, 2))
X1 = np.column_stack([z[:, 0] + 0.4 * rng.standard_normal(n), 0.6 * z[:, 1] + 0.9 * rng.standard_normal(n)])
X2 = np.column_stack([
    z[:, 0] + 0.3 * z[:, 1] + 0.5 * rng.standard_normal(n),
    0.7 * z[:, 1] + 0.8 * rng.standard_normal(n),
    rng.standard_normal(n),
])


def inv_sqrt(A):
    w, V = np.linalg.eigh(A)
    return V @ np.diag(w**-0.5) @ V.T


S = np.cov(np.column_stack([X1, X2]).T)
p = X1.shape[1]
S11, S12, S22 = S[:p, :p], S[:p, p:], S[p:, p:]
Y = inv_sqrt(S11) @ S12 @ inv_sqrt(S22)
P1, rho, P2t = np.linalg.svd(Y)
A = (inv_sqrt(S11) @ P1).T
B = (inv_sqrt(S22) @ P2t.T[:, :p]).T
U = (X1 - X1.mean(axis=0)) @ A.T
V = (X2 - X2.mean(axis=0)) @ B.T
fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), sharex=True, sharey=True)
for k, ax in enumerate(axes):
    ax.plot(U[:, k], V[:, k], "o", ms=3, alpha=0.6, color=f"C{k}")
    ax.set_title(f"pair {k + 1}: sample canonical correlation = {rho[k]:.2f}")
    ax.set_xlabel(f"U_{k + 1}")
    ax.set_ylabel(f"V_{k + 1}")
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
fig.tight_layout()
