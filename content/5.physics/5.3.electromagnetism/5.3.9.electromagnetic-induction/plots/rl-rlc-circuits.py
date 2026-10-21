"""Current in an RL circuit (switch on and off) and charge in a series RLC circuit."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))

# RL circuit, time in units of tau = L / R, current in units of emf / R
t = np.linspace(0, 6, 601)
ax1.plot(t, 1 - np.exp(-t), lw=2, label="switch closed: 1 - exp(-t/tau)")
ax1.plot(t, np.exp(-t), lw=2, label="source removed: exp(-t/tau)")
ax1.axvline(1, color="0.6", lw=0.8, ls="--")
ax1.axhline(1 - np.exp(-1), color="0.6", lw=0.8, ls=":")
ax1.axhline(np.exp(-1), color="0.6", lw=0.8, ls=":")
ax1.text(1.08, 0.05, "t = tau = L/R", fontsize=9)
ax1.set_xlabel("t / tau")
ax1.set_ylabel("i / (emf / R)")
ax1.set_title("RL circuit", fontsize=10)
ax1.legend(fontsize=8, loc="center right")

# series RLC, free decay from q(0) = q0, i(0) = 0; time in units of 1/omega0
t = np.linspace(0, 20, 2001)
for zeta, name in [(0.1, "underdamped"), (1.0, "critically damped"), (2.0, "overdamped")]:
    # q'' + 2 zeta q' + q = 0
    if zeta < 1:
        wd = np.sqrt(1 - zeta**2)
        q = np.exp(-zeta * t) * (np.cos(wd * t) + zeta / wd * np.sin(wd * t))
    elif zeta == 1:
        q = np.exp(-t) * (1 + t)
    else:
        s = np.sqrt(zeta**2 - 1)
        r1, r2 = -zeta + s, -zeta - s
        q = (r2 * np.exp(r1 * t) - r1 * np.exp(r2 * t)) / (r2 - r1)
    ax2.plot(t, q, lw=1.8, label=f"{name}, R/(2L omega0) = {zeta:g}")
ax2.axhline(0, color="0.6", lw=0.7)
ax2.set_xlabel("omega0 t,  omega0 = 1/sqrt(LC)")
ax2.set_ylabel("q / q0")
ax2.set_title("series RLC circuit, capacitor initially charged", fontsize=10)
ax2.legend(fontsize=8)
fig.tight_layout()
