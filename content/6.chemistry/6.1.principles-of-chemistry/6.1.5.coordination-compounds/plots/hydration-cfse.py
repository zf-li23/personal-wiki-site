import numpy as np
import matplotlib.pyplot as plt

# Hydration enthalpies of M2+(g) (kJ/mol, approximate textbook values) and Delta_o of [M(H2O)6]2+ (cm^-1).
ions = ["Ca", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
d = np.array([0, 3, 4, 5, 6, 7, 8, 9, 10])
dh = -np.array([1579, 1918, 1904, 1841, 1946, 1996, 2105, 2100, 2046], dtype=float)
delta_o = np.array([0, 12600, 14000, 7800, 10400, 9300, 8500, 12600, 0], dtype=float)

weak = np.array([0, -0.4, -0.8, -1.2, -0.6, 0, -0.4, -0.8, -1.2, -0.6, 0])  # CFSE / Delta_o, high spin
strong = np.array([0, -0.4, -0.8, -1.2, -1.6, -2.0, -2.4, -1.8, -1.2, -0.6, 0])  # orbital term only, low spin
cfse = weak[d] * delta_o / 83.59  # kJ/mol

# Smooth baseline through the three ions with zero CFSE (d0, d5, d10).
coef = np.polyfit([0, 5, 10], dh[[0, 3, 8]], 2)
n = np.linspace(0, 10, 200)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))
a1.plot(n, np.polyval(coef, n), color="#94a3b8", lw=1.2, ls="--", label="baseline through d$^0$, d$^5$, d$^{10}$")
a1.plot(d, dh, "o-", color="#2563eb", lw=1.6, label=r"measured $\Delta_{hyd}H$")
a1.plot(d, dh - cfse, "s", color="#dc2626", ms=6, label=r"$\Delta_{hyd}H$ $-$ CFSE")
a1.set_xticks(d)
a1.set_xticklabels([f"{m}$^{{2+}}$\nd$^{{{k}}}$" for m, k in zip(ions, d)], fontsize=9)
a1.set_ylabel(r"$\Delta_{hyd}H$ / (kJ mol$^{-1}$)")
a1.set_title(r"M$^{2+}$(g) + 6 H$_2$O $\to$ [M(H$_2$O)$_6$]$^{2+}$(aq)", fontsize=11)
a1.legend(fontsize=9, loc="upper right")
a1.grid(alpha=0.3)

k = np.arange(11)
a2.plot(k, weak, "o-", color="#2563eb", label="weak field (high spin)")
a2.plot(k, strong, "s--", color="#d97706", label="strong field (low spin, pairing energy not included)")
a2.set_xticks(k)
a2.set_xticklabels([f"d$^{{{i}}}$" for i in k])
a2.set_ylabel(r"CFSE / $\Delta_o$")
a2.set_title("Octahedral crystal field stabilization energy", fontsize=11)
a2.legend(fontsize=9, loc="lower left")
a2.grid(alpha=0.3)
fig.tight_layout()
