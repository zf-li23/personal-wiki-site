import numpy as np
import matplotlib.pyplot as plt

# Molar Gibbs energy (chemical potential) of pure water phases versus T, built from
# S_m and C_p,m (CRC data, taken constant within each phase); zero at the melting point.
R = 8.314
Tm, Tb = 273.15, 372.76  # melting point and boiling point at 1 bar
dHfus, dHvap = 6010.0, 40660.0
Cs, Cl, Cg = 38.0, 75.3, 33.6
Sl_m = 63.3  # S_m(l) at Tm, J/(K mol)
Ss_m = Sl_m - dHfus / Tm


def mu(T, T0, mu0, S0, Cp):
    return mu0 - S0 * (T - T0) - Cp * (T * np.log(T / T0) - (T - T0))


mu_l_b = mu(Tb, Tm, 0.0, Sl_m, Cl)
Sl_b = Sl_m + Cl * np.log(Tb / Tm)
Sg_b = Sl_b + dHvap / Tb

T = np.linspace(230, 480, 500)
mus = mu(T, Tm, 0.0, Ss_m, Cs)
mul = mu(T, Tm, 0.0, Sl_m, Cl)
mug = mu(T, Tb, mu_l_b, Sg_b, Cg)
mug10 = mug + R * T * np.log(10.0)  # 10 bar, ideal vapour; condensed phases barely shift

fig, ax = plt.subplots(figsize=(8, 5.2))
ax.plot(T, mus / 1e3, color="#2563eb", lw=2, label="solid (ice)")
ax.plot(T, mul / 1e3, color="#16a34a", lw=2, label="liquid")
ax.plot(T, mug / 1e3, color="#dc2626", lw=2, label="gas, 1 bar")
ax.plot(T, mug10 / 1e3, color="#dc2626", lw=1.5, ls="--", label="gas, 10 bar")
for Tx, lab in [(Tm, "$T_\\mathrm{fus}$"), (Tb, "$T_\\mathrm{b}$ (1 bar)")]:
    ax.axvline(Tx, color="#94a3b8", lw=0.8, ls=":")
    ax.annotate(lab, (Tx, -29), textcoords="offset points", xytext=(4, 0), fontsize=9)
hot = T > 380
i10 = np.where(hot)[0][np.argmin(np.abs((mug10 - mul)[hot]))]
ax.plot([T[i10]], [mul[i10] / 1e3], "o", color="#dc2626")
ax.annotate(f"$T_\\mathrm{{b}}$ (10 bar) $\\approx$ {T[i10]:.0f} K", (T[i10], mul[i10] / 1e3),
            textcoords="offset points", xytext=(-150, -6), fontsize=9, color="#dc2626")
ax.set_xlim(230, 480)
ax.set_ylim(-30, 4)
ax.set_xlabel("$T$ / K")
ax.set_ylabel(r"$\mu^*$ / (kJ mol$^{-1}$), zero at the melting point")
ax.set_title(r"Slopes $(\partial\mu^*/\partial T)_p = -S_\mathrm{m}$: the stable phase has the lowest $\mu^*$", fontsize=11)
ax.legend(fontsize=9, loc="lower left")
ax.grid(alpha=0.3)
fig.tight_layout()
