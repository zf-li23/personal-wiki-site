"""Gradient matching with competition: compression and expansion of the retinotectal map after ablations.

N = 40 retinal axons, labeled by retinal position u in [0, 1] (nasal to temporal) with EphA level R = u. The tectal
ligand level rises from anterior (x = 0) to posterior (x = 1): L(x) = x. Axons keep their order (high R first, anterior)
and occupy the tectal interval [a, b] that is available. The positions x_1 < ... < x_n minimize
  E = alpha sum_k R_k L(x_k) + beta sum_k 1 / (x_{k+1} - x_k),
the first term being the repulsion of each axon by ephrin (high-R axons are pushed anteriorly) and the second a
density penalty (competition: axons cannot pile up; the boundary term 1/x_1^0 is omitted).
Conditions: normal ([a, b] = [0, 1]); posterior half of the tectum removed ([0, 0.5], all axons); temporal half of
the retina removed (axons with u < 0.5 remain, tectum [0, 1]). Gaze and Sharma 1970, Sharma 1972, Yoon 1972.
A: the normal map for increasing strength of repulsion relative to the density penalty (alpha/beta). B: maps u -> x for the three conditions; C: position along the tectum against the retinal
position (rank) for the normal map and the two ablated maps, normalized to the remaining retina.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

import wikibio as bio

P = bio.P
alpha, beta = 40.0, 1.0


def solve(u, a, b):
    """u sorted descending (temporal first). Returns x_k."""
    n = len(u)
    R = u

    def f(x):
        d = np.diff(x)
        if np.any(d <= 1e-6):
            return 1e12 + 1e8 * np.sum(np.clip(1e-6 - d, 0, None))
        return alpha * np.sum(R * x) + beta * np.sum(1 / d)

    def g(x):
        d = np.diff(x)
        d = np.maximum(d, 1e-6)
        gr = alpha * R
        gr[:-1] += beta / d**2
        gr[1:] -= beta / d**2
        return gr

    x0 = np.linspace(a, b, n)
    res = minimize(f, x0, jac=g, method="L-BFGS-B", bounds=[(a, b)] * n,
                   options=dict(maxiter=5000, ftol=1e-14, gtol=1e-10))
    return res.x


u_all = np.linspace(1, 0, 40)  # temporal (1) to nasal (0)
x_norm = solve(u_all, 0, 1)
x_tect = solve(u_all, 0, 0.5)
u_half = u_all[u_all < 0.5]
x_ret = solve(u_half, 0, 1)

fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
for al, col in ((0.0, P.edge("neutral")), (40.0, P.edge("dna")), (400.0, P.edge("rna")), (3000.0, P.edge("positive"))):
    alpha = al
    ax.plot(u_all, solve(u_all, 0, 1), "o-", ms=2.5, lw=1.3, color=col, label=rf"$\alpha/\beta$ = {al:g}")
alpha = 40.0
ax.set_xlabel("Retinal position u (1 = temporal)")
ax.set_ylabel("Tectal position x (0 = anterior)")
ax.invert_xaxis()
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Gradient strength against competition", loc="left", fontsize=10)

bx = axs[1]
bx.plot(u_all, x_norm, "o-", ms=3, lw=1.2, color=P.edge("neutral"), label="normal")
bx.plot(u_all, x_tect, "o-", ms=3, lw=1.2, color=P.edge("dna"), label="posterior tectum removed")
bx.plot(u_half, x_ret, "o-", ms=3, lw=1.2, color=P.edge("rna"), label="temporal retina removed")
bx.set_xlabel("Retinal position u (1 = temporal)")
bx.set_ylabel("Tectal position x of the terminal (0 = anterior)")
bx.invert_xaxis()
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Maps after ablations", loc="left", fontsize=10)

cx = axs[2]
cx.hist(x_norm, bins=np.linspace(0, 1, 11), histtype="step", color=P.edge("neutral"), lw=2, label="normal")
cx.hist(x_tect, bins=np.linspace(0, 1, 11), histtype="step", color=P.edge("dna"), lw=2, label="posterior tectum removed")
cx.hist(x_ret, bins=np.linspace(0, 1, 11), histtype="step", color=P.edge("rna"), lw=2, label="temporal retina removed")
cx.set_xlabel("Tectal position x")
cx.set_ylabel("Terminals per bin")
cx.legend(frameon=False, fontsize=8, loc="upper right")
cx.set_title("C  Terminals fill the available tectum", loc="left", fontsize=10)
fig.tight_layout()
