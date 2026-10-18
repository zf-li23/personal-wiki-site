"""Hidden extrapolation: a point inside the marginal ranges of X1 and X2 but outside their joint region."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n = 60
cov = np.array([[1.0, 0.85], [0.85, 1.0]])
z = rng.multivariate_normal([0.0, 0.0], cov, size=n)
x1 = 50 + 10 * z[:, 0]
x2 = 20 + 4 * z[:, 1]

fig, ax = plt.subplots(figsize=(7, 5.5))
ax.plot(x1, x2, "o", color="C0", alpha=0.75, label="observed cases")

# 95% ellipse of the fitted normal distribution as the joint region of the data
mean = np.array([x1.mean(), x2.mean()])
S = np.cov(np.vstack([x1, x2]))
vals, vecs = np.linalg.eigh(S)
t = np.linspace(0, 2 * np.pi, 300)
circle = np.vstack([np.cos(t), np.sin(t)]) * np.sqrt(5.99 * vals)[:, None]
ell = vecs @ circle + mean[:, None]
ax.plot(ell[0], ell[1], color="C2", lw=1.8, label="region covered jointly")

lo1, hi1 = x1.min(), x1.max()
lo2, hi2 = x2.min(), x2.max()
ax.plot([lo1, hi1, hi1, lo1, lo1], [lo2, lo2, hi2, hi2, lo2], color="C1", ls="--", lw=1.2,
        label="ranges of X1 and X2")

new = np.array([lo1 + 0.2 * (hi1 - lo1), lo2 + 0.85 * (hi2 - lo2)])
ax.plot(*new, marker="*", ms=16, color="C3", ls="none", label="new x_h")
ax.annotate("inside both ranges,\noutside the data", xy=new, xytext=(new[0] + 8, new[1] - 1.0),
            arrowprops=dict(arrowstyle="->", color="C3"), color="C3")
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_title("Hidden extrapolation with correlated explanatory variables")
ax.legend(loc="lower right", fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
