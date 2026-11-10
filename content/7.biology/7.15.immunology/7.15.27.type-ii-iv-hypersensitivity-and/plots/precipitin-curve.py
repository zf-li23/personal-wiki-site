# Heidelberger-Kendall precipitin curve from a random-bonding model of antigen-antibody lattices (illustrative).
# Antigen: f identical sites (n_Ag = 1000 molecules, F = f n_Ag sites); antibody: 2 sites (A = 2 n_Ab sites).
# Binding is taken as strong, so min(F, A) bonds form between randomly chosen free sites of the two kinds
# (Flory-Stockmayer type random graph; cyclic bonds and steric limits are ignored).
# Mean-field gel window: gelation requires p_A p_B > 1/(f - 1) where p are the fractions of reacted sites, i.e.
#   1/(f - 1) < F/A < f - 1.
# A: fraction of antigen molecules in the largest complex (the precipitate), versus F/A on a log scale;
# B: weight-average size of all other (soluble) complexes, in antigen+antibody molecules.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N_AG = 1000


def simulate(f, ratio):
    F = f * N_AG
    n_ab = max(1, int(round(F / ratio / 2)))
    A = 2 * n_ab
    ag_sites = np.repeat(np.arange(N_AG), f)
    ab_sites = N_AG + np.repeat(np.arange(n_ab), 2)
    rng.shuffle(ag_sites)
    rng.shuffle(ab_sites)
    k = min(F, A)
    parent = np.arange(N_AG + n_ab)

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for u, v in zip(ag_sites[:k], ab_sites[:k]):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    roots = np.array([find(i) for i in range(N_AG + n_ab)])
    ids, counts = np.unique(roots, return_counts=True)
    big = ids[np.argmax(counts)]
    ag_in_big = np.sum(roots[:N_AG] == big) / N_AG
    rest = counts[ids != big]
    sw = (rest ** 2).sum() / rest.sum() if rest.size else 0.0
    return ag_in_big, sw


ratios = np.logspace(-1.7, 1.7, 60)
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.6))
for f, tok in ((4, "protein"), (8, "negative")):
    res = np.array([np.mean([simulate(f, r) for _ in range(6)], axis=0) for r in ratios])
    axs[0].plot(ratios, res[:, 0], color=charts.line(tok), lw=1.6, label=f"f = {f}")
    axs[1].plot(ratios, np.where(res[:, 1] > 0, res[:, 1], np.nan), color=charts.line(tok), lw=1.6, label=f"f = {f}")
    for r in (1 / (f - 1), f - 1):
        axs[0].axvline(r, color=charts.line(tok), lw=0.6, ls=":")
for a in axs:
    a.set_xscale("log")
    a.axvline(1.0, color=P.muted(), lw=0.7, ls="--")
axs[1].set_yscale("log")
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
axs[0].text(1.06, 0.05, "equivalence", fontsize=6.5, color=P.muted())
charts.style_axes(axs[0], "antigen sites / antibody sites (F / A)", "antigen in the largest complex")
charts.style_axes(axs[1], "antigen sites / antibody sites (F / A)", "mean size of soluble complexes")
charts.title(axs[0], "A")
charts.title(axs[1], "B")
fig.tight_layout()
