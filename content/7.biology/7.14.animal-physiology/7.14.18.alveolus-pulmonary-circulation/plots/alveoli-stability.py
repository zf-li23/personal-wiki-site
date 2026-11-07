"""Two alveoli connected to the same airway: surface tension, surfactant and the tissue network.

Pressure needed to hold an alveolus of radius r open: P(r) = 2 gamma(r)/r + P_t(r) (Laplace pressure plus the
recoil of the fibre network, which rises steeply only near full inflation: P_t = 20 exp((r - 130)/10) Pa, r in um).
Cases: water (gamma = 70 mN/m), surfactant (gamma rises from 1 mN/m at r = 60 um to 25 mN/m at r = 160 um as
the film is expanded, gamma = 1 + 24 ((r - 60)/100)^2), and water without the tissue network.
Dynamics (B): total volume fixed, air flows from the alveolus with the higher pressure to the other,
dV1/dt = -(P1 - P2)/R; time in arbitrary units. Starting radii 100 and 115 um (diameters 200 and 230 um).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def tissue(r):
    return 20 * np.exp((r - 130) / 10)


def p_water(r, with_tissue=True):
    return 2 * 0.070 / (r * 1e-6) + (tissue(r) if with_tissue else 0)


def p_surf(r):
    g = 1e-3 * (1 + 24 * np.clip((r - 60) / 100, 0, None) ** 2)
    return 2 * g / (r * 1e-6) + tissue(r)


cases = [("water + tissue network", p_water, P.edge("dna"), "-"),
         ("water, no tissue network", lambda r: p_water(r, False), P.muted(), "--"),
         ("surfactant + tissue network", p_surf, P.edge("blood"), "-")]

fig, axs = plt.subplots(1, 2, figsize=(12, 4.3))
ax = axs[0]
r = np.linspace(40, 165, 400)
for lab, f, c, ls in cases:
    ax.plot(r, f(r), color=c, lw=2, ls=ls, label=lab)
ax.set_yscale("log")
ax.set_ylim(20, 5000)
ax.set_xlabel("Alveolar radius $r$ / $\\mu$m")
ax.set_ylabel("Pressure to hold the alveolus open / Pa")
ax.axvspan(100, 150, color=P.fill("highlight"), alpha=0.25, lw=0)
ax.text(125, 3500, "worked example\n(r = 100 vs 150 um)", ha="center", fontsize=8, color=P.muted())
ax.legend(frameon=False, fontsize=8, loc="center left", bbox_to_anchor=(0.0, 0.42))
ax.set_title("A  Laplace pressure P = 2 gamma / r (+ tissue)", loc="left", fontsize=10)

ax = axs[1]
vol = lambda x: 4 / 3 * np.pi * x ** 3
rad = lambda v: (3 * v / (4 * np.pi)) ** (1 / 3)
for lab, f, c, ls in cases:
    v1, v2 = vol(100.0), vol(115.0)
    tot = v1 + v2
    ts, r1s, r2s = [], [], []
    dt = 0.01
    for i in range(3000):
        r1, r2 = rad(v1), rad(v2)
        ts.append(i * dt)
        r1s.append(r1)
        r2s.append(r2)
        q = (f(r1) - f(r2)) * 2e3
        v1 = min(max(v1 - q * dt, vol(15.0)), tot - vol(15.0))
        v2 = tot - v1
    ax.plot(ts, r1s, color=c, lw=2, ls=ls, label=lab)
    ax.plot(ts, r2s, color=c, lw=1.2, ls=ls)
ax.set_xlabel("Time (arbitrary units)")
ax.set_ylabel("Radius / $\\mu$m")
ax.set_ylim(0, 160)
ax.text(29, 103, "surfactant: radii converge", ha="right", fontsize=8, color=P.edge("blood"))
ax.text(29, 22, "water: the smaller alveolus collapses", ha="right", fontsize=8, color=P.edge("dna"))
ax.legend(frameon=False, fontsize=8, loc="center right")
ax.set_title("B  Two connected alveoli, start 100 and 115 um", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
