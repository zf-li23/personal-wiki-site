"""Simulated chromatograms of the n-alkanes C6-C14 (equal amounts) on a capillary column
(hold-up time 1 min, N = 50 000). Retention follows ln k = a + b n + (h0 + h1 n)/(R T) with
illustrative constants (about 4.5 kJ/mol of retention enthalpy per CH2 group), so k grows
geometrically with the carbon number n and falls with temperature. Isothermal at 80 °C the
late peaks are broad, low and very slow; at 180 °C the early peaks crowd together near the
hold-up time; a program of 50 °C + 10 °C/min spaces the homologues almost evenly with
similar widths. Elution under the program is found by integrating dz/dt = (L/tM)/(1 + k(T(t)))."""

import numpy as np
import matplotlib.pyplot as plt

R = 8.314
a, b, h0, h1 = -7.6, -0.55, 5000.0, 4500.0
tM, N = 1.0, 5.0e4
ns = np.arange(6, 15)


def k_of(n, T):
    return np.exp(a + b * n + (h0 + h1 * n) / (R * T))


def peaks(tr, sig, t):
    y = np.zeros_like(t)
    for m, s in zip(tr, sig):
        y += np.exp(-0.5 * ((t - m) / s) ** 2) / s
    return y


fig, axes = plt.subplots(3, 1, figsize=(9.0, 6.6))
t = np.linspace(0, 32, 120000)
for ax, Tc in zip(axes[:2], [80, 180]):
    k = k_of(ns, Tc + 273.15)
    tr = tM * (1 + k)
    sig = tr / np.sqrt(N)
    y = peaks(tr, sig, t)
    ax.plot(t, y / y.max(), color="C0", lw=0.8)
    shown = [(n, m) for n, m in zip(ns, tr) if m < 31]
    for j, (n, m) in enumerate(shown):
        if Tc == 180 and n < 11:
            ax.annotate(f"C{n}", (m, 0.0), xytext=(1.6 + 0.9 * j, 1.0 - 0.13 * j), fontsize=7,
                        arrowprops=dict(arrowstyle="-", color="0.6", lw=0.5))
        else:
            ax.text(m, 1.04, f"C{n}", ha="center", fontsize=7)
    late = [m for m in tr if m >= 31]
    if late:
        ax.text(31.5, 0.6, f"C{ns[len(shown)]}-C14 elute at {late[0]:.0f}-{late[-1]:.0f} min",
                ha="right", fontsize=8)
    ax.set_title(f"isothermal {Tc} \u00b0C", fontsize=9, loc="left")

# temperature program 50 °C + 10 °C/min, hold at 250 C
dt = 0.0005
tt = np.arange(0, 40, dt)
T = np.minimum(50 + 10 * tt, 250) + 273.15
tr, sig = [], []
for n in ns:
    kk = k_of(n, T)
    z = np.cumsum(dt / (tM * (1 + kk)))          # fraction of column length travelled
    i = np.searchsorted(z, 1.0)
    tr.append(tt[i])
    sig.append(tM * (1 + kk[i]) / np.sqrt(N))
y = peaks(tr, sig, t)
axes[2].plot(t, y / y.max(), color="C3", lw=0.8)
for n, m in zip(ns, tr):
    axes[2].text(m, 1.04, f"C{n}", ha="center", fontsize=7)
axes[2].set_title("programmed: 50 \u00b0C, then 10 \u00b0C/min", fontsize=9, loc="left")
for ax in axes:
    ax.set_xlim(0, 32)
    ax.set_ylim(0, 1.2)
    ax.set_yticks([])
axes[2].set_xlabel("time / min")
fig.tight_layout()
