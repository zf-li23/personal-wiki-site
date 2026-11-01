"""How certain is a percent spliced in? A: the posterior distribution of PSI for one skipped exon with the
same ratio of inclusion to skipping reads (I : S = 3 : 1, PSI = 0.60) at three depths, from a uniform prior
on the probability that a junction read supports inclusion, transformed to PSI with the effective lengths
(read length 100, anchor 8). B, C: differential splicing with replicates, in a model like that of rMATS:
logit PSI of each replicate is normal around its group mean with a shared variance, and junction reads are
binomial given PSI; the likelihood ratio test compares equal and unequal group means. Each replicate has
about 96 junction reads. In B the three replicates of each group agree, in C they disagree: the evidence for
a difference is much weaker, although a Fisher test on the pooled counts, which ignores replicates, still
reports a tiny p-value. Points: PSI of each replicate with 95% intervals; lines: fitted
group means."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, optimize, special
import wikibio as bio
from wikibio import charts

P = bio.P
L, a = 100, 8
lS = L - 2 * a + 1
lI = 2 * lS


def psi_of_p(p):
    return p * lS / (p * lS + (1 - p) * lI)


def p_of_psi(psi):
    return psi * lI / (psi * lI + (1 - psi) * lS)


fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.6))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.3)
ax = axs[0]
g = np.linspace(0.001, 0.999, 999)
for (I, S), tok in [((6, 2), "neutral"), ((60, 20), "rna"), ((600, 200), "dna")]:
    p = p_of_psi(g)
    # density of PSI: Beta(I+1, S+1) density of p times dp/dpsi
    dp = lI * lS / (g * lI + (1 - g) * lS) ** 2
    dens = stats.beta.pdf(p, I + 1, S + 1) * dp
    lo, hi = psi_of_p(stats.beta.ppf([0.025, 0.975], I + 1, S + 1))
    ax.plot(g, dens, color=charts.line(tok), lw=1.6, label=f"I = {I}, S = {S}: 95% [{lo:.2f}, {hi:.2f}]")
ax.axvline(0.6, color=P.muted(), lw=0.7, ls="--")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_ylim(0, 30)
charts.style_axes(ax, "PSI", "posterior density")
charts.title(ax, "A  Depth sets the uncertainty")

xg, wg = np.polynomial.hermite_e.hermegauss(40)  # quadrature for a standard normal
wg = wg / wg.sum()


def nll(mu, sig, I, S):
    out = 0.0
    for i, s in zip(I, S):
        psi = special.expit(mu + sig * xg)
        out -= np.log(np.sum(wg * stats.binom.pmf(i, i + s, p_of_psi(psi))) + 1e-300)
    return out


def fit(I1, S1, I2, S2):
    def lg(I, S):
        return special.logit(psi_of_p((I + 0.5) / (I + S + 1)))
    l1, l2 = lg(I1, S1), lg(I2, S2)
    opts = {"xatol": 1e-7, "fatol": 1e-9, "maxiter": 8000}
    best_f, best_n = None, None
    for ls in (-2.0, -1.0, 0.0, 1.0):
        f = optimize.minimize(lambda t: nll(t[0], np.exp(t[2]), I1, S1) + nll(t[1], np.exp(t[2]), I2, S2),
                              [l1.mean(), l2.mean(), ls], method="Nelder-Mead", options=opts)
        n = optimize.minimize(lambda t: nll(t[0], np.exp(t[1]), np.r_[I1, I2], np.r_[S1, S2]),
                              [np.r_[l1, l2].mean(), ls], method="Nelder-Mead", options=opts)
        best_f = f if best_f is None or f.fun < best_f.fun else best_f
        best_n = n if best_n is None or n.fun < best_n.fun else best_n
    lr = 2 * (best_n.fun - best_f.fun)
    return best_f.x, lr, stats.chi2.sf(lr, 1)


sets = {"B  Replicates agree": ([84, 70, 95], [12, 15, 10], [30, 45, 22], [40, 30, 38]),
        "C  Replicates disagree": ([94, 84, 60], [2, 12, 36], [73, 38, 13], [23, 58, 83])}
for ax, (ttl, (I1, S1, I2, S2)) in zip(axs[1:], sets.items()):
    th, lr, pv = fit(np.array(I1), np.array(S1), np.array(I2), np.array(S2))
    for k, (I, S, tok) in enumerate([(I1, S1, "dna"), (I2, S2, "rna")]):
        for j, (i, s) in enumerate(zip(I, S)):
            lo, hi = psi_of_p(stats.beta.ppf([0.025, 0.975], i + 1, s + 1))
            x = k + (j - 1) * 0.12
            ax.plot([x, x], [lo, hi], color=charts.line(tok), lw=1.2)
            ax.plot(x, psi_of_p(i / (i + s)), "o", ms=4.5, color=charts.line(tok))
        m = special.expit(th[k])
        ax.plot([k - 0.3, k + 0.3], [m, m], color=charts.line(tok), lw=2)
    dpsi = special.expit(th[0]) - special.expit(th[1])
    pooled = stats.fisher_exact([[sum(I1), sum(S1)], [sum(I2), sum(S2)]])[1]
    ax.text(0.5, 0.03, f"pooled counts: I = {sum(I1)}, {sum(I2)}; S = {sum(S1)}, {sum(S2)}\n"
            f"dPSI = {dpsi:.2f}, LR = {lr:.1f}, p = {pv:.1g}  (pooled Fisher p = {pooled:.0e})",
            transform=ax.transAxes, ha="center", fontsize=7.2, color=P.ink())
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["control (3 replicates)", "treated (3 replicates)"])
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.25, 1.02)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    charts.style_axes(ax, None, "PSI")
    charts.title(ax, ttl)
    print(ttl, th, lr, pv, dpsi, pooled)
