"""Kepler's second law: an orbit in an inverse-square central force, integrated numerically.
Sectors swept in equal time intervals have equal areas; the speed is largest at perihelion."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

GM = 1.0
e = 0.6           # eccentricity
a = 1.0           # semi-major axis
r_p = a * (1 - e)  # perihelion distance
v_p = np.sqrt(GM * (1 + e) / r_p)  # speed at perihelion (vis-viva)
period = 2 * np.pi * np.sqrt(a**3 / GM)


def rhs(t, y):
    x, z, vx, vz = y
    r3 = np.hypot(x, z) ** 3
    return [vx, vz, -GM * x / r3, -GM * z / r3]


n_sectors = 12
t_eval = np.linspace(0, period, 1201)
sol = solve_ivp(rhs, (0, period), [r_p, 0, 0, v_p], t_eval=t_eval, rtol=1e-10, atol=1e-12)
x, z, vx, vz = sol.y

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw={"width_ratios": [1.25, 1]})
ax1.plot(x, z, color="0.4", lw=1.2)
step = (len(t_eval) - 1) // n_sectors
for k in range(n_sectors):
    idx = slice(k * step, (k + 1) * step + 1)
    if k % 2 == 0:
        ax1.fill(np.r_[0, x[idx], 0], np.r_[0, z[idx], 0], color="C0", alpha=0.35, lw=0)
    ax1.plot([0, x[k * step]], [0, z[k * step]], color="C0", lw=0.6)
ax1.plot(0, 0, "o", color="C1", ms=8, label="center of force (Sun)")
ax1.set_aspect("equal")
ax1.set_xlabel("x / a")
ax1.set_ylabel("y / a")
ax1.set_title(f"Equal times, equal areas (e = {e}, {n_sectors} sectors)", fontsize=10)
ax1.legend(fontsize=8, loc="lower left")

# areal velocity (1/2)|r x v| and speed along the orbit
areal = 0.5 * np.abs(x * vz - z * vx)
speed = np.hypot(vx, vz)
ax2.plot(t_eval / period, speed / speed.mean(), color="C1", lw=1.8, label="speed / mean speed")
ax2.plot(t_eval / period, areal / areal[0], color="C0", lw=1.8, ls="--", label="areal velocity / initial value")
ax2.set_xlabel("t / T")
ax2.set_xlim(0, 1)
ax2.set_title("Speed varies, areal velocity is constant", fontsize=10)
ax2.legend(fontsize=8, loc="upper center")
fig.tight_layout()
