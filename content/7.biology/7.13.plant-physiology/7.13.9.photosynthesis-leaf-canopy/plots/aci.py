"""CO2 response of C3 photosynthesis in the Farquhar, von Caemmerer and Berry (1980) model.

25 C kinetic constants of Bernacchi et al. (2001): Kc = 404.9 umol mol-1, Ko = 278.4 mmol mol-1,
Gamma* = 42.75 umol mol-1, O = 210 mmol mol-1. A: Vcmax = 80, J = 150, TPU = 9, Rd = 1 umol m-2 s-1.
Net assimilation is the minimum of the rubisco-limited rate Ac, the RuBP-regeneration (electron
transport) limited rate Aj and the triose-phosphate-use limited rate Ap. The open circle marks the
operating point at ci = 0.7 x 420 umol mol-1. B: the same leaf at three photon flux densities; J follows
a non-rectangular hyperbola in light (Jmax = 150, alpha = 0.3 electrons per incident photon, theta = 0.7).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import photosynthesis as ps

P = bio.P
ci = np.linspace(0, 1500, 601)
vc, j, tpu, rd = 80.0, 150.0, 9.0, 1.0
A, ac, aj, ap = ps.farquhar(ci, vcmax=vc, j=j, rd=rd, tpu=tpu)

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
a.plot(ci, ac, color=P.edge("negative"), lw=1.2, ls="--", label="$A_{\\mathrm{c}}$ rubisco-limited")
a.plot(ci, aj, color=P.edge("dna"), lw=1.2, ls="--", label="$A_{\\mathrm{j}}$ RuBP-regeneration-limited")
a.plot(ci, ap, color=P.edge("lipid"), lw=1.2, ls="--", label="$A_{\\mathrm{p}}$ TPU-limited")
a.plot(ci, A, color=P.ink(), lw=2.4, label="$A = \\min(A_{\\mathrm{c}}, A_{\\mathrm{j}}, A_{\\mathrm{p}})$")
gam = ci[np.argmin(np.abs(A))]
a.plot([gam], [0], "o", color=P.ink(), ms=5)
a.annotate("CO$_2$ compensation\npoint $\\Gamma$", (gam, 0), xytext=(150, -6), fontsize=8, color=P.ink(),
           arrowprops=dict(arrowstyle="->", color=P.muted()))
c0 = 0.7 * 420
A0 = float(np.interp(c0, ci, A))
a.plot([c0], [A0], "o", mfc="none", mec=P.ink(), ms=9, mew=1.5)
a.text(c0 + 30, A0 - 2.5, "operating point", fontsize=8, color=P.ink())
a.axhline(0, color=P.muted(), lw=0.8)
a.set_xlim(0, 1500)
a.set_ylim(-8, 32)
a.set_xlabel("Intercellular CO$_2$ $c_{\\mathrm{i}}$ / µmol mol$^{-1}$")
a.set_ylabel("Net assimilation $A$ / µmol m$^{-2}$ s$^{-1}$")
a.legend(frameon=False, fontsize=8, loc="lower right")
a.set_title("A  A/c$_{\\mathrm{i}}$ curve and its three limitations", loc="left", fontsize=10)

jmax, alpha, th = 150.0, 0.3, 0.7
for I, col in ((100, P.edge("dna")), (400, P.edge("plant")), (1500, P.edge("rna"))):
    s = alpha * I + jmax
    J = (s - np.sqrt(s * s - 4 * th * alpha * I * jmax)) / (2 * th)
    Ai = ps.farquhar(ci, vcmax=vc, j=J, rd=rd, tpu=tpu)[0]
    b.plot(ci, Ai, color=col, lw=2, label=f"PPFD {I} µmol m$^{{-2}}$ s$^{{-1}}$ ($J$ = {J:.0f})")
b.axhline(0, color=P.muted(), lw=0.8)
b.set_xlim(0, 1500)
b.set_ylim(-8, 32)
b.set_xlabel("Intercellular CO$_2$ $c_{\\mathrm{i}}$ / µmol mol$^{-1}$")
b.set_ylabel("Net assimilation $A$ / µmol m$^{-2}$ s$^{-1}$")
b.legend(frameon=False, fontsize=8, loc="upper left")
b.set_title("B  Light sets the RuBP-regeneration limit", loc="left", fontsize=10)
for x in (a, b):
    x.grid(True, alpha=0.3)
fig.tight_layout()
