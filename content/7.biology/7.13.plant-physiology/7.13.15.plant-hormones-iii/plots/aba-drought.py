# Leaf ABA and stomata during soil drying and rewatering (schematic model), and the Tardieu-Davies
# model of stomatal conductance: gs = gmin + (gmax - gmin) exp(-beta [ABA]xyl exp(-delta Psi_leaf)).
import matplotlib.pyplot as plt
import numpy as np

# A: time course. Leaf water potential falls during drying (days 0-6), recovers after rewatering.
t = np.linspace(0, 9, 900)
dt = t[1] - t[0]
psi = np.where(t < 6, -0.45 - 0.9 * (1 - np.exp(-t / 3.0)) * (t / 6) ** 1.5, 0)
psi6 = psi[t < 6][-1]
psi = np.where(t >= 6, -0.45 + (psi6 + 0.45) * np.exp(-(t - 6) / 0.35), psi)
# ABA synthesis rises exponentially as Psi falls below a threshold; first-order clearance (k = 0.69 h^-1).
k = 0.69 * 24          # d^-1
s = k * 1.0 * np.exp(np.clip(-(psi + 0.7) / 0.11, 0, 4))
aba = np.empty_like(t)
aba[0] = 1.0
for i in range(1, len(t)):
    aba[i] = aba[i - 1] + dt * (s[i - 1] - k * aba[i - 1])
gs = 0.03 + 0.37 * np.exp(-0.035 * aba * np.exp(-1.0 * psi))
rs = 1 / gs

fig = plt.figure(figsize=(11.2, 4.6))
gsa = fig.add_gridspec(3, 2, width_ratios=[1.15, 1], hspace=0.12, wspace=0.32)
axs = [fig.add_subplot(gsa[i, 0]) for i in range(3)]
for a in axs[1:]:
    a.sharex(axs[0])
axs[0].plot(t, psi, color="#2f6fb5", lw=2)
axs[0].set_ylabel("Ψleaf / MPa", fontsize=8.5)
axs[1].plot(t, aba, color="#c0504d", lw=2)
axs[1].set_ylabel("Leaf ABA\n(fold of control)", fontsize=8.5)
axs[2].plot(t, rs, color="#4f9a52", lw=2)
axs[2].set_ylabel("Stomatal\nresistance / (m² s mol⁻¹)", fontsize=8.5)
axs[2].set_xlabel("Time / d")
for a in axs:
    a.axvline(6, color="0.5", lw=0.8, ls="--")
    a.spines[["top", "right"]].set_visible(False)
    a.tick_params(labelsize=8)
for a in axs[:2]:
    plt.setp(a.get_xticklabels(), visible=False)
axs[0].text(6.1, -0.6, "rewatered", fontsize=8)
axs[0].text(0.05, 0.85, "A", transform=axs[0].transAxes, fontsize=12, fontweight="bold")

# B: Tardieu-Davies surface
b = fig.add_subplot(gsa[:, 1])
c = np.logspace(-3, 1, 300)    # umol L^-1
for pl, col in ((-0.4, "#2f6fb5"), (-0.8, "#d08a2c"), (-1.2, "#c0504d")):
    g = 0.03 + 0.37 * np.exp(-1.2 * c * np.exp(-1.0 * pl))
    b.plot(c, g, color=col, lw=2.2, label=f"Ψleaf = {pl} MPa")
b.set_xscale("log")
b.set_xlabel("[ABA] in xylem sap / (µmol L⁻¹)")
b.set_ylabel("gs / (mol m⁻² s⁻¹)")
b.set_ylim(0, 0.45)
b.legend(frameon=False, fontsize=8.5, loc="lower left")
b.spines[["top", "right"]].set_visible(False)
b.text(0.03, 0.95, "B", transform=b.transAxes, fontsize=12, fontweight="bold")
