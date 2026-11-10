"""Love plot: absolute normalized differences before and after matching (simulated data)."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n_t, n_c = 300, 1500
names = ["age", "education", "earnings", "married", "children", "region"]


def draw(n, shift):
    z = rng.normal(0, 1, (n, 3))
    age = 35 + 8 * (z[:, 0] + shift)
    educ = 12 + 2 * (0.5 * z[:, 0] + z[:, 1] + 0.6 * shift)
    earn = 20 + 6 * (z[:, 2] - 0.8 * shift)
    married = (rng.random(n) < 0.5 + 0.15 * shift).astype(float)
    kids = rng.poisson(1.2 + 0.4 * shift, n).astype(float)
    region = (rng.random(n) < 0.4).astype(float)
    return np.column_stack([age, educ, earn, married, kids, region])


x_t, x_c = draw(n_t, 0.6), draw(n_c, 0.0)
x = np.vstack([x_t, x_c])
w = np.r_[np.ones(n_t), np.zeros(n_c)]


def norm_diff(a, b):
    return np.abs(a.mean(0) - b.mean(0)) / np.sqrt((a.var(0, ddof=1) + b.var(0, ddof=1)) / 2)


def logistic_newton(h, y, steps=25):
    phi = np.zeros(h.shape[1])
    phi[0] = np.log(y.mean() / (1 - y.mean()))
    for _ in range(steps):
        e = 1 / (1 + np.exp(-h @ phi))
        phi -= np.linalg.solve(-(h * (e * (1 - e))[:, None]).T @ h, h.T @ (y - e))
    return phi


h = np.column_stack([np.ones(len(w)), (x - x.mean(0)) / x.std(0)])
lin = h @ logistic_newton(h, w)          # linearized propensity score
s_inv = np.linalg.inv(np.cov(x_c, rowvar=False))


def match(dist):
    """Greedy one-to-one nearest-neighbor matching without replacement, treated in order."""
    free = np.ones(n_c, bool)
    chosen = []
    for i in range(n_t):
        d = np.where(free, dist(i), np.inf)
        j = int(np.argmin(d))
        free[j] = False
        chosen.append(j)
    return x_c[chosen]


def d_mahal(i):
    diff = x_c - x_t[i]
    return np.einsum("ij,jk,ik->i", diff, s_inv, diff)


def d_ps(i):
    return np.abs(lin[n_t:] - lin[i])


rows = [("before matching", norm_diff(x_t, x_c), "o", "C3"),
        ("Mahalanobis matching", norm_diff(x_t, match(d_mahal)), "s", "C0"),
        ("propensity score matching", norm_diff(x_t, match(d_ps)), "^", "C2")]

fig, ax = plt.subplots(figsize=(7, 3.8))
ypos = np.arange(len(names))[::-1]
for label, values, marker, colour in rows:
    ax.plot(values, ypos, marker, color=colour, label=label, ms=7, ls="none")
ax.axvline(0.1, color="grey", ls="--", lw=1)
ax.set_yticks(ypos)
ax.set_yticklabels(names)
ax.set_xlabel("absolute normalized difference")
ax.set_xlim(left=0)
ax.legend(fontsize=8, loc="lower right")
fig.tight_layout()
