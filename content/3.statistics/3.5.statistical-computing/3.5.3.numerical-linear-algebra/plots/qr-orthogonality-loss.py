"""Loss of orthogonality ||I - Q^T Q|| of classical Gram-Schmidt, modified Gram-Schmidt and Householder QR."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
m, n = 50, 12
eps = np.finfo(float).eps


def cgs(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            v -= (Q[:, i] @ A[:, j]) * Q[:, i]  # coefficient from the original column
        Q[:, j] = v / np.linalg.norm(v)
    return Q


def mgs(A):
    V = A.copy()
    m, n = A.shape
    Q = np.zeros((m, n))
    for i in range(n):
        Q[:, i] = V[:, i] / np.linalg.norm(V[:, i])
        for j in range(i + 1, n):
            V[:, j] -= (Q[:, i] @ V[:, j]) * Q[:, i]  # coefficient from the updated column
    return Q


def test_matrix(kappa):
    U, _ = np.linalg.qr(rng.standard_normal((m, n)))
    V, _ = np.linalg.qr(rng.standard_normal((n, n)))
    s = np.logspace(0, -np.log10(kappa), n)
    return U @ np.diag(s) @ V.T


kappas = np.logspace(1, 15, 29)
loss = {"CGS": [], "MGS": [], "Householder": []}
for k in kappas:
    A = test_matrix(k)
    for name, Q in [("CGS", cgs(A)), ("MGS", mgs(A)), ("Householder", np.linalg.qr(A)[0])]:
        loss[name].append(np.linalg.norm(np.eye(n) - Q.T @ Q, 2))

fig, ax = plt.subplots(figsize=(7, 4.6))
styles = {"CGS": ("C3", "o"), "MGS": ("C0", "s"), "Householder": ("C2", "^")}
for name, vals in loss.items():
    c, mk = styles[name]
    ax.loglog(kappas, vals, marker=mk, ms=4, lw=1.4, color=c, label=name)
ax.loglog(kappas, eps * kappas, ls="--", lw=1, color="gray", label="eps * kappa")
ax.loglog(kappas, np.minimum(eps * kappas**2, 10), ls=":", lw=1, color="gray", label="eps * kappa^2")
ax.set_xlabel("condition number kappa(A)")
ax.set_ylabel("||I - Q^T Q||_2")
ax.set_title("Loss of orthogonality of the computed Q (50 x 12)")
ax.set_ylim(1e-17, 1e2)
ax.legend(loc="upper left")
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
