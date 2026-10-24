"""Racemization L <-> D as two opposing first-order reactions with equal rate constants k:
ee(t) = exp(-2kt), D/L = (1 - ee)/(1 + ee), so ln[(1 + D/L)/(1 - D/L)] = 2kt. Half-racemization
(ee = 1/2) is reached at D/L = 1/3. For comparison, the epimerization of L-isoleucine to
D-alloisoleucine (equilibrium ratio about 1.3) with the same forward rate constant."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 400)  # in units of 1/k
ee = np.exp(-2 * t)
DL = (1 - ee) / (1 + ee)
K = 1.3  # [allo]/[Ile] at equilibrium
kf, kb = 1.0, 1.0 / K
Ile = (kb + kf * np.exp(-(kf + kb) * t)) / (kf + kb)
allo = 1 - Ile

fig, axs = plt.subplots(1, 2, figsize=(10, 3.7))
axs[0].plot(t, DL, color="C0", lw=2, label="D/L (racemization)")
axs[0].plot(t, allo / Ile, color="C1", lw=2, ls="--", label="D-allo-Ile / L-Ile (epimerization)")
t_half = np.log(2) / 2
axs[0].plot([t_half, t_half], [0, 1 / 3], color="0.6", ls=":")
axs[0].plot([0, t_half], [1 / 3, 1 / 3], color="0.6", ls=":")
axs[0].text(t_half + 0.05, 0.25, "D/L = 1/3\nhalf-racemization", fontsize=8)
axs[0].set_xlabel("$kt$")
axs[0].set_ylabel("ratio")
axs[0].legend(frameon=False, fontsize=8)
axs[0].set_xlim(0, 3)
axs[0].set_ylim(0, 1.4)
axs[1].plot(t, np.log((1 + DL) / (1 - np.minimum(DL, 0.9999))), color="C0", lw=2)
axs[1].set_xlabel("$kt$")
axs[1].set_ylabel(r"$\ln\frac{1 + D/L}{1 - D/L}$")
axs[1].set_title("linear in time: slope 2k", fontsize=10)
axs[1].set_xlim(0, 3)
for ax in axs:
    ax.grid(alpha=0.3)
fig.tight_layout()
