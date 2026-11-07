"""Chemical control of breathing: CO2-O2 interaction and ventilatory acclimatisation to altitude (illustrative).

Controller (after Lloyd and Cunningham 1963): VE = S0 (1 + A / (PaO2 - 32)) (PaCO2 - B), VE >= 0,
S0 = 0.75 L/(min mmHg), A = 40 mmHg, B = 35 mmHg (the apnoeic threshold set by the central chemoreceptors).
Plant: PaCO2 = 863 VCO2 / VA with VA = 0.7 VE, VCO2 = 0.2 L/min (the "metabolic hyperbola");
PAO2 = PIO2 - 1.2 PaCO2 (alveolar gas equation, R = 0.8), PaO2 = PAO2 - 5 mmHg.
A: ventilation against PaCO2 at fixed PaO2 (the "fan"), with the metabolic hyperbola; the operating point at sea
level is the intersection for PaO2 = 95. B: ventilation against PaO2 with PaCO2 held at 40 (isocapnic) and with
PaCO2 free to fall (poikilocapnic, the real situation without added CO2).
C: ascent to 4500 m (barometric pressure 430 mmHg, PIO2 = 80 mmHg) at day 0. Acclimatisation: B falls from 35 to
27 mmHg (tau = 1.5 d; renal HCO3- excretion and CSF pH correction) and A rises from 40 to 70 mmHg
(tau = 3 d; carotid body sensitisation). Each day the steady state is solved.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio

P = bio.P
S0, VCO2 = 0.75, 0.2


def ctrl(pao2, paco2, A=40.0, B=35.0):
    return max(0.0, S0 * (1 + A / max(pao2 - 32, 1.0)) * (paco2 - B))


def steady(pio2, A=40.0, B=35.0):
    def f(ve):
        paco2 = 863 * VCO2 / (0.7 * ve)
        pao2 = pio2 - 1.2 * paco2 - 5
        return ctrl(pao2, paco2, A, B) - ve
    ve = brentq(f, 1.0, 200.0)
    paco2 = 863 * VCO2 / (0.7 * ve)
    return ve, paco2, pio2 - 1.2 * paco2 - 5


fig, axs = plt.subplots(1, 3, figsize=(15.5, 4.3))
ax = axs[0]
pc = np.linspace(30, 60, 200)
cols = [P.edge("blood"), P.edge("drug"), P.edge("antibody"), P.ink(), P.edge("dna")]
for po, c in zip([40, 50, 70, 95, 200], cols):
    ax.plot(pc, [ctrl(po, x) for x in pc], color=c, lw=2, label=f"PaO$_2$ = {po} mmHg")
ve = np.linspace(2, 60, 200)
ax.plot(863 * VCO2 / (0.7 * ve), ve, color=P.muted(), lw=1.4, ls="--", label="metabolic hyperbola")
v0, c0, o0 = steady(149)
ax.plot(c0, v0, "o", color=P.ink(), ms=6)
ax.set_xlim(30, 60)
ax.set_ylim(0, 60)
ax.set_xlabel("Arterial $P_{CO_2}$ / mmHg")
ax.set_ylabel("Ventilation $\\dot V_E$ / (L min$^{-1}$)")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  CO$_2$ response at several PaO$_2$", loc="left", fontsize=10)

ax = axs[1]
po = np.linspace(36, 150, 300)
ax.plot(po, [ctrl(x, 40) for x in po], color=P.edge("blood"), lw=2, label="isocapnic (PaCO$_2$ held at 40)")
poik = []
for pio2 in np.linspace(62, 149, 120):
    v, c, o = steady(pio2)
    poik.append((o, v))
poik = np.array(poik)
ax.plot(poik[:, 0], poik[:, 1], color=P.edge("dna"), lw=2, ls="--", label="poikilocapnic (CO$_2$ falls)")
ax.set_xlim(30, 150)
ax.set_ylim(0, 30)
ax.set_xlabel("Arterial $P_{O_2}$ / mmHg")
ax.set_ylabel("Ventilation $\\dot V_E$ / (L min$^{-1}$)")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("B  Hypoxic response", loc="left", fontsize=10)

ax = axs[2]
days = np.linspace(-1, 10, 221)
pio2_alt = 0.2093 * (430 - 47)
res = []
for d in days:
    if d < 0:
        res.append(steady(149))
    else:
        B = 27 + (35 - 27) * np.exp(-d / 1.5)
        A = 70 - 30 * np.exp(-d / 3)
        res.append(steady(pio2_alt, A, B))
res = np.array(res)
ax.plot(days, res[:, 1], color=P.edge("dna"), lw=2, label="PaCO$_2$")
ax.plot(days, res[:, 2], color=P.edge("blood"), lw=2, label="PaO$_2$")
ax.plot([], [], color=P.ink(), lw=2, ls="--", label="ventilation (right axis)")
tx = ax.twinx()
tx.plot(days, res[:, 0], color=P.ink(), lw=2, ls="--")
tx.set_ylim(0, 12)
tx.set_ylabel("Ventilation $\\dot V_E$ / (L min$^{-1}$)")
ax.axvline(0, color=P.muted(), lw=0.8, ls=":")
ax.text(0.1, 97, "ascent to 4500 m", fontsize=8, color=P.muted())
ax.set_xlim(-1, 10)
ax.set_ylim(0, 105)
ax.set_xlabel("Days")
ax.set_ylabel("Arterial partial pressure / mmHg")
ax.legend(frameon=False, fontsize=8, loc="center right")
ax.set_title("C  Ventilatory acclimatisation", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
