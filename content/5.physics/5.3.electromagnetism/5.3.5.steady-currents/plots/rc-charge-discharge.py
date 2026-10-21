"""Charging and discharging of a capacitor through a resistor: exponential approach with time constant tau = RC.
The right panel checks the analytic solution against a numerical integration of R dq/dt + q/C = emf."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R, C, emf = 1.0e3, 1.0e-3, 10.0  # 1 kOhm, 1 mF, 10 V -> tau = 1 s
tau = R * C
t = np.linspace(0, 5 * tau, 500)

u_charge = emf * (1 - np.exp(-t / tau))
u_discharge = emf * np.exp(-t / tau)
i_charge = emf / R * np.exp(-t / tau)

sol = solve_ivp(lambda s, q: [(emf - q[0] / C) / R], (0, 5 * tau), [0.0], t_eval=t[::25], rtol=1e-9)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.8))
ax1.plot(t / tau, u_charge / emf, lw=2, label="charging: $u_C$")
ax1.plot(t / tau, u_discharge / emf, lw=2, ls="--", label="discharging: $u_C$")
ax1.plot(sol.t / tau, sol.y[0] / C / emf, "o", ms=4, color="C0", mfc="none", label="numerical (charging)")
ax1.axhline(1 - np.exp(-1), color="0.6", lw=0.8, ls=":")
ax1.axvline(1, color="0.6", lw=0.8, ls=":")
ax1.text(1.05, 0.05, r"$t = \tau$", fontsize=9)
ax1.text(1.1, 1 - np.exp(-1) - 0.07, r"$1 - \mathrm{e}^{-1} \approx 0.63$", fontsize=9)
ax1.set_xlabel(r"$t / \tau$")
ax1.set_ylabel(r"$u_C / \mathcal{E}$")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 1.05)
ax1.legend(fontsize=8, loc="lower right", bbox_to_anchor=(1.0, 0.12))

ax2.plot(t / tau, i_charge * R / emf, lw=2, color="C2", label="charging current")
ax2.plot(t / tau, -i_charge * R / emf, lw=2, ls="--", color="C3", label="discharging current")
ax2.axhline(0, color="0.5", lw=0.8)
ax2.set_xlabel(r"$t / \tau$")
ax2.set_ylabel(r"$i R / \mathcal{E}$")
ax2.set_xlim(0, 5)
ax2.legend(fontsize=8, loc="upper right")
fig.tight_layout()
