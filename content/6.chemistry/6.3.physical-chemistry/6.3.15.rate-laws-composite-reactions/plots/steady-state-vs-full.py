"""Mechanism A <=> C (k1, k-1), C + B -> P (pseudo-first-order k2' = k2[B]).
Full rate equations (implicit Radau solver) compared with the steady-state and
pre-equilibrium approximations, for two sets of rate constants."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

cases = [
    (1.0, 100.0, 10.0, r"$k_{-1} = 100,\ k_2' = 10$"),
    (1.0, 1.0, 100.0, r"$k_{-1} = 1,\ k_2' = 100$"),
]
fig, axs = plt.subplots(1, 3, figsize=(13, 3.5))
for ax, (k1, km1, k2, label) in zip(axs[:2], cases):
    def rhs(t, y):
        a, c, p = y
        return [-k1 * a + km1 * c, k1 * a - km1 * c - k2 * c, k2 * c]
    tmax = 6.0 / (k1 * k2 / (km1 + k2))
    t = np.linspace(0, tmax, 400)
    sol = solve_ivp(rhs, (0, tmax), [1.0, 0.0, 0.0], method="Radau", t_eval=t, rtol=1e-8, atol=1e-11)
    k_ss = k1 * k2 / (km1 + k2)
    k_pe = k1 * k2 / km1
    ax.plot(t, sol.y[2], color="C0", lw=2.2, label="full equations")
    ax.plot(t, 1 - np.exp(-k_ss * t), color="C1", ls="--", label="steady state")
    ax.plot(t, 1 - np.exp(-k_pe * t), color="C3", ls=":", lw=1.8, label="pre-equilibrium")
    ax.set_ylim(-0.03, 1.05)
    ax.set_xlabel(r"$t$ (units of $1/k_1$)")
    ax.set_ylabel(r"$[\mathrm{P}]/[\mathrm{A}]_0$")
    ax.set_title(r"$k_1 = 1,\ $" + label, fontsize=10)
    ax.legend(frameon=False, fontsize=8, loc="lower right")

# Intermediate concentration for case 1 on a log time axis: fast transient, then quasi-steady state
k1, km1, k2, _ = cases[0]
def rhs(t, y):
    a, c, p = y
    return [-k1 * a + km1 * c, k1 * a - km1 * c - k2 * c, k2 * c]
t = np.logspace(-4, 2, 400)
sol = solve_ivp(rhs, (0, t[-1]), [1.0, 0.0, 0.0], method="Radau", t_eval=t, rtol=1e-8, atol=1e-12)
a = sol.y[0]
axs[2].semilogx(t, sol.y[1], color="C0", lw=2.2, label="[C], full equations")
axs[2].semilogx(t, k1 * a / (km1 + k2), color="C1", ls="--", label=r"$k_1[\mathrm{A}]/(k_{-1}+k_2')$")
axs[2].axvline(1 / (km1 + k2), color="0.6", ls=":", lw=1)
axs[2].text(1.3 / (km1 + k2), 0.0005, r"$1/(k_{-1}+k_2')$", fontsize=8, color="0.45")
axs[2].set_xlabel(r"$t$ (units of $1/k_1$)")
axs[2].set_ylabel(r"$[\mathrm{C}]/[\mathrm{A}]_0$")
axs[2].set_title("intermediate, first case", fontsize=10)
axs[2].set_ylim(0, 0.0125)
axs[2].legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
