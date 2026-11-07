"""Heat-balance model of human thermoregulation: core temperature against ambient temperature.

One-compartment core (heat capacity C = 245 kJ/K, 70 kg) with proportional controllers acting on the error
e = Tc - Tset (Tset = 37 C), nude subject at rest:
  metabolism M = 80 W * Q10^((Tc - 37)/10), Q10 = 2.3; shivering S = 250 W * clip(-e/0.5 C, 0, 1), fading between
  33 and 30 C core temperature (hypothalamic depression);
  core-to-environment conductance K = 12 W/K (vasoconstricted) to 25 W/K (vasodilated), sigmoid in e;
  evaporation E = 20 W (insensible) + sweating min(Emax, 1000 W/C * max(e, 0)); Emax = 500 W in dry air (about
  0.75 L/h of sweat evaporated) and 0 W in saturated air.
  C dTc/dt = M + S - K (Tc - Ta) - E.
A: core temperature after 6 h at each ambient temperature (capped at 44 C and 20 C): a plateau between about 11 and
54 C in dry air, narrowed to below 35 C in saturated air; outside it the feedback fails and Q10 makes it run away.
B: steady heat flows in dry air.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
Cap = 245e3


def flows(tc, ta, emax):
    e = tc - 37.0
    m = 80 * 2.3 ** ((tc - 37) / 10)
    fade = np.clip((tc - 30) / 3, 0, 1)
    s = 250 * np.clip(-e / 0.5, 0, 1) * fade
    k = 12 + 13 / (1 + np.exp(-(e - 0.1) / 0.08))
    ev = 20 + min(emax, 1000 * max(e, 0))
    return m + s, k * (tc - ta), ev


def settle(ta, emax, hours=6, dt=10.0):
    tc = 37.0
    for _ in range(int(hours * 3600 / dt)):
        h, d, ev = flows(tc, ta, emax)
        tc += dt * (h - d - ev) / Cap
        if tc > 44 or tc < 20:
            break
    return tc


ta = np.linspace(-10, 65, 151)
dry = np.array([settle(t, 500) for t in ta])
wet = np.array([settle(t, 0) for t in ta])

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.6))
ax.plot(ta, np.clip(dry, 20, 44), color=P.edge("dna"), lw=2.2, label="dry air")
ax.plot(ta, np.clip(wet, 20, 44), color=P.edge("rna"), lw=2, ls="--", label="saturated air (no evaporation)")
ax.axhspan(36.5, 37.5, color=P.fill("positive"), alpha=0.25, lw=0)
ax.axhline(40.5, color=P.edge("negative"), ls=":", lw=1)
ax.text(-9, 40.8, "heatstroke", fontsize=8, color=P.edge("negative"))
ax.axhline(35, color=P.edge("dna2"), ls=":", lw=1)
ax.text(-9, 34.2, "hypothermia", fontsize=8, color=P.edge("dna2"))
ax.set_xlabel("Ambient temperature $T_{\\mathrm{a}}$ / $^\\circ$C")
ax.set_ylabel("Core temperature after 6 h / $^\\circ$C")
ax.set_ylim(20, 44.5)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  Feedback keeps the core temperature on a plateau", loc="left", fontsize=10)

ta2 = np.linspace(12, 56, 89)
H, D, E = [], [], []
for t in ta2:
    tc = settle(t, 500, hours=12)
    h, d, ev = flows(tc, t, 500)
    H.append(h)
    D.append(d)
    E.append(ev)
bx.plot(ta2, H, color=P.edge("carbohydrate"), lw=2, label="heat production (metabolism + shivering)")
bx.plot(ta2, D, color=P.edge("dna"), lw=2, label="dry heat loss K (Tc - Ta)")
bx.plot(ta2, E, color=P.edge("blood"), lw=2, label="evaporative heat loss")
bx.axhline(0, color=P.muted(), lw=0.8)
bx.axvline(37, color=P.muted(), lw=0.8, ls=":")
bx.text(37.5, 420, "Ta = Tc: only\nevaporation can\nremove heat", fontsize=8, color=P.muted())
bx.set_xlabel("Ambient temperature $T_{\\mathrm{a}}$ / $^\\circ$C")
bx.set_ylabel("Heat flow / W")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Heat flows at steady state (dry air)", loc="left", fontsize=10)
fig.tight_layout()
