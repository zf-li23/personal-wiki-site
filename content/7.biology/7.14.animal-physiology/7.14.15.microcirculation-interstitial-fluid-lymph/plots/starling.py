"""Starling forces along a systemic capillary and the interstitial safety margin.

A: J_v/K_f = (P_c - P_i) - (pi_c - pi_i), the classical picture (Guyton values, mmHg): capillary pressure falls
linearly from 30 to 10 along the capillary, interstitial free-fluid pressure P_i = -3, plasma colloid osmotic
pressure pi_c = 28, interstitial colloid osmotic pressure pi_i = 8; net pressure +13 at the arterial end,
-7 at the venous end, about +0.3 on average (capillary pressure averaged over the bed, 17.3 mmHg).
Dotted: the same capillary when venous pressure rises by 10 mmHg (e.g. heart failure).
B: schematic tissue compliance and lymph flow against interstitial pressure: below 0 mmHg the gel is stiff
(small volume change), above 0 free fluid accumulates (edema); lymph flow rises about 20-fold from -6 to 0 mmHg.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
x = np.linspace(0, 1, 200)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.3))
Pc = 30 - 20 * x
Pi, pic, pii = -3.0, 28.0, 8.0
nfp = (Pc - Pi) - (pic - pii)
ax.plot(x, Pc, color=P.edge("blood"), lw=2, label="capillary pressure P$_c$")
ax.axhline(pic, color=P.edge("protein"), lw=2, label="plasma colloid osmotic pressure")
ax.plot(x, nfp, color=P.ink(), lw=2.2, label="net filtration pressure")
ax.fill_between(x, 0, nfp, where=nfp > 0, color=P.fill("negative"), alpha=0.35, lw=0)
ax.fill_between(x, 0, nfp, where=nfp < 0, color=P.fill("positive"), alpha=0.35, lw=0)
nfp2 = (Pc + 10 * x + 2 - Pi) - (pic - pii)
ax.plot(x, nfp2, color=P.ink(), lw=1.2, ls=":", label="net, venous pressure +10")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.text(0.12, 4, "filtration", fontsize=8, color=P.muted())
ax.text(0.72, -4.5, "reabsorption", fontsize=8, color=P.muted())
ax.set_xlabel("Position along capillary (arterial 0, venous 1)")
ax.set_ylabel("Pressure / mmHg")
ax.set_ylim(-12, 36)
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
ax.set_title("A  Classical Starling picture", loc="left", fontsize=10)

p = np.linspace(-8, 4, 300)
vol = 10 + 0.7 * (p + 7) + 3 * np.log1p(np.exp(p / 0.6)) * 0.6 / 0.6
lymph = 1 + 19 / (1 + np.exp(-(p + 2.5) / 0.7))
bx.plot(p, vol, color=P.edge("dna"), lw=2, label="interstitial volume")
bx.set_xlabel("Interstitial free-fluid pressure / mmHg")
bx.set_ylabel("Interstitial fluid volume / L", color=P.edge("dna"))
bx.axvspan(0, 4, color=P.fill("negative"), alpha=0.2, lw=0)
bx.axvline(-3, color=P.muted(), ls=":", lw=1)
bx.text(-2.9, 27, "normal", fontsize=8, color=P.muted())
bx.text(1.0, 27, "edema", fontsize=8, color=P.muted())
cx = bx.twinx()
cx.plot(p, lymph, color=P.edge("rna"), lw=2, ls="--", label="lymph flow")
cx.set_ylabel("Lymph flow (x resting)", color=P.edge("rna"))
cx.set_ylim(0, 24)
bx.set_ylim(8, 30)
bx.set_title("B  Stiff gel and lymph guard against edema", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
