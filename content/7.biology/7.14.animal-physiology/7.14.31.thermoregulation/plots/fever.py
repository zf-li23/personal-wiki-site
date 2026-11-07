"""Fever as a raised set point: the same controller as the heat-balance model, with Tset(t) as the input.

Core heat capacity 245 kJ/K; metabolism 80 W * 2.3^((Tc - 37)/10); shivering up to 250 W (full at e = -0.5 C);
conductance 7-25 W/K sigmoid in e (lightly covered subject in bed); sweating 1000 W/C * max(e, 0), at most 500 W; e = Tc - Tset; room at 28 C.
Tset rises from 37.0 to 39.5 C over 20 min at t = 1 h (pyrogen -> PGE2 in the preoptic area) and returns to 37 C at
t = 7 h (pyrogen cleared or antipyretic). A: set point and core temperature. B: effector outputs: shivering and
skin vasoconstriction in the chill phase, then sweating and vasodilation in the flush phase (defervescence).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
Cap, Ta, dt = 245e3, 28.0, 5.0
t = np.arange(0, 10 * 3600, dt)


def tset(s):
    h = s / 3600
    up = np.clip((h - 1) / (1 / 3), 0, 1)
    down = np.clip((h - 7) / (1 / 3), 0, 1)
    return 37 + 2.5 * up - 2.5 * down


tc = 37.0
rec = np.zeros((len(t), 5))
for i, s in enumerate(t):
    ts = tset(s)
    e = tc - ts
    m = 80 * 2.3 ** ((tc - 37) / 10)
    sh = 250 * np.clip(-e / 0.5, 0, 1)
    k = 7 + 18 / (1 + np.exp(-(e - 0.25) / 0.08))
    sw = min(500, 1000 * max(e, 0))
    tc += dt * (m + sh - k * (tc - Ta) - 20 - sw) / Cap
    rec[i] = ts, tc, sh, k, sw

h = t / 3600
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.4))
ax.plot(h, rec[:, 0], color=P.edge("negative"), lw=1.6, ls="--", label="set point")
ax.plot(h, rec[:, 1], color=P.edge("dna"), lw=2.2, label="core temperature")
for x0, x1, lab in ((1, 2.1, "chill"), (2.1, 7, "plateau"), (7, 8.0, "flush")):
    ax.axvspan(x0, x1, color=P.fill("neutral"), alpha=0.15 if lab == "plateau" else 0.3, lw=0)
    ax.text((x0 + x1) / 2, 39.85, lab, ha="center", fontsize=8.5, color=P.muted())
ax.set_ylim(36.6, 40.1)
ax.set_xlabel("Time / h")
ax.set_ylabel("Temperature / $^\\circ$C")
ax.legend(frameon=False, fontsize=8, loc="center right")
ax.set_title("A  Core temperature follows a raised set point", loc="left", fontsize=10)

bx.plot(h, rec[:, 2], color=P.edge("carbohydrate"), lw=2, label="shivering / W")
bx.plot(h, rec[:, 4], color=P.edge("blood"), lw=2, label="sweating (evaporative) / W")
bx2 = bx.twinx()
bx2.plot(h, rec[:, 3], color=P.edge("dna2"), lw=1.6, ls=":", label="skin conductance / W K$^{-1}$")
bx2.set_ylim(0, 30)
bx2.set_ylabel("Core-to-skin conductance / W K$^{-1}$ (dotted)")
bx.set_xlabel("Time / h")
bx.set_ylabel("Heat flow / W")
h1, l1 = bx.get_legend_handles_labels()
h2, l2 = bx2.get_legend_handles_labels()
bx.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="upper center")
bx.set_title("B  Effectors: heat gain first, heat loss at the crisis", loc="left", fontsize=10)
fig.tight_layout()
