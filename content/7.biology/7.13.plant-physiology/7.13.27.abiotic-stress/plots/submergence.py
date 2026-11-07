# Two strategies of rice under submergence (illustrative model).
# State: plant height h (m), carbohydrate reserve C (% of initial). Underwater, maintenance consumes C at a rate
# m (quiescence: 3 %/d; elongation: 6-7 %/d) plus 0.25 % per cm of elongation; once the leaf tips are above water
# the plant gains 4 %/d. Death when C reaches 0.
# A: flash flood, water at 1.1 m for 14 days. SUB1A (quiescence) restrains elongation (0.5 cm/d) and survives;
# a lowland variety without SUB1A elongates (5 cm/d) and exhausts its reserve before emerging.
# B: deepwater flood rising 7 cm/d to 3 m. Deepwater rice with SNORKEL1/2 elongates up to 25 cm/d and keeps its
# leaves above water; the quiescent SUB1A plant stays submerged and starves.
import matplotlib.pyplot as plt
import numpy as np


def run(water, rate_max, maint, days, h0=0.4, track=False):
    dt = 0.05
    t = np.arange(0, days, dt)
    h, C = h0, 100.0
    H, CC, alive = [], [], True
    for ti in t:
        w = water(ti)
        sub = h < w + 0.05
        if alive:
            if sub:
                g = rate_max if not track else min(rate_max, max(0.0, (w + 0.15 - h) / dt))
                C -= dt * (maint + 25 * g)
                h += dt * g
            else:
                g = 0.01
                if track:
                    g = min(rate_max, max(0.0, (w + 0.15 - h) / dt))
                h += dt * g
                C += dt * (4.0 - 25 * g)
            C = min(C, 100.0)
            if C <= 0:
                alive, C = False, 0.0
        H.append(h)
        CC.append(C)
    return t, np.array(H), np.array(CC)


fig, ax = plt.subplots(2, 2, figsize=(12, 6.6), sharex="col")
flash = lambda t: 1.1 if t < 14 else 0.0
deep = lambda t: min(3.0, 0.07 * t)
cases = [
    (0, flash, 30, [("SUB1A: quiescence", 0.005, 3.0, False, "#2e9e5b"), ("no SUB1A: elongation", 0.05, 7.0, False, "#d9463b")]),
    (1, deep, 60, [("SNORKEL1/2: escape", 0.25, 6.0, True, "#3e7cb8"), ("SUB1A: quiescence", 0.005, 3.0, False, "#2e9e5b")]),
]
for col, water, days, plants in cases:
    tt = np.arange(0, days, 0.05)
    ax[0, col].plot(tt, [water(x) for x in tt], color="0.55", lw=6, alpha=0.35, label="water level", solid_capstyle="butt")
    for name, r, m, tr, c in plants:
        t, H, C = run(water, r, m, days, track=tr)
        dead = np.argmax(C <= 0) if np.any(C <= 0) else None
        ax[0, col].plot(t, H, color=c, lw=2.2, label=name)
        ax[1, col].plot(t, C, color=c, lw=2.2, label=name)
        if dead:
            ax[1, col].plot([t[dead]], [0], "x", color=c, ms=9, mew=2)
    ax[1, col].set_xlabel("Time / d")
    ax[0, col].legend(frameon=False, fontsize=8, loc="upper left")
ax[0, 0].set_ylabel("Height / m")
ax[1, 0].set_ylabel("Carbohydrate reserve / %")
ax[0, 0].set_title("A   Flash flood (1.1 m for 14 d)", loc="left", fontsize=10)
ax[0, 1].set_title("B   Deepwater flood (rising 7 cm/d to 3 m)", loc="left", fontsize=10)
ax[0, 0].set_ylim(0, 1.6)
ax[0, 1].set_ylim(0, 3.6)
for k in (0, 1):
    ax[1, k].set_ylim(-3, 105)
ax[1, 0].text(15, 8, "× = death", fontsize=8.5, color="0.4")
fig.tight_layout()
