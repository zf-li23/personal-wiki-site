"""Simulated first-order 1H NMR spectrum of 1-chloropropane, CH3-CH2-CH2Cl, at 400 MHz with an
integral trace. Shifts and couplings (CDCl3): CH2Cl 3.52 (t, J = 6.6 Hz), CH2 1.81 (couples to
2 H with 6.6 Hz and 3 H with 7.4 Hz: 12 lines that crowd into an apparent sextet), CH3 1.04
(t, J = 7.4 Hz). Insets show each multiplet on a Hz scale."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb

MHZ = 400.0
WIDTH = 0.6  # Lorentzian half-width at half-height, Hz


def lines(delta, n_h, couplings):
    """First-order multiplet: positions (ppm) and intensities. couplings = [(n equivalent spins, J in Hz)]."""
    pos, amp = np.array([delta * MHZ]), np.array([float(n_h)])
    for n, j in couplings:
        offs = np.array([(k - n / 2) * j for k in range(n + 1)])
        wts = np.array([comb(n, k) for k in range(n + 1)], float) / 2**n
        pos = (pos[:, None] + offs[None, :]).ravel()
        amp = (amp[:, None] * wts[None, :]).ravel()
    return pos / MHZ, amp


def spectrum(x_ppm, groups):
    y = np.zeros_like(x_ppm)
    xh = x_ppm * MHZ
    for g in groups:
        p, a = lines(*g)
        for pi, ai in zip(p * MHZ, a):
            y += ai * WIDTH / np.pi / ((xh - pi) ** 2 + WIDTH**2)
    return y


groups = [(3.52, 2, [(2, 6.6)]), (1.81, 2, [(2, 6.6), (3, 7.4)]), (1.04, 3, [(2, 7.4)])]
names = ["CH$_2$Cl (t)", "CH$_2$ (12 lines)", "CH$_3$ (t)"]
x = np.linspace(-0.3, 4.2, 40000)
y = spectrum(x, groups + [(0.0, 0.3, [])])
top = y.max()

fig = plt.figure(figsize=(9, 5.4))
ax = fig.add_axes([0.05, 0.42, 0.92, 0.55])
ax.plot(x, y / top, color="C0", lw=1)
integral = np.cumsum(y[::-1])[::-1]
integral = (integral - integral[-1]) / (integral[0] - integral[-1])
ax.plot(x, 1.1 + 0.4 * integral, color="C3", lw=1)
ax.set_xlim(4.2, -0.3)
ax.set_ylim(-0.05, 1.65)
ax.set_yticks([])
ax.set_xlabel(r"$\delta$ / ppm")
for d, n, _ in groups:
    ax.text(d - 0.08, 1.05, f"{n} H", ha="left", fontsize=9, color="C3")
for (d, n, _), name in zip(groups, names):
    ax.text(d, 0.72 if n == 3 else 0.62, name, ha="center", fontsize=9)
ax.text(0.0, 0.2, "TMS", ha="center", fontsize=8)

for i, ((d, n, cpl), name) in enumerate(zip(groups, names)):
    inset = fig.add_axes([0.05 + 0.32 * i, 0.08, 0.28, 0.22])
    xi = np.linspace(d - 0.08, d + 0.08, 4000)
    yi = spectrum(xi, [(d, n, cpl)])
    inset.plot((xi - d) * MHZ, yi / yi.max(), color="C0", lw=1)
    inset.set_xlim(30, -30)
    inset.set_yticks([])
    inset.tick_params(labelsize=8)
    inset.set_xlabel(f"Hz from {d:.2f} ppm", fontsize=8)
    inset.set_title(name, fontsize=9)
