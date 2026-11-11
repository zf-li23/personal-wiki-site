"""Temperature, voltage and ligands converge on the gating of thermosensitive TRP channels.

Two-state model with a voltage sensor: P_o = 1 / (1 + exp[-z F (V - V_half(T)) / (R T)]),
V_half(T) = (dH - T dS + dG_lig) / (z F), gating charge z = 0.8.
TRPV1 (heat): dH = +280 kJ/mol, dS = +0.903 kJ/(mol K). TRPM8 (cold): dH = -202 kJ/mol,
dS = -0.695 kJ/(mol K). Illustrative values chosen to reproduce the measured thresholds and
Q10 values of order 10-30. Ligands and modulators act as an extra free energy of opening dG_lig:
menthol on TRPM8 (-8 kJ/mol); protons or PKC phosphorylation in inflammation on TRPV1 (-5 kJ/mol);
capsaicin on TRPV1 (-15 kJ/mol).
A: TRPM8 activation curves at 15, 25 and 35 C, and at 35 C with menthol.
B: TRPV1 open probability at -60 mV against temperature, normal, sensitized and with capsaicin.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
F, R, z = 96485.0, 8.314, 0.8


def po(V, Tc, dH, dS, dG=0.0):
    T = Tc + 273.15
    vh = (dH - T * dS + dG) / (z * F)
    return 1 / (1 + np.exp(-z * F * (V - vh) / (R * T)))


m8 = (-202e3, -695.0)
v1 = (280e3, 903.0)

fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1))
ax = axs[0]
V = np.linspace(-0.15, 0.25, 400)
cols = [P.edge("dna"), P.edge("enzyme"), P.edge("rna")]
for Tc, c in zip((15, 25, 35), cols):
    ax.plot(V * 1e3, po(V, Tc, *m8), color=c, lw=2, label=f"{Tc} C")
ax.plot(V * 1e3, po(V, 35, *m8, dG=-8e3), color=P.edge("rna"), lw=2, ls="--", label="35 C + menthol")
ax.axvline(-60, color=P.muted(), lw=0.8, ls=":")
ax.text(-57, 0.92, "-60 mV", fontsize=8, color=P.muted())
ax.set_xlabel("Membrane potential / mV")
ax.set_ylabel("Open probability")
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  TRPM8: cooling shifts voltage activation", loc="left", fontsize=10)

ax = axs[1]
Tc = np.linspace(20, 55, 400)
for dG, c, lab in ((0, P.edge("dna"), "normal"), (-5e3, P.edge("rna"), "sensitized (inflammation)"),
                   (-15e3, P.edge("negative"), "with capsaicin")):
    ax.plot(Tc, po(-0.06, Tc, *v1, dG=dG), color=c, lw=2, label=lab)
ax.axvline(37, color=P.muted(), lw=0.8, ls=":")
ax.text(37.4, 0.92, "body temperature", fontsize=8, color=P.muted())
ax.set_xlabel("Temperature / C")
ax.set_ylabel("Open probability at -60 mV")
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("B  TRPV1: modulators lower the heat threshold", loc="left", fontsize=10)
fig.tight_layout()
