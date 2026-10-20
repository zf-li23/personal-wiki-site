"""EM as maximization of a lower bound: the observed log-likelihood of a mixing proportion and the minorizing functions."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

rng = np.random.default_rng(5288)
n, a_true = 100, 0.4
z = rng.random(n) < a_true
x = np.where(z, rng.normal(1, 2, n), rng.normal(4, 1, n))
f1, f2 = norm.pdf(x, 1, 2), norm.pdf(x, 4, 1)


def loglik(a):
    return np.sum(np.log(a * f1 + (1 - a) * f2))


def lower_bound(a, a_t):
    # g_t(a) = sum_i E_q[log p(x_i, z_i | a) - log q(z_i)], q = posterior at a_t
    lam = a_t * f1 / (a_t * f1 + (1 - a_t) * f2)
    comp = lam * np.log(a * f1) + (1 - lam) * np.log((1 - a) * f2)
    ent = -(lam * np.log(lam) + (1 - lam) * np.log(1 - lam))
    return np.sum(comp + ent)


def em_step(a):
    lam = a * f1 / (a * f1 + (1 - a) * f2)
    return lam.mean()


grid = np.linspace(0.02, 0.95, 400)
fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(grid, [loglik(a) for a in grid], color="C0", lw=2, label="observed log-likelihood l(alpha)")
a_t = 0.05
for t, c in zip(range(3), ["C3", "C1", "C2"]):
    lb = np.array([lower_bound(a, a_t) for a in grid])
    a_next = em_step(a_t)
    ax.plot(grid, lb, "--", color=c, lw=1.2, label=f"lower bound g_{t}, touching at alpha_{t} = {a_t:.3f}")
    ax.plot(a_t, loglik(a_t), "o", color=c)
    ax.plot(a_next, lower_bound(a_next, a_t), "^", color=c)
    ax.annotate("", xy=(a_next, loglik(a_next)), xytext=(a_next, lower_bound(a_next, a_t)),
                arrowprops=dict(arrowstyle="->", color=c, lw=1))
    a_t = a_next
ax.set_ylim(loglik(0.02) - 5, loglik(grid[np.argmax([loglik(a) for a in grid])]) + 8)
ax.set_xlabel("mixing proportion alpha")
ax.set_ylabel("log-likelihood")
ax.set_title("each M-step maximizes a bound that touches l at the current value", fontsize=10)
ax.legend(fontsize=8, loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
