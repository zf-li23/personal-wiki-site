"""I2(g) = 2 I(g): standard equilibrium constant from molecular partition functions
(rigid rotor, harmonic oscillator; spectroscopic constants of I2, ground-state dissociation
energy D0 = 12440.9 cm^-1, iodine atom 2P3/2 ground level with 2P1/2 at 7603 cm^-1),
compared with thermochemical estimates from 298.15 K data (constant Delta_r C_p, or Delta_r C_p = 0).
Right: degree of dissociation at a total pressure of 1 bar."""

import numpy as np
import matplotlib.pyplot as plt

h, k, NA, c = 6.62607015e-34, 1.380649e-23, 6.02214076e23, 299792458.0
R = k * NA
c2 = h * c * 100 / k                                # second radiation constant, cm K
p0 = 1e5


def ln_qt_per_n(M, T):
    m = M * 1e-3 / NA
    return np.log((2 * np.pi * m * k * T / h**2) ** 1.5 * k * T / p0)


th_r, th_v, d0 = c2 * 0.03737, c2 * 214.5, c2 * 12440.9


def ln_k_stat(T):
    ln_q_i = ln_qt_per_n(126.90447, T) + np.log(4 + 2 * np.exp(-c2 * 7603.15 / T))
    ln_q_i2 = ln_qt_per_n(253.80894, T) + np.log(T / (2 * th_r)) - np.log(-np.expm1(-th_v / T))
    return 2 * ln_q_i - ln_q_i2 - d0 / T


# CRC data at 298.15 K: I(g) and I2(g)
dh298 = (2 * 106.76 - 62.42) * 1e3
ds298 = 2 * 180.79 - 260.69
dcp = 2 * 20.79 - 36.90


def ln_k_thermo(T, dcp=dcp):
    dh = dh298 + dcp * (T - 298.15)
    ds = ds298 + dcp * np.log(T / 298.15)
    return -(dh - T * ds) / (R * T)


T = np.linspace(600, 1800, 300)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.plot(1000 / T, ln_k_stat(T) / np.log(10), color="C0", lw=1.8, label="partition functions")
a1.plot(1000 / T, ln_k_thermo(T) / np.log(10), color="C1", lw=1.4, ls="--", label=r"thermochemical, constant $\Delta_\mathrm{r}C_p$")
a1.plot(1000 / T, ln_k_thermo(T, 0.0) / np.log(10), color="C2", lw=1.2, ls=":", label=r"thermochemical, $\Delta_\mathrm{r}C_p = 0$")
a1.set_xlabel(r"$1000\,\mathrm{K}/T$")
a1.set_ylabel(r"$\lg K^\circ$")
a1.legend(frameon=False, fontsize=9)

kk = np.exp(ln_k_stat(T))
alpha = np.sqrt(kk / (kk + 4))                      # K = 4 a^2 / (1 - a^2) at p = p0
a2.plot(T, alpha, color="C0", lw=1.8)
a2.set_xlabel(r"$T$ / K")
a2.set_ylabel(r"degree of dissociation at $p = p^\circ$")
a2.set_ylim(0, 1)
fig.tight_layout()
