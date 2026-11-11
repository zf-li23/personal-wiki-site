"""Noise correlations and the information in a population.

A, B: responses (spike counts) of two neurons to two nearby stimuli (ellipses: 1 s.d. contours of
Gaussian noise with equal variances) when the noise correlation is positive (A: both neurons
have the same slope, so the signal direction is along the long axis of the noise) or
positive with opposite slopes (B: signal direction across the long axis).
C: linear Fisher information I = f'^T Sigma^-1 f' of N von Mises tuned neurons on a circle
(r0 = 2, A = 20, kappa = 2, Fano factor 1) with Sigma_ij = sqrt(f_i f_j) c_ij:
independent (c_ij = delta_ij); limited-range correlations c_ij = delta_ij + (1 - delta_ij) 0.2
exp(-|d theta|/(pi/12)) (d theta the difference of preferred directions); and information-limiting
(differential) correlations Sigma = Sigma_0 + eps f' f'^T, eps = 1/400 (saturation at 400).
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

import wikibio as bio

P = bio.P
r0, A, kap = 2.0, 20.0, 2.0


def ell(ax, c, a, rho, col, ls="-"):
    w, v = np.linalg.eigh(np.array([[1, rho], [rho, 1]]) * a ** 2)
    ang = np.degrees(np.arctan2(v[1, 1], v[0, 1]))
    ax.add_patch(Ellipse(c, 2 * np.sqrt(w[1]), 2 * np.sqrt(w[0]), angle=ang, fill=False, ec=col, lw=2, ls=ls))


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
for ax, sgn, ttl in ((axs[0], 1, "A  Same slopes (dashed: independent)"), (axs[1], -1, "B  Opposite slopes")):
    c1, c2 = np.array([10.0, 10.0 * sgn]), np.array([12.0, 12.0 * sgn])
    for rho, ls, lab in ((0.0, "--", "independent"), (0.7, "-", "correlation 0.7")):
        ell(ax, c1, 2.0, rho, P.edge("dna"), ls)
        ell(ax, c2, 2.0, rho, P.edge("rna"), ls)
    ax.plot(*c1, "o", color=P.edge("dna"), ms=4)
    ax.plot(*c2, "o", color=P.edge("rna"), ms=4)
    ax.set_xlim(2, 20)
    ax.set_ylim(-20, -2) if sgn < 0 else ax.set_ylim(2, 20)
    ax.set_aspect("equal")
    ax.set_xlabel("Neuron 1 spike count")
    ax.set_ylabel("Neuron 2 spike count")
    ax.set_title(ttl, loc="left", fontsize=10)

ax = axs[2]
Ns = np.array([8, 16, 32, 64, 128, 256, 512])
res = {k: [] for k in ("independent", "limited-range", "information-limiting")}
for N in Ns:
    th = np.linspace(-np.pi, np.pi, N, endpoint=False)
    s = 0.3
    f = r0 + A * np.exp(kap * (np.cos(s - th) - 1))
    df = -A * kap * np.sin(s - th) * np.exp(kap * (np.cos(s - th) - 1))
    d = np.abs((th[:, None] - th[None, :] + np.pi) % (2 * np.pi) - np.pi)
    C = np.eye(N) + (1 - np.eye(N)) * 0.2 * np.exp(-d / (np.pi / 12))
    sq = np.sqrt(f)
    S = sq[:, None] * C * sq[None, :]
    res["independent"].append(np.sum(df ** 2 / f))
    res["limited-range"].append(df @ np.linalg.solve(S, df))
    S0 = np.diag(f)
    res["information-limiting"].append(df @ np.linalg.solve(S0 + df[:, None] * df[None, :] / 400, df))
for (k, v), c in zip(res.items(), (P.edge("dna"), P.edge("protein"), P.edge("rna"))):
    ax.loglog(Ns, v, "o-", color=c, lw=1.8, ms=4, label=k)
ax.axhline(400, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Number of neurons N")
ax.set_ylabel("Fisher information I_F (rad^-2)")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("C  Which correlations limit information", loc="left", fontsize=10)
fig.tight_layout()
