"""Soil water retention curves and plant-available water.

van Genuchten (1980) curves theta(h) = theta_r + (theta_s - theta_r) / (1 + (alpha h)^n)^(1 - 1/n) with the class-mean
parameters of Carsel & Parrish (1988) for sand, sandy loam, loam, silt loam and clay (alpha in 1/cm, h = suction head in cm,
1 kPa = 10.2 cm). Field capacity taken at -33 kPa, permanent wilting point at -1500 kPa.
Top axis of A: diameter of the largest pore still water-filled at that suction, d = 4 gamma / |psi| with
gamma = 0.072 N/m (Young-Laplace for a cylindrical capillary, contact angle 0).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
SOILS = [  # name, theta_r, theta_s, alpha (1/cm), n, token
    ("sand", 0.045, 0.43, 0.145, 2.68, "metabolite"),
    ("sandy loam", 0.065, 0.41, 0.075, 1.89, "highlight"),
    ("loam", 0.078, 0.43, 0.036, 1.56, "plant"),
    ("silt loam", 0.067, 0.45, 0.020, 1.41, "dna"),
    ("clay", 0.068, 0.38, 0.008, 1.09, "rna"),
]


def theta(h, tr, ts, a, n):
    return tr + (ts - tr) / (1 + (a * h) ** n) ** (1 - 1 / n)


kpa = np.logspace(-1, 5, 400)
h = kpa * 10.2
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.8), gridspec_kw={"width_ratios": [1.5, 1]})
fc, pwp = 33.0, 1500.0
awc = []
for name, tr, ts, a, n, tok in SOILS:
    ax.plot(kpa, theta(h, tr, ts, a, n), color=P.edge(tok), lw=2.0, label=name)
    awc.append((name, theta(fc * 10.2, tr, ts, a, n), theta(pwp * 10.2, tr, ts, a, n), tok))
ax.axvspan(fc, pwp, color=P.fill("positive"), alpha=0.3, lw=0)
for v, lab in ((fc, "field capacity\n(-33 kPa)"), (pwp, "wilting point\n(-1.5 MPa)")):
    ax.axvline(v, color=P.muted(), lw=1.0, ls="--")
    ax.text(v * 1.15, 0.46, lab, fontsize=7.5, color=P.muted(), va="top")
ax.text(np.sqrt(fc * pwp), 0.015, "plant-available", fontsize=8, color=P.edge("positive"), ha="center")
ax.set_xscale("log")
ax.set_xlim(0.1, 1e5)
ax.set_ylim(0, 0.48)
ax.set_xlabel("soil water suction $|\\psi|$ / kPa")
ax.set_ylabel("volumetric water content $\\theta$")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("A  Water retention curves", loc="left", fontsize=10)
top = ax.secondary_xaxis("top", functions=(lambda k: 4 * 0.072 / (np.maximum(k, 1e-9) * 1e3) * 1e6,
                                           lambda d: 4 * 0.072 / (np.maximum(d, 1e-9) * 1e-6) / 1e3))
top.set_xlabel("largest water-filled pore diameter / $\\mu$m", fontsize=8)
top.tick_params(labelsize=7)

x = np.arange(len(awc))
for i, (name, tfc, tpwp, tok) in enumerate(awc):
    bx.bar(i, tpwp, width=0.6, color=P.fill("neutral"), alpha=0.3, edgecolor=P.muted(), lw=0.8)
    bx.bar(i, tfc - tpwp, bottom=tpwp, width=0.6, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
    bx.text(i, tfc + 0.01, f"{tfc - tpwp:.2f}", ha="center", fontsize=8, color=P.ink())
bx.set_xticks(x)
bx.set_xticklabels([a[0] for a in awc])
bx.set_ylim(0, 0.45)
bx.set_ylabel("volumetric water content $\\theta$")
bx.text(-0.4, 0.42, "colored: available water\ngray: held below the wilting point", fontsize=7.5, color=P.muted(),
        va="top")
bx.set_title("B  Available water capacity", loc="left", fontsize=10)
for a in (ax, bx):
    for s in ("right",):
        a.spines[s].set_visible(False)
bx.spines["top"].set_visible(False)
fig.tight_layout()
