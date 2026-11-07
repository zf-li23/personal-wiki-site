"""Oxygen and carbon dioxide dissociation curves of blood (37 C), illustrative.

A: saturation curves with the Hill equation S = P^n / (P^n + P50^n): adult blood P50 = 26.8 mmHg, n = 2.7;
Bohr shifts to P50 = 33 (pH 7.2, high PCO2, warm, high 2,3-BPG); fetal blood P50 = 19;
llama blood P50 about 21 (adult human blood at pH 7.6 is similar); myoglobin P50 = 2.8 mmHg, n = 1.
B: O2 content (mL per 100 mL blood) = 1.34 Hb S + 0.003 P: normal (Hb 150 g/L), anaemia (Hb 75 g/L) and
50 % carboxyhaemoglobin (Hb 150 g/L, half the sites blocked by CO, remaining curve shifted left to P50 = 13).
C: CO2 content = 8.62 PCO2^0.465 + 3.5 (1 - S) mL/100 mL for fully oxygenated (S = 1) and deoxygenated (S = 0)
blood; the arterial point a (PCO2 40, S 0.975) and the mixed venous point v (46, 0.75) give the physiological
line; the difference between the two curves is the Haldane effect.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
p = np.linspace(0, 120, 500)


def hill(p, p50, n=2.7):
    return p ** n / (p ** n + p50 ** n)


fig, axs = plt.subplots(1, 3, figsize=(15, 4.3))
ax = axs[0]
ax.plot(p, 100 * hill(p, 2.8, 1.0), color=P.edge("muscle"), lw=2, label="myoglobin (P50 2.8)")
ax.plot(p, 100 * hill(p, 19), color=P.edge("enzyme"), lw=2, label="fetal blood (P50 19)")
ax.plot(p, 100 * hill(p, 21), color=P.edge("protein"), lw=1.6, ls="-.", label="llama; adult at pH 7.6 (P50 about 21)")
ax.plot(p, 100 * hill(p, 26.8), color=P.ink(), lw=2.4, label="adult, pH 7.4 (P50 26.8)")
ax.plot(p, 100 * hill(p, 33), color=P.edge("blood"), lw=2, ls="--", label="adult, pH 7.2 / warm / BPG (P50 33)")
ax.axhline(50, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("$P_{O_2}$ / mmHg")
ax.set_ylabel("Saturation / %")
ax.set_xlim(0, 120)
ax.set_ylim(0, 102)
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
ax.set_title("A  Shifts of the curve", loc="left", fontsize=10)

ax = axs[1]
ax.plot(p, 1.34 * 15 * hill(p, 26.8) + 0.003 * p, color=P.ink(), lw=2.4, label="normal (Hb 150 g/L)")
ax.plot(p, 1.34 * 7.5 * hill(p, 26.8) + 0.003 * p, color=P.edge("dna"), lw=2, ls="--", label="anaemia (Hb 75 g/L)")
ax.plot(p, 1.34 * 7.5 * hill(p, 13) + 0.003 * p, color=P.edge("blood"), lw=2, label="50 % COHb (Hb 150 g/L)")
ax.axvline(40, color=P.muted(), lw=0.8, ls=":")
ax.axvline(95, color=P.muted(), lw=0.8, ls=":")
ax.text(41, 1, "tissue 40", fontsize=8, color=P.muted())
ax.text(94, 1, "arterial 95", ha="right", fontsize=8, color=P.muted())
ax.set_xlabel("$P_{O_2}$ / mmHg")
ax.set_ylabel("O$_2$ content / (mL per 100 mL)")
ax.set_xlim(0, 120)
ax.set_ylim(0, 22)
ax.legend(frameon=False, fontsize=8, loc="center right", bbox_to_anchor=(1.0, 0.7))
ax.set_title("B  Content: anaemia vs CO", loc="left", fontsize=10)

ax = axs[2]
pc = np.linspace(1, 80, 300)
c = lambda pc, s: 8.62 * pc ** 0.465 + 3.5 * (1 - s)
ax.plot(pc, c(pc, 0), color=P.edge("dna"), lw=2, label="deoxygenated blood")
ax.plot(pc, c(pc, 1), color=P.edge("blood"), lw=2, label="oxygenated blood")
pa, pv = (40, c(40, 0.975)), (46, c(46, 0.75))
ax.plot(*zip(pa, pv), "o-", color=P.ink(), lw=1.4, ms=5)
ax.annotate("a", pa, xytext=(-12, 4), textcoords="offset points", fontsize=9, color=P.ink())
ax.annotate("v", pv, xytext=(4, -12), textcoords="offset points", fontsize=9, color=P.ink())
ax.set_xlabel("$P_{CO_2}$ / mmHg")
ax.set_ylabel("CO$_2$ content / (mL per 100 mL)")
ax.set_xlim(0, 80)
ax.set_ylim(0, 75)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("C  CO$_2$ curve and the Haldane effect", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
