"""Functional connectivity and a hierarchy of intrinsic time scales in a linear network of cortical areas.

30 areas in 5 modules; structural connectivity W: sparse random weights, denser within modules
(probability 0.5 within, 0.06 between), normalized to spectral radius 1. Each area k has a position
h_k in [0, 1] along the sensory-association hierarchy and a local recurrent strength
w_k = 0.2 + 0.6 h_k (stronger in association areas, as in Chaudhuri et al. 2015).
Dynamics (Ornstein-Uhlenbeck): tau dx = (-x + diag(w) x + g W x) dt + noise, tau = 20 ms, g = 0.15.
Stationary covariance from the Lyapunov equation A S + S A^T + Q = 0; functional connectivity is
the correlation matrix; autocorrelation of area k at lag t is [expm(A t) S]_kk / S_kk.
A: structural connectivity. B: functional connectivity. C: FC against SC for all pairs.
D: autocorrelation functions of areas low, middle and high in the hierarchy, with their
intrinsic time scales (integral of the autocorrelation).
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov

import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)
n, m = 30, 5
mod = np.repeat(np.arange(m), n // m)
prob = np.where(mod[:, None] == mod[None, :], 0.5, 0.06)
W = (rng.random((n, n)) < prob) * rng.uniform(0.2, 1.0, (n, n))
W = (W + W.T) / 2
np.fill_diagonal(W, 0)
W /= np.max(np.abs(np.linalg.eigvals(W)))
h = rng.permutation(np.linspace(0, 1, n))
w = 0.2 + 0.6 * h
tau, g = 20.0, 0.15
A = (-np.eye(n) + np.diag(w) + g * W) / tau
assert np.max(np.linalg.eigvals(A).real) < 0
S = solve_continuous_lyapunov(A, -np.eye(n))
sd = np.sqrt(np.diag(S))
FC = S / np.outer(sd, sd)

fig, axs = plt.subplots(1, 4, figsize=(15, 3.8))
im = axs[0].imshow(W, cmap="Blues", vmin=0)
axs[0].set_title("A  Structural connectivity", loc="left", fontsize=10)
fig.colorbar(im, ax=axs[0], fraction=0.046)
F2 = FC.copy()
np.fill_diagonal(F2, np.nan)
im = axs[1].imshow(F2, cmap="Reds", vmin=0)
axs[1].set_title("B  Functional connectivity", loc="left", fontsize=10)
fig.colorbar(im, ax=axs[1], fraction=0.046)
for a in axs[:2]:
    a.set_xlabel("Area")
    a.set_ylabel("Area")
iu = np.triu_indices(n, 1)
ax = axs[2]
ax.scatter(W[iu], FC[iu], s=6, color=P.edge("negative"), alpha=0.6)
r = np.corrcoef(W[iu], FC[iu])[0, 1]
ax.text(0.97, 0.05, f"r = {r:.2f}", transform=ax.transAxes, ha="right", fontsize=9, color=P.ink())
ax.set_xlabel("Structural weight")
ax.set_ylabel("Functional correlation")
ax.set_title("C  FC against SC", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)
ax = axs[3]
lags = np.linspace(0, 600, 121)
E1 = expm(A * (lags[1] - lags[0]))
ac = np.empty((len(lags), n))
M = S.copy()
for i in range(len(lags)):
    ac[i] = np.diag(M) / np.diag(S)
    M = E1 @ M
tau_int = np.trapezoid(ac, lags, axis=0) if hasattr(np, "trapezoid") else np.trapz(ac, lags, axis=0)
order = np.argsort(h)
picks = [order[0], order[n // 2], order[-1]]
names = ["low (sensory)", "middle", "high (association)"]
for k, nm, col in zip(picks, names, (P.edge("dna"), P.edge("enzyme"), P.edge("negative"))):
    ax.plot(lags, ac[:, k], color=col, lw=1.8, label=f"{nm}: {tau_int[k]:.0f} ms")
ax.set_xlabel("Lag / ms")
ax.set_ylabel("Autocorrelation")
ax.set_title("D  Intrinsic time scales", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5)
ax.grid(True, alpha=0.3)
fig.tight_layout()
