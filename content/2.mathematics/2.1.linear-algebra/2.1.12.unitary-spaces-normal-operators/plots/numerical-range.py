"""Numerical range W(A) = {x^H A x : ||x|| = 1} of a normal matrix and of a
non-normal matrix with the same eigenvalues."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
lam = np.array([1.0 + 0.0j, -0.5 + 1.0j, -0.8 - 0.6j])
Q, _ = np.linalg.qr(rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3)))
normal = Q @ np.diag(lam) @ Q.conj().T                      # unitarily diagonalizable
triangular = np.diag(lam) + np.array([[0, 1.2, 0.8], [0, 0, 1.0], [0, 0, 0]])
cases = [(normal, "normal: $W(A)$ = convex hull of the eigenvalues"),
         (triangular, "non-normal (upper triangular), same eigenvalues")]


def boundary(A, m=720):
    """Support points of W(A): top eigenvector of the Hermitian part of e^{it} A."""
    pts = []
    for t in np.linspace(0, 2 * np.pi, m):
        B = np.exp(1j * t) * A
        H = (B + B.conj().T) / 2
        w, V = np.linalg.eigh(H)
        x = V[:, -1]
        pts.append(x.conj() @ A @ x)
    return np.array(pts)


fig, axes = plt.subplots(1, 2, figsize=(11, 5), sharex=True, sharey=True)
for ax, (A, title) in zip(axes, cases):
    X = rng.standard_normal((3, 4000)) + 1j * rng.standard_normal((3, 4000))
    X /= np.linalg.norm(X, axis=0)
    samples = np.einsum("ij,ik,kj->j", X.conj(), A, X)      # x^H A x for random unit x
    ax.plot(samples.real, samples.imag, ".", markersize=1.5, color="C0", alpha=0.35)
    b = boundary(A)
    ax.plot(b.real, b.imag, color="C0", linewidth=1.8, label="boundary of $W(A)$")
    ev = np.linalg.eigvals(A)
    ax.plot(ev.real, ev.imag, "o", color="C3", markersize=8, label="eigenvalues")
    hull = np.append(lam, lam[0])
    ax.plot(hull.real, hull.imag, "--", color="C1", linewidth=1.2, label="convex hull of eigenvalues")
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("Re")
    ax.grid(True, alpha=0.3)
axes[0].set_ylabel("Im")
axes[0].legend(loc="lower right", fontsize=8)
fig.tight_layout()
