"""Rat tumor example, beta-binomial hierarchical model with p(alpha, beta) proportional to (alpha + beta)^(-5/2).
Three samplers, four chains each from dispersed starting values, 4000 iterations, the first 1000 discarded:
(1) Metropolis-within-Gibbs (Gibbs for theta, random-walk steps N(., 1) for alpha and beta);
(2) collapsed sampler with the same componentwise steps on p(alpha, beta | y);
(3) collapsed sampler with an adapted joint random walk on (log(alpha/beta), log(alpha + beta)).
Split-R-hat and effective sample size of alpha are shown in the titles."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

table = """0/20 0/20 0/20 0/20 0/20 0/20 0/20 0/19 0/19 0/19
0/19 0/18 0/18 0/17 1/20 1/20 1/20 1/20 1/19 1/19
1/18 1/18 2/25 2/24 2/23 2/20 2/20 2/20 2/20 2/20
2/20 1/10 5/49 2/19 5/46 3/27 2/17 7/49 7/47 3/20
3/20 2/13 9/48 10/50 4/20 4/20 4/20 4/20 4/20 4/20
4/20 10/48 4/19 4/19 4/19 5/22 11/46 12/49 5/20 5/20
6/23 5/19 6/22 6/20 6/20 6/20 16/52 15/47 15/46 9/24 4/14"""
pairs = [tuple(int(v) for v in s.split("/")) for s in table.split()]
y = np.array([a for a, _ in pairs])
n = np.array([b for _, b in pairs])
J = y.size
rng = np.random.default_rng(0)
T, warm = 4000, 1000
starts = [(1.0, 1.0), (5.0, 30.0), (0.5, 10.0), (4.0, 8.0)]


def log_cond_alpha(a, b, slog):
    return (a - 1) * slog - J * special.betaln(a, b) - 2.5 * np.log(a + b)


def mwg(a, b):
    out = np.empty((T, 2))
    for t in range(T):
        theta = rng.beta(a + y, b + n - y)
        s1, s2 = np.log(theta).sum(), np.log1p(-theta).sum()
        cand = a + rng.normal()
        if cand > 0 and np.log(rng.uniform()) < log_cond_alpha(cand, b, s1) - log_cond_alpha(a, b, s1):
            a = cand
        cand = b + rng.normal()
        # the full conditional of beta has the same form with log(1 - theta_j) in place of log(theta_j)
        if cand > 0 and np.log(rng.uniform()) < log_cond_alpha(cand, a, s2) - log_cond_alpha(b, a, s2):
            b = cand
        out[t] = a, b
    return out


def log_marg(a, b):
    return np.sum(special.betaln(a + y, b + n - y) - special.betaln(a, b)) - 2.5 * np.log(a + b)


def collapsed(a, b):
    out = np.empty((T, 2))
    lp = log_marg(a, b)
    for t in range(T):
        cand = a + rng.normal()
        if cand > 0:
            lc = log_marg(cand, b)
            if np.log(rng.uniform()) < lc - lp:
                a, lp = cand, lc
        cand = b + rng.normal()
        if cand > 0:
            lc = log_marg(a, cand)
            if np.log(rng.uniform()) < lc - lp:
                b, lp = cand, lc
        out[t] = a, b
    return out


def log_marg_uv(z):
    # density of (u, v) = (log(alpha/beta), log(alpha + beta)) includes the Jacobian alpha * beta
    s = np.exp(z[1])
    a = s / (1 + np.exp(-z[0]))
    b = s - a
    return log_marg(a, b) + np.log(a) + np.log(b)


def rw_uv(z, S, iters):
    L = np.linalg.cholesky(S)
    out = np.empty((iters, 2))
    lp = log_marg_uv(z)
    for t in range(iters):
        cand = z + L @ rng.normal(size=2)
        lc = log_marg_uv(cand)
        if np.log(rng.uniform()) < lc - lp:
            z, lp = cand, lc
        out[t] = z
    return out


# adaptation (B = 10 rounds of M = 100 iterations), then fixed proposal 2.4^2 S / d
S, z, hist = 0.1 * np.eye(2), np.array([np.log(1 / 5), np.log(6.0)]), []
for b in range(10):
    draws = rw_uv(z, 2.4 ** 2 * S / 2, 100)
    hist.append(draws)
    z = draws[-1]
    S = np.cov(np.vstack(hist).T)


def joint(a, b):
    zz = rw_uv(np.array([np.log(a / b), np.log(a + b)]), 2.4 ** 2 * S / 2, T)
    s = np.exp(zz[:, 1])
    al = s / (1 + np.exp(-zz[:, 0]))
    return np.column_stack([al, s - al])


def rhat_ess(chains):
    # split-R-hat and effective sample size (Gelman et al., 2013), chains: m x n array
    h = chains.shape[1] // 2
    c = np.vstack([chains[:, :h], chains[:, h:2 * h]])
    m, k = c.shape
    B = k * c.mean(axis=1).var(ddof=1)
    W = c.var(axis=1, ddof=1).mean()
    var_plus = (k - 1) / k * W + B / k
    rho = np.array([1 - np.mean((c[:, t:] - c[:, :-t]) ** 2) / (2 * var_plus) for t in range(1, k)])
    s = 0.0
    for t in range(0, k - 2, 2):
        if rho[t] + rho[t + 1] < 0:
            break
        s += rho[t] + rho[t + 1]
    return np.sqrt(var_plus / W), m * k / (1 + 2 * s)


samplers = (("Metropolis-within-Gibbs", mwg), ("Collapsed, componentwise", collapsed),
            ("Collapsed, joint on (log(α/β), log(α+β))", joint))
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True, sharey=True)
summary = {}
for ax, (name, f) in zip(axes, samplers):
    chains = np.array([f(*st) for st in starts])
    alpha = chains[:, warm:, 0]
    r, ess = rhat_ess(alpha)
    summary[name] = (r, ess, rhat_ess(chains[:, warm:, 1]))
    for k in range(len(starts)):
        ax.plot(np.arange(T), chains[k, :, 0], lw=0.5)
    ax.axvline(warm, color="gray", ls=":")
    ax.set_ylabel("α")
    ax.set_title(f"{name}: R-hat {r:.3f}, effective sample size {ess:.0f} of {alpha.size}", fontsize=10)
axes[0].set_ylim(0, 8)
axes[-1].set_xlabel("iteration")
fig.tight_layout()
