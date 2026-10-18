"""Power curves of the two-sided t-test of zero slope for two designs."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def power(beta1, n, sig2, ssx, alpha=0.05):
    df = n - 2
    delta = beta1 / np.sqrt(sig2 / ssx)
    c = stats.t.ppf(1 - alpha / 2, df)
    return stats.nct.sf(c, df, delta) + stats.nct.cdf(-c, df, delta)


beta1 = np.linspace(-2, 2, 401)
fig, ax = plt.subplots(figsize=(7.5, 4.5))
for k, (n, ssx) in enumerate([(25, 19800), (45, 35800)]):
    ax.plot(beta1, power(beta1, n, 2500, ssx), color=f"C{k}", lw=2, label=f"n = {n}, S_XX = {ssx}")
    p1 = power(1.0, n, 2500, ssx)
    ax.plot([1.0], [p1], "o", color=f"C{k}")
    ax.annotate(f"{p1:.2f}", xy=(1.0, p1), xytext=(1.12, p1 - 0.08), fontsize=9, color=f"C{k}")
ax.axhline(0.05, color="gray", ls=":", lw=1)
ax.axhline(0.95, color="gray", ls="--", lw=1)
ax.set_xlabel("beta_1")
ax.set_ylabel("power")
ax.set_title("Power for the slope in simple linear regression (sigma^2 = 2500, alpha = 0.05)", fontsize=10)
ax.legend(fontsize=9, loc="lower left")
ax.grid(alpha=0.3)
fig.tight_layout()
