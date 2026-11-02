"""Fish length example: prior, posterior and posterior predictive for a normal mean with known variance."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

sigma, n, ybar, mu0, tau0 = 2.0, 12, 32.0, 30.0, 4.0
prec = 1 / tau0**2 + n / sigma**2
mun, taun = (mu0 / tau0**2 + n * ybar / sigma**2) / prec, prec**-0.5

x = np.linspace(16, 44, 1201)
fig, ax = plt.subplots(figsize=(8, 3.9))
ax.plot(x, stats.norm(mu0, tau0).pdf(x), color="0.5", ls="--", lw=1.5, label=r"prior of $\theta$: N(30, $4^2$)")
ax.plot(x, stats.norm(mun, taun).pdf(x), color="C3", lw=1.8, label=rf"posterior of $\theta$: N({mun:.2f}, {taun:.3f}$^2$)")
sd_pred = np.hypot(sigma, taun)
ax.plot(x, stats.norm(mun, sd_pred).pdf(x), color="C0", lw=1.8, label=rf"posterior predictive of $\tilde y$: N({mun:.2f}, {sd_pred:.2f}$^2$)")
ax.plot(x, stats.norm(mu0, np.hypot(sigma, tau0)).pdf(x), color="C2", ls=":", lw=1.5, label=r"prior predictive of $y$: N(30, 20)")
ax.set_xlabel("fish length (cm)")
ax.set_ylabel("density")
ax.legend(fontsize=9)
ax.grid(alpha=0.3)
fig.tight_layout()
