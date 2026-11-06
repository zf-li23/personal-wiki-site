"""Carbon isotope discrimination and the d13C of C3, C4 and CAM plants.

A: discrimination Delta against ci/ca. C3 (Farquhar, O'Leary and Berry 1982): Delta = a + (b - a) ci/ca with
a = 4.4 per mil (diffusion in air) and b = 27 per mil (net carboxylation). C4 (Farquhar 1983):
Delta = a + (b4 + b3 phi - a) ci/ca with b4 = -5.7 per mil (CO2 hydration and PEP carboxylase), b3 = 30 per mil
(rubisco) and bundle-sheath leakiness phi = 0.2 and 0.35. Dots: typical operating points (C3 ci/ca = 0.7,
C4 0.4). Right axis: the corresponding plant d13C for atmospheric d13C = -8.5 per mil.
B: schematic frequency distributions of leaf d13C (C3 mean about -28, C4 about -14 per mil; CAM plants
spread between, depending on the share of night-time fixation). Not data.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
a, b, b3, b4, da = 4.4, 27.0, 30.0, -5.7, -8.5
r = np.linspace(0, 1, 101)

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.3))
c3 = a + (b - a) * r
ax.plot(r, c3, color=P.edge("dna"), lw=2, label="C3")
for phi, ls in ((0.2, "-"), (0.35, "--")):
    ax.plot(r, a + (b4 + b3 * phi - a) * r, color=P.edge("plant"), lw=2, ls=ls, label=f"C4, leakiness $\\phi$ = {phi}")
ax.plot([0.7], [a + (b - a) * 0.7], "o", color=P.edge("dna"), ms=7)
ax.plot([0.4], [a + (b4 + b3 * 0.2 - a) * 0.4], "o", color=P.edge("plant"), ms=7)
ax.annotate("drought: stomata close,\n$c_{\\mathrm{i}}/c_{\\mathrm{a}}$ falls", (0.55, a + (b - a) * 0.55),
            xytext=(0.12, 19), fontsize=8, color=P.ink(), arrowprops=dict(arrowstyle="->", color=P.muted()))
ax.set_xlim(0, 1)
ax.set_ylim(-2, 30)
ax.set_xlabel("$c_{\\mathrm{i}}/c_{\\mathrm{a}}$")
ax.set_ylabel("Discrimination $\\Delta$ / ‰")
ax.legend(frameon=False, fontsize=8, loc="upper left")
sec = ax.secondary_yaxis("right", functions=(lambda D: (da - D) / (1 + D / 1000), lambda d: (da - d) / (1 + d / 1000)))
sec.set_ylabel("Plant $\\delta^{13}$C / ‰")
ax.set_title("A  $\\Delta = a + (b - a)\\,c_{\\mathrm{i}}/c_{\\mathrm{a}}$", loc="left", fontsize=10)

d = np.linspace(-36, -6, 600)


def g(m, s):
    return np.exp(-0.5 * ((d - m) / s) ** 2)


dens = [("C3", g(-28, 2.3), "dna"), ("C4", g(-14, 1.2), "plant"),
        ("CAM", 0.35 * g(-16, 2.0) + 0.2 * g(-21, 3.0), "rna")]
for name, y, tok in dens:
    bx.fill_between(d, 0, y, color=P.fill(tok), alpha=0.6, lw=0)
    bx.plot(d, y, color=P.edge(tok), lw=1.6, label=name)
bx.axvline(da, color=P.muted(), lw=1, ls=":")
bx.text(da - 0.3, 0.9, "air CO$_2$", rotation=90, fontsize=8, color=P.muted(), ha="right")
bx.set_xlim(-36, -6)
bx.set_ylim(0, 1.05)
bx.set_yticks([])
bx.set_xlabel("Leaf $\\delta^{13}$C / ‰")
bx.set_ylabel("Relative frequency (schematic)")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  $\\delta^{13}$C of the three pathways", loc="left", fontsize=10)
for x in (ax, bx):
    x.grid(True, alpha=0.3)
fig.tight_layout()
