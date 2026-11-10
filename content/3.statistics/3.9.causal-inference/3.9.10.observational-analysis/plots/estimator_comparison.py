"""Sampling distributions of estimators of an average effect in simulated observational studies."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n, reps, tau = 1000, 300, 2.0


def simulate():
    x = rng.normal(0, 1, (n, 2))
    lin = -0.8 + 1.2 * x[:, 0] + 0.6 * x[:, 1]
    w = rng.random(n) < 1 / (1 + np.exp(-lin))
    mu0 = 1.5 * x[:, 0] + 0.8 * x[:, 0] ** 2 + x[:, 1]          # nonlinear control mean
    y = mu0 + tau * w + rng.normal(0, 1, n)                     # constant effect: ATE = ATT = tau
    return x, w, y


def ols(design, y):
    return np.linalg.lstsq(design, y, rcond=None)[0]


def logistic_newton(h, y, steps=25):
    phi = np.zeros(h.shape[1])
    phi[0] = np.log(y.mean() / (1 - y.mean()))
    for _ in range(steps):
        e = 1 / (1 + np.exp(-h @ phi))
        phi -= np.linalg.solve(-(h * (e * (1 - e))[:, None]).T @ h, h.T @ (y - e))
    return phi


def estimates(x, w, y):
    one = np.ones(n)
    out = {"difference in means": y[w].mean() - y[~w].mean()}
    out["regression"] = ols(np.column_stack([one, w, x]), y)[1]
    h = np.column_stack([one, x])
    e = 1 / (1 + np.exp(-h @ logistic_newton(h, w.astype(float))))
    wt, wc = 1 / e[w], 1 / (1 - e[~w])
    out["weighting (IPW)"] = (wt @ y[w]) / wt.sum() - (wc @ y[~w]) / wc.sum()
    edges = np.quantile(e, np.linspace(0, 1, 6))
    block = np.clip(np.searchsorted(edges, e, side="right") - 1, 0, 4)
    plain, adjusted = 0.0, 0.0
    for j in range(5):
        b = block == j
        plain += b.mean() * (y[b & w].mean() - y[b & ~w].mean())
        adjusted += b.mean() * ols(np.column_stack([one[b], w[b], x[b]]), y[b])[1]
    out["5 blocks"] = plain
    out["5 blocks + regression"] = adjusted
    # matching each treated unit to its nearest control (with replacement), effect on the treated
    xt, xc, yc = x[w], x[~w], y[~w]
    m = np.argmin(((xt[:, None, :] - xc[None, :, :]) ** 2).sum(-1), axis=1)
    out["matching"] = np.mean(y[w] - yc[m])
    used = np.unique(m)                                         # regression on the matched controls
    beta_c = ols(np.column_stack([np.ones(len(used)), xc[used]]), yc[used])[1:]
    out["bias-corrected matching"] = np.mean(y[w] - yc[m] - (xt - xc[m]) @ beta_c)
    return out


results = [estimates(*simulate()) for _ in range(reps)]
labels = list(results[0])
values = [[r[k] for r in results] for k in labels]

fig, ax = plt.subplots(figsize=(8, 4.2))
ax.boxplot(values, orientation="horizontal", widths=0.6, showfliers=False)
ax.set_yticks(range(1, len(labels) + 1))
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.axvline(tau, color="C3", ls="--", lw=1.2, label="true effect")
ax.set_xlabel(f"estimate over {reps} simulated data sets (N = {n})")
ax.legend(fontsize=8, loc="lower right")
fig.tight_layout()
