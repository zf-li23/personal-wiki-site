"""Dominance of the most probable distribution.

N distinguishable particles on three non-degenerate, equally spaced levels (0, e, 2e)
with total energy U = M e and M = N/2. A distribution is fixed by j = N_2:
N_1 = M - 2j, N_0 = N - M + j, and t_D = N! / (N_0! N_1! N_2!).
Left: t_D / Omega against N_2 / N for growing N (exact log-gamma arithmetic); the dashed
line marks the Boltzmann prediction N_2 / N = x^2 / (1 + x + x^2), with x = exp(-e/kT)
fixed by the mean energy. Right: ln t_max / ln Omega approaches 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln
from scipy.optimize import brentq

x_b = brentq(lambda x: (x + 2 * x**2) / (1 + x + x**2) - 0.5, 1e-6, 1.0)
f2_b = x_b**2 / (1 + x_b + x_b**2)


def log_t(n):
    m = n // 2
    j = np.arange(0, m // 2 + 1)
    n1, n0 = m - 2 * j, n - m + j
    lt = gammaln(n + 1) - gammaln(n0 + 1) - gammaln(n1 + 1) - gammaln(j + 1)
    return j, lt


fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
for n, c in zip([40, 400, 4000, 40000], ["C0", "C1", "C2", "C3"]):
    j, lt = log_t(n)
    log_omega = lt.max() + np.log(np.exp(lt - lt.max()).sum())
    a1.plot(j / n, np.exp(lt - log_omega) * n, color=c, lw=1.6, label=f"N = {n}")
a1.axvline(f2_b, color="0.4", ls="--", lw=1)
a1.annotate("Boltzmann\n" + rf"$N_2/N$ = {f2_b:.3f}", (f2_b + 0.01, 60), fontsize=9)
a1.set_xlim(0, 0.25)
a1.set_xlabel(r"$N_2/N$")
a1.set_ylabel(r"$N\,t_D/\Omega$ (probability density)")
a1.legend(frameon=False, fontsize=9)

ns = np.unique(np.logspace(1, 6, 30).astype(int) // 4 * 4)
ratio = []
for n in ns:
    j, lt = log_t(int(n))
    log_omega = lt.max() + np.log(np.exp(lt - lt.max()).sum())
    ratio.append(lt.max() / log_omega)
a2.semilogx(ns, ratio, "o-", color="C0", ms=3, lw=1.4)
a2.axhline(1, color="0.4", ls="--", lw=1)
a2.set_xlabel(r"$N$")
a2.set_ylabel(r"$\ln t_{\max}/\ln\Omega$")
fig.tight_layout()
