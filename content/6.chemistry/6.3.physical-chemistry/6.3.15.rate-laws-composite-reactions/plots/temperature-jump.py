"""Temperature-jump relaxation of A + B <=> C. After the jump the deviation from the new
equilibrium decays exponentially with 1/tau = k1([A]eq + [B]eq) + k-1, the eigenvalue of
the linearized rate equation; the full nonlinear solution is compared with it."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

k1, km1 = 1.0e9, 1.0e4      # L mol^-1 s^-1 and s^-1 at the final temperature
A0, B0 = 2.0e-5, 1.0e-5     # total concentrations, mol L^-1
K_old = 1.5 * k1 / km1      # equilibrium constant before the jump (exothermic: K falls on heating)

def eq_c(K):
    return brentq(lambda c: c - K * (A0 - c) * (B0 - c), 0, min(A0, B0))

c_old, c_new = eq_c(K_old), eq_c(k1 / km1)
inv_tau = k1 * ((A0 - c_new) + (B0 - c_new)) + km1
tau = 1 / inv_tau

def rhs(t, y):
    c = y[0]
    return [k1 * (A0 - c) * (B0 - c) - km1 * c]

t = np.linspace(0, 5 * tau, 300)
sol = solve_ivp(rhs, (0, t[-1]), [c_old], t_eval=t, method="Radau", rtol=1e-10, atol=1e-16)
dev = sol.y[0] - c_new

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
axs[0].plot(t * 1e6, sol.y[0] * 1e6, color="C0")
axs[0].axhline(c_new * 1e6, color="0.6", ls=":", lw=1)
axs[0].axhline(c_old * 1e6, color="0.6", ls=":", lw=1)
axs[0].text(t[-1] * 1e6, c_old * 1e6, "old equilibrium", ha="right", va="bottom", fontsize=8)
axs[0].text(t[-1] * 1e6, c_new * 1e6, "new equilibrium", ha="right", va="top", fontsize=8)
axs[0].set_ylim(c_new * 1e6 - 0.12, c_old * 1e6 + 0.06)
axs[0].set_xlabel(r"$t$ / $\mu$s")
axs[0].set_ylabel(r"$[\mathrm{C}]$ / ($\mu$mol L$^{-1}$)")
axs[0].set_title("after the jump", fontsize=10)

axs[1].semilogy(t / tau, np.abs(dev) / abs(dev[0]), color="C0", lw=2.2, label="full equation")
axs[1].semilogy(t / tau, np.exp(-t / tau), color="C1", ls="--", label=r"$\mathrm{e}^{-t/\tau}$")
axs[1].set_xlabel(r"$t/\tau$")
axs[1].set_ylabel(r"$\Delta x(t)/\Delta x(0)$")
axs[1].set_title(rf"$\tau$ = {tau * 1e6:.1f} $\mu$s", fontsize=10)
axs[1].legend(frameon=False, fontsize=8)
fig.tight_layout()
