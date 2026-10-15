import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [6.0, 1.0, 0.5, 0.0],
    [0.5, 2.0, 0.0, 0.5],
    [1.0, 1.0, -3.0, 1.0],
    [0.0, 0.5, 0.5, 3.0 + 2.5j],
])
eigenvalues = np.linalg.eigvals(A)

fig, ax = plt.subplots(figsize=(7, 4.5))
for i in range(A.shape[0]):
    center = A[i, i]
    radius = np.sum(np.abs(A[i])) - np.abs(center)
    ax.add_patch(plt.Circle((center.real, center.imag), radius, alpha=0.25, color=f"C{i}"))
    ax.add_patch(plt.Circle((center.real, center.imag), radius, fill=False, color=f"C{i}"))
    ax.plot(center.real, center.imag, "+", color=f"C{i}", markersize=9)
    ax.annotate(f"$G_{i + 1}$", (center.real, center.imag + radius), textcoords="offset points",
                xytext=(0, 4), ha="center", color=f"C{i}")
ax.plot(eigenvalues.real, eigenvalues.imag, "kx", markersize=8, label="eigenvalues")
ax.set_aspect("equal")
ax.set_xlim(-6.5, 9)
ax.set_ylim(-3.5, 5)
ax.axhline(0, color="gray", linewidth=0.8)
ax.axvline(0, color="gray", linewidth=0.8)
ax.set_xlabel("Re z")
ax.set_ylabel("Im z")
ax.set_title("Gershgorin discs (centers +) and eigenvalues (x)")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
