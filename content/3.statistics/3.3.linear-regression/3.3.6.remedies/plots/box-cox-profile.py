"""Box-Cox procedure on simulated data whose spread shrinks with the predictor."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(4)
age = np.repeat(np.arange(5.0), 5)
y = (0.22 + 0.06 * age + 0.02 * rng.normal(size=age.size)) ** -2
n = y.size
k2 = np.exp(np.mean(np.log(y)))


def sse(lam):
    if abs(lam) < 1e-12:
        h = k2 * np.log(y)
    else:
        h = (y**lam - 1) / (lam * k2 ** (lam - 1))
    b1, b0 = np.polyfit(age, h, 1)
    r = h - (b0 + b1 * age)
    return r @ r


lams = np.linspace(-1.5, 1.0, 251)
loglik = np.array([-n / 2 * np.log(sse(l) / n) for l in lams])
best = lams[np.argmax(loglik)]
cut = loglik.max() - stats.chi2.ppf(0.95, 1) / 2
inside = lams[loglik >= cut]

fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.8))
axes[0].plot(age, y, "o", color="C0", ms=4)
axes[0].set_title("original scale: spread shrinks with X", fontsize=10)
axes[0].set_ylabel("Y")
axes[1].plot(age, y**-0.5, "o", color="C2", ms=4)
axes[1].set_title("after Y' = Y^(-1/2)", fontsize=10)
axes[1].set_ylabel("Y^(-1/2)")
for ax in axes[:2]:
    ax.set_xlabel("X")
    ax.grid(alpha=0.3)
ax = axes[2]
ax.plot(lams, loglik, color="C0", lw=1.6)
ax.axhline(cut, color="0.5", ls=":", lw=1)
ax.axvline(best, color="C3", ls="--", lw=1)
ax.axvspan(inside.min(), inside.max(), color="C1", alpha=0.15)
ax.set_title(f"profile log-likelihood: lambda_hat = {best:.2f},\n95% CI [{inside.min():.2f}, {inside.max():.2f}]", fontsize=10)
ax.set_xlabel("lambda")
ax.set_ylabel("log-likelihood (up to a constant)")
ax.grid(alpha=0.3)
fig.tight_layout()
