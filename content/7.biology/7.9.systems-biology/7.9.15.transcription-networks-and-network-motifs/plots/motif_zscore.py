"""Detecting network motifs in a simulated transcription network.

The network (seed 0) has 400 genes, of which the first 60 encode transcription factors. Each factor
gets a heavy-tailed out-degree (rounded 2 U^(-0.8), at most 60, U uniform); arcs only point down a
hierarchy (from lower to higher index), so there are no feedback cycles. Factors are wired from the
bottom of the hierarchy up; each new target is, with probability 0.5, a target of a factor that the
regulator already controls (closing a feed-forward loop), with probability 0.2 a target of another
regulator of one of its targets (overlapping regulons), and otherwise a random gene below it.
There are no self-arcs.
For the real network and for 200 networks of each null ensemble the script counts feed-forward
loops (X->Y, X->Z, Y->Z), three-node feedback cycles and bi-fans (two regulators sharing two targets).
Null ensembles: Erdos-Renyi digraphs with the same numbers of vertices and arcs, and degree-preserving
randomizations (10 x arcs double-edge swaps that keep every in- and out-degree).
A: distribution of the FFL count in the two ensembles and the observed count.
B: z-scores of the three subgraphs against the two ensembles.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N, NTF = 400, 60
arcs = set()
out = {x: [] for x in range(N)}
for x in reversed(range(NTF)):
    d = int(min(60, round(2.0 * rng.random() ** -0.8)))
    tries = 0
    while len(out[x]) < d and tries < 50 * d:
        tries += 1
        u = rng.random()
        tf_targets = [y for y in out[x] if y < NTF]
        if tf_targets and u < 0.5:
            y = tf_targets[rng.integers(len(tf_targets))]
            cand = out[y]
        elif out[x] and u < 0.7:
            z0 = out[x][rng.integers(len(out[x]))]
            regs = [w for w in range(x + 1, NTF) if z0 in out[w]]
            cand = out[regs[rng.integers(len(regs))]] if regs else []
        else:
            cand = [int(rng.integers(x + 1, N))]
        cand = [z for z in cand if z > x and z not in out[x]]
        if not cand:
            continue
        z = cand[rng.integers(len(cand))]
        out[x].append(z)
        arcs.add((x, z))
arcs = sorted(arcs)
E = len(arcs)


def adj(arc_list):
    A = np.zeros((N, N))
    a = np.array(arc_list)
    A[a[:, 0], a[:, 1]] = 1
    return A


def counts(A):
    A2 = A @ A
    ffl = float(np.sum(A2 * A))
    fbl = float(np.trace(A2 @ A)) / 3
    M = A @ A.T
    np.fill_diagonal(M, 0)
    bifan = float(np.sum(M * (M - 1) / 2)) / 2
    return np.array([ffl, fbl, bifan])


real = counts(adj(arcs))

er = []
for _ in range(200):
    A = np.zeros((N, N))
    idx = rng.choice(N * (N - 1), size=E, replace=False)
    r, c = idx // (N - 1), idx % (N - 1)
    c = c + (c >= r)
    A[r, c] = 1
    er.append(counts(A))
er = np.array(er)

dp = []
src = np.array([a for a, b in arcs])
dst = np.array([b for a, b in arcs])
for _ in range(200):
    s, d = src.copy(), dst.copy()
    present = set(zip(s.tolist(), d.tolist()))
    for _k in range(10 * E):
        i, j = rng.integers(E, size=2)
        a, b, c2, e2 = s[i], d[i], s[j], d[j]
        if a == e2 or c2 == b or (a, e2) in present or (c2, b) in present:
            continue
        present.discard((a, b)); present.discard((c2, e2))
        present.add((a, e2)); present.add((c2, b))
        d[i], d[j] = e2, b
    dp.append(counts(adj(list(zip(s, d)))))
dp = np.array(dp)

fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
ax = axes[0]
bins = np.arange(-0.5, max(dp[:, 0].max(), real[0]) + 3, 1)
ax.hist(er[:, 0], bins=bins, color=charts.line("neutral"), alpha=0.6, label="Erdos-Renyi")
ax.hist(dp[:, 0], bins=bins, color=charts.line("protein"), alpha=0.6, label="degree-preserving")
ax.axvline(real[0], color=charts.line("negative"), lw=2)
ax.text(real[0] - 1, ax.get_ylim()[1] * 0.9, f"observed: {real[0]:.0f}", fontsize=7, color=P.ink(), ha="right")
ax.legend(fontsize=7, frameon=False, loc="center right")
charts.style_axes(ax, "number of feed-forward loops", "randomized networks")
charts.title(ax, "A  FFL count in two null ensembles")

ax = axes[1]
names = ["FFL", "3-cycle", "bi-fan"]
z_er = (real - er.mean(0)) / np.maximum(er.std(0, ddof=1), 1e-9)
z_dp = (real - dp.mean(0)) / np.maximum(dp.std(0, ddof=1), 1e-9)
xs = np.arange(3)
ax.bar(xs - 0.2, np.sign(z_er) * np.log10(1 + np.abs(z_er)), 0.38, color=charts.line("neutral"), label="vs Erdos-Renyi")
ax.bar(xs + 0.2, np.sign(z_dp) * np.log10(1 + np.abs(z_dp)), 0.38, color=charts.line("protein"), label="vs degree-preserving")
for k in range(3):
    for off, z in [(-0.2, z_er[k]), (0.2, z_dp[k])]:
        v = np.sign(z) * np.log10(1 + abs(z))
        ax.text(xs[k] + off, v + (0.05 if v >= 0 else -0.12), f"{z:.1f}", fontsize=6.5, color=P.ink(), ha="center")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_xticks(xs)
ax.set_xticklabels(names)
ax.set_ylim(-0.3, 3.4)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, None, "sign(z) log10(1 + |z|)")
charts.title(ax, "B  z-scores (numbers: z)")
