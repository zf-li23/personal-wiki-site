"""Two-part normal mixture: EM for the mixing proportion and Louis's acceleration."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

rng = np.random.default_rng(5288)
mu1, s1, mu2, s2, a0, n = 1, 2, 4, 1, 0.4, 100
z = rng.random(n) < a0
x = np.where(z, rng.normal(mu1, s1, n), rng.normal(mu2, s2, n))
f1, f2 = norm.pdf(x, mu1, s1), norm.pdf(x, mu2, s2)


def loglik(a):
    return np.sum(np.log(a * f1 + (1 - a) * f2))


def responsibilities(a):
    return a * f1 / (a * f1 + (1 - a) * f2)


def em_step(a):
    return responsibilities(a).mean()


def info_obs(a):
    # observed information -l''(a)
    return np.sum(((f1 - f2) / (a * f1 + (1 - a) * f2)) ** 2)


def info_com(a):
    # expected complete-data information given x, at the current a
    lam = responsibilities(a)
    return np.sum(lam / a ** 2 + (1 - lam) / (1 - a) ** 2)


def louis_step(a):
    return a + info_com(a) / info_obs(a) * (em_step(a) - a)


mle = 0.5
for _ in range(100):  # Newton's method on the score, for a reference value of the MLE
    lam = responsibilities(mle)
    score = np.sum(lam / mle - (1 - lam) / (1 - mle))
    mle = mle + score / info_obs(mle)
iters = 8
em, acc = [0.1], [0.1]
for _ in range(iters):
    em.append(em_step(em[-1]))
    acc.append(louis_step(acc[-1]))
em, acc = np.array(em), np.array(acc)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axes[0]
ax.hist(x, bins=14, density=True, color="C0", alpha=0.35, edgecolor="C0", label="data, n = 100")
grid = np.linspace(x.min() - 1, x.max() + 1, 400)
ax.plot(grid, mle * norm.pdf(grid, mu1, s1) + (1 - mle) * norm.pdf(grid, mu2, s2), color="C3", lw=2,
        label=f"fitted mixture, alpha_hat = {mle:.4f}")
ax.plot(grid, mle * norm.pdf(grid, mu1, s1), "--", color="C1", lw=1, label="alpha_hat N(1, 2^2)")
ax.plot(grid, (1 - mle) * norm.pdf(grid, mu2, s2), ":", color="C2", lw=1.5, label="(1 - alpha_hat) N(4, 1)")
ax.plot(x, np.zeros_like(x), "|", color="gray", ms=8)
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
e_em = np.abs(em - mle)
e_acc = np.abs(acc - mle)
e_acc = np.where(e_acc < 1e-15, np.nan, e_acc)
ax.semilogy(np.arange(iters + 1), e_em, "o-", color="C0", ms=4, label="standard EM")
ax.semilogy(np.arange(iters + 1), e_acc, "s-", color="C3", ms=4, label="Louis acceleration")
ax.set_xlabel("iteration")
ax.set_ylabel("|alpha_t - MLE|")
ax.set_title("start alpha_0 = 0.1", fontsize=10)
ax.legend(fontsize=9)
ax.grid(alpha=0.3, which="both")
fig.tight_layout()
