# One-dimensional Muench (pressure-flow) model of a sieve tube, solved numerically (finite volumes).
# A tube of radius a and length L; 0-0.2 m is the source (sucrose loaded at a constant rate per length),
# 0.8-1.0 m the sink (first-order unloading, rate constant ku). Water exchanges with the xylem across the
# sieve-element membrane: inflow per length = 2 pi a Lp (Psi_x - P + c R T). Axial flow obeys Hagen-
# Poiseuille with sieve plates multiplying the resistance by f. Steady state (Eqs. 11.1-11.3), closed ends.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root

R, T = 8.314, 298.15
a, L, eta, f = 10e-6, 1.0, 1.7e-3, 2.0
Lp = 5e-14          # m s^-1 Pa^-1
psix = -0.5e6       # Pa
n = 120
dx = L / n
x = (np.arange(n) + 0.5) * dx
src = x < 0.2
snk = x > 0.8
area = np.pi * a**2
s_load = 1.8e-10                     # mol s^-1 per metre of source
ku = 1.2e-3                          # s^-1
cond = np.pi * a**4 / (8 * eta * f * dx)   # m^3 s^-1 Pa^-1 between neighbouring cells


def resid(z):
    P = z[:n] * 1e6
    c = z[n:] * 1e3
    Q = np.zeros(n + 1)
    Q[1:-1] = cond * (P[:-1] - P[1:])
    w = 2 * np.pi * a * Lp * dx * (psix - P + c * R * T)
    r1 = (Q[1:] - Q[:-1] - w) / 1e-14
    cu = np.where(Q[1:-1] > 0, c[:-1], c[1:])
    J = np.zeros(n + 1)
    J[1:-1] = Q[1:-1] * cu
    s = np.where(src, s_load * dx, 0.0) - np.where(snk, ku * c * area * dx, 0.0)
    r2 = (J[1:] - J[:-1] - s) / 1e-13
    return np.concatenate([r1, r2])


z0 = np.concatenate([np.linspace(1.0, 0.6, n), np.full(n, 0.5)])
sol = root(resid, z0, method="hybr", options=dict(maxfev=20000))
P = sol.x[:n]
c = sol.x[n:]
Pf = P * 1e6
Q = cond * (Pf[:-1] - Pf[1:])
xm = x[:-1] + dx / 2
u = Q / area * 3600

fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.9))
for ax in axs:
    ax.axvspan(0, 0.2, color="#4caf50", alpha=0.13, lw=0)
    ax.axvspan(0.8, 1.0, color="#e08a2c", alpha=0.13, lw=0)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Distance along sieve tube x / m")
    ax.spines[["top", "right"]].set_visible(False)
axs[0].plot(x, P, color="#2f6fb5", lw=2.3)
axs[0].set_ylabel("Turgor pressure P / MPa")
axs[0].set_title("A   Pressure", loc="left", fontsize=10)
axs[0].text(0.1, 0.04, "source", transform=axs[0].get_xaxis_transform(), ha="center", fontsize=8)
axs[0].text(0.9, 0.04, "sink", transform=axs[0].get_xaxis_transform(), ha="center", fontsize=8)
axs[1].plot(x, c, color="#b5482f", lw=2.3)
axs[1].set_ylabel("Sucrose c / (mol L⁻¹)")
axs[1].set_ylim(0, 1.1 * c.max())
axs[1].set_title("B   Concentration", loc="left", fontsize=10)
axs[2].plot(xm, u, color="#3a8a3a", lw=2.3)
axs[2].set_ylabel("Mean velocity u / (m h⁻¹)")
axs[2].set_ylim(0, 1.15 * u.max())
axs[2].set_title("C   Velocity", loc="left", fontsize=10)
fig.tight_layout()
