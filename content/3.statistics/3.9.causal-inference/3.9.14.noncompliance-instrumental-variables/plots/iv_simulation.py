"""Naive analyses and the IV (Wald) estimator in a randomized experiment with noncompliance."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n, reps = 2000, 500
# compliance types: never-taker, complier, always-taker; no defiers (monotonicity)
effects = {"nt": 0.5, "co": 1.0, "at": 4.0}


def one_study():
    u = rng.normal(0, 1, n)                                   # unobserved health
    score = u + rng.normal(0, 1, n)
    g = np.where(score < -0.6, "nt", np.where(score < 0.9, "co", "at"))
    z = rng.permutation(n) < n // 2                            # randomized assignment
    w = (g == "at") | ((g == "co") & z)                       # receipt of treatment
    y0 = 1.0 + 1.5 * u + rng.normal(0, 1, n)
    tau_i = np.vectorize(effects.get)(g) + rng.normal(0, 0.5, n)
    y = y0 + w * tau_i                                        # exclusion restriction: z enters only via w
    itt_y = y[z].mean() - y[~z].mean()
    itt_w = w[z].mean() - w[~z].mean()
    return {
        "as treated": y[w].mean() - y[~w].mean(),
        "per protocol": y[w & z].mean() - y[~w & ~z].mean(),
        "intention to treat": itt_y,
        "IV (Wald) = CACE estimate": itt_y / itt_w,
    }, tau_i[g == "co"].mean(), tau_i.mean()


runs = [one_study() for _ in range(reps)]
labels = list(runs[0][0])
values = [[r[0][k] for r in runs] for k in labels]
cace = np.mean([r[1] for r in runs])
ate = np.mean([r[2] for r in runs])

fig, ax = plt.subplots(figsize=(8, 3.6))
ax.boxplot(values, orientation="horizontal", widths=0.6, showfliers=False)
ax.set_yticks(range(1, len(labels) + 1))
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.axvline(cace, color="C3", ls="--", lw=1.2, label=f"complier effect ({cace:.2f})")
ax.axvline(ate, color="C0", ls=":", lw=1.5, label=f"population average effect ({ate:.2f})")
ax.set_xlabel(f"estimate over {reps} simulated experiments (N = {n})")
ax.legend(fontsize=8, loc="lower right")
fig.tight_layout()
