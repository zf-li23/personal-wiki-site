"""Storage capacity of the Amari-Hopfield network.

Random patterns, Hebbian weights w_ij = (1/N) sum_mu xi_i^mu xi_j^mu, w_ii = 0.
A: start exactly in a stored pattern and run asynchronous dynamics to convergence (at most
   15 sweeps); plot the final overlap with that pattern against the load alpha = K/N for
   N = 200 (16 networks per point) and N = 400 (6 networks). Dashed line: alpha_c = 0.138 (Amit, Gutfreund
   and Sompolinsky, 1985). Retrieval degrades sharply near alpha_c, more sharply for larger N.
B: fraction of units that are unstable in a stored pattern before any update (local field of
   opposite sign to the unit), simulation (dots, N = 500) and the signal-to-noise prediction
   P_err = Phi(-1 / sqrt(alpha)) (line, Proposition 43.4.1).
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)


def converge(W, x, sweeps=15):
    N = x.size
    for _ in range(sweeps):
        changed = 0
        for i in rng.permutation(N):
            s = 1.0 if W[i] @ x >= 0 else -1.0
            if s != x[i]:
                x[i] = s
                changed += 1
        if changed == 0:
            break
    return x


alphas = np.array([0.04, 0.08, 0.10, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18, 0.22, 0.26])
fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
for N, c, reps in ((200, P.edge("dna"), 16), (400, P.edge("negative"), 6)):
    mean = []
    for a in alphas:
        K = max(1, int(round(a * N)))
        vals = []
        for _ in range(reps):
            X = rng.choice([-1.0, 1.0], size=(K, N))
            W = X.T @ X / N
            np.fill_diagonal(W, 0)
            xf = converge(W, X[0].copy())
            vals.append(X[0] @ xf / N)
        mean.append(np.mean(vals))
    axs[0].plot(alphas, mean, "o-", ms=4, lw=1.8, color=c, label=f"N = {N}")
axs[0].axvline(0.138, ls="--", color=P.muted(), lw=1)
axs[0].text(0.142, 0.4, "$\\alpha_c \\approx 0.138$", fontsize=8, color=P.muted())
axs[0].set_xlabel("Load $\\alpha = K/N$")
axs[0].set_ylabel("Final overlap with stored pattern")
axs[0].set_title("A  Retrieval collapses near $\\alpha_c$", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="lower left")

N = 500
a2 = np.linspace(0.02, 0.4, 12)
sim = []
for a in a2:
    K = int(round(a * N))
    X = rng.choice([-1.0, 1.0], size=(K, N))
    W = X.T @ X / N
    np.fill_diagonal(W, 0)
    H = X @ W  # local fields in each stored pattern
    sim.append(np.mean(H * X < 0))
aa = np.linspace(0.01, 0.42, 200)
axs[1].plot(aa, norm.cdf(-1 / np.sqrt(aa)), color=P.edge("dna"), lw=2, label="$\\Phi(-1/\\sqrt{\\alpha})$")
axs[1].plot(a2, sim, "o", ms=5, color=P.edge("negative"), label="Simulation")
axs[1].set_xlabel("Load $\\alpha = K/N$")
axs[1].set_ylabel("Fraction of unstable units")
axs[1].set_title("B  Signal-to-noise estimate", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
