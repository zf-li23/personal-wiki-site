"""Kinetic versus thermodynamic control. Top: A gives B over the lower barrier and C over the higher
one, but C is more stable. Bottom: the composition at 298 K computed from the Eyring equation
(transmission coefficient 1) for the reversible scheme B <=> A <=> C, by the matrix exponential of
the first-order rate matrix. At short times B dominates (B:C = ratio of the forward rate constants,
about 56:1); only after the slow reverse reaction of B has run for hours does the mixture reach
equilibrium, where C dominates (C:B = exp(10 kJ/mol / RT), also about 56:1)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

R, T = 8.314462618, 298.15
kB, h = 1.380649e-23, 6.62607015e-34


def eyring(dg_kj):
    return kB * T / h * np.exp(-dg_kj * 1e3 / (R * T))


# Free energies (kJ/mol) relative to A: B is the kinetic product, C the thermodynamic product.
G = {"A": 0.0, "B": -10.0, "C": -20.0, "TS_AB": 80.0, "TS_AC": 90.0}
k_ab, k_ba = eyring(G["TS_AB"] - G["A"]), eyring(G["TS_AB"] - G["B"])
k_ac, k_ca = eyring(G["TS_AC"] - G["A"]), eyring(G["TS_AC"] - G["C"])

ink = plt.rcParams["text.color"]
fig, (a, b) = plt.subplots(2, 1, figsize=(7.5, 7.6), gridspec_kw={"height_ratios": [1, 1]})


def segment(ax, x0, x1, y0, y1, **kw):
    t = np.linspace(0, 1, 60)
    ax.plot(x0 + (x1 - x0) * t, y0 + (y1 - y0) * (1 - np.cos(np.pi * t)) / 2, **kw)


blue, orange = "#2563eb", "#f97316"
segment(a, 0, -1, G["A"], G["TS_AB"], color=blue, lw=2)
segment(a, -1, -2, G["TS_AB"], G["B"], color=blue, lw=2)
segment(a, 0, 1, G["A"], G["TS_AC"], color=orange, lw=2)
segment(a, 1, 2, G["TS_AC"], G["C"], color=orange, lw=2)
for x, y, s in ((0, G["A"], "A"), (-2, G["B"], "B (kinetic)"), (2, G["C"], "C (thermodynamic)")):
    a.text(x, y - 9, s, ha="center", va="top", fontsize=10)
a.text(-1, G["TS_AB"] + 3, f"{G['TS_AB']:.0f}", ha="center", fontsize=9)
a.text(1, G["TS_AC"] + 3, f"{G['TS_AC']:.0f}", ha="center", fontsize=9)
a.text(-2, G["B"] + 4, f"{G['B']:.0f}", ha="center", fontsize=9)
a.text(2, G["C"] + 4, f"{G['C']:.0f}", ha="center", fontsize=9)
a.set_xlim(-2.6, 2.6)
a.set_ylim(-45, 105)
a.set_xticks([])
a.set_ylabel(r"$G$ / kJ mol$^{-1}$")
for side in ("top", "right"):
    a.spines[side].set_visible(False)

# Rate matrix for d[x]/dt = K x, x = ([A], [B], [C]).
K = np.array([
    [-(k_ab + k_ac), k_ba, k_ca],
    [k_ab, -k_ba, 0.0],
    [k_ac, 0.0, -k_ca],
])
times = np.logspace(-1, 9, 400)
x = np.array([expm(K * t) @ np.array([1.0, 0.0, 0.0]) for t in times])
b.semilogx(times, x[:, 0], color=ink, lw=1.5, label="A")
b.semilogx(times, x[:, 1], color=blue, lw=2, label="B (kinetic)")
b.semilogx(times, x[:, 2], color=orange, lw=2, label="C (thermodynamic)")
for t, s in ((60, "1 min"), (3600, "1 h"), (86400, "1 d"), (3.15e7, "1 yr")):
    b.axvline(t, color="0.6", lw=0.6, ls=":")
    b.text(t * 1.15, 0.5, s, fontsize=8, color="0.45", rotation=90, va="center")
b.set_xlabel("time / s")
b.set_ylabel("mole fraction")
b.set_ylim(0, 1.02)
b.legend(frameon=False, loc="center right")
for side in ("top", "right"):
    b.spines[side].set_visible(False)
fig.tight_layout()
