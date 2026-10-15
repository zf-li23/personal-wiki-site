import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
t = np.linspace(0, 4, 12)
y = 0.4 * t**2 - 0.6 * t + 1.0 + rng.normal(0, 0.35, t.size)

fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, degree, title in zip(axes, [1, 2], ["linear fit", "quadratic fit"]):
    # Columns f_j(t) = t^j; solve the least squares problem with a reduced QR factorization
    A = np.vander(t, degree + 1, increasing=True)
    Q1, R1 = np.linalg.qr(A)
    coef = np.linalg.solve(R1, Q1.T @ y)
    fitted = A @ coef
    grid = np.linspace(-0.2, 4.2, 200)
    ax.plot(grid, np.vander(grid, degree + 1, increasing=True) @ coef, linewidth=2, label="fitted curve")
    ax.vlines(t, fitted, y, colors="tab:red", linewidth=1, label="residuals")
    ax.plot(t, y, "o", color="tab:blue", markersize=5, label="data")
    rss = np.sum((y - fitted) ** 2)
    ax.set_title(f"{title}: residual sum of squares = {rss:.2f}")
    ax.set_xlabel("t")
    ax.grid(True, alpha=0.3)
axes[0].set_ylabel("y")
axes[0].legend(fontsize=9)
fig.tight_layout()
