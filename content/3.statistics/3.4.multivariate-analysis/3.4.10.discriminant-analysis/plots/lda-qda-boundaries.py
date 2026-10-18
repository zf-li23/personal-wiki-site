"""LDA versus QDA decision boundaries for two simulated normal populations with unequal covariance matrices."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis

rng = np.random.default_rng(0)
mu1, mu2 = np.array([0.0, 0.0]), np.array([2.0, 1.5])
S1 = np.array([[1.0, 0.6], [0.6, 1.0]])
S2 = np.array([[0.3, -0.1], [-0.1, 2.0]])
n = 150
X = np.vstack([rng.multivariate_normal(mu1, S1, n), rng.multivariate_normal(mu2, S2, n)])
y = np.repeat([0, 1], n)

xx, yy = np.meshgrid(np.linspace(-3.5, 5, 400), np.linspace(-3.5, 5.5, 400))
grid = np.c_[xx.ravel(), yy.ravel()]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True)
for ax, model, name in zip(axes, [LinearDiscriminantAnalysis(), QuadraticDiscriminantAnalysis()], ["LDA", "QDA"]):
    model.fit(X, y)
    z = model.predict_proba(grid)[:, 1].reshape(xx.shape)
    ax.contourf(xx, yy, z, levels=[0, 0.5, 1], colors=["C0", "C1"], alpha=0.15)
    ax.contour(xx, yy, z, levels=[0.5], colors="k", linewidths=1.5)
    ax.scatter(*X[y == 0].T, s=12, color="C0", label="population 1")
    ax.scatter(*X[y == 1].T, s=12, color="C1", marker="^", label="population 2")
    err = np.mean(model.predict(X) != y)
    ax.set_title(f"{name} (apparent error rate {err:.3f})")
    ax.set_xlabel("x1")
    ax.set_xlim(-3.5, 5)
    ax.set_ylim(-3.5, 5.5)
axes[0].set_ylabel("x2")
axes[0].legend(loc="upper left", fontsize=8)
fig.tight_layout()
