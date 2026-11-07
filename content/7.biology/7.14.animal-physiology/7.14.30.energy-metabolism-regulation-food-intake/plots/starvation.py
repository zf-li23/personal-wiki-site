"""Depletion of fuel stores during total starvation (schematic compartment model).

Stores are drawn in a fixed order: glycogen first, then fat with a small protein share, protein last.
Energy density: glycogen and protein 17 kJ/g, fat 39 kJ/g. Lean tissue is ~4 g wet mass per g protein.
A, lean 70 kg man: 0.23 kg glycogen, 15 kg fat, 6 kg protein; expenditure 7.5 MJ/d falling by 20 % with a
14-day time constant (adaptive reduction of metabolic rate). Protein oxidation starts at ~75 g/d and falls towards
20 g/d (time constant 10 d) as ketone bodies replace glucose for the brain; when fat is nearly exhausted (< 3 %)
protein must cover the whole expenditure. Death is placed where half of body protein is lost.
B, male emperor penguin (schematic, illustrative parameters): 38 kg, 12 kg fat, 5 kg protein, 4 MJ/d; phase I
(short, falling protein use), phase II (protein ~4 % of energy), phase III (fat < 15 % of initial: protein share
rises progressively); the bird abandons the egg early in phase III (refeeding signal).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def run(days, gly0, fat0, prot0, E0, adapt, p_hi, p_lo, tau_p, fat_end, dt=0.05):
    n = int(days / dt)
    g, f, p = gly0, fat0, prot0
    out = np.zeros((n, 5))
    for i in range(n):
        t = i * dt
        E = E0 * (1 - adapt * (1 - np.exp(-t / 14)))  # MJ/d
        if g > 0:
            dg = min(g, E / 17 * dt)  # kg glycogen
            g -= dg
            e_left = E - dg / dt * 17
        else:
            e_left = E
        pr = p_lo + (p_hi - p_lo) * np.exp(-t / tau_p)  # kg/d protein while fat is plentiful
        pr = min(pr, e_left / 17)
        if f < fat_end * fat0:  # fat running out: protein takes over progressively
            s0 = pr * 17 / e_left
            s = s0 + (1 - s0) * (1 - f / (fat_end * fat0)) ** 0.5
            pr = s * e_left / 17
        fr = (e_left - pr * 17) / 39
        if f <= 0:
            pr, fr = e_left / 17, 0.0
        p -= pr * dt
        f = max(f - fr * dt, 0.0)
        share = pr * 17 / E
        out[i] = t, g / gly0, f / fat0, p / prot0, share
        if p < 0.5 * prot0:
            return out[: i + 1]
    return out


fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.6))
o = run(150, 0.23, 15, 6, 7.5, 0.2, 0.075, 0.02, 10, 0.03)
t = o[:, 0]
ax.plot(t, 100 * o[:, 1], color=P.edge("carbohydrate"), lw=2, label="glycogen (0.23 kg)")
ax.plot(t, 100 * o[:, 2], color=P.edge("lipid"), lw=2, label="fat (15 kg)")
ax.plot(t, 100 * o[:, 3], color=P.edge("protein"), lw=2, label="protein (6 kg)")
ax.axhline(50, color=P.edge("negative"), ls=":", lw=1)
ax.text(2, 52, "half of body protein lost: death", fontsize=8, color=P.edge("negative"))
ax.plot(t[-1], 50, "x", color=P.edge("negative"), ms=9, mew=2)
ax.set_xlabel("Days of total starvation")
ax.set_ylabel("Store remaining / % of initial")
ax.set_ylim(0, 105)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title(f"A  Lean 70 kg man (model: death on day {t[-1]:.0f})", loc="left", fontsize=10)

o = run(160, 0.15, 12, 5, 4.0, 0.0, 0.06, 0.008, 3, 0.15)
t = o[:, 0]
mass = 38 - (12 * (1 - o[:, 2]) + 4 * 5 * (1 - o[:, 3]) + 0.15 * (1 - o[:, 1]))
bx.plot(t, mass, color=P.edge("animal"), lw=2, label="body mass")
bx.set_xlabel("Days of fasting")
bx.set_ylabel("Body mass / kg")
bx2 = bx.twinx()
bx2.plot(t, 100 * o[:, 4], color=P.edge("protein"), lw=1.8, ls="--", label="protein share of energy")
bx2.set_ylabel("Protein share of energy / % (dashed)")
bx2.set_ylim(0, 100)
i3 = np.argmax(o[:, 2] <= 0.15 + 1e-9)
for x0, x1, lab in ((0, 4, "I"), (4, t[i3], "II"), (t[i3], t[-1], "III")):
    bx.axvspan(x0, x1, color=P.fill("neutral") if lab != "II" else P.fill("positive"), alpha=0.18, lw=0)
    bx.text((x0 + x1) / 2, 37.3, lab, ha="center", fontsize=10, color=P.muted())
bx.annotate("refeeding signal:\negg abandoned", (t[i3] + 2, mass[i3]), xytext=(t[i3] - 75, 22),
            fontsize=8, color=P.muted(), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
bx.set_ylim(15, 39)
h1, l1 = bx.get_legend_handles_labels()
h2, l2 = bx2.get_legend_handles_labels()
bx.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  Fasting male emperor penguin (schematic)", loc="left", fontsize=10)
fig.tight_layout()
