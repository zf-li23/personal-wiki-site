import numpy as np
import matplotlib.pyplot as plt

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))

# Left: the four sign combinations of Delta H and Delta S (schematic, Delta G = Delta H - T Delta S).
T = np.linspace(0, 1000, 200)
cases = [
    (-60, 0.08, "#16a34a", r"$\Delta H<0,\ \Delta S>0$: always"),
    (60, -0.08, "#dc2626", r"$\Delta H>0,\ \Delta S<0$: never"),
    (-80, -0.16, "#2563eb", r"$\Delta H<0,\ \Delta S<0$: low $T$"),
    (80, 0.12, "#d97706", r"$\Delta H>0,\ \Delta S>0$: high $T$"),
]
for dh, ds, c, label in cases:
    a1.plot(T, dh - T * ds, color=c, lw=2, label=label)
    if dh * ds > 0:
        a1.plot([dh / ds], [0], "o", color=c)
a1.axhline(0, color="#94a3b8", lw=1)
a1.set_xlabel("T (arbitrary units)")
a1.set_ylabel(r"$\Delta G$ (arbitrary units)")
a1.set_title("Four combinations (spontaneous where $\\Delta G<0$)", fontsize=11)
a1.legend(fontsize=9, loc="lower left")
a1.set_ylim(-150, 150)
a1.grid(alpha=0.3)

# Right: two real reactions with Delta G(T) = Delta H(298) - T Delta S(298).
T = np.linspace(200, 1400, 300)
reactions = [
    (-91.8, -0.1981, "#2563eb", r"N$_2$ + 3H$_2$ $\to$ 2NH$_3$"),
    (179.2, 0.1602, "#d97706", r"CaCO$_3$ $\to$ CaO + CO$_2$"),
]
for dh, ds, c, label in reactions:
    a2.plot(T, dh - T * ds, color=c, lw=2, label=label)
    t0 = dh / ds
    a2.plot([t0], [0], "o", color=c)
    a2.annotate(f"{t0:.0f} K", (t0, 0), textcoords="offset points", xytext=(6, 8 if ds < 0 else -16), fontsize=9, color=c)
a2.axhline(0, color="#94a3b8", lw=1)
a2.axvline(298.15, color="#94a3b8", lw=0.8, ls=":")
a2.set_xlabel("T / K")
a2.set_ylabel(r"$\Delta_r G^\circ_m$ / (kJ mol$^{-1}$)")
a2.set_title("Linear approximation, Eq. (6.4)", fontsize=11)
a2.legend(fontsize=9, loc="upper right")
a2.grid(alpha=0.3)
fig.tight_layout()
