# Ligand binding as statistical mechanics.
# A, B: occupancy p_b = c^n / (c^n + K^n) for a simple binding site (n = 1) and for all-or-none binding of n = 2
#    and n = 4 ligands (Hill functions with the same half-saturation concentration K), on linear and
#    logarithmic concentration axes. Dotted guides in B mark 10 % and 90 % occupancy: c must change by 81-fold
#    for n = 1, 9-fold for n = 2 and 3-fold for n = 4.
# C: the lattice model with Omega sites and L ligands, one receptor: exact occupancy
#    p_b = x / (1 + x) with x = L exp(-beta d_eps) / (Omega - L + 1) (points), against the dilute-solution
#    result p_b = c / (c + Kd), c = L / Omega, Kd = exp(beta d_eps) (line), for d_eps = -2 kBT and Omega = 1000;
#    the two agree while L << Omega and part company as the lattice fills.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.7))
toks = {1: "dna", 2: "protein", 4: "negative"}

ax = axs[0]
c = np.linspace(0, 5, 400)
for n, tok in toks.items():
    ax.plot(c, c ** n / (c ** n + 1), color=charts.line(tok), lw=1.8, label=f"n = {n}")
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.02)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "c / K", "occupancy p_b")
ax.set_title("A   Linear axis", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
c = np.logspace(-3, 3, 400)
for n, tok in toks.items():
    ax.semilogx(c, c ** n / (c ** n + 1), color=charts.line(tok), lw=1.8, label=f"n = {n}")
for y in (0.1, 0.9):
    ax.axhline(y, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(1e-3, 1e3)
ax.set_ylim(0, 1.02)
charts.style_axes(ax, "c / K", "occupancy p_b")
ax.set_title("B   Logarithmic axis", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
omega, de = 1000, -2.0
L = np.unique(np.logspace(0, np.log10(900), 30).astype(int))
x = L * np.exp(-de) / (omega - L + 1)
ax.semilogx(L / omega, x / (1 + x), "o", color=charts.line("protein"), ms=4, label="exact lattice model")
cc = np.logspace(-3.2, 0, 300)
kd = np.exp(de)
ax.semilogx(cc, cc / (cc + kd), color=charts.line("neutral"), lw=1.6, label="c / (c + K_d)")
ax.axvline(kd, color=P.muted(), lw=0.7, ls=":")
ax.text(kd / 1.2, 0.9, "K_d = e^(βΔε)", fontsize=7, color=P.muted(), ha="right")
ax.set_ylim(0, 1.02)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "ligand concentration c = L/Ω", "occupancy p_b")
ax.set_title("C   Lattice model, Δε = −2 kBT", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
