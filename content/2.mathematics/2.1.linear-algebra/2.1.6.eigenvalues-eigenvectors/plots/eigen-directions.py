import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack([np.cos(theta), np.sin(theta)])
samples = np.linspace(0, 2 * np.pi, 24, endpoint=False)
X = np.vstack([np.cos(samples), np.sin(samples)])

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

# Left: real eigenvalues 2.5 and 1; eigenvectors keep their direction
ax = axes[0]
A = np.array([[2.0, 1.0], [0.5, 1.5]])
img = A @ circle
ax.plot(circle[0], circle[1], color="gray", lw=1, ls="--", label=r"unit circle $\|\boldsymbol{x}\| = 1$")
ax.plot(img[0], img[1], color="C0", lw=1.5, label=r"image $\{A\boldsymbol{x}\}$")
AX = A @ X
for i in range(X.shape[1]):
    ax.annotate("", xy=AX[:, i], xytext=X[:, i],
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8, alpha=0.7))
vals, vecs = np.linalg.eig(A)
for k, color in zip(range(2), ["C1", "C2"]):
    u = vecs[:, k] / np.linalg.norm(vecs[:, k])
    s = np.linspace(-3.2, 3.2, 2)
    ax.plot(s * u[0], s * u[1], color=color, lw=1, ls=":")
    for sign in [1, -1]:
        ax.annotate("", xy=sign * vals[k] * u, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.2, mutation_scale=14))
    offset = np.array([0.15, 0.15]) if vals[k] > 1.5 else np.array([-0.9, 0.1])
    ax.text(*(vals[k] * u * 1.05 + offset), f"$\\lambda = {vals[k]:.3g}$", color=color, fontsize=11)
ax.set_title(r"$A = [2\ \ 1;\ 0.5\ \ 1.5]$: eigenvectors are only stretched")
ax.set_aspect("equal")
ax.set_xlim(-3.3, 3.3)
ax.set_ylim(-3.0, 3.0)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9)

# Right: complex eigenvalues 0.9 e^{+-i pi/6}; every vector is rotated, none keeps its direction
ax = axes[1]
r, phi = 0.9, np.pi / 6
B = r * np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
img = B @ circle
ax.plot(circle[0], circle[1], color="gray", lw=1, ls="--", label=r"unit circle")
ax.plot(img[0], img[1], color="C0", lw=1.5, label=r"image $\{B\boldsymbol{x}\}$")
BX = B @ X
for i in range(X.shape[1]):
    ax.annotate("", xy=BX[:, i], xytext=X[:, i],
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8, alpha=0.7))
orbit = [np.array([1.0, 0.0]) * 1.5]
for _ in range(30):
    orbit.append(B @ orbit[-1])
orbit = np.array(orbit)
ax.plot(orbit[:, 0], orbit[:, 1], "o-", color="C3", markersize=3, lw=1, label=r"orbit $B^t\boldsymbol{x}_0$")
ax.set_title(r"$B = 0.9\,R_{\pi/6}$: eigenvalues $0.9\,\mathrm{e}^{\pm\mathrm{i}\pi/6}$, no real eigenvector")
ax.set_aspect("equal")
ax.set_xlim(-1.7, 1.7)
ax.set_ylim(-1.55, 1.55)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
