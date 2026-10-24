"""Fraction of the equatorial conformer of a monosubstituted cyclohexane at 298 K as a function of
the A value (Gibbs energy difference, axial minus equatorial): x_eq = K / (1 + K), K = exp(A/RT)."""

import numpy as np
import matplotlib.pyplot as plt

R, T = 8.314e-3, 298.15  # kJ/(mol K), K
A = np.linspace(0, 22, 400)
x = 100 / (1 + np.exp(-A / (R * T)))
groups = {"F": 1.0, "Cl": 1.8, "OH": 3.6, "COOH": 5.9, "CH$_3$": 7.3, "CH(CH$_3$)$_2$": 9.2, "C$_6$H$_5$": 11.7, "C(CH$_3$)$_3$": 20.5}

fig, ax = plt.subplots(figsize=(7.5, 3.9))
ax.plot(A, x, color="C0", lw=2)
offsets = {"F": (0.6, -4), "Cl": (0.6, -6), "OH": (0.7, -7), "COOH": (0.6, -9), "CH$_3$": (-1.6, 4),
           "CH(CH$_3$)$_2$": (0.4, -10), "C$_6$H$_5$": (0.4, -7), "C(CH$_3$)$_3$": (-1.0, -9)}
for name, a in groups.items():
    xe = 100 / (1 + np.exp(-a / (R * T)))
    ax.plot(a, xe, "o", color="C3", ms=5)
    dx, dy = offsets[name]
    text = f"{name}: {xe:.1f}%" if xe < 99.9 else f"{name}: >99.9%"
    ax.annotate(text, (a, xe), xytext=(a + dx, xe + dy), fontsize=8, ha="left",
                arrowprops=dict(arrowstyle="-", color="0.6", lw=0.6))
ax.set_xlim(0, 22)
ax.set_ylim(48, 104)
ax.set_xlabel(r"A value $= -\Delta G^\circ$ (axial $\rightleftharpoons$ equatorial) / (kJ mol$^{-1}$)")
ax.set_ylabel("equatorial conformer at 298 K / %")
ax.grid(alpha=0.3)
fig.tight_layout()
