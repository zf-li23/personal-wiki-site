"""Power of Fisher's exact test for three statistics under three outcome models."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rankdata

rng = np.random.default_rng(0)
n, n_t = 100, 50
alpha, k_draws, reps = 0.10, 300, 300

# Reference assignments shared by all simulated data sets (random draws from the CRE)
idx = np.array([rng.permutation(n) for _ in range(k_draws)])
treat_idx, ctrl_idx = idx[:, :n_t], idx[:, n_t:]
W = np.zeros((k_draws, n))
np.put_along_axis(W, treat_idx, 1.0, axis=1)


def p_values(y_obs, w_obs):
    """Simulated two-sided p-values for difference in means, medians and ranks."""
    r = rankdata(y_obs) - (n + 1) / 2
    out = []
    for v in (y_obs, None, r):
        if v is None:
            t_obs = abs(np.median(y_obs[w_obs]) - np.median(y_obs[~w_obs]))
            t_ref = np.abs(np.median(y_obs[treat_idx], axis=1) - np.median(y_obs[ctrl_idx], axis=1))
        else:
            t_obs = abs(v[w_obs].mean() - v[~w_obs].mean())
            t_ref = np.abs(W @ v / n_t - (1 - W) @ v / (n - n_t))
        out.append((1 + np.sum(t_ref >= t_obs - 1e-12)) / (k_draws + 1))
    return out


def draw_y0(model):
    if model == "outliers":
        y0 = rng.normal(0, 1, n)
        bad = rng.random(n) < 0.1
        y0[bad] = rng.normal(0, 5, bad.sum())
        return y0
    if model == "multiplicative":
        return np.exp(rng.normal(0, 1, n))
    return rng.normal(0, 1, n)


models = {
    "Additive, normal outcomes": ("normal", np.linspace(0, 0.8, 9)),
    "Additive, with outliers": ("outliers", np.linspace(0, 0.8, 9)),
    "Multiplicative, log-normal": ("multiplicative", np.linspace(0, 0.8, 9)),
}
names = ["difference in means", "difference in medians", "rank statistic"]
styles = ["-", "--", ":"]
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True)
for ax, (title, (model, taus)) in zip(axes, models.items()):
    power = np.zeros((len(taus), 3))
    for a, tau in enumerate(taus):
        rejections = np.zeros(3)
        for _ in range(reps):
            y0 = draw_y0(model)
            y1 = y0 * np.exp(tau) if model == "multiplicative" else y0 + tau
            w_obs = np.zeros(n, dtype=bool)
            w_obs[rng.choice(n, n_t, replace=False)] = True
            y_obs = np.where(w_obs, y1, y0)
            rejections += np.array(p_values(y_obs, w_obs)) <= alpha
        power[a] = rejections / reps
    for j in range(3):
        ax.plot(taus, power[:, j], ls=styles[j], lw=2, label=names[j])
    ax.axhline(alpha, color="gray", lw=0.8)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("effect size tau")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("power at level 0.1")
axes[0].legend(fontsize=8, loc="upper left")
fig.tight_layout()
