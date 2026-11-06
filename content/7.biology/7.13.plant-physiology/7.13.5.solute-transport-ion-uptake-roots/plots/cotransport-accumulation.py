# How far a transporter can accumulate a solute: the equilibrium accumulation ratio c_in/c_out at which the
# free-energy change of the whole transport cycle is zero, as a function of the plasma membrane potential V_m,
# with pH 5.5 outside and 7.2 in the cytosol (delta pH = 1.7) at 25 C. For a solute of charge z moved inward
# together with n protons:  ln(c_in/c_out) = -(z + n) F V_m / RT + n ln(10) (pH_in - pH_out).
# Channels (n = 0) for a cation and an anion, H+ symport of an uncharged solute (sucrose, 1:1), electroneutral
# 1 H+ : 1 NO3- symport and electrogenic 2 H+ : 1 NO3- symport. The shaded band is the usual range of V_m
# in root cells (-120 to -200 mV). Concentration ratios over about 10^6 are not physiologically reached.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
F, R, T = 96485.0, 8.314, 298.15
dpH = 1.7
V = np.linspace(-250, 0, 300)  # mV
cases = [("K$^+$ channel ($z$ = +1, $n$ = 0)", 1, 0, "k", "-"),
         ("NO$_3^-$ channel ($z$ = −1, $n$ = 0)", -1, 0, "neutral", "-"),
         ("H$^+$–sucrose symport (0, 1)", 0, 1, "carbohydrate", "-"),
         ("1 H$^+$ : 1 NO$_3^-$ (−1, 1)", -1, 1, "dna", "--"),
         ("2 H$^+$ : 1 NO$_3^-$ (−1, 2)", -1, 2, "dna", "-")]
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.axvspan(-200, -120, color=P.fill("highlight"), alpha=0.3, lw=0)
for lab, z, n, tok, ls in cases:
    lnr = -(z + n) * F * V / 1000 / (R * T) + n * np.log(10) * dpH
    ax.plot(V, lnr / np.log(10), color=charts.line(tok), lw=2.0, ls=ls, label=lab)
ax.axhline(0, color=P.muted(), lw=0.7)
ax.text(-160, 9.3, "root cells", ha="center", fontsize=7, color=P.muted())
ax.set_xlim(-250, 0)
ax.set_ylim(-5, 10)
ax.legend(fontsize=6.8, frameon=False, loc="upper right")
charts.style_axes(ax, "membrane potential $V_{\\mathrm{m}}$ / mV", "lg($c_{\\mathrm{in}}/c_{\\mathrm{out}}$) at equilibrium")
