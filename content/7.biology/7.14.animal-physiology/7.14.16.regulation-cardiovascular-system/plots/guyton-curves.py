"""Guyton's graphical analysis and the renal-body fluid set point.

A: venous return VR = (P_msf - P_ra)/R_VR, with R_VR = 1.4 mmHg min/L and mean systemic filling pressure
P_msf = 7 mmHg (normal); VR plateaus when P_ra falls below about -4 mmHg because the great veins collapse.
Cardiac function curves are logistic: CO = CO_max / (1 + exp(-(P_ra - P0)/1.6)), normal CO_max = 13 L/min,
P0 = 0.75 mmHg (CO = 5 L/min at P_ra = 0). Strong sympathetic stimulation: CO_max = 25, P0 = -0.5, P_msf = 17
(venoconstriction). Transfusion of about 20 % of blood volume: P_msf = 14. Heart failure: CO_max = 6, P0 = 3.
Circles mark the operating points (CO = VR).
B: renal output curve U = ((P - 55)/45)^3 (x normal) for P > 55 mmHg; intake lines. Long-term arterial
pressure sits where output equals intake: doubling intake raises it only slightly; shifting the renal curve
to the right by 30 mmHg (impaired pressure natriuresis) raises it by 30 mmHg.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio

P = bio.P
pra = np.linspace(-8, 14, 400)


def vr(p, pms, rvr=1.4):
    return np.clip((pms - np.maximum(p, -4)) / rvr, 0, None)


def cf(p, comax, p0):
    return comax / (1 + np.exp(-(p - p0) / 1.6))


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.4))
cases = [("normal heart", 13, 0.75, P.ink(), "-"), ("sympathetic", 25, -0.5, P.edge("blood"), "-"),
         ("heart failure", 6, 3.0, P.edge("protein"), "-")]
for name, cm, p0, c, ls in cases:
    ax.plot(pra, cf(pra, cm, p0), color=c, lw=2, ls=ls, label=f"cardiac function: {name}")
vcases = [("normal VR (P$_{msf}$ = 7)", 7, P.edge("dna"), "--"), ("transfusion (14)", 14, P.edge("positive"), "--"),
          ("sympathetic (17)", 17, P.edge("blood"), "--")]
for name, pms, c, ls in vcases:
    ax.plot(pra, vr(pra, pms), color=c, lw=1.8, ls=ls, label=name)
pts = [(13, 0.75, 7), (13, 0.75, 14), (25, -0.5, 17), (6, 3.0, 7)]
for cm, p0, pms in pts:
    x0 = brentq(lambda p: cf(p, cm, p0) - vr(p, pms), -3.9, 14)
    ax.plot(x0, cf(x0, cm, p0), "o", color=P.ink(), ms=6, zorder=5)
ax.set_xlim(-8, 14)
ax.set_ylim(0, 26)
ax.set_xlabel("Right atrial pressure / mmHg")
ax.set_ylabel("Cardiac output or venous return / L min$^{-1}$")
ax.legend(frameon=False, fontsize=7, loc="upper left")
ax.set_title("A  Heart and vessels meet at one point", loc="left", fontsize=10)

pa = np.linspace(40, 200, 400)


def renal(p, shift=0.0):
    return np.where(p > 55 + shift, ((p - 55 - shift) / 45) ** 3, 0.0)


bx.plot(pa, renal(pa), color=P.edge("dna"), lw=2, label="renal output, normal kidney")
bx.plot(pa, renal(pa, 30), color=P.edge("negative"), lw=2, label="impaired natriuresis (+30)")
for k, lab in ((1, "normal intake"), (2, "intake x2")):
    bx.axhline(k, color=P.muted(), lw=1, ls=":")
    bx.text(42, k + 0.12, lab, fontsize=8, color=P.muted())
for k, sh in ((1, 0), (2, 0), (1, 30)):
    p0 = 55 + sh + 45 * k ** (1 / 3)
    bx.plot(p0, k, "o", color=P.ink(), ms=6)
    bx.text(p0 + 2, k - 0.35, f"{p0:.0f}", fontsize=8)
bx.set_ylim(0, 6)
bx.set_xlim(40, 200)
bx.set_xlabel("Mean arterial pressure / mmHg")
bx.set_ylabel("Salt and water output or intake (x normal)")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Pressure natriuresis fixes the long-term level", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
