"""On-axis magnetic field of finite solenoids and of a pair of coaxial coils.
Left: B(x) = (mu0 n I / 2)(cos theta2 - cos theta1) for solenoids of length L and radius R.
Right: two coils of radius R a distance d apart; d = R (Helmholtz) makes the field flattest at the midpoint."""

import numpy as np
import matplotlib.pyplot as plt

R = 1.0
x = np.linspace(-12, 12, 1201)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.9))
for L in (2.0, 5.0, 10.0):
    # distances from the field point to the two ends
    u1, u2 = x + L / 2, x - L / 2
    B = 0.5 * (u1 / np.hypot(u1, R) - u2 / np.hypot(u2, R))  # in units of mu0 n I
    ax1.plot(x, B, lw=1.8, label=f"L = {L:g} R")
ax1.axhline(1, color="0.5", ls=":", lw=1, label="infinite solenoid")
ax1.axvline(5, color="0.6", ls="--", lw=0.8)
ax1.axvline(-5, color="0.6", ls="--", lw=0.8)
ax1.set_xlabel(r"$x / R$")
ax1.set_ylabel(r"$B / (\mu_0 n I)$")
ax1.set_xlim(-12, 12)
ax1.set_ylim(0, 1.08)
ax1.legend(fontsize=8, loc="upper left")
ax1.set_title("Finite solenoids (dashed: ends of L = 10 R)", fontsize=10)

xs = np.linspace(-2, 2, 801)


def coil(xc):
    # single coil, in units of mu0 N I / R
    return 0.5 * R**3 / (R**2 + (xs - xc) ** 2) ** 1.5


for d in (0.6, 1.0, 1.6):
    B = coil(-d / 2) + coil(d / 2)
    ax2.plot(xs, B, lw=2 if d == 1.0 else 1.4, label=f"d = {d:g} R" + (" (Helmholtz)" if d == 1.0 else ""))
ax2.axhline(8 / (5 * np.sqrt(5)), color="0.5", ls=":", lw=1)
ax2.set_xlabel(r"$x / R$ (from the midpoint)")
ax2.set_ylabel(r"$B / (\mu_0 N I / R)$")
ax2.set_xlim(-2, 2)
ax2.legend(fontsize=8, loc="lower center")
ax2.set_title("Two coaxial coils", fontsize=10)
fig.tight_layout()
