"""p-n junction: band bending in equilibrium, and the current-voltage characteristic of a silicon diode."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))

# Left: equilibrium band diagram (energies in eV); the Fermi level is flat across the junction
x = np.linspace(-1, 1, 600)  # position in units of the depletion half-width
eU0 = 0.9
shift = -eU0 / 2 * np.tanh(2.5 * x)  # electron potential energy is higher on the p side
Eg = 1.12
Ec = 0.57 + shift  # p side: E_v just below E_F; n side: E_c just above E_F
Ev = Ec - Eg
ax1.plot(x, Ec, color="C0", lw=1.8, label=r"conduction band edge $E_{\mathrm{c}}$")
ax1.plot(x, Ev, color="C1", lw=1.8, label=r"valence band edge $E_{\mathrm{v}}$")
ax1.axhline(0.0, color="0.4", ls="--", lw=1.2)
ax1.text(-0.98, 0.04, r"$E_{\mathrm{F}}$", fontsize=9, color="0.4")
ax1.axvspan(-0.5, 0.5, color="0.6", alpha=0.15)
ax1.text(0, -1.25, "depletion layer", ha="center", fontsize=9)
ax1.text(-0.8, 0.8, "p", fontsize=13)
ax1.text(0.55, 0.8, "n", fontsize=13)
ax1.annotate("", xy=(0.9, Ec[-1]), xytext=(0.9, Ec[0]), arrowprops=dict(arrowstyle="<->", lw=1))
ax1.text(0.66, (Ec[0] + Ec[-1]) / 2, r"$eU_0$", fontsize=10)
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1.4, 1.6)
ax1.set_xticks([])
ax1.set_xlabel("position")
ax1.set_ylabel("electron energy / eV")
ax1.set_title("Band bending in equilibrium")
ax1.legend(fontsize=8, loc="upper center")

# Right: Shockley diode equation plus a schematic reverse breakdown
UT = 0.02585  # thermal voltage k_B T / e at 300 K, in V
Is = 1e-14  # saturation current in A
n_ideal = 1.0
U = np.linspace(-6, 0.72, 2000)
I = Is * (np.exp(U / (n_ideal * UT)) - 1)
U_br = -5.0
I = np.where(U < U_br, I - 2e-3 * (np.exp((U_br - U) / 0.08) - 1), I)
ax2.plot(U, I * 1e3, color="C3", lw=1.8)
ax2.axhline(0, color="0.4", lw=0.8)
ax2.axvline(0, color="0.4", lw=0.8)
ax2.text(0.1, 6, "forward bias", fontsize=9)
ax2.text(-3.8, 1.2, r"reverse bias: $I \approx -I_{\mathrm{s}}$ (tiny)", fontsize=9)
ax2.text(-5.9, -9, "breakdown", fontsize=9)
ax2.set_xlim(-6, 1)
ax2.set_ylim(-12, 12)
ax2.set_xlabel("U / V")
ax2.set_ylabel("I / mA")
ax2.set_title(r"$I = I_{\mathrm{s}}\,(\mathrm{e}^{eU/k_{\mathrm{B}}T} - 1)$ for a silicon diode")
fig.tight_layout()
