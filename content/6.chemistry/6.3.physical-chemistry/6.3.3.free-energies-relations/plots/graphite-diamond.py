import numpy as np
import matplotlib.pyplot as plt

# C(graphite) -> C(diamond), 298.15 K data (CRC): dG = 2.900 kJ/mol, S(graphite) = 5.74, S(diamond) = 2.38 J/(K mol).
M = 12.011e-3
dV = M * (1 / 3513 - 1 / 2260)  # m^3/mol, taken independent of T and p
dG0, dS = 2900.0, 2.38 - 5.74
p0 = 1e5

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.6))
p = np.linspace(0, 2.5e9, 200)
dG = dG0 + dV * (p - p0)
p_eq = p0 - dG0 / dV
a1.plot(p / 1e9, dG / 1e3, color="#2563eb", lw=2)
a1.axhline(0, color="#94a3b8", lw=1)
a1.plot([p_eq / 1e9], [0], "o", color="#dc2626")
a1.annotate(f"{p_eq / 1e9:.2f} GPa", (p_eq / 1e9, 0), textcoords="offset points", xytext=(8, 8),
            fontsize=10, color="#dc2626")
a1.text(0.15, -1.2, "diamond stable", fontsize=10, color="#16a34a")
a1.text(1.6, 2.2, "graphite stable", fontsize=10, color="#64748b")
a1.set_xlabel("$p$ / GPa")
a1.set_ylabel(r"$\Delta_\mathrm{trs}G_\mathrm{m}$ / (kJ mol$^{-1}$)")
a1.set_title("298.15 K: $\\Delta G(p) = \\Delta G^\\circ + \\Delta V\\,(p - p^\\circ)$", fontsize=11)
a1.grid(alpha=0.3)

T = np.linspace(0, 3000, 300)
dGT = dG0 - dS * (T - 298.15)  # constant dH and dS
p_line = p0 - dGT / dV
a2.plot(T, p_line / 1e9, color="#2563eb", lw=2, label="constant $\\Delta S$, $\\Delta V$ (this text)")
Tb = np.linspace(1200, 3000, 50)
a2.plot(Tb, (7.1 + 0.027 * Tb) / 10, color="#d97706", lw=1.5, ls="--", label="Berman-Simon line (experiment)")
a2.fill_between([1600, 2100], 5.0, 6.5, color="#16a34a", alpha=0.2, label="HPHT synthesis (metal solvent)")
a2.text(200, 7.0, "diamond", fontsize=11)
a2.text(2000, 1.2, "graphite", fontsize=11)
a2.set_xlim(0, 3000)
a2.set_ylim(0, 9)
a2.set_xlabel("$T$ / K")
a2.set_ylabel("$p$ / GPa")
a2.set_title("Graphite-diamond equilibrium line", fontsize=11)
a2.legend(fontsize=9, loc="upper left")
a2.grid(alpha=0.3)
fig.tight_layout()
