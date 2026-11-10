"""The check loss rho_tau for several tau, and the expected check loss whose minimizer is the tau-quantile."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

r = np.linspace(-2, 2, 401)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for i, tau in enumerate([0.1, 0.5, 0.9]):
    rho = r * (tau - (r < 0))
    axes[0].plot(r, rho, color=f"C{i}", lw=2, label=f"tau = {tau}")
axes[0].plot(r, r ** 2 / 2, color="gray", ls="--", lw=1.5, label="squared loss / 2")
axes[0].set_xlabel("residual r = y - c")
axes[0].set_ylabel("loss")
axes[0].set_title("Check loss: slope tau for r > 0, slope tau - 1 for r < 0")
axes[0].set_ylim(-0.05, 1.9)
axes[0].legend(frameon=False)
axes[0].grid(alpha=0.3)

# expected check loss for Y ~ Gamma(shape 2): minimized at the tau-quantile
y = stats.gamma(2)
c = np.linspace(0, 8, 400)
s = np.linspace(0, 25, 6001)
dens = y.pdf(s)
for i, tau in enumerate([0.1, 0.5, 0.9]):
    risk = [np.trapezoid((s - cc) * (tau - (s < cc)) * dens, s) for cc in c]
    q = y.ppf(tau)
    axes[1].plot(c, risk, color=f"C{i}", lw=2, label=f"tau = {tau}, quantile {q:.2f}")
    axes[1].axvline(q, color=f"C{i}", ls=":", lw=1.2)
axes[1].set_xlabel("c")
axes[1].set_ylabel("E rho_tau(Y - c)")
axes[1].set_title("Y ~ Gamma(2, 1): minimizers are the quantiles")
axes[1].legend(frameon=False, fontsize=9)
axes[1].grid(alpha=0.3)
fig.tight_layout()
