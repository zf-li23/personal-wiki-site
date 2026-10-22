import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Schematic substance: Debye solid (theta = 150 K) melting at 160 K, boiling at 300 K.
R = 8.314
THETA, T_FUS, T_B, T_END = 150.0, 160.0, 300.0, 400.0
DH_FUS, DH_VAP = 8.0e3, 25.0e3  # J/mol
CP_L, CP_G = 110.0, 50.0  # J/(mol K), taken constant


def debye_cv(t):
    if t <= 0:
        return 0.0
    x_max = THETA / t
    integral, _ = quad(lambda x: x**4 * np.exp(x) / np.expm1(x) ** 2, 0, x_max)
    return 9 * R * (t / THETA) ** 3 * integral


def cp(t):
    if t < T_FUS:
        return debye_cv(t)
    if t < T_B:
        return CP_L
    return CP_G


T = np.linspace(1, T_END, 800)
cp_over_t = np.array([cp(t) / t for t in T])
S = np.zeros_like(T)
for i in range(1, len(T)):
    S[i] = S[i - 1] + 0.5 * (cp_over_t[i] + cp_over_t[i - 1]) * (T[i] - T[i - 1])
    if T[i - 1] < T_FUS <= T[i]:
        S[i] += DH_FUS / T_FUS
    if T[i - 1] < T_B <= T[i]:
        S[i] += DH_VAP / T_B

fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
colors = ["#2563eb", "#16a34a", "#d97706"]
for (lo, hi), c, name in zip([(0, T_FUS), (T_FUS, T_B), (T_B, T_END)], colors, ["solid", "liquid", "gas"]):
    m = (T >= lo) & (T < hi)
    a1.plot(T[m], cp_over_t[m], color=c, lw=2, label=name)
    a1.fill_between(T[m], cp_over_t[m], color=c, alpha=0.2)
    a2.plot(T[m], S[m], color=c, lw=2)
for t, text in [(T_FUS, r"$\Delta_{fus}H/T_{fus}$"), (T_B, r"$\Delta_{vap}H/T_b$")]:
    a1.axvline(t, color="#94a3b8", lw=0.8, ls="--")
    a2.axvline(t, color="#94a3b8", lw=0.8, ls="--")
    i = np.searchsorted(T, t)
    a2.annotate(text, (t, (S[i - 1] + S[i]) / 2), textcoords="offset points", xytext=(8, 0), fontsize=10, va="center")
a1.annotate(r"Debye $T^3$ region", (12, cp(12) / 12), xytext=(40, 0.05), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#94a3b8"))
a1.set_ylabel(r"$C_{p,m}/T$ / (J mol$^{-1}$ K$^{-2}$)")
a1.legend(fontsize=9, loc="upper right")
a1.set_title("Calorimetric (third-law) entropy of a model substance (schematic)", fontsize=11)
a2.set_xlabel("T / K")
a2.set_ylabel(r"$S_m$ / (J mol$^{-1}$ K$^{-1}$)")
a1.grid(alpha=0.3)
a2.grid(alpha=0.3)
a2.set_xlim(0, T_END)
fig.tight_layout()
