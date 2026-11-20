"""Dissolved oxygen: solubility and the diel cycle of a productive pond.

A: air-saturated O2 concentration from the Garcia & Gordon (1992) fit to the Benson & Krause data (mL/L, converted
with 1.429 mg/mL), for salinity 0, 17.5 and 35 at sea level, and for fresh water at 2000 and 4000 m (pressure from
the standard atmosphere, corrected for water vapour).
B: a one-box pond model dC/dt = P(t) - R + k (C_s - C) with daylight photosynthesis
P(t) = P_max sin(pi (t - 6) / 12) for 6 < t < 18 h, constant respiration R and re-aeration rate k = 0.08 per h,
at 25 C (C_s = 8.26 mg/L). Two ponds: moderate (P_max 1.2, R 0.6 mg/L/h) and eutrophic (P_max 2.4, R 1.0).
Run for 5 days from saturation; the last day is shown.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio

P = bio.P

A = [2.00907, 3.22014, 4.05010, 4.94457, -0.256847, 3.88767]
B = [-6.24523e-3, -7.37614e-3, -1.03410e-2, -8.17083e-3]
C0 = -4.88682e-7


def o2_sat(t, s):
    """Air-saturated O2 in mg/L at 1 atm (Garcia and Gordon 1992, Benson-Krause coefficients)."""
    ts = np.log((298.15 - t) / (273.15 + t))
    ln_c = sum(a * ts ** i for i, a in enumerate(A)) + s * sum(b * ts ** i for i, b in enumerate(B)) + C0 * s * s
    return np.exp(ln_c) * 1.429


def pressure(z):
    """Standard-atmosphere pressure in kPa at altitude z (m)."""
    return 101.325 * (1 - 2.25577e-5 * z) ** 5.25588


def vapour(t):
    return 0.61078 * np.exp(17.27 * t / (t + 237.3))


fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.6))
t = np.linspace(0, 35, 200)
for s, tok, lab in ((0, "dna", "fresh water, sea level"), (17.5, "highlight", "brackish (S = 17.5)"),
                    (35, "plant", "sea water (S = 35)")):
    ax.plot(t, o2_sat(t, s), color=P.edge(tok), lw=2.0, label=lab)
for z, ls in ((2000, "--"), (4000, ":")):
    f = (pressure(z) - vapour(t)) / (101.325 - vapour(t))
    ax.plot(t, o2_sat(t, 0) * f, color=P.edge("dna"), lw=1.5, ls=ls, label=f"fresh water, {z} m")
ax.set_xlim(0, 35)
ax.set_ylim(0, 15.5)
ax.set_xlabel("water temperature / $^\\circ$C")
ax.set_ylabel("air-saturated O$_2$ / (mg L$^{-1}$)")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Solubility falls with temperature, salinity and altitude", loc="left", fontsize=10)

cs = o2_sat(25.0, 0)


def light(h):
    h = h % 24
    return np.where((h > 6) & (h < 18), np.sin(np.pi * (h - 6) / 12), 0.0)


for pmax, r, tok, lab in ((1.2, 0.6, "positive", "moderate pond"), (2.4, 1.0, "negative", "eutrophic pond")):
    sol = solve_ivp(lambda tt, c: pmax * light(tt) - r + 0.08 * (cs - c), (0, 120), [cs], max_step=0.05,
                    dense_output=True)
    hh = np.linspace(96, 120, 400)
    c = np.maximum(sol.sol(hh)[0], 0.0)
    bx.plot(hh - 96, c, color=P.edge(tok), lw=2.0, label=lab)
bx.axhline(cs, color=P.muted(), lw=1.0, ls="--")
bx.text(0.3, cs + 0.3, "saturation", fontsize=8, color=P.muted())
bx.axhspan(0, 2.0, color=P.fill("negative"), alpha=0.3, lw=0, zorder=0.6)
bx.text(12, 1.0, "hypoxic (< 2 mg L$^{-1}$)", fontsize=8, color=P.edge("negative"), ha="center", va="center")
bx.axvspan(0, 6, color=P.fill("neutral"), alpha=0.3, lw=0)
bx.axvspan(18, 24, color=P.fill("neutral"), alpha=0.3, lw=0)
bx.set_xlim(0, 24)
bx.set_ylim(0, 14)
bx.set_xticks([0, 6, 12, 18, 24])
bx.set_xlabel("time of day / h (gray: night)")
bx.set_ylabel("dissolved O$_2$ / (mg L$^{-1}$)")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Diel cycle: supersaturation by day, crash before dawn", loc="left", fontsize=10)
for a in (ax, bx):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
