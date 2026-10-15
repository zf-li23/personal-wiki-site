import numpy as np
import matplotlib.pyplot as plt

# Surfaces z = d1*x^2 + d2*y^2 for the five non-constant congruence normal forms
cases = [
    ((1, 1), "diag(1, 1): minimum"),
    ((-1, -1), "diag(-1, -1): maximum"),
    ((1, -1), "diag(1, -1): saddle"),
    ((1, 0), "diag(1, 0): degenerate"),
    ((-1, 0), "diag(-1, 0): degenerate"),
]

t = np.linspace(-1.0, 1.0, 41)
x, y = np.meshgrid(t, t)

fig = plt.figure(figsize=(15, 3.6))
for k, ((d1, d2), title) in enumerate(cases, start=1):
    ax = fig.add_subplot(1, 5, k, projection="3d")
    z = d1 * x**2 + d2 * y**2
    ax.plot_surface(x, y, z, cmap="viridis", linewidth=0, antialiased=True, alpha=0.9)
    ax.set_title(title, fontsize=10)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])
    ax.set_zlim(-2, 2)
    ax.set_xlabel("y1")
    ax.set_ylabel("y2")
    ax.view_init(elev=25, azim=-60)
fig.tight_layout()
