import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Cp,m = a + bT + c/T^2 (J K^-1 mol^-1), standard fits valid roughly 298-2000 K.
CP = {
    "CO2": (44.22, 8.79e-3, -8.62e5),
    "H2O": (30.54, 10.29e-3, 0.0),
    "N2": (28.58, 3.77e-3, -0.50e5),
    "O2": (29.96, 4.18e-3, -1.67e5),
}
T0 = 298.15
DH_C = -802.5e3  # CH4(g) + 2 O2(g) -> CO2(g) + 2 H2O(g), J/mol


def dh(species, t):
    a, b, c = CP[species]
    return a * (t - T0) + b / 2 * (t**2 - T0**2) - c * (1 / t - 1 / T0)


def flame_t(excess, n2_per_o2=79 / 21):
    n_o2 = 2 * excess
    products = {"CO2": 1, "H2O": 2, "O2": n_o2 - 2, "N2": n_o2 * n2_per_o2}
    return brentq(lambda t: DH_C + sum(n * dh(s, t) for s, n in products.items()), 300, 8000)


lam = np.linspace(1.0, 3.0, 81)
t_air = np.array([flame_t(x) for x in lam])
fig, ax = plt.subplots(figsize=(7.2, 4.5))
ax.plot(lam, t_air, color="#dc2626", lw=2)
ax.plot([1], [t_air[0]], "o", color="#dc2626")
ax.annotate(f"stoichiometric air: {t_air[0]:.0f} K", (1, t_air[0]), xytext=(1.35, 2250), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#94a3b8"))
ax.axhline(2225, color="#94a3b8", lw=0.8, ls="--")
ax.text(2.95, 2240, "with dissociation: about 2225 K", ha="right", fontsize=8.5)
ax.set_xlabel(r"air supplied / stoichiometric air, $\lambda$")
ax.set_ylabel(r"adiabatic flame temperature / K")
ax.set_title("Methane burning in air at constant pressure (no dissociation, reactants at 298.15 K)", fontsize=10)
ax.grid(alpha=0.3)
fig.tight_layout()
