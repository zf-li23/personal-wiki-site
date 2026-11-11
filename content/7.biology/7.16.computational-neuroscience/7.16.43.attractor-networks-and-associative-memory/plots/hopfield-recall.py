"""Retrieval and sequence recall in the Amari-Hopfield network.

N = 500 binary units x_i = +-1, K random patterns xi^mu, Hebbian weights
w_ij = (1/N) sum_mu xi_i^mu xi_j^mu, w_ii = 0, asynchronous updates x_i <- sgn(sum_j w_ij x_j)
in random order; time is counted in sweeps (N single-unit updates). Seed 0.
A: K = 25 (load alpha = 0.05); the cue is pattern 1 with 30 % of its units flipped (overlap 0.4).
   Overlap m_mu = (1/N) xi^mu . x with the cued pattern (thick) and with the other patterns (thin).
B: energy E = -(1/2) sum_ij w_ij x_i x_j along the same trajectory, sampled after every
   N/20 updates: it never increases.
C: basins of attraction: final overlap with the cued pattern against the initial overlap, for
   alpha = 0.05, 0.10 and 0.13 (10 cues per point).
D: sequence recall with asymmetric weights w_ij = (1/N) sum_mu xi_i^(mu+1) xi_j^mu
   (5 patterns in a cycle) and synchronous updates: the state steps through the sequence.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N = 500


def weights(X):
    W = X.T @ X / N
    np.fill_diagonal(W, 0.0)
    return W


def cue(x, m0):
    y = x.copy()
    flip = rng.random(N) < (1 - m0) / 2
    y[flip] *= -1
    return y


def run(W, x, sweeps, record=None, X=None):
    ms, es = [], []
    for s in range(sweeps):
        order = rng.permutation(N)
        for k, i in enumerate(order):
            h = W[i] @ x
            x[i] = 1.0 if h >= 0 else -1.0
            if record is not None and k % (N // 20) == 0:
                ms.append(X @ x / N)
                es.append(-0.5 * x @ W @ x)
    return x, np.array(ms), np.array(es)


fig, axs = plt.subplots(1, 4, figsize=(15, 3.7))
X = rng.choice([-1.0, 1.0], size=(25, N))
W = weights(X)
x0 = cue(X[0], 0.4)
_, ms, es = run(W, x0.copy(), 4, record=True, X=X)
tt = np.arange(len(ms)) / 20
ax = axs[0]
for mu in range(1, 25):
    ax.plot(tt, ms[:, mu], color=P.muted(), lw=0.6)
ax.plot(tt, ms[:, 0], color=P.edge("dna"), lw=2.2, label="Cued pattern")
ax.set_xlabel("Time / sweeps")
ax.set_ylabel("Overlap $m_\\mu$")
ax.set_ylim(-0.3, 1.05)
ax.set_title("A  Pattern completion", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="center right")
ax = axs[1]
ax.plot(tt, es, color=P.edge("negative"), lw=2)
ax.set_xlabel("Time / sweeps")
ax.set_ylabel("Energy $E$")
ax.set_title("B  Energy descent", loc="left", fontsize=10)

ax = axs[2]
m0s = np.linspace(0.0, 0.9, 10)
for alpha, c in zip((0.05, 0.10, 0.13), (P.edge("dna"), P.edge("positive"), P.edge("negative"))):
    K = int(alpha * N)
    X2 = rng.choice([-1.0, 1.0], size=(K, N))
    W2 = weights(X2)
    out = []
    for m0 in m0s:
        vals = []
        for _ in range(10):
            xf, _, _ = run(W2, cue(X2[0], m0), 6)
            vals.append(X2[0] @ xf / N)
        out.append(np.mean(vals))
    ax.plot(m0s, out, "o-", ms=4, color=c, lw=1.8, label=f"$\\alpha$ = {alpha}")
ax.plot([0, 1], [0, 1], ls="--", color=P.muted(), lw=1)
ax.set_xlabel("Initial overlap")
ax.set_ylabel("Final overlap")
ax.set_title("C  Basins shrink with load", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")

ax = axs[3]
S = rng.choice([-1.0, 1.0], size=(5, N))
Wseq = sum(np.outer(S[(m + 1) % 5], S[m]) for m in range(5)) / N
x = cue(S[0], 0.6)
traj = []
for step in range(12):
    traj.append(S @ x / N)
    x = np.where(Wseq @ x >= 0, 1.0, -1.0)
traj = np.array(traj)
for m in range(5):
    ax.plot(np.arange(12), traj[:, m], "o-", ms=3, lw=1.6, color=P.edge(P.protein(m)), label=f"$\\xi^{m + 1}$")
ax.set_xlabel("Time step")
ax.set_ylabel("Overlap")
ax.set_title("D  Sequence recall", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.0))
ax.set_ylim(-0.4, 1.3)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
