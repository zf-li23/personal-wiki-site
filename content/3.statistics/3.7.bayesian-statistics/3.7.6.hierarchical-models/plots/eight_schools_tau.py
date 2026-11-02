"""Eight schools: marginal posterior of tau and conditional posterior means and sds of the school effects."""

import numpy as np
import matplotlib.pyplot as plt

y = np.array([28, 8, -3, 7, -1, 1, 18, 12], dtype=float)
sigma = np.array([15, 10, 16, 11, 9, 11, 10, 18], dtype=float)
names = list("ABCDEFGH")
tau = np.linspace(1e-3, 30, 1500)


def mu_hat_and_V(t):
    w = 1 / (sigma**2 + t**2)
    V = 1 / w.sum()
    return V * np.sum(w * y), V


# p(tau | y) under the uniform prior p(tau) ~ 1 (and p(mu | tau) ~ 1)
logp = []
cond_mean, cond_sd = [], []
for t in tau:
    m, V = mu_hat_and_V(t)
    logp.append(0.5 * np.log(V) - 0.5 * np.sum(np.log(sigma**2 + t**2)) - 0.5 * np.sum((y - m) ** 2 / (sigma**2 + t**2)))
    Vj = 1 / (1 / sigma**2 + 1 / t**2)
    cond_mean.append(Vj * (y / sigma**2 + m / t**2))
    # E and Var of theta_j given tau, averaging over mu | tau, y
    cond_sd.append(np.sqrt(Vj + (Vj / t**2) ** 2 * V))
logp = np.array(logp)
dens = np.exp(logp - logp.max())
dens /= np.trapezoid(dens, tau)
cond_mean = np.array(cond_mean)
cond_sd = np.array(cond_sd)

fig, axes = plt.subplots(1, 3, figsize=(13.5, 3.9))
ax = axes[0]
ax.plot(tau, dens, color="C0", lw=1.8)
ax.set_title(r"marginal posterior $p(\tau \mid y)$", fontsize=11)
ax.set_xlabel(r"$\tau$")
ax.set_ylim(bottom=0)
ax.grid(alpha=0.3)
for ax, vals, title in [(axes[1], cond_mean, r"$E(\theta_j \mid \tau, y)$"), (axes[2], cond_sd, r"$sd(\theta_j \mid \tau, y)$")]:
    for j in range(8):
        ax.plot(tau, vals[:, j], lw=1.3, color=f"C{j}", label=names[j])
    ax.set_title(title, fontsize=11)
    ax.set_xlabel(r"$\tau$")
    ax.set_xlim(0, 30)
    ax.grid(alpha=0.3)
axes[1].legend(fontsize=8, ncol=2, loc="upper left")
fig.tight_layout()
