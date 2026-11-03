"""The selection bias of the KH test, in the large-sample normal approximation. The log-likelihoods of
m candidate trees are correlated normal variables (correlation 0.5, so that each pairwise difference has
standard deviation 1); the true tree has the same expected log-likelihood as the others (the worst case,
solid lines) or a higher one by one standard deviation of a difference (dashed). The probability that the
true tree is rejected at the one-sided 5% level, from 100 000 simulated data sets: by the KH test against
the tree with the highest likelihood (the common but invalid use), which grows with the number of
candidate trees, and by the SH test, calibrated on the distribution of the maximum, which stays at or
below 5%."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(2)
ms = np.array([2, 3, 5, 10, 20, 50, 100])
crit = norm.isf(0.05)
N = 100000


def draws(m):
    return np.sqrt(0.5) * rng.standard_normal((N, 1)) + np.sqrt(0.5) * rng.standard_normal((N, m))


curves = {}
for adv in (0.0, 1.0):
    kh, sh = [], []
    for m in ms:
        Z = draws(m)
        Z[:, 0] += adv
        T = Z.max(1) - Z[:, 0]
        kh.append((T > crit).mean())
        Z0 = draws(m)
        q = np.quantile(Z0.max(1) - Z0[:, 0], 0.95)
        sh.append((T > q).mean())
    curves[adv] = (np.array(kh), np.array(sh))

fig, a = plt.subplots(figsize=(7.0, 3.9))
fig.subplots_adjust(left=0.1, right=0.97, bottom=0.16, top=0.95)
for adv, ls, lab in ((0.0, "-", "equal fit"), (1.0, "--", "true tree better by 1 SD")):
    kh, sh = curves[adv]
    a.plot(ms, kh, "o" + ls, color=charts.line("negative"), lw=1.5, ms=4, label=f"KH against the ML tree, {lab}")
    a.plot(ms, sh, "^" + ls, color=charts.line("plant"), lw=1.5, ms=4, label=f"SH test, {lab}")
a.axhline(0.05, color=P.muted(), lw=0.8, ls=":")
a.text(100, 0.06, "5%", fontsize=FT["tiny"], color=P.muted(), va="bottom", ha="right")
a.set_xscale("log")
a.set_xticks(ms, [str(v) for v in ms])
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "number of candidate trees $m$", "rejection rate of the true tree")
