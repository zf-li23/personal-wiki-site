"""Bootstrap distribution of the sample correlation for the law school data (15 schools),
with the normal, basic, percentile and BCa 95% intervals."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lsat = np.array([576, 635, 558, 578, 666, 580, 555, 661, 651, 605, 653, 575, 545, 572, 594], dtype=float)
gpa = np.array([339, 330, 281, 303, 344, 307, 300, 343, 336, 313, 312, 274, 276, 288, 296]) / 100
n = len(lsat)


def corr(i):
    return np.corrcoef(lsat[i], gpa[i])[0, 1]


rng = np.random.default_rng(0)
B = 2000
theta_hat = corr(np.arange(n))
reps = np.array([corr(rng.integers(0, n, n)) for _ in range(B)])

alpha = 0.05
z = stats.norm.ppf(1 - alpha / 2)
se = reps.std(ddof=1)
lo, hi = np.quantile(reps, [alpha / 2, 1 - alpha / 2])
normal = (theta_hat - z * se, theta_hat + z * se)
basic = (2 * theta_hat - hi, 2 * theta_hat - lo)
percentile = (lo, hi)

# BCa: bias correction from the bootstrap replicates, acceleration from the jackknife
z0 = stats.norm.ppf(np.mean(reps < theta_hat))
jack = np.array([corr(np.delete(np.arange(n), i)) for i in range(n)])
d = jack.mean() - jack
a = np.sum(d ** 3) / (6 * np.sum(d ** 2) ** 1.5)
a1 = stats.norm.cdf(z0 + (z0 - z) / (1 - a * (z0 - z)))
a2 = stats.norm.cdf(z0 + (z0 + z) / (1 - a * (z0 + z)))
bca = tuple(np.quantile(reps, [a1, a2]))

fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.hist(reps, bins=50, density=True, color="C0", alpha=0.55, label=f"bootstrap replicates (B = {B})")
ax.axvline(theta_hat, color="C3", lw=2, label=f"sample correlation = {theta_hat:.3f}")
top = ax.get_ylim()[1]
intervals = [("normal", normal, "C1"), ("basic", basic, "C2"), ("percentile", percentile, "C4"), ("BCa", bca, "C5")]
for k, (name, (u, v), col) in enumerate(intervals):
    yk = top * (0.92 - 0.08 * k)
    ax.plot([u, v], [yk, yk], color=col, lw=3, solid_capstyle="butt")
    ax.text(v + 0.01, yk, f"{name}: ({u:.2f}, {v:.2f})", va="center", fontsize=8, color=col)
ax.set_xlim(0.0, 1.45)
ax.axvline(1.0, color="gray", lw=1, ls=":")
ax.set_xlabel("bootstrap correlation r*")
ax.set_ylabel("density")
ax.set_title(f"Law school data: bootstrap se = {se:.3f}, bias = {reps.mean() - theta_hat:+.3f}", fontsize=10)
ax.legend(fontsize=8, loc="center left")
ax.grid(alpha=0.3)
fig.tight_layout()
