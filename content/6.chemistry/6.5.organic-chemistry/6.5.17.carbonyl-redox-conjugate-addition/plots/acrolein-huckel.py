"""Hueckel pi orbitals of acrolein, CH2=CH-CH=O (atoms numbered O, C1, C2, C3 from oxygen). Oxygen is
given the Coulomb integral alpha + beta (h_O = 1) and the C=O resonance integral beta (k = 1); the
carbons have alpha and beta. Energies are E = alpha + x beta with x the eigenvalues of the
connectivity matrix (beta < 0, so larger x is lower in energy). Left: the four levels with the four
pi electrons. Right: the LUMO coefficients: largest on the beta carbon C3, then on C1."""

import matplotlib.pyplot as plt
import numpy as np

H = np.array([[1.0, 1.0, 0.0, 0.0],
              [1.0, 0.0, 1.0, 0.0],
              [0.0, 1.0, 0.0, 1.0],
              [0.0, 0.0, 1.0, 0.0]])
x, c = np.linalg.eigh(H)
order = np.argsort(-x)  # lowest energy first
x, c = x[order], c[:, order]
lumo = c[:, 2] * np.sign(c[3, 2])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 3.6), gridspec_kw={"width_ratios": [1, 1.3]})
for i, xi in enumerate(x):
    e = -xi
    ax1.hlines(e, 0.2, 0.8, lw=2.2, color="C0" if i < 2 else "C3")
    if i < 2:
        ax1.text(0.5, e + 0.12, r"$\uparrow\downarrow$", ha="center", va="bottom", fontsize=12)
    ax1.text(0.85, e, rf"$\alpha {'+' if xi >= 0 else '-'} {abs(xi):.2f}\beta$", va="center", fontsize=10)
    ax1.text(0.15, e, ["$\\pi_1$", "$\\pi_2$ (HOMO)", "$\\pi_3$ (LUMO)", "$\\pi_4$"][i], va="center", ha="right", fontsize=10)
ax1.set_xlim(-0.55, 1.45)
ax1.set_ylim(-2.4, 2.2)
ax1.set_ylabel(r"energy (units of $|\beta|$, relative to $\alpha$)")
ax1.set_xticks([])
for side in ("top", "right", "bottom"):
    ax1.spines[side].set_visible(False)

names = ["O", "C1", "C2", r"C3 ($\beta$)"]
ax2.bar(names, lumo, color=["C3" if v > 0 else "C0" for v in lumo], width=0.6)
for i, v in enumerate(lumo):
    ax2.text(i, v + (0.03 if v >= 0 else -0.03), f"{v:+.2f}", ha="center", va="bottom" if v >= 0 else "top", fontsize=10)
ax2.axhline(0, lw=0.8, color="0.5")
ax2.set_ylabel("LUMO coefficient")
ax2.set_ylim(-0.8, 0.85)
ax2.set_title("LUMO of acrolein", fontsize=11)
fig.tight_layout()
