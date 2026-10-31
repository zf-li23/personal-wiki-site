# RNA secondary structure by dynamic programming in a simple base-pair model.
# Sequence of 32 nt (made up for illustration). Each base pair contributes an energy -3 (G-C), -2 (A-U)
# or -1 (G-U) in units of k_B T; hairpin loops must contain at least 3 unpaired nucleotides; pseudoknots
# are excluded. The decomposition used for both recursions considers whether nucleotide i is unpaired
# or paired with some k:
#   E(i, j) = min[ E(i+1, j),  min_k ( e(i, k) + E(i+1, k-1) + E(k+1, j) ) ]       (Nussinov-type)
#   Z(i, j) = Z(i+1, j) + sum_k exp(-e(i, k)) Z(i+1, k-1) Z(k+1, j)              (McCaskill-type)
# A: the dynamic-programming matrix E(i, j) (lowest energy of the subsequence i..j), filled from the
#    diagonal outward; the optimum for the whole sequence is in the top right corner.
# B: the optimal structure from the traceback, drawn as an arc diagram, with its dot-bracket notation.
# C: base-pair probabilities from 2000 structures sampled from the Boltzmann ensemble by stochastic
#    traceback of Z (upper triangle) and the optimal pairs (lower triangle): the ensemble contains the
#    optimal helices with high probability, and alternative pairings with lower probability.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(7)
seq = "GGGCAUAGCCCAAGGCUCGAAAGAGCCUAUAC"
n = len(seq)
pe = {("G", "C"): 3, ("C", "G"): 3, ("A", "U"): 2, ("U", "A"): 2, ("G", "U"): 1, ("U", "G"): 1}


def epair(i, k):
    return -pe[(seq[i], seq[k])] if (seq[i], seq[k]) in pe and k - i > 3 else None


E = np.zeros((n + 1, n + 1))
Z = np.ones((n + 1, n + 1))
for length in range(1, n):
    for i in range(0, n - length):
        j = i + length
        best = E[i + 1, j]
        z = Z[i + 1, j]
        for k in range(i + 4, j + 1):
            ep = epair(i, k)
            if ep is None:
                continue
            inner = E[i + 1, k - 1] if k - 1 >= i + 1 else 0.0
            right = E[k + 1, j] if k + 1 <= j else 0.0
            best = min(best, ep + inner + right)
            zi = Z[i + 1, k - 1] if k - 1 >= i + 1 else 1.0
            zr = Z[k + 1, j] if k + 1 <= j else 1.0
            z += np.exp(-ep) * zi * zr
        E[i, j] = best
        Z[i, j] = z


def get(M, i, j):
    return M[i, j] if j >= i else (0.0 if M is E else 1.0)


def trace(i, j, pairs):
    if j - i < 4:
        return
    if np.isclose(E[i, j], get(E, i + 1, j)):
        trace(i + 1, j, pairs)
        return
    for k in range(i + 4, j + 1):
        ep = epair(i, k)
        if ep is not None and np.isclose(E[i, j], ep + get(E, i + 1, k - 1) + get(E, k + 1, j)):
            pairs.append((i, k))
            trace(i + 1, k - 1, pairs)
            trace(k + 1, j, pairs)
            return


def sample(i, j, pairs):
    while j - i >= 4:
        r = rng.random() * Z[i, j]
        acc = get(Z, i + 1, j)
        if r < acc:
            i += 1
            continue
        for k in range(i + 4, j + 1):
            ep = epair(i, k)
            if ep is None:
                continue
            acc += np.exp(-ep) * get(Z, i + 1, k - 1) * get(Z, k + 1, j)
            if r < acc:
                pairs.append((i, k))
                sample(i + 1, k - 1, pairs)
                i = k + 1
                break
        else:
            return


opt = []
trace(0, n - 1, opt)
db = ["."] * n
for a, b in opt:
    db[a], db[b] = "(", ")"
prob = np.zeros((n, n))
ns = 2000
for _ in range(ns):
    ps = []
    sample(0, n - 1, ps)
    for a, b in ps:
        prob[a, b] += 1 / ns

fig = plt.figure(figsize=(14, 4.6))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1.5, 1])
ax = fig.add_subplot(gs[0, 0])
M = np.where(np.triu(np.ones((n, n)), 1) > 0, E[:n, :n], np.nan)
im = ax.imshow(M, cmap="viridis_r", origin="upper")
ax.set_xticks(range(n))
ax.set_xticklabels(list(seq), fontsize=5)
ax.set_yticks(range(n))
ax.set_yticklabels(list(seq), fontsize=5)
ax.tick_params(length=0, labelcolor=P.ink())
cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
cb.set_label("E(i, j) / k_B T", fontsize=8, color=P.ink())
charts.title(ax, f"A   DP matrix (optimum {E[0, n - 1]:.0f} k_B T)")

ax = fig.add_subplot(gs[0, 1])
for i, ch in enumerate(seq):
    ax.text(i, 0, ch, ha="center", va="center", fontsize=8, family="monospace",
            color=P.NUCLEOTIDE[ch], weight="bold")
    ax.text(i, -1.0, db[i], ha="center", va="center", fontsize=8, family="monospace", color=P.ink())
for a, b in opt:
    t = np.linspace(0, np.pi, 60)
    cx, r = (a + b) / 2, (b - a) / 2
    ax.plot(cx + r * np.cos(t), 0.5 + 0.55 * r * np.sin(t), color=charts.line("rna"), lw=1.1)
ax.set_xlim(-1, n)
ax.set_ylim(-1.8, 0.55 * n / 2 + 1.5)
ax.axis("off")
charts.title(ax, f"B   Optimal structure: {len(opt)} base pairs")

ax = fig.add_subplot(gs[0, 2])
show = np.full((n, n), np.nan)
iu = np.triu_indices(n, 1)
show[iu] = prob[iu]
for a, b in opt:
    show[b, a] = 1.0
im = ax.imshow(np.ma.masked_less(np.nan_to_num(show), 0.02), cmap="magma_r", vmin=0, vmax=1, origin="upper")
ax.plot([-0.5, n - 0.5], [-0.5, n - 0.5], color=P.muted(), lw=0.6)
ax.set_xticks([])
ax.set_yticks([])
cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
cb.set_label("pair probability", fontsize=8, color=P.ink())
ax.text(n * 0.98, n * 0.05, "Boltzmann\nensemble", ha="right", va="top", fontsize=7, color=P.ink())
ax.text(n * 0.02, n * 0.95, "optimal\nstructure", ha="left", va="bottom", fontsize=7, color=P.ink())
charts.title(ax, "C   Base-pair probabilities")
fig.tight_layout()
