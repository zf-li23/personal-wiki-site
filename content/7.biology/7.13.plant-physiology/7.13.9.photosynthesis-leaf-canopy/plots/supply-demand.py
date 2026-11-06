"""Supply and demand for CO2: where the stomata and the chloroplasts meet.

Demand: the Farquhar model of Figure 1 (Vcmax = 80, J = 150, TPU = 9, Rd = 1 umol m-2 s-1).
Supply: Fick's law A = gc (ca - ci), straight lines from ca = 420 umol mol-1 on the ci axis with slope
-gc, for total conductances to CO2 gc = 0.05, 0.15 and 0.30 mol m-2 s-1; the operating point is the
intersection. The dashed line A0 is the rate the leaf would reach with infinite conductance (ci = ca);
the stomatal limitation is l = 1 - A/A0 (Farquhar and Sharkey 1982). B: with a finite mesophyll
conductance gm = 0.2 mol m-2 s-1 bar-1, the chloroplast CO2 cc = ci - A/gm is lower still; the same
demand curve plotted against cc and ci.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import photosynthesis as ps

P = bio.P
ca = 420.0
c = np.linspace(0, 700, 1401)
A = ps.farquhar(c, vcmax=80, j=150, rd=1, tpu=9)[0]
A0 = float(np.interp(ca, c, A))

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
a.plot(c, A, color=P.ink(), lw=2.4, label="demand (Farquhar model)")
cols = [P.edge("negative"), P.edge("rna"), P.edge("plant")]
for gc, col in zip((0.05, 0.15, 0.30), cols):
    supply = gc * (ca - c)
    a.plot(c, supply, color=col, lw=1.6, label=f"supply, $g_{{\\mathrm{{c}}}}$ = {gc} mol m$^{{-2}}$ s$^{{-1}}$")
    k = np.argmin(np.abs(supply - A))
    a.plot([c[k]], [A[k]], "o", color=col, ms=7)
    a.text(c[k] + 8, A[k] - 2.2, f"$c_{{\\mathrm{{i}}}}$ = {c[k]:.0f}\n$l$ = {1 - A[k] / A0:.2f}", fontsize=7, color=col)
a.axhline(A0, color=P.muted(), lw=0.9, ls="--")
a.text(440, A0 + 0.6, "$A_0$ (no stomatal limitation)", fontsize=8, color=P.muted())
a.axvline(ca, color=P.muted(), lw=0.8, ls=":")
a.text(ca + 6, 1.0, "$c_{\\mathrm{a}}$", fontsize=9, color=P.muted())
a.set_xlim(0, 700)
a.set_ylim(-3, 30)
a.set_xlabel("Intercellular CO$_2$ $c_{\\mathrm{i}}$ / µmol mol$^{-1}$")
a.set_ylabel("Net assimilation $A$ / µmol m$^{-2}$ s$^{-1}$")
a.legend(frameon=False, fontsize=7.5, loc="center right", bbox_to_anchor=(1.0, 0.4))
a.set_title("A  Supply and demand", loc="left", fontsize=10)

gm = 0.2                                   # mol m-2 s-1 bar-1 (~ per mol mol-1 at 1 bar)
ci_eq = c + A / gm                         # ci that gives cc = c
b.plot(c, A, color=P.ink(), lw=2.2, label="$A$ against chloroplast CO$_2$ $c_{\\mathrm{c}}$")
b.plot(ci_eq, A, color=P.edge("dna"), lw=2.2, ls="--", label="$A$ against $c_{\\mathrm{i}}$ ($g_{\\mathrm{m}}$ = 0.2)")
b.annotate("", xy=(200, float(np.interp(200, c, A))), xytext=(200 + float(np.interp(200, c, A)) / gm,
           float(np.interp(200, c, A))), arrowprops=dict(arrowstyle="->", color=P.muted()))
b.text(225, float(np.interp(200, c, A)) - 2.2, "$c_{\\mathrm{i}} - c_{\\mathrm{c}} = A/g_{\\mathrm{m}}$",
       fontsize=8, color=P.ink())
b.set_xlim(0, 700)
b.set_ylim(-3, 30)
b.set_xlabel("CO$_2$ / µmol mol$^{-1}$")
b.set_ylabel("Net assimilation $A$ / µmol m$^{-2}$ s$^{-1}$")
b.legend(frameon=False, fontsize=8, loc="upper left")
b.set_title("B  Mesophyll conductance", loc="left", fontsize=10)
for x in (a, b):
    x.grid(True, alpha=0.3)
fig.tight_layout()
