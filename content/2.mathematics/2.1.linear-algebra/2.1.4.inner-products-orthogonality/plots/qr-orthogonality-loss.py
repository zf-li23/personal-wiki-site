import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
m, n = 60, 30


def classical_gs(A):
    # Classical Gram-Schmidt: project a_j onto the original q_1..q_{j-1} at once
    m, n = A.shape
    Q = np.zeros((m, n))
    for j in range(n):
        v = A[:, j] - Q[:, :j] @ (Q[:, :j].T @ A[:, j])
        Q[:, j] = v / np.linalg.norm(v)
    return Q


def modified_gs(A):
    # Modified Gram-Schmidt: remove each direction from the updated vector in turn
    V = A.astype(float).copy()
    m, n = V.shape
    Q = np.zeros((m, n))
    for j in range(n):
        Q[:, j] = V[:, j] / np.linalg.norm(V[:, j])
        for k in range(j + 1, n):
            V[:, k] -= (Q[:, j] @ V[:, k]) * Q[:, j]
    return Q


def householder_qr(A):
    # Householder QR: apply reflections H_v = I - 2 v v^T, then form the first n columns of Q
    R = A.astype(float).copy()
    m, n = R.shape
    vs = []
    for j in range(n):
        x = R[j:, j]
        v = x.copy()
        v[0] += np.copysign(np.linalg.norm(x), x[0])
        v /= np.linalg.norm(v)
        R[j:, j:] -= 2.0 * np.outer(v, v @ R[j:, j:])
        vs.append(v)
    Q = np.eye(m)[:, :n]
    for j in reversed(range(n)):
        v = vs[j]
        Q[j:, :] -= 2.0 * np.outer(v, v @ Q[j:, :])
    return Q


exponents = np.linspace(0, 15, 31)
conds = 10.0 ** exponents
U, _ = np.linalg.qr(rng.standard_normal((m, n)))
V, _ = np.linalg.qr(rng.standard_normal((n, n)))
methods = {
    "classical Gram-Schmidt": classical_gs,
    "modified Gram-Schmidt": modified_gs,
    "Householder": householder_qr,
}
losses = {name: [] for name in methods}
for c in conds:
    s = np.logspace(0, -np.log10(c), n)
    A = U @ np.diag(s) @ V.T
    for name, f in methods.items():
        Q = f(A)
        losses[name].append(np.linalg.norm(np.eye(n) - Q.T @ Q, 2))

fig, ax = plt.subplots(figsize=(7, 4.5))
for (name, vals), marker in zip(losses.items(), ["o", "s", "^"]):
    ax.loglog(conds, np.maximum(vals, 1e-17), marker=marker, markersize=4, label=name)
ax.loglog(conds, 1e-16 * conds, "k--", linewidth=1, label=r"$\varepsilon\,\kappa(A)$")
ax.loglog(conds, 1e-16 * conds**2, "k:", linewidth=1, label=r"$\varepsilon\,\kappa(A)^2$")
ax.set_ylim(1e-17, 1e1)
ax.set_xlabel(r"condition number $\kappa(A)$")
ax.set_ylabel(r"loss of orthogonality $\|I - Q^{T}Q\|_2$")
ax.set_title(f"QR of a {m} x {n} matrix in double precision")
ax.legend(fontsize=9, loc="lower right", bbox_to_anchor=(1.0, 0.1))
ax.grid(True, which="major", alpha=0.3)
fig.tight_layout()
