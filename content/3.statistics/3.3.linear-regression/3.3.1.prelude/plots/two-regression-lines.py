"""Two regression lines of a bivariate normal distribution, and the regression effect in simulated heights."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
rho = 0.5
cov = np.array([[1.0, rho], [rho, 1.0]])
xy = rng.multivariate_normal([0.0, 0.0], cov, size=200)

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

ax = axes[0]
g = np.linspace(-3, 3, 200)
gx, gy = np.meshgrid(g, g)
inv = np.linalg.inv(cov)
q = inv[0, 0] * gx**2 + 2 * inv[0, 1] * gx * gy + inv[1, 1] * gy**2
ax.contour(gx, gy, q, levels=[0.5, 1.5, 3, 5, 8], colors="gray", linewidths=0.8)
ax.plot(xy[:, 0], xy[:, 1], "o", ms=3, color="C0", alpha=0.6)
t = np.linspace(-3, 3, 2)
ax.plot(t, rho * t, color="C3", lw=2, label="E(Y | X = x) = 0.5 x")
ax.plot(rho * t, t, color="C2", lw=2, label="E(X | Y = y) = 0.5 y, i.e. y = 2 x")
ax.plot(t, t, color="black", lw=1, ls="--", label="major axis y = x")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Standard bivariate normal, rho = 0.5", fontsize=10)
ax.legend(fontsize=8, loc="upper left")

ax = axes[1]
n = 900
mu, sd, r = 68.0, 1.8, 0.65
z = rng.multivariate_normal([0.0, 0.0], [[1.0, r], [r, 1.0]], size=n)
parent = mu + sd * z[:, 0]
child = mu + sd * z[:, 1]
ax.plot(parent, child, "o", ms=2.5, color="C0", alpha=0.35)
bins = np.arange(63.5, 73.6, 1.0)
centers, medians = [], []
for lo, hi in zip(bins[:-1], bins[1:]):
    sel = (parent >= lo) & (parent < hi)
    if sel.sum() >= 10:
        centers.append((lo + hi) / 2)
        medians.append(np.median(child[sel]))
ax.plot(centers, medians, "s", color="C3", ms=6, label="median child height per parent group")
line = np.linspace(63, 73, 2)
ax.plot(line, mu + r * (line - mu), color="C3", lw=1.5)
ax.plot(line, line, color="black", lw=1, ls="--", label="child = parent")
ax.set_xlabel("mid-parent height (inches)")
ax.set_ylabel("child height (inches)")
ax.set_title("Regression toward the mean (simulated heights)", fontsize=10)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
