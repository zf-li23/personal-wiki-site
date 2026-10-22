import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator
from scipy.integrate import cumulative_trapezoid

# Approximate heat capacity of ice Ih (J K^-1 mol^-1), rescaled below so that the
# calorimetric entropy of ice at 273.15 K equals 38.1 J K^-1 mol^-1 (Giauque and Stout, 1936).
T_ICE = np.array([10, 15, 20, 30, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 273.15])
C_ICE = np.array([0.29, 0.9, 2.1, 4.6, 6.9, 10.7, 13.4, 15.7, 17.9, 20.0, 22.1, 24.1, 26.2, 28.4, 30.8, 33.6, 35.6])
_t = np.linspace(10, 273.15, 4000)
_s = C_ICE[0] / 3 + np.trapezoid(PchipInterpolator(T_ICE, C_ICE)(_t) / _t, _t)
C_ICE = C_ICE * 38.1 / _s
T_FUS, T_B, T_END = 273.15, 373.12, 423.15
DH_FUS, DH_VAP = 6.01e3, 40.65e3
CP_L, CP_G = 75.3, 33.8

ice = PchipInterpolator(T_ICE, C_ICE)


def cp(t):
    if t < 10:
        return C_ICE[0] * (t / 10) ** 3  # Debye T^3 extrapolation
    if t < T_FUS:
        return float(ice(t))
    if t < T_B:
        return CP_L
    return CP_G


segments = [(0.5, T_FUS, "ice"), (T_FUS, T_B, "liquid"), (T_B, T_END, "vapour")]
colors = ["#2563eb", "#16a34a", "#d97706"]
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
s0 = 0.0
ends = []
for (lo, hi, name), c in zip(segments, colors):
    t = np.linspace(lo, hi, 400)
    y = np.array([cp(x) / x for x in t])
    s = s0 + cumulative_trapezoid(y, t, initial=0)
    if name == "ice":
        s += C_ICE[0] * (0.5 / 10) ** 3 / 3
    a1.plot(t, y, color=c, lw=2, label=name)
    a1.fill_between(t, y, color=c, alpha=0.2)
    a2.plot(t, s, color=c, lw=2)
    ends.append((hi, s[-1]))
    s0 = s[-1] + (DH_FUS / T_FUS if name == "ice" else DH_VAP / T_B if name == "liquid" else 0)
for t in (T_FUS, T_B):
    a1.axvline(t, color="#94a3b8", lw=0.8, ls="--")
    a2.axvline(t, color="#94a3b8", lw=0.8, ls="--")
summary = (
    f"ice at 273.15 K: {ends[0][1]:.1f}\n"
    + r"$\Delta_{\mathrm{fus}}H/T_{\mathrm{fus}}$" + f" = {DH_FUS / T_FUS:.1f}\n"
    + f"liquid at 373.12 K: {ends[1][1]:.1f}\n"
    + r"$\Delta_{\mathrm{vap}}H/T_{\mathrm{b}}$" + f" = {DH_VAP / T_B:.1f}\n"
    + f"vapour at 423.15 K: {ends[2][1]:.1f}"
)
a2.text(15, 190, summary, fontsize=9, va="top", bbox=dict(boxstyle="round", fc="none", ec="#94a3b8"))
a1.set_ylabel(r"$C_{p,\mathrm{m}}/T$ / (J mol$^{-1}$ K$^{-2}$)")
a1.set_ylim(0, 0.45)
a1.legend(fontsize=9, loc="upper right")
a1.set_title("Calorimetric entropy of water from 0 K to 423 K at about 1 atm (approximate data)", fontsize=11)
a2.set_xlabel(r"$T$ / K")
a2.set_ylabel(r"$S_{\mathrm{m}}$ / (J mol$^{-1}$ K$^{-1}$)")
a2.set_xlim(0, T_END + 5)
a1.grid(alpha=0.3)
a2.grid(alpha=0.3)
fig.tight_layout()
