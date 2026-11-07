"""Thermal sensors: two-state TRP channels, fibre discharge and the pain threshold.

A: open probability of a two-state channel, p_o = 1 / (1 + exp[(dH/R)(1/T - 1/T_half)]),
for illustrative parameters of the order reported for thermo-TRPs: TRPM8 (T_half = 25 C,
dH = -250 kJ/mol, cold), TRPV1 (43 C, +400 kJ/mol), TRPV2 (52 C, +400 kJ/mol).
B: schematic static discharge of cold fibres, warm fibres and heat nociceptors against skin
temperature, each built from two such sigmoids (activation times high-temperature or
low-temperature silencing), normalised to a peak of 1.
C: cumulative fraction of people reporting pain against skin temperature, modelled as a normal
distribution of thresholds (mean 45 C, s.d. 1.2 C; schematic, after population studies).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
R = 8.314
Tc = np.linspace(0, 60, 601)
T = Tc + 273.15


def po(t_half, dH):
    return 1 / (1 + np.exp(dH * 1e3 / R * (1 / T - 1 / (t_half + 273.15))))


fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(12, 3.9))
for name, th, dh, c in (("TRPM8", 25, -250, P.edge("dna")), ("TRPV1", 43, 400, P.edge("rna")),
                        ("TRPV2", 52, 400, P.edge("protein"))):
    ax.plot(Tc, po(th, dh), color=c, lw=2, label=f"{name} ($T_{{1/2}}$ = {th} °C)")
ax.set_xlabel("Temperature / °C")
ax.set_ylabel("Open probability")
ax.legend(frameon=False, fontsize=7.5, loc="center left")
ax.set_title("A  Two-state thermo-TRPs", loc="left", fontsize=10)

cold = po(31, -150) * po(17, 300)
warm = po(37, 300) * po(46, -600)
heat = po(46, 500)
for r, c, lab in ((cold, P.edge("dna"), "cold fibre"), (warm, P.edge("enzyme"), "warm fibre"),
                  (heat, P.edge("rna"), "heat nociceptor")):
    bx.plot(Tc, r / r.max(), color=c, lw=2, label=lab)
bx.set_xlabel("Skin temperature / °C")
bx.set_ylabel("Static discharge (normalised)")
bx.legend(frameon=False, fontsize=7.5, loc="upper left")
bx.set_title("B  Fibre types (schematic)", loc="left", fontsize=10)

x = np.linspace(38, 52, 400)
from math import erf
cdf = np.array([0.5 * (1 + erf((v - 45) / (1.2 * np.sqrt(2)))) for v in x])
cx.plot(x, 100 * cdf, color=P.edge("rna"), lw=2)
cx.axvline(45, color=P.muted(), lw=0.7, ls=":")
cx.text(45.3, 15, "median\n45 °C", fontsize=8, color=P.muted())
cx.set_xlabel("Skin temperature / °C")
cx.set_ylabel("People reporting pain / %")
cx.set_title("C  Pain threshold in a population", loc="left", fontsize=10)
for a in (ax, bx, cx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
