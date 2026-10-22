"""Schematic comparison of a first-order transition, an Ehrenfest second-order transition
and a lambda (continuous) transition at constant pressure: molar Gibbs energy (chemical
potential), molar entropy and heat capacity against temperature. Arbitrary units."""

import numpy as np
import matplotlib.pyplot as plt

Tt = 1.0
T = np.linspace(0.6, 1.4, 801)
lo, hi = T < Tt, T >= Tt

fig, axes = plt.subplots(3, 3, figsize=(8.4, 6.6), sharex=True)
titles = ["first order", "second order (Ehrenfest)", "lambda transition"]

# first order: two phases with different entropies; mu curves cross with a kink
S1, S2 = 1.0, 2.0
mu1 = -S1 * (T - Tt) - 0.3 * (T - Tt) ** 2
mu2 = -S2 * (T - Tt) - 0.3 * (T - Tt) ** 2
ax = axes[0, 0]
ax.plot(T[lo], mu1[lo], color="C0", lw=1.8)
ax.plot(T[hi], mu1[hi], color="C0", lw=1.0, ls="--")
ax.plot(T[hi], mu2[hi], color="C1", lw=1.8)
ax.plot(T[lo], mu2[lo], color="C1", lw=1.0, ls="--")
ax.text(0.65, 0.25, r"$\alpha$", color="C0")
ax.text(1.3, -0.75, r"$\beta$", color="C1")
S = np.where(lo, S1 + 0.6 * (T - Tt), S2 + 0.6 * (T - Tt))
axes[1, 0].plot(T[lo], S[lo], color="C0", lw=1.8)
axes[1, 0].plot(T[hi], S[hi], color="C1", lw=1.8)
axes[1, 0].annotate("", (Tt, S2), (Tt, S1), arrowprops=dict(arrowstyle="<->", color="0.5"))
axes[1, 0].text(1.03, 1.45, r"$\Delta S_\mathrm{m} = \Delta H_\mathrm{m}/T$", fontsize=8)
Cp = np.where(lo, 1.0, 1.3)
axes[2, 0].plot(T[lo], Cp[lo], color="C0", lw=1.8)
axes[2, 0].plot(T[hi], Cp[hi], color="C1", lw=1.8)
axes[2, 0].annotate("", (Tt, 3.2), (Tt, 1.3), arrowprops=dict(arrowstyle="->", color="C3", lw=1.5))
axes[2, 0].text(1.03, 2.7, "latent heat\n" + r"($\delta$ peak)", fontsize=8, color="C3")

# second order: S continuous with a kink, Cp jumps
Cp2 = np.where(lo, 1.0 + 1.2 * (T - 0.6) / 0.4, 0.8)
S2c = np.cumsum(Cp2 / T) * (T[1] - T[0])
mu = -np.cumsum(S2c) * (T[1] - T[0])
axes[0, 1].plot(T, mu - mu[400], color="C2", lw=1.8)
axes[1, 1].plot(T, S2c, color="C2", lw=1.8)
axes[2, 1].plot(T[lo], Cp2[lo], color="C2", lw=1.8)
axes[2, 1].plot(T[hi], Cp2[hi], color="C2", lw=1.8)
axes[2, 1].plot([Tt, Tt], [0.8, 2.2], color="C2", lw=0.8, ls=":")
axes[2, 1].text(1.03, 1.9, r"finite jump $\Delta C_p$", fontsize=8)

# lambda: logarithmic divergence of Cp on both sides
eps = np.abs(T - Tt) + 1e-4
Cpl = np.where(lo, 1.0 - 0.45 * np.log(eps), 0.6 - 0.3 * np.log(eps))
Cpl = np.clip(Cpl, 0, 4.5)
Sl = np.cumsum(Cpl / T) * (T[1] - T[0])
mul = -np.cumsum(Sl) * (T[1] - T[0])
axes[0, 2].plot(T, mul - mul[400], color="C4", lw=1.8)
axes[1, 2].plot(T, Sl, color="C4", lw=1.8)
axes[2, 2].plot(T, Cpl, color="C4", lw=1.8)
axes[2, 2].text(1.05, 3.6, r"$C_p \to \infty$", fontsize=8)

for j in range(3):
    axes[0, j].set_title(titles[j], fontsize=10)
    for i in range(3):
        ax = axes[i, j]
        ax.axvline(Tt, color="0.7", lw=0.8, ls=":")
        ax.set_yticks([])
        ax.set_xticks([Tt])
        ax.set_xticklabels([r"$T_\mathrm{trs}$"])
axes[0, 0].set_ylabel(r"$\mu = G_\mathrm{m}$")
axes[1, 0].set_ylabel(r"$S_\mathrm{m}$")
axes[2, 0].set_ylabel(r"$C_{p,\mathrm{m}}$")
for j in range(3):
    axes[2, j].set_xlabel(r"$T$")
    axes[2, j].set_ylim(0, 4.0)
fig.tight_layout()
