"""Scoring cell-cell communication from expression (simulated). Four cell types of 150 cells each; a
ligand is expressed mainly by type 1 (mean 4 molecules per cell, 0.3 elsewhere), its receptor by types 2
(mean 3) and 3 (mean 1), and weakly by the rest (0.3); counts are Poisson with log-normal size factors,
normalized by the shifted logarithm. A: the communication probability of each sender-receiver pair in the
CellChat form P = L R / (K + L R), with L and R the trimean (Q1 + 2 Q2 + Q3)/4 of the normalized
ligand and receptor in the two groups and K = 0.5; stars mark pairs whose probability exceeds that of 99 %
of 1000 random permutations of the cell labels. B: the permutation null distribution for two pairs, with
the observed values (vertical lines)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
nT, nc, K = 4, 150, 0.5
lab = np.repeat(np.arange(nT), nc)
size = rng.lognormal(0, 0.3, lab.size)
muL = np.array([4.0, 0.3, 0.3, 0.3])[lab]
muR = np.array([0.3, 3.0, 1.0, 0.3])[lab]
L = np.log1p(rng.poisson(muL * size) / size)
R = np.log1p(rng.poisson(muR * size) / size)


def trimean(x):
    q1, q2, q3 = np.quantile(x, [0.25, 0.5, 0.75])
    return (q1 + 2 * q2 + q3) / 4


def probs(labels):
    Lm = np.array([trimean(L[labels == k]) for k in range(nT)])
    Rm = np.array([trimean(R[labels == k]) for k in range(nT)])
    LR = np.outer(Lm, Rm)
    return LR / (K + LR)


obs = probs(lab)
B = 1000
null = np.empty((B, nT, nT))
for b in range(B):
    null[b] = probs(rng.permutation(lab))
pval = (1 + (null >= obs).sum(0)) / (B + 1)
np.set_printoptions(precision=3, suppress=True)
print("observed\n", obs)
print("p\n", pval)

names = ["type 1", "type 2", "type 3", "type 4"]
fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.9), gridspec_kw={"width_ratios": [1, 1.25]})
fig.subplots_adjust(left=0.1, right=0.98, bottom=0.16, top=0.88, wspace=0.35)
ax = axs[0]
im = ax.imshow(obs, cmap="Oranges", vmin=0, vmax=1)
for i in range(nT):
    for j in range(nT):
        txt = f"{obs[i, j]:.2f}" + ("*" if pval[i, j] < 0.01 else "")
        ax.text(j, i, txt, ha="center", va="center", fontsize=7.5,
                color=P.on_fill() if obs[i, j] < 0.6 else "white")
ax.set_xticks(range(nT)); ax.set_xticklabels(names)
ax.set_yticks(range(nT)); ax.set_yticklabels(names)
cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
charts.style_axes(ax, "receiver (receptor)", "sender (ligand)", box=True)
charts.title(ax, "A  Communication probability")

ax = axs[1]
for (i, j), tok in [((0, 1), "rna"), ((0, 2), "dna")]:
    ax.hist(null[:, i, j], bins=30, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.4, alpha=0.85,
            label=f"null, {names[i]} to {names[j]}")
    ax.axvline(obs[i, j], color=charts.line(tok), lw=1.6)
    ax.text(obs[i, j], ax.get_ylim()[1] * 0.0 + 20, f"  observed {obs[i, j]:.2f}", fontsize=7.5,
            color=P.ink(), rotation=90, va="bottom")
ax.legend(frameon=False, fontsize=7.5, loc="upper center")
charts.style_axes(ax, "communication probability", "permutations")
charts.title(ax, "B  Label permutation null")
