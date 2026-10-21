"""Maxwell speed distribution f(v) for N2 at several temperatures and for several gases at 300 K."""

import numpy as np
import matplotlib.pyplot as plt

kB = 1.380649e-23
NA = 6.02214076e23


def maxwell(v, M, T):
    m = M / NA
    a = m / (2 * kB * T)
    return 4 * np.pi * (a / np.pi) ** 1.5 * v**2 * np.exp(-a * v**2)


v = np.linspace(0, 3000, 1500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

M_N2 = 0.028
for i, T in enumerate([100, 300, 1000]):
    f = maxwell(v, M_N2, T)
    ax1.plot(v, f * 1e3, color=f"C{i}", lw=1.6, label=f"T = {T} K")
    vp = np.sqrt(2 * kB * T * NA / M_N2)
    ax1.plot([vp, vp], [0, maxwell(vp, M_N2, T) * 1e3], ":", color=f"C{i}", lw=1)
ax1.set_xlim(0, 2000)
ax1.set_ylim(bottom=0)
ax1.set_xlabel(r"$v$ / (m s$^{-1}$)")
ax1.set_ylabel(r"$f(v)$ / ($10^{-3}$ s m$^{-1}$)")
ax1.set_title(r"N$_2$ at different temperatures")
ax1.legend(fontsize=9)

gases = [("Xe", 0.1313), ("O$_2$", 0.032), ("He", 0.004), ("H$_2$", 0.002016)]
for i, (name, M) in enumerate(gases):
    ax2.plot(v, maxwell(v, M, 300) * 1e3, color=f"C{i}", lw=1.6, label=name)
ax2.set_xlim(0, 3000)
ax2.set_ylim(bottom=0)
ax2.set_xlabel(r"$v$ / (m s$^{-1}$)")
ax2.set_ylabel(r"$f(v)$ / ($10^{-3}$ s m$^{-1}$)")
ax2.set_title("Different gases at T = 300 K")
ax2.legend(fontsize=9)

fig.tight_layout()
