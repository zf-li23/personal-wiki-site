"""Loss functions rho and their derivatives psi (proportional to the influence function)
for the mean (squared loss), the median (absolute loss) and the Huber M-estimator (k = 1.345)."""

import numpy as np
import matplotlib.pyplot as plt

k = 1.345
t = np.linspace(-4, 4, 801)
rho = {
    "squared, $t^2/2$ (mean)": t**2 / 2,
    "absolute, $|t|$ (median)": np.abs(t),
    "Huber, $k = 1.345$": np.where(np.abs(t) <= k, t**2 / 2, k * np.abs(t) - k**2 / 2),
}
psi = {
    "squared, $t^2/2$ (mean)": t,
    "absolute, $|t|$ (median)": np.sign(t),
    "Huber, $k = 1.345$": np.clip(t, -k, k),
}
colors = ["C2", "C0", "C3"]

fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.0))
for (label, values), color in zip(rho.items(), colors):
    axes[0].plot(t, values, color=color, lw=1.9, label=label)
for (label, values), color in zip(psi.items(), colors):
    axes[1].plot(t, values, color=color, lw=1.9, label=label)
for x0 in (-k, k):
    axes[0].axvline(x0, color="0.5", ls=":", lw=1)
    axes[1].axvline(x0, color="0.5", ls=":", lw=1)
axes[0].set_ylim(-0.2, 5)
axes[0].set_title(r"A. loss $\rho(t)$", fontsize=10)
axes[1].set_title(r"B. $\psi(t) = \rho'(t)$, the shape of the influence function", fontsize=10)
axes[1].set_ylim(-3, 3)
for ax in axes:
    ax.set_xlabel("standardized residual $t$")
    ax.grid(alpha=0.3)
axes[0].legend(fontsize=8, loc="upper center")
fig.tight_layout()
