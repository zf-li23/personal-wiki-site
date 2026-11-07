"""Alveolar PO2 and PCO2 against alveolar ventilation (steady state, sea level, BTPS).

PACO2 = 863 VCO2 / VA (VCO2 in L STPD/min, VA in L BTPS/min, inspired CO2 = 0), and the alveolar gas equation
PAO2 = PIO2 - PACO2 (FIO2 + (1 - FIO2) / R), PIO2 = 0.2093 (760 - 47) = 149 mmHg.
Rest: VO2 = 0.25 L/min, R = 0.8; moderate exercise: VO2 = 1.0 L/min, R = 0.8.
The dots mark the normal resting point (VA = 4.2 L/min) and the same alveolar gas at four times the uptake.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
FIO2, PB, PH2O = 0.2093, 760.0, 47.0
PIO2 = FIO2 * (PB - PH2O)
va = np.linspace(0.8, 40, 400)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
for vo2, ls, lab in [(0.25, "-", "rest, $\\dot V_{O_2}$ = 250 mL/min"), (1.0, "--", "exercise, $\\dot V_{O_2}$ = 1000 mL/min")]:
    R = 0.8
    paco2 = 863 * vo2 * R / va
    pao2 = PIO2 - paco2 * (FIO2 + (1 - FIO2) / R)
    pao2 = np.where(pao2 > 0, pao2, np.nan)
    axs[0].plot(va, pao2, color=P.edge("blood"), lw=2, ls=ls, label=lab)
    axs[1].plot(va, paco2, color=P.edge("dna"), lw=2, ls=ls, label=lab.replace("O_2", "CO_2").replace("250", "200").replace("1000", "800"))
for va0, vo2 in [(4.2, 0.25), (16.8, 1.0)]:
    pc = 863 * vo2 * 0.8 / va0
    po = PIO2 - pc * (FIO2 + (1 - FIO2) / 0.8)
    axs[0].plot(va0, po, "o", color=P.edge("blood"), ms=6)
    axs[1].plot(va0, pc, "o", color=P.edge("dna"), ms=6)
axs[0].axhline(PIO2, color=P.muted(), lw=1, ls=":")
axs[0].text(39, PIO2 + 3, "inspired $P_{O_2}$ = 149 mmHg", ha="right", fontsize=8, color=P.muted())
axs[0].set_ylim(0, 170)
axs[0].set_ylabel("Alveolar $P_{O_2}$ / mmHg")
axs[0].set_title("A  Alveolar PO2", loc="left", fontsize=10)
axs[1].set_ylim(0, 160)
axs[1].set_ylabel("Alveolar $P_{CO_2}$ / mmHg")
axs[1].set_title("B  Alveolar PCO2", loc="left", fontsize=10)
for a in axs:
    a.set_xlabel("Alveolar ventilation / (L min$^{-1}$)")
    a.set_xlim(0, 40)
    a.legend(frameon=False, fontsize=8, loc="right")
    a.grid(True, alpha=0.3)
    sec = a.secondary_yaxis("right", functions=(lambda p: p * 0.13332, lambda k: k / 0.13332))
    sec.set_ylabel("kPa")
fig.tight_layout()
