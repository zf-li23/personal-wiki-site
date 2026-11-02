"""Eight schools: information criteria for three models, and the Bayes factor as a function of the prior scale."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import logsumexp

rng = np.random.default_rng(0)
y = np.array([28, 8, -3, 7, -1, 1, 18, 12.0])
s = np.array([15, 10, 16, 11, 9, 11, 10, 18.0])
S = 20000


def hierarchical_draws(y, s, size):
    """Draws of (mu, tau, theta) under p(mu, tau) ∝ 1, using p(tau | y) on a grid."""
    tau = np.linspace(0.01, 60, 3000)
    V = s[None] ** 2 + tau[:, None] ** 2
    v_mu = 1 / np.sum(1 / V, 1)
    m_mu = v_mu * np.sum(y / V, 1)
    logp = 0.5 * np.log(v_mu) - 0.5 * np.sum(np.log(V), 1) - 0.5 * np.sum((y - m_mu[:, None]) ** 2 / V, 1)
    p = np.exp(logp - logp.max())
    t = rng.choice(tau, size=size, p=p / p.sum())
    V = s[None] ** 2 + t[:, None] ** 2
    v_mu = 1 / np.sum(1 / V, 1)
    mu = v_mu * np.sum(y / V, 1) + np.sqrt(v_mu) * rng.standard_normal(size)
    prec = 1 / s**2 + 1 / t[:, None] ** 2
    theta = (y / s**2 + mu[:, None] / t[:, None] ** 2) / prec + rng.standard_normal((size, len(y))) / np.sqrt(prec)
    return mu, t, theta


def criteria(theta, k=None, mle=None):
    L = stats.norm.logpdf(y, theta, s)
    lppd = np.sum(logsumexp(L, axis=0) - np.log(len(L)))
    lp_bayes = stats.norm.logpdf(y, theta.mean(0), s).sum()
    p_dic = 2 * (lp_bayes - L.sum(1).mean())
    p_waic = np.sum(L.var(0))
    out = {"DIC": -2 * lp_bayes + 2 * p_dic, "WAIC": -2 * (lppd - p_waic)}
    if mle is not None:
        out["AIC"] = -2 * stats.norm.logpdf(y, mle, s).sum() + 2 * k
    return out


w = 1 / s**2
pooled_mean, pooled_var = np.sum(w * y) / w.sum(), 1 / w.sum()
res = {
    "no pooling": criteria(y + s * rng.standard_normal((S, 8)), 8, y),
    "complete pooling": criteria(np.repeat(pooled_mean + np.sqrt(pooled_var) * rng.standard_normal((S, 1)), 8, 1), 1,
                                 np.full(8, pooled_mean)),
    "hierarchical": criteria(hierarchical_draws(y, s, S)[2]),
}
# exact leave-one-out predictive densities
loo_pool, loo_hier = 0.0, 0.0
for i in range(8):
    keep = np.arange(8) != i
    wi = 1 / s[keep] ** 2
    m, v = np.sum(wi * y[keep]) / wi.sum(), 1 / wi.sum()
    loo_pool += stats.norm.logpdf(y[i], m, np.sqrt(v + s[i] ** 2))
    mu, t, _ = hierarchical_draws(y[keep], s[keep], S)
    loo_hier += logsumexp(stats.norm.logpdf(y[i], mu, np.sqrt(t**2 + s[i] ** 2))) - np.log(S)
res["complete pooling"]["LOO-CV"] = -2 * loo_pool
res["hierarchical"]["LOO-CV"] = -2 * loo_hier

fig, axes = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axes[0]
names = ["AIC", "DIC", "WAIC", "LOO-CV"]
for j, (model, marker) in enumerate(zip(res, ["o", "s", "D"])):
    xs = [i + (j - 1) * 0.18 for i, c in enumerate(names) if c in res[model]]
    vals = [res[model][c] for c in names if c in res[model]]
    ax.scatter(xs, vals, marker=marker, s=45, color=f"C{j}", label=model, zorder=3)
ax.set_xticks(range(len(names)), names)
ax.set_ylabel("deviance scale (lower is better)")
ax.set_title("estimated -2 elppd", fontsize=11)
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Bayes factor p(y | complete pooling) / p(y | separate), both with N(0, A^2) priors
A = np.logspace(0, 3, 200)
log_bf = []
for a in A:
    log_sep = stats.norm.logpdf(y, 0, np.sqrt(s**2 + a**2)).sum()
    log_pool = stats.multivariate_normal(np.zeros(8), np.diag(s**2) + a**2).logpdf(y)
    log_bf.append(log_pool - log_sep)
ax = axes[1]
ax.plot(A, np.array(log_bf) / np.log(10), color="C3", lw=1.8)
ax.axhline(0, color="0.5", lw=1, ls="--")
ax.set_xscale("log")
ax.set_xlabel("prior scale A")
ax.set_ylabel(r"$\log_{10}$ BF (pooling vs separate)")
ax.set_title("Bayes factor under proper N(0, A^2) priors", fontsize=11)
ax.grid(alpha=0.3)
fig.tight_layout()
