"""Ventilation-perfusion ratio and the composition of alveolar gas (one lung unit, steady state, sea level).

Mass balance (Riley and Cournand; Rahn and Fenn), end-capillary blood in equilibrium with alveolar gas:
  (VA/Q) (PIO2 - PAO2) / 863 = CcO2 - CvO2,    (VA/Q) PACO2 / 863 = CvCO2 - CcCO2   (contents in mL/mL).
O2 content: 1.34 Hb S + 0.00003 P (Hb = 150 g/L, Severinghaus 1979 saturation curve, Bohr effect as a shift
P_eff = P (40/PCO2)^0.29). CO2 content (mL/100 mL): 8.62 PCO2^0.465 + 3.5 (1 - S) (fitted to arterial 48 at
40 mmHg and mixed venous 52 at 46 mmHg; the second term is the Haldane effect).
Mixed venous blood: PO2 = 40, PCO2 = 46 mmHg; inspired gas PIO2 = 149, PICO2 = 0 mmHg.
A: the O2-CO2 diagram: every possible alveolar composition lies on one curve from v (VA/Q = 0, shunt) to
I (VA/Q -> infinity, dead space). B: PAO2 and PACO2 against VA/Q; normal lung average VA/Q = 0.8 to 1.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

import wikibio as bio

P = bio.P
PIO2, PVO2, PVCO2 = 149.0, 40.0, 46.0


def sat(po2, pco2):
    pe = po2 * (40.0 / max(pco2, 1.0)) ** 0.29
    pe = max(pe, 0.1)
    return 1 / (23400 / (pe ** 3 + 150 * pe) + 1)


def co2c(po2, pco2):
    s = sat(po2, pco2)
    return 1.34 * 0.15 * s + 3e-5 * po2


def cco2(po2, pco2):
    s = sat(po2, pco2)
    return (8.62 * max(pco2, 0.01) ** 0.465 + 3.5 * (1 - s)) / 100


cvo2, cvco2 = co2c(PVO2, PVCO2), cco2(PVO2, PVCO2)


def solve(vq, guess):
    def f(x):
        po, pc = x
        return [vq * (PIO2 - po) / 863 - (co2c(po, pc) - cvo2),
                vq * pc / 863 - (cvco2 - cco2(po, pc))]
    return fsolve(f, guess)


vqs = np.logspace(-2.5, 2.5, 200)
sol = []
g = [PVO2 + 0.5, PVCO2 - 0.1]
for vq in vqs:
    g = solve(vq, g)
    sol.append(g)
sol = np.array(sol)

fig, axs = plt.subplots(1, 2, figsize=(12, 4.4))
ax = axs[0]
ax.plot(sol[:, 0], sol[:, 1], color=P.edge("protein"), lw=2.2)
ax.plot([PVO2], [PVCO2], "o", color=P.edge("dna"), ms=7)
ax.plot([PIO2], [0], "o", color=P.edge("blood"), ms=7)
ax.text(PVO2 + 2, PVCO2 + 2, "mixed venous $\\bar v$\n($\\dot V_A/\\dot Q$ = 0, shunt)", fontsize=8, color=P.ink())
ax.text(PIO2 - 2, 4, "inspired I\n(dead space)", ha="right", fontsize=8, color=P.ink())
for vq in [0.1, 0.3, 0.8, 3, 10]:
    x = solve(vq, sol[np.argmin(abs(vqs - vq))])
    ax.plot(*x, "s", color=P.ink(), ms=4)
    ax.annotate(f"{vq:g}", x, xytext=(6, 4), textcoords="offset points", fontsize=8, color=P.ink())
ax.set_xlabel("$P_{O_2}$ / mmHg")
ax.set_ylabel("$P_{CO_2}$ / mmHg")
ax.set_xlim(30, 155)
ax.set_ylim(0, 55)
ax.set_title("A  O$_2$-CO$_2$ diagram (numbers: $\\dot V_A/\\dot Q$)", loc="left", fontsize=10)

ax = axs[1]
ax.semilogx(vqs, sol[:, 0], color=P.edge("blood"), lw=2, label="alveolar $P_{O_2}$")
ax.semilogx(vqs, sol[:, 1], color=P.edge("dna"), lw=2, label="alveolar $P_{CO_2}$")
ax.axvspan(0.8, 1.0, color=P.fill("highlight"), alpha=0.35, lw=0)
ax.text(0.9, 152, "normal\naverage", ha="center", va="top", fontsize=8, color=P.muted())
ax.text(0.006, 52, "low: shunt-like,\nhypoxaemia", fontsize=8, color=P.muted())
ax.text(30, 60, "high: dead-\nspace-like", ha="center", fontsize=8, color=P.muted())
ax.set_xlabel("Ventilation-perfusion ratio $\\dot V_A/\\dot Q$")
ax.set_ylabel("Partial pressure / mmHg")
ax.set_ylim(0, 155)
ax.legend(frameon=False, fontsize=8, loc="center left")
ax.set_title("B  Alveolar gas against $\\dot V_A/\\dot Q$", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
