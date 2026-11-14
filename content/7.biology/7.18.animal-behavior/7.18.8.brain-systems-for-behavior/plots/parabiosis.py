"""Feedback model of Coleman's parabiosis experiments (Example 8.2.1; arbitrary units).

dL_i/dt = s_i F_i - c L_i + q (L_j - L_i)
dF_i/dt = eta (Imax / (1 + rho_i (L_i/K)^n) - E0 - k F_i),  F_i >= 0
ob/ob: s = 0; db/db: rho = 0.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c, Imax, E0, k, K, n, eta = 1.0, 3.0, 0.5, 0.1, 5.0, 4, 0.5
geno = {"normal": (1.0, 1.0), "ob/ob": (0.0, 1.0), "db/db": (1.0, 0.0)}
tok = {"normal": "positive", "ob/ob": "drug", "db/db": "dna"}


def run(g1, g2, q, F0, T=80.0, dt=0.01):
    s = np.array([geno[g1][0], geno[g2][0]]); rho = np.array([geno[g1][1], geno[g2][1]])
    F = np.array(F0, float); L = s * F / c
    out = []
    for _ in range(int(T / dt)):
        dL = s * F - c * L + q * (L[::-1] - L)
        I = Imax / (1 + rho * (L / K) ** n)
        dF = eta * (I - E0 - k * F)
        L = L + dt * dL; F = np.maximum(F + dt * dF, 0.0)
        out.append(F.copy())
    return np.arange(len(out)) * dt, np.array(out)


def steady(g):
    _, f = run(g, g, 0.0, [10.0, 10.0], T=200)
    return f[-1, 0]


pairs = [("normal", "normal"), ("ob/ob", "normal"), ("db/db", "normal"), ("ob/ob", "db/db")]
fig, axs = plt.subplots(1, 4, figsize=(12, 3.3), sharey=True)
for ax, (g1, g2), letter in zip(axs, pairs, "ABCD"):
    t, F = run(g1, g2, 1.0, [steady(g1), steady(g2)])
    ls = ["-", "--"] if g1 == g2 else ["-", "-"]
    ax.plot(t, F[:, 0], color=P.edge(tok[g1]), lw=2, ls=ls[0], label=g1 + (" (1)" if g1 == g2 else ""))
    ax.plot(t, F[:, 1], color=P.edge(tok[g2]), lw=2, ls=ls[1], label=g2 + (" (2)" if g1 == g2 else ""))
    ax.set_title(f"{letter}  {g1} + {g2}", loc="left", fontsize=10)
    ax.set_xlabel("Days after joining")
    ax.set_ylim(0, 28)
    ax.legend(frameon=False, fontsize=8)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
axs[0].set_ylabel("Fat mass (a.u.)")
fig.tight_layout()
