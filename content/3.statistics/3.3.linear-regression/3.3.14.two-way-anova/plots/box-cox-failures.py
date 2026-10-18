"""Box-Cox transformation for the time between computer failures at three locations."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

y = np.array([4.41, 100.65, 14.45, 47.13, 85.21,
              8.24, 81.16, 7.35, 12.29, 1.61,
              106.19, 33.83, 78.88, 342.81, 44.33])
g = np.repeat([1, 2, 3], 5)
n = len(y)


def boxcox(v, lam):
    return np.log(v) if abs(lam) < 1e-12 else (v**lam - 1) / lam


def profile_loglik(lam):
    z = boxcox(y, lam)
    sse = sum(((z[g == k] - z[g == k].mean()) ** 2).sum() for k in (1, 2, 3))
    return -n / 2 * np.log(sse / n) + (lam - 1) * np.log(y).sum()


lams = np.linspace(-2, 2, 801)
ll = np.array([profile_loglik(l) for l in lams])
best = lams[np.argmax(ll)]
cut = ll.max() - stats.chi2.ppf(0.95, 1) / 2
inside = lams[ll >= cut]

rng = np.random.default_rng(0)
jitter = rng.uniform(-0.08, 0.08, n)
fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))
ax = axes[0]
ax.scatter(g + jitter, y, s=20, color="C0", zorder=3)
ax.set_title("Raw times")
ax.set_ylabel("time between failures")

ax = axes[1]
ax.plot(lams, ll, color="C0", lw=1.8)
ax.axhline(cut, color="gray", ls="--", lw=1)
ax.axvline(inside.min(), color="gray", ls=":", lw=1)
ax.axvline(inside.max(), color="gray", ls=":", lw=1)
ax.plot(best, ll.max(), "o", color="C3")
ax.annotate(f"lambda_hat = {best:.2f}", (best, ll.max()), xytext=(best + 0.5, ll.max() - 15),
            arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("lambda")
ax.set_ylabel("profile log-likelihood")
ax.set_title("Box-Cox profile, 95% interval dotted")
ax.grid(alpha=0.3)

ax = axes[2]
ax.scatter(g + jitter, np.log(y), s=20, color="C2", zorder=3)
ax.set_title("log(time), lambda = 0")
ax.set_ylabel("log time between failures")
for ax in (axes[0], axes[2]):
    ax.set_xticks([1, 2, 3])
    ax.set_xlabel("location")
    ax.grid(alpha=0.3)
fig.tight_layout()
