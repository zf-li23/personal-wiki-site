import numpy as np
import matplotlib.pyplot as plt

# H2O(l) -> H2O(s) at 100 kPa and temperature T, data near 273 K.
T_FUS, DH_FUS = 273.15, 6.01e3
CP_L, CP_S = 75.3, 37.6
T = np.linspace(250, 290, 300)
dH = -DH_FUS + (CP_S - CP_L) * (T - T_FUS)
dS_sys = -DH_FUS / T_FUS + (CP_S - CP_L) * np.log(T / T_FUS)
dS_sur = -dH / T
dS_tot = dS_sys + dS_sur

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2))
a1.plot(T, dS_sys, color="#2563eb", lw=2, label=r"$\Delta S_{\mathrm{sys}}$")
a1.plot(T, dS_sur, color="#d97706", lw=2, label=r"$\Delta S_{\mathrm{sur}} = -\Delta H/T$")
a1.set_xlabel(r"$T$ / K")
a1.set_ylabel(r"entropy change / (J K$^{-1}$ mol$^{-1}$)")
a1.set_title("Freezing of 1 mol of water: system and surroundings", fontsize=10.5)
a1.legend(fontsize=9)
a1.grid(alpha=0.3)
a2.plot(T, dS_tot, color="#16a34a", lw=2)
a2.axhline(0, color="#94a3b8", lw=0.8)
a2.axvline(T_FUS, color="#94a3b8", lw=0.8, ls="--")
a2.plot([263.15], [np.interp(263.15, T, dS_tot)], "o", color="#16a34a")
a2.annotate("263.15 K: +0.81", (263.15, np.interp(263.15, T, dS_tot)), xytext=(251, -0.9), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#94a3b8"))
a2.text(263, 1.3, "freezing spontaneous", fontsize=9)
a2.text(274, 0.3, "melting spontaneous", fontsize=9)
a2.set_xlabel(r"$T$ / K")
a2.set_ylabel(r"$\Delta S_{\mathrm{sys}} + \Delta S_{\mathrm{sur}}$ / (J K$^{-1}$ mol$^{-1}$)")
a2.set_title("Total entropy change changes sign at 273.15 K", fontsize=10.5)
a2.grid(alpha=0.3)
fig.tight_layout()
