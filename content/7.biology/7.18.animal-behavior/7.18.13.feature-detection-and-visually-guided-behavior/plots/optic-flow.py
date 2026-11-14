"""Two flight controllers that use only image speed (after Srinivasan and colleagues).

A: centring in a corridor. A bee at lateral position y between walls at y = -1 and +1 flies at
speed v; the image of each wall moves across the eye at angular speed v / (distance), reduced
by the wall's own speed if the wall moves in the bee's direction. Steering: dy/dt = -k (w_left - w_right) (left wall at y = +1),
moving away from the side with faster image motion. With stationary walls the bee centres; if the
right wall moves forward at 0.5 v, the image there slows and the bee equilibrates closer to it.
B, C: grazing landing. If the bee keeps the angular speed of the ground image constant
(w = v / h) while descending at a constant angle, both height and forward speed fall
exponentially and the bee arrives with near-zero speed, without measuring distance or speed.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6))
a = axs[0]
x = np.linspace(0, 6, 600)
dx = x[1] - x[0]
for wall_speed, y0, col, lab in ((0.0, 0.7, P.edge("dna"), "walls stationary"),
                                  (0.0, -0.6, P.edge("dna"), None),
                                  (0.5, 0.5, P.edge("rna"), "right wall moving with the bee")):
    y = [y0]
    for _ in x[1:]:
        wl = 1.0 / (1 - y[-1])
        wr = (1.0 - wall_speed) / (1 + y[-1])
        y.append(y[-1] - 1.2 * (wl - wr) * dx * 0.5)
    a.plot(x, y, color=col, lw=2, label=lab)
a.axhline(1, color=P.ink(), lw=2); a.axhline(-1, color=P.ink(), lw=2)
a.text(5.9, -1.15, "right wall", fontsize=7.5, ha="right", va="top", color=P.muted())
a.text(5.9, 1.08, "left wall", fontsize=7.5, ha="right", color=P.muted())
a.set_ylim(-1.3, 1.3)
a.set_xlabel("Distance along corridor")
a.set_ylabel("Lateral position y")
a.legend(frameon=False, fontsize=7.5, loc="center right", bbox_to_anchor=(1, 0.3))
a.set_title("A", loc="left", fontweight="bold")
w, gamma = 2.0, np.radians(30)
t = np.linspace(0, 3, 300)
h0 = 1.0
h = h0 * np.exp(-w * np.tan(gamma) * t)
v = w * h
axs[1].plot(t, h, color=P.edge("dna"), lw=2, label="height h")
axs[1].plot(t, v, color=P.edge("rna"), lw=2, label="forward speed v")
axs[1].set_xlabel("Time / s")
axs[1].set_ylabel("Height / m; speed / m s$^{-1}$")
axs[1].legend(frameon=False, fontsize=8)
axs[1].set_title("B", loc="left", fontweight="bold")
axs[2].plot(h, v, color=P.edge("dna"), lw=2)
axs[2].text(0.15, 1.6, "v = ω h:\nspeed proportional\nto height", fontsize=8, color=P.ink())
axs[2].set_xlabel("Height / m")
axs[2].set_ylabel("Forward speed / m s$^{-1}$")
axs[2].set_title("C", loc="left", fontweight="bold")
for ax in axs:
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
