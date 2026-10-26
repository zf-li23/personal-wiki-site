# A minimal version of the phase-separation model of transcriptional control (Hnisz, Shrinivas, Young,
# Chakraborty and Sharp, 2017), simulated with the Gillespie algorithm.
# N chains (enhancer components: transcription factors, coactivators, the Pol II CTD) in a fixed volume each
# carry f sites. A site can be modified (e.g. phosphorylated) and demodified at rates k_mod and k_demod; only
# modified sites on different chains can form a noncovalent cross-link (rate k_on per pair of free modified
# sites, scaled by the volume), and a cross-link breaks with rate k_off; a site in a cross-link is protected
# from demodification. Transcriptional activity is taken as the size of the largest connected cluster divided
# by N (TA), averaged over the steady state and over replicate runs.
# The volume is the same for both systems, so the larger N (a super-enhancer, N = 50) also means a higher
# concentration of interacting chains than for a typical enhancer (N = 10), as in the original model.
# A: TA against valency f (number of modifiable sites per chain): the super-enhancer switches on abruptly at
#    low valency, the typical enhancer rises gradually; dashed lines are Hill fits, with the Hill coefficients
#    shown. B: the same TA against the modifier/demodifier ratio at fixed f = 4: a signal that changes the
#    fraction of modified sites switches the super-enhancer sharply.
# Parameters (dimensionless): k_mod = k_demod = 0.05 per site times the modifier or demodifier level,
# k_on = 0.5 / V, k_off = 0.5 (K_eq = 1), V = 25; 10 replicates of 200 time units per point (first 80 discarded).
import math
import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import wikibio as bio
from wikibio import charts

P = bio.P
rnd = random.Random(0)
V = 25.0
KON, KOFF = 0.5 / V, 0.5


def largest_cluster(n, bonds):
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for i, j in bonds:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
    counts = [0] * n
    for k in range(n):
        counts[find(k)] += 1
    return max(counts)


def pick(weights, total):
    """Index chosen with probability weights[i] / total."""
    r = rnd.random() * total
    for i, w in enumerate(weights):
        r -= w
        if r < 0:
            return i
    return len(weights) - 1


def simulate(n, f, mod_level=1.0, demod_level=1.0, t_end=200.0, t_burn=80.0, every=4.0):
    u = [f] * n  # unmodified sites per chain
    m = [0] * n  # free modified sites per chain
    bonds = []  # one entry per cross-link
    kmod, kdem = 0.05 * mod_level, 0.05 * demod_level
    U, M, S2 = n * f, 0, 0  # totals and sum of m_i^2
    t, acc, cnt, nxt = 0.0, 0.0, 0, t_burn
    while True:
        a_mod, a_dem = kmod * U, kdem * M
        a_on = KON * 0.5 * (M * M - S2)
        a_off = KOFF * len(bonds)
        a0 = a_mod + a_dem + a_on + a_off
        t += -math.log(1.0 - rnd.random()) / a0
        while nxt < t and nxt <= t_end:  # sample the state at regular times
            acc += largest_cluster(n, bonds) / n
            cnt += 1
            nxt += every
        if t > t_end:
            return acc / cnt
        r = rnd.random() * a0
        if r < a_mod:
            i = pick(u, U)
            u[i] -= 1
            S2 += 2 * m[i] + 1
            m[i] += 1
            U -= 1
            M += 1
        elif r < a_mod + a_dem:
            i = pick(m, M)
            S2 -= 2 * m[i] - 1
            m[i] -= 1
            u[i] += 1
            M -= 1
            U += 1
        elif r < a_mod + a_dem + a_on:
            while True:
                i, j = pick(m, M), pick(m, M)
                if i != j:
                    break
            S2 -= 2 * m[i] - 1
            m[i] -= 1
            S2 -= 2 * m[j] - 1
            m[j] -= 1
            M -= 2
            bonds.append((i, j))
        else:
            k = rnd.randrange(len(bonds))
            i, j = bonds[k]
            bonds[k] = bonds[-1]
            bonds.pop()
            S2 += 2 * m[i] + 1
            m[i] += 1
            S2 += 2 * m[j] + 1
            m[j] += 1
            M += 2


def ta_curve(n, xs, kind, reps=10):
    out = []
    for x in xs:
        if kind == "f":
            vals = [simulate(n, int(x)) for _ in range(reps)]
        else:
            vals = [simulate(n, 4, mod_level=x, demod_level=1.0) for _ in range(reps)]
        out.append(np.mean(vals))
    return np.array(out)


def hill(x, lo, hi, k, h):
    return lo + (hi - lo) * x ** h / (k ** h + x ** h)


fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.9))
fs = np.arange(1, 13)
ratios = np.logspace(-1, 1, 13)
for n, tok, name in ((50, "negative", "super-enhancer, N = 50"), (10, "dna", "typical enhancer, N = 10")):
    ta = ta_curve(n, fs, "f")
    ax = axs[0]
    ax.plot(fs, ta, "o", color=charts.line(tok), ms=4.5, label=name)
    try:
        p, _ = curve_fit(hill, fs, ta, p0=[ta.min(), 1.0, 5.0, 3.0], bounds=([0, 0, 1, 0.5], [1, 1.2, 20, 40]))
        xx = np.linspace(fs[0], fs[-1], 200)
        ax.plot(xx, hill(xx, *p), color=charts.line(tok), lw=1.2, ls=(0, (4, 2.4)))
        xt, yt = (1.0, 0.5) if n == 50 else (7.2, 0.62)
        ax.text(xt, yt, f"Hill n ≈ {p[3]:.1f}", fontsize=7, color=charts.line(tok), ha="left")
    except RuntimeError:
        pass
    tb = ta_curve(n, ratios, "r")
    axs[1].semilogx(ratios, tb, "o-", color=charts.line(tok), ms=4.5, lw=1.4, label=name)

ax = axs[0]
ax.set_ylim(0, 1.05)
ax.set_xlim(0.5, 12.5)
charts.style_axes(ax, "valency f (modifiable sites per chain)", "TA = largest cluster / N")
ax.legend(fontsize=7, frameon=False, loc="upper left")
ax.set_title("A   Activity against valency", loc="left", fontsize=9, color=P.ink())
ax = axs[1]
ax.set_ylim(0, 1.05)
charts.style_axes(ax, "modifier / demodifier ratio (f = 4)", "TA = largest cluster / N")
ax.legend(fontsize=7, frameon=False, loc="upper left")
ax.set_title("B   Activity against a signal", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
