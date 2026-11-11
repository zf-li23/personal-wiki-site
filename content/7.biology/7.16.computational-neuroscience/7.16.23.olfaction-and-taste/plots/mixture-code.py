"""Combinatorial receptor codes for single odorants and for odour mixtures.

A: each of 300 receptor types binds a given odorant with a dissociation constant drawn
log-normally (median 1 mM, 1.5 decades s.d.); occupancy c/(c + K). The number of receptor types
more than half occupied grows with concentration, so the code of one odorant changes with its
concentration. B, C: mixture codes. A mixture of N components (drawn from 128 odorants, as in
Bushdid et al. 2014) is coded by the mean occupancy vector of its components; independent Gaussian
noise per receptor type has s.d. sigma = 0.8 occupancy units, an effective noise (including downstream
variability) chosen so that 30-component mixtures approach d' = 1 when about a third of the components
differ, the order of the experimental limit. Discriminability d' = ||m1 - m2|| / sigma.
B: d' against the fraction of components that differ (N = 10, 20, 30; R = 300).
C: d' between two mixtures with no shared component against N for R = 3, 30, 300 receptor types;
lines are the prediction d'^2 = 2 (1 - f) tr(Sigma) / (N sigma^2) (Proposition 23.2.1).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)

fig, axs = plt.subplots(1, 3, figsize=(13, 4.1))

# A: recruitment of receptors with concentration
R = 300
ax = axs[0]
conc = np.logspace(-6, 0, 200)  # mol/L
cols = [P.edge("dna"), P.edge("rna"), P.edge("enzyme")]
for i in range(3):
    logK = rng.normal(np.log10(1e-3), 1.5, R)
    K = 10.0**logK
    occ = conc[:, None] / (conc[:, None] + K[None, :])
    ax.plot(conc * 1e3, (occ > 0.5).sum(axis=1), color=cols[i], lw=2, label=f"odorant {i + 1}")
ax.set_xscale("log")
ax.set_xlabel("Concentration / mM")
ax.set_ylabel("Receptor types > half occupied")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Recruitment with concentration", loc="left", fontsize=10)

# library of 128 odorants coded by 300 receptors at a fixed concentration
M = 128
sigma = 0.8


def library(R):
    K = 10.0 ** rng.normal(np.log10(1e-3), 1.5, (M, R))
    c = 1e-4
    return c / (c + K)  # M x R occupancies


def dprime(A, N, n_diff, trials=300):
    out = np.empty(trials)
    for t in range(trials):
        idx = rng.permutation(M)
        shared = idx[: N - n_diff]
        u1 = idx[N - n_diff: N]
        u2 = idx[N: N + n_diff]
        m1 = A[np.concatenate([shared, u1])].mean(axis=0)
        m2 = A[np.concatenate([shared, u2])].mean(axis=0)
        out[t] = np.linalg.norm(m1 - m2) / sigma
    return out.mean()


ax = axs[1]
A300 = library(300)
for N, c in zip((10, 20, 30), cols):
    nd = np.arange(0, N + 1, max(1, N // 10))
    d = [dprime(A300, N, k) for k in nd]
    ax.plot(nd / N, d, "o-", color=c, ms=3.5, lw=1.6, label=f"N = {N}")
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.text(0.85, 0.85, "d' = 1", fontsize=8, color=P.muted())
ax.set_xlabel("Fraction of components that differ")
ax.set_ylabel("Discriminability d'")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("B  Mixtures of N components (R = 300)", loc="left", fontsize=10)

ax = axs[2]
Ns = np.array([1, 2, 4, 8, 16, 32, 60])
for Rr, c in zip((3, 30, 300), cols):
    A = library(Rr)
    d = [dprime(A, n, n, trials=200) for n in Ns]
    trS = np.trace(np.cov(A, rowvar=False))
    theory = np.sqrt(2 * trS / (Ns * sigma**2))
    ax.plot(Ns, d, "o", color=c, ms=4, label=f"R = {Rr}")
    ax.plot(Ns, theory, "-", color=c, lw=1.2)
ax.set_xscale("log")
ax.set_yscale("log")
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Components per mixture N")
ax.set_ylabel("d' between disjoint mixtures")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("C  Towards olfactory white", loc="left", fontsize=10)

fig.tight_layout()
