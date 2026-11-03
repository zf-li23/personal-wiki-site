"""The consistency index does not measure phylogenetic accuracy (after Yang 2014). Data of
500 sites are simulated under JC69 on the unrooted tree ((a:0.5, b:0.5):0.1, c:0.6, d:1.4) with all branch
lengths multiplied by a constant, so that the tree length (expected substitutions per site, summed over
branches) varies along the x-axis. For 200 data sets per point: the probability that maximum parsimony
recovers the true tree, and the mean consistency index CI = sum of minimum possible changes / sum of
changes on the most parsimonious tree. Accuracy rises quickly, peaks at an intermediate divergence and
then declines, while CI hardly changes and says nothing about whether the tree is right."""
import itertools
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

PATS = np.array(list(itertools.product(range(4), repeat=4)))
CODES = PATS @ np.array([64, 16, 4, 1])


def fitch_len(x):
    """Fitch length of a four-taxon site x on ((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))."""
    out = []
    for (i, j, k, l) in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)):
        s1, s2 = {x[i]} & {x[j]} or {x[i], x[j]}, {x[k]} & {x[l]} or {x[k], x[l]}
        cost = int(x[i] != x[j]) + int(x[k] != x[l]) + int(not (s1 & s2))
        out.append(cost)
    return out


LEN = np.array([fitch_len(p) for p in PATS])                 # 256 x 3
MIN = np.array([len(set(p)) - 1 for p in PATS])              # minimum possible changes


def pjc(t):
    return 0.25 + 0.75 * np.exp(-4 * t / 3)


def simulate(b, n, rng):
    """((0,1),(2,3)) with b = (t0, t1, t2, t3, t4)."""
    def evolve(x, t):
        ch = rng.random(n) > pjc(t)
        return np.where(ch, (x + rng.integers(1, 4, n)) % 4, x)
    u = rng.integers(0, 4, n)
    v = evolve(u, b[0])
    tips = np.stack([evolve(u, b[1]), evolve(u, b[2]), evolve(v, b[3]), evolve(v, b[4])], 1)
    return np.bincount(tips @ np.array([64, 16, 4, 1]), minlength=256)


rng = np.random.default_rng(4)
base = np.array([0.1, 0.5, 0.5, 0.6, 1.4])
lengths = np.array([0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5, 6.5, 8, 10])
pc, ci = [], []
for T in lengths:
    b = base * T / base.sum()
    ok = cis = 0.0
    for _ in range(200):
        c = simulate(b, 500, rng)
        tot = c @ LEN
        best = np.flatnonzero(tot == tot.min())
        ok += float(0 in best) / len(best)
        cis += (c @ MIN) / tot[best[0]] if tot[best[0]] > 0 else 1.0
    pc.append(ok / 200)
    ci.append(cis / 200)

fig, ax = plt.subplots(figsize=(6.6, 3.8))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.16, top=0.95)
ax.plot(lengths, pc, "o-", color=charts.line("dna"), lw=1.6, ms=4, label="probability of the true tree")
ax.plot(lengths, ci, "s-", color=charts.line("rna"), lw=1.6, ms=4, label="consistency index of the MP tree")
ax.set_ylim(0, 1.02)
ax.set_xlim(0, 10.3)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "tree length (expected substitutions per site)", "probability / CI")
