"""Dense associative memory: polynomial energies store more patterns than neurons.

N = 60 binary units, K random patterns. Energy E(x) = -sum_mu F(xi^mu . x), F(z) = z^n.
Asynchronous update (Krotov and Hopfield, 2016): unit i takes the sign that gives lower energy,
x_i <- sgn( sum_mu [ F(xi_i^mu + s_mu) - F(-xi_i^mu + s_mu) ] ), s_mu = sum_{j != i} xi_j^mu x_j.
For n = 2 this is the classical Hebbian network. Cue: a stored pattern with 10 % of units flipped;
retrieval counts as successful if the final state equals the pattern (6 sweeps, 12 cues per point).
A: fraction of successful retrievals against the number of stored patterns K for n = 2, 3, 4;
   the dotted line marks K = N.
B: signal-to-noise prediction of the capacity, K_max = N^(n-1) / ((2n-3)!! z^2) with z = 3
   (Proposition 43.7.1), against N on log axes.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N = 60


def retrieve(X, x, n, sweeps=6):
    for _ in range(sweeps):
        changed = False
        for i in rng.permutation(N):
            s = X @ x - X[:, i] * x[i]
            d = np.sum((X[:, i] + s) ** n - (-X[:, i] + s) ** n)
            new = 1.0 if d >= 0 else -1.0
            if new != x[i]:
                x[i] = new
                changed = True
        if not changed:
            break
    return x


fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
Ks = {2: [2, 4, 6, 8, 10, 14, 20], 3: [5, 20, 40, 60, 90, 130, 180], 4: [100, 300, 1000, 2000, 4000, 8000]}
cols = {2: P.edge("neutral"), 3: P.edge("dna"), 4: P.edge("negative")}
for n in (2, 3, 4):
    succ = []
    for K in Ks[n]:
        X = rng.choice([-1, 1], size=(K, N)).astype(np.int64)
        ok = 0
        for t in range(12):
            mu = rng.integers(K)
            x = X[mu].copy()
            x[rng.choice(N, N // 10, replace=False)] *= -1
            ok += np.array_equal(retrieve(X, x, n), X[mu])
        succ.append(ok / 12)
    axs[0].semilogx(Ks[n], succ, "o-", ms=4, lw=1.8, color=cols[n], label=f"n = {n}")
axs[0].axvline(N, ls=":", color=P.muted(), lw=1)
axs[0].text(N * 1.08, 0.5, "K = N", fontsize=8, color=P.muted())
axs[0].set_xlabel("Number of stored patterns K")
axs[0].set_ylabel("Fraction retrieved exactly")
axs[0].set_title(f"A  Retrieval, N = {N}", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="lower left")

Ns = np.logspace(1, 4, 50)
dfact = {2: 1, 3: 3, 4: 15, 5: 105}
for n, c in ((2, P.edge("neutral")), (3, P.edge("dna")), (4, P.edge("negative")), (5, P.edge("positive"))):
    axs[1].loglog(Ns, Ns ** (n - 1) / (dfact[n] * 9), lw=2, color=c, label=f"n = {n}")
axs[1].loglog(Ns, Ns, ls=":", color=P.muted(), lw=1)
axs[1].text(2500, 900, "K = N", fontsize=8, color=P.muted())
axs[1].set_xlabel("Number of neurons N")
axs[1].set_ylabel("Capacity $K_{\\max}$")
axs[1].set_title("B  Capacity grows as $N^{n-1}$", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
