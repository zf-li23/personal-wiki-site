"""Coalescence times under the isolation-with-migration model for two species (Eqs. (25.5)-(25.6)):
symmetric model with theta_1 = theta_2 = 0.005, theta_A = 0.003 for the ancestor and divergence time
tau = 0.005 (all in expected mutations per site), and M = N m = 0.01, 0.1, 1 or 10 migrants per
generation in each direction. The density of the divergence time t of two sequences is computed
from the transition probabilities P(t) = exp(Qt) of the five-state Markov chain of the two
lineages. A: two sequences from the same species. B: one sequence from each species; without
migration they cannot coalesce before tau (dotted), with frequent migration the two species behave
as one population."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
th, tha, tau = 0.005, 0.003, 0.005


def density(M, start, t):
    m = 4 * M / th
    c = 2 / th
    Q = np.array([[-2 * (m + 1 / th), 2 * m, 0, c, 0],
                  [m, -2 * m, m, 0, 0],
                  [0, 2 * m, -2 * (m + 1 / th), 0, c],
                  [0, 0, 0, -m, m],
                  [0, 0, 0, m, -m]])
    out = []
    Ptau = expm(Q * tau)[start]
    surv = Ptau[:3].sum()
    for x in t:
        if x < tau:
            p = expm(Q * x)[start]
            out.append(p[0] * c + p[2] * c)
        else:
            out.append(surv * 2 / tha * np.exp(-2 * (x - tau) / tha))
    return np.array(out)


t = np.linspace(1e-5, 0.012, 300)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.12)
toks = ["dna", "protein", "positive", "rna"]
for ax, start, name in ((axs[0], 0, "A  Two sequences from the same species"),
                        (axs[1], 1, "B  One sequence from each species")):
    for M, tok in zip([0.01, 0.1, 1, 10], toks):
        ax.plot(t, density(M, start, t), color=charts.line(tok), lw=1.5, label=f"$M = {M:g}$")
    ax.axvline(tau, color=P.muted(), lw=0.8, ls=":")
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
    charts.style_axes(ax, "divergence time $t$ (mutations per site)", "density" if start == 0 else None)
    charts.title(ax, name)
