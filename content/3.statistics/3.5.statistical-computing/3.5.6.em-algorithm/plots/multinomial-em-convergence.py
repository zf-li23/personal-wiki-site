"""EM for the genetic linkage multinomial (125, 18, 20, 34): monotone likelihood and linear convergence."""

import numpy as np
import matplotlib.pyplot as plt

x1, x2, x3, x4 = 125, 18, 20, 34


def loglik(t):
    # observed-data log-likelihood up to a constant
    return x1 * np.log(2 + t) + (x2 + x3) * np.log(1 - t) + x4 * np.log(t)


def em_step(t):
    x12 = x1 * t / (2 + t)  # E-step: expected count in the hidden sub-cell
    return (x12 + x4) / (x12 + x2 + x3 + x4)  # M-step


path = [0.05]
for _ in range(40):
    path.append(em_step(path[-1]))
path = np.array(path)
mle = path[-1]

# fraction of missing information: I_mis / I_com at the MLE
x12 = x1 * mle / (2 + mle)
i_com = (x12 + x4) / mle ** 2 + (x2 + x3) / (1 - mle) ** 2
i_obs = x1 / (2 + mle) ** 2 + (x2 + x3) / (1 - mle) ** 2 + x4 / mle ** 2
rate = (i_com - i_obs) / i_com

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
grid = np.linspace(0.02, 0.98, 400)
ax.plot(grid, loglik(grid), color="C0", lw=1.5, label="observed log-likelihood l(theta)")
k = 5
ax.plot(path[:k + 1], loglik(path[:k + 1]), "o--", color="C3", ms=5, lw=1, label="EM iterates from theta_0 = 0.05")
for t in range(3):
    ax.annotate(f"{t}", (path[t], loglik(path[t])), textcoords="offset points", xytext=(-10, 4), fontsize=8)
ax.axvline(mle, color="gray", ls="--", lw=0.8)
ax.set_ylim(loglik(0.02) - 5, loglik(mle) + 10)
ax.set_xlabel("theta")
ax.set_ylabel("log-likelihood (up to a constant)")
ax.set_title(f"l(theta_t) increases at every step; MLE = {mle:.7f}", fontsize=9)
ax.legend(fontsize=8, loc="lower right")
ax.grid(alpha=0.3)

ax = axes[1]
k = 14
err = np.abs(path[:k + 1] - mle)
ax.semilogy(np.arange(k + 1), err, "o-", color="C3", ms=4, label="|theta_t - MLE|")
ax.semilogy(np.arange(k + 1), err[0] * rate ** np.arange(k + 1) * err[3] / (err[0] * rate ** 3),
            "--", color="gray", label=f"slope = I_mis / I_com = {rate:.4f}")
ax.set_xlabel("iteration t")
ax.set_ylabel("error (log scale)")
ax.set_title("linear convergence with the fraction of missing information", fontsize=9)
ax.legend(fontsize=9)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
