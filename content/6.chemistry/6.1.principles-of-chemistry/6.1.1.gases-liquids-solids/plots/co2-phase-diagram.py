"""Schematic phase diagram of CO2 with a logarithmic pressure axis."""

import numpy as np
import matplotlib.pyplot as plt

R = 8.314462618
Tt, pt = 216.59, 518.0      # triple point (K, kPa)
Tc, pc = 304.13, 7377.0     # critical point (K, kPa)
Ts, ps = 194.65, 101.325    # sublimation point at 1 atm

# Clausius-Clapeyron lines through the reference points
Hvap = R * np.log(pc / pt) / (1 / Tt - 1 / Tc)
Hsub = R * np.log(pt / ps) / (1 / Ts - 1 / Tt)


def cc(T, T1, p1, H):
    return p1 * np.exp(-H / R * (1 / T - 1 / T1))


T_sub = np.linspace(170, Tt, 200)
T_vap = np.linspace(Tt, Tc, 200)
p_fus = np.logspace(np.log10(pt), 5, 200)
T_fus = Tt * (1 + (p_fus - pt) / 4.0e5) ** (1 / 2.6)  # Simon-Glatzel melting curve

fig, ax = plt.subplots(figsize=(7.0, 4.8))
ax.plot(T_sub, cc(T_sub, Tt, pt, Hsub), color="C0", lw=1.8)
ax.plot(T_vap, cc(T_vap, Tt, pt, Hvap), color="C0", lw=1.8)
ax.plot(T_fus, p_fus, color="C0", lw=1.8)
ax.set_yscale("log")
ax.set_xlim(170, 340)
ax.set_ylim(20, 1e5)

# supercritical region
ax.fill_between([Tc, 340], pc, 1e5, color="C2", alpha=0.15, lw=0)
ax.text(318, 2.5e4, "supercritical\nfluid", ha="center", fontsize=9)

ax.plot([Tt], [pt], "o", color="C3")
ax.annotate("triple point\n216.6 K, 518 kPa", (Tt, pt), xytext=(228, 150), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.plot([Tc], [pc], "o", color="C3")
ax.annotate("critical point\n304.1 K, 7.38 MPa", (Tc, pc), xytext=(268, 2.2e4), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.axhline(101.325, color="0.55", lw=0.9, ls="--")
ax.plot([Ts], [ps], "s", color="C1", ms=5)
ax.text(172, 112, "101.325 kPa", fontsize=8)
ax.annotate("sublimes at\n194.7 K", (Ts, ps), xytext=(178, 30), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))

ax.text(185, 3000, "solid", fontsize=12)
ax.text(262, 4000, "liquid", fontsize=12)
ax.text(285, 300, "gas", fontsize=12)

ax.set_xlabel(r"$T\,/\,\mathrm{K}$")
ax.set_ylabel(r"$p\,/\,\mathrm{kPa}$")
fig.tight_layout()
