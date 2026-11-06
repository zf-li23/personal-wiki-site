# A pulse of auxin moving down a stem segment: 1-D advection-diffusion-decay equation
# dc/dt = D d2c/dx2 - v dc/dx - k c, solved for an instantaneous pulse (Gaussian solution),
# with polar transport (v = 10 mm/h) and without it (v = 0, diffusion and loss only).
import matplotlib.pyplot as plt
import numpy as np

D = 2.5      # mm^2 h^-1 (aqueous diffusion of IAA ~ 7e-10 m^2 s^-1)
v = 10.0     # mm h^-1
k = 0.1      # h^-1


def conc(x, t, vel):
    return np.exp(-(x - vel * t) ** 2 / (4 * D * t)) / np.sqrt(4 * np.pi * D * t) * np.exp(-k * t)


fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 4.2))
x = np.linspace(-10, 80, 900)
cols = ["#2f6fb5", "#4f9a52", "#d08a2c", "#c0504d"]
for t, col in zip((1, 2, 4, 6), cols):
    a1.plot(x, conc(x, t, v), color=col, lw=2.1, label=f"t = {t} h")
    a1.plot(x, conc(x, t, 0.0), color=col, lw=1.1, ls="--")
a1.set_xlabel("Distance from source x / mm")
a1.set_ylabel("Auxin (fraction of pulse per mm)")
a1.set_xlim(-10, 80)
a1.set_ylim(0, 0.2)
a1.text(-8, 0.185, "A", fontsize=12, fontweight="bold")
a1.text(14, 0.188, "solid: polar transport, v = 10 mm/h\ndashed: diffusion only, v = 0", fontsize=8.5)
a1.legend(frameon=False, fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 0.86))

t = np.linspace(0.02, 8, 800)
for xr, col in ((10, "#2f6fb5"), (30, "#c0504d")):
    cp = conc(xr, t, v)
    a2.plot(t, cp, color=col, lw=2.1, label=f"receiver at {xr} mm, v = 10 mm/h")
    a2.plot(t, conc(xr, t, 0.0), color=col, lw=1.1, ls="--", label=f"receiver at {xr} mm, v = 0")
    j = np.argmax(cp)
    a2.axvline(t[j], color=col, lw=0.7, ls=":")
a2.set_xlabel("Time after pulse t / h")
a2.set_ylabel("Auxin arriving (fraction per mm)")
a2.set_xlim(0, 8)
a2.set_ylim(0, 0.17)
a2.text(0.15, 0.158, "B", fontsize=12, fontweight="bold")
a2.legend(frameon=False, fontsize=8, loc="upper right")
for a in (a1, a2):
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
