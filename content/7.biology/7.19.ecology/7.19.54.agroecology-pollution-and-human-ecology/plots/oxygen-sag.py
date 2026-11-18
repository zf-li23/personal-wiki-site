"""Streeter-Phelps oxygen sag below an organic effluent (Section 54.2.2).

BOD remaining L and oxygen deficit D = O_sat - O in a river parcel travelling at speed u:
    dL/dt = -k1 L,  dD/dt = k1 L - k2 D,
k1 = 0.3 per day (deoxygenation), k2 = 0.6 per day (reaeration), u = 20 km per day,
O_sat = 9 mg/L, initial deficit D0 = 1 mg/L; initial BOD after mixing L0 = 8, 15, 25 mg/L.
Solution D(t) = k1 L0 (e^{-k1 t} - e^{-k2 t}) / (k2 - k1) + D0 e^{-k2 t}; critical time
t_c = ln[(k2/k1)(1 - D0 (k2 - k1)/(k1 L0))] / (k2 - k1) (Proposition 54.2.1). Oxygen cannot fall
below zero; where the model predicts it, the river becomes anoxic (the model no longer applies).
A: dissolved oxygen against distance downstream; dots mark the critical point.
B: minimum oxygen against L0: the largest load that keeps oxygen above 5 mg/L.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
k1, k2, u, Os, D0 = 0.3, 0.6, 20.0, 9.0, 1.0


def deficit(t, L0):
    return k1 * L0 * (np.exp(-k1 * t) - np.exp(-k2 * t)) / (k2 - k1) + D0 * np.exp(-k2 * t)


def tcrit(L0):
    return np.log(k2 / k1 * (1 - D0 * (k2 - k1) / (k1 * L0))) / (k2 - k1)


fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.0), gridspec_kw={"width_ratios": [1.6, 1]})
ax = axes[0]
x = np.linspace(-20, 300, 700)
t = np.clip(x, 0, None) / u
cols = [C.line("dna"), C.line("rna"), C.line("negative")]
for L0, col in zip((8, 15, 25), cols):
    O = np.where(x < 0, Os - D0, Os - deficit(t, L0))
    ax.plot(x, np.clip(O, 0, None), color=col, lw=2, label=f"BOD after mixing L0 = {L0} mg/L")
    tc = tcrit(L0)
    ax.plot([u * tc], [max(Os - deficit(tc, L0), 0)], "o", color=col, ms=5)
ax.axvline(0, color=P.muted(), lw=0.8)
ax.text(2, 9.4, "outfall", color=P.muted(), fontsize=FS["tiny"])
ax.axhline(5, color=P.muted(), lw=0.8, ls=(0, (4, 2)))
ax.text(298, 5.15, "5 mg/L: most fish", color=P.muted(), fontsize=FS["tiny"], ha="right")
ax.axhline(Os, color=P.muted(), lw=0.6, ls=":")
for xa, xb, lab in ((-20, 0, "clean"), (0, 30, "degradation"), (30, 110, "active decomposition"),
                    (110, 300, "recovery")):
    ax.text((xa + xb) / 2, 0.35, lab, color=P.ink(), fontsize=FS["tiny"], ha="center")
ax.set_xlim(-20, 300)
ax.set_ylim(0, 10)
C.style_axes(ax, "distance downstream (km)", "dissolved oxygen (mg/L)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right", bbox_to_anchor=(1, 0.08))
C.title(ax, "A  The oxygen sag curve")

ax = axes[1]
L = np.linspace(2, 30, 300)
omin = Os - deficit(tcrit(L), L)
ax.plot(L, np.clip(omin, 0, None), color=P.ink(), lw=2.2)
ax.axhline(5, color=P.muted(), lw=0.8, ls=(0, (4, 2)))
Lmax = L[np.argmin(np.abs(omin - 5))]
ax.plot([Lmax], [5], "o", color=C.line("negative"), ms=6)
ax.text(Lmax + 0.8, 5.3, f"allowable load ≈ {Lmax:.1f} mg/L", color=C.line("negative"), fontsize=FS["tiny"])
ax.set_xlim(0, 30)
ax.set_ylim(0, 9)
C.style_axes(ax, "BOD after mixing, L0 (mg/L)", "minimum dissolved oxygen (mg/L)")
C.title(ax, "B  Carrying capacity for effluent")
fig.tight_layout()
