"""PO2 and PCO2 of blood along a pulmonary capillary (illustrative compartment model).

O2: dC/dt = (D_L / V_c) (P_A - P), C(P) = 1.34 Hb S(P) + 0.00003 P (Hb = 150 g/L, Severinghaus saturation curve),
integrated as dP/dt = (D_L / V_c)(P_A - P) / (dC/dP). P_A = 100 mmHg.
Rest: D_L = 21 mL/(min mmHg), V_c = 70 mL, transit time 0.75 s, mixed venous PO2 = 40 mmHg.
Exercise: D_L = 65, V_c = 110 mL (recruitment), transit 0.25 s, mixed venous PO2 = 25 mmHg.
Thickened barrier (fibrosis): D_L divided by 3.
CO2 (C): first-order approach to P_A = 40 mmHg from 46 mmHg with an effective rate constant set by the
red-cell reactions (HCO3- dehydration and chloride shift), k = 15 /s; with the thick barrier k = 7 /s.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
PA = 100.0


def sat(p):
    p = max(p, 0.1)
    return 1 / (23400 / (p ** 3 + 150 * p) + 1)


def content(p):
    return 1.34 * 0.15 * sat(p) + 3e-5 * p


def run(dl, vc, pv, T=0.75, dt=1e-4):
    k = dl / (vc * 60.0)
    t = np.arange(0, T, dt)
    p = np.empty_like(t)
    x = pv
    for i in range(len(t)):
        p[i] = x
        slope = (content(x + 0.05) - content(x - 0.05)) / 0.1
        x += dt * k * (PA - x) / slope
    return t, p


fig, axs = plt.subplots(1, 3, figsize=(15, 4.2))
for ax, factor, title in [(axs[0], 1.0, "A  O$_2$, normal barrier"), (axs[1], 1 / 3, "B  O$_2$, thickened barrier ($D_L$ / 3)")]:
    t, p = run(21 * factor, 70, 40)
    ax.plot(t, p, color=P.edge("blood"), lw=2, label="rest (transit 0.75 s)")
    t, p = run(65 * factor, 110, 25, T=0.25)
    ax.plot(t, p, color=P.edge("blood"), lw=2, ls="--", label="exercise (transit 0.25 s)")
    ax.axhline(PA, color=P.muted(), lw=1, ls=":")
    ax.axvline(0.25, color=P.muted(), lw=0.8, ls=":")
    ax.text(0.74, PA + 2, "alveolar 100 mmHg", ha="right", fontsize=8, color=P.muted())
    ax.set_ylim(20, 110)
    ax.set_xlim(0, 0.75)
    ax.set_xlabel("Time in the capillary / s")
    ax.set_ylabel("Capillary $P_{O_2}$ / mmHg")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.set_title(title, loc="left", fontsize=10)

ax = axs[2]
t = np.linspace(0, 0.75, 300)
for k, ls, lab in [(15, "-", "normal"), (7, "--", "thickened barrier")]:
    ax.plot(t, 40 + 6 * np.exp(-k * t), color=P.edge("dna"), lw=2, ls=ls, label=lab)
ax.axhline(40, color=P.muted(), lw=1, ls=":")
ax.set_ylim(38, 47)
ax.set_xlim(0, 0.75)
ax.set_xlabel("Time in the capillary / s")
ax.set_ylabel("Capillary $P_{CO_2}$ / mmHg")
ax.legend(frameon=False, fontsize=8)
ax.set_title("C  CO$_2$ (rest)", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
