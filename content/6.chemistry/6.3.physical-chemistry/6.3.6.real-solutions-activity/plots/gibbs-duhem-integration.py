"""Activity coefficient of B obtained from measurements of gamma_A alone by integrating the
Gibbs-Duhem equation x_A dln(gamma_A) + x_B dln(gamma_B) = 0 (constant T, p).
Synthetic 'data': two-parameter Margules model (A_AB = 0.9, A_BA = 1.6) with 1 % noise on gamma_A;
the noisy ln gamma_A is smoothed by a polynomial in x_B before the numerical integration."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

a_ab, a_ba = 0.9, 1.6


def ln_gA(xb):
    xa = 1 - xb
    return xb**2 * (a_ab + 2 * (a_ba - a_ab) * xa)


def ln_gB(xb):
    xa = 1 - xb
    return xa**2 * (a_ba + 2 * (a_ab - a_ba) * xb)


rng = np.random.default_rng(0)
xb_data = np.linspace(0.05, 0.95, 19)
lnA_data = ln_gA(xb_data) + np.log(1 + 0.01 * rng.standard_normal(xb_data.size))

# smooth: ln gamma_A must vanish like x_B^2 as x_B -> 0, so fit c2 x^2 + c3 x^3 + c4 x^4
X = np.vstack([xb_data**2, xb_data**3, xb_data**4]).T
c, *_ = np.linalg.lstsq(X, lnA_data, rcond=None)
xb = np.linspace(1e-4, 1, 2000)
lnA_fit = c[0] * xb**2 + c[1] * xb**3 + c[2] * xb**4
dlnA = np.gradient(lnA_fit, xb)
# d ln gamma_B = -(x_A/x_B) d ln gamma_A; integrate from x_B = 1 where gamma_B = 1 (Raoult convention)
integrand = -(1 - xb) / xb * dlnA
lnB = cumulative_trapezoid(integrand, xb, initial=0)
lnB = lnB - lnB[-1]

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(xb_data, lnA_data, "o", color="C0", ms=4, label=r"'measured' $\ln\gamma_\mathrm{A}$")
ax.plot(xb, lnA_fit, color="C0", lw=1.4, label=r"smoothed $\ln\gamma_\mathrm{A}$")
ax.plot(xb, lnB, color="C1", lw=2.0, label=r"$\ln\gamma_\mathrm{B}$ from Gibbs-Duhem")
ax.plot(xb, ln_gB(xb), color="C3", lw=1.0, ls="--", label=r"true $\ln\gamma_\mathrm{B}$ (model)")
ax.set_xlabel(r"$x_\mathrm{B}$")
ax.set_ylabel(r"$\ln\gamma$")
ax.set_xlim(0, 1)
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
