"""Kinetic versus thermodynamic control in the addition of HBr to 1,3-butadiene.
Figure 1: free-energy profile from the allylic cation (with bromide) to the 1,2- and 1,4-adducts.
Figure 2: the same model solved as a linear rate system (first-order steps, Eyring rate constants)
at -80 C and +40 C: the fraction of 1,4-adduct as a function of time. The barriers are model values
chosen to reproduce the classic product ratios (about 80:20 at -80 C, about 15:85 at +40 C)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# Model Gibbs energies (kJ/mol) relative to the allylic cation + bromide (I).
G = {"I": 0.0, "TS12": 20.0, "TS14": 22.2, "P12": -80.0, "P14": -84.5}

fig, ax = plt.subplots(figsize=(6.4, 4.0))


def path(x0, x1, y0, y1):
    """A smooth cosine-shaped segment between two stationary points."""
    x = np.linspace(x0, x1, 60)
    return x, y0 + (y1 - y0) * (1 - np.cos(np.pi * (x - x0) / (x1 - x0))) / 2


# Figure 1 is drawn on a compressed, schematic scale so that both differences are visible.
S = {"TS12": 16.0, "TS14": 24.0, "P12": -22.0, "P14": -32.0}
for ts, p, color, label in (("TS12", "P12", "C0", "1,2-adduct"), ("TS14", "P14", "C3", "1,4-adduct")):
    xa, ya = path(0, 1, G["I"], S[ts])
    xb, yb = path(1, 2.2, S[ts], S[p])
    ax.plot(np.r_[xa, xb], np.r_[ya, yb], color=color, lw=2, label=label)
    ax.hlines(S[p], 2.2, 2.7, color=color, lw=2)
ax.hlines(0, -0.5, 0, color="0.3", lw=2)
ax.text(-0.25, 2, "allylic cation\n+ Br$^-$", ha="center", va="bottom", fontsize=9)
ax.annotate("", xy=(1.0, S["TS14"]), xytext=(1.0, S["TS12"]), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text(1.12, 20, "lower barrier:\n1,2 forms faster", fontsize=9, va="center")
ax.annotate("", xy=(2.85, S["P14"]), xytext=(2.85, S["P12"]), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text(2.95, -27, "1,4 more\nstable", fontsize=9, va="center")
ax.set_xlim(-0.7, 4.0)
ax.set_ylim(-40, 34)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("reaction coordinate")
ax.set_ylabel("$G$ (schematic)")
ax.legend(loc="lower left", frameon=False)

# Figure 2: time course from the linear rate equations.
kB, h, R = 1.380649e-23, 6.62607015e-34, 8.314462618


def k(dG, T):
    return kB * T / h * np.exp(-dG * 1e3 / (R * T))


fig2, ax2 = plt.subplots(figsize=(6.4, 3.8))
t = np.logspace(-12, 6, 400)
for T, color in ((193.15, "C0"), (313.15, "C3")):
    k1, k2 = k(G["TS12"] - G["I"], T), k(G["TS14"] - G["I"], T)
    km1, km2 = k(G["TS12"] - G["P12"], T), k(G["TS14"] - G["P14"], T)
    # state vector (I, P12, P14)
    K = np.array([[-(k1 + k2), km1, km2], [k1, -km1, 0.0], [k2, 0.0, -km2]])
    x = np.array([expm(K * ti) @ np.array([1.0, 0.0, 0.0]) for ti in t])
    frac = x[:, 2] / np.maximum(x[:, 1] + x[:, 2], 1e-300)
    ax2.semilogx(t, 100 * frac, color=color, lw=2, label=f"{T - 273.15:+.0f} °C")
ax2.axhline(100 * 1 / (1 + np.exp(-4.5e3 / (R * 313.15))), color="C3", ls=":", lw=1)
ax2.set_xlabel("time / s")
ax2.set_ylabel("1,4-adduct / %")
ax2.set_ylim(0, 100)
ax2.set_xlim(1e-12, 1e6)
ax2.legend(frameon=False, loc="upper left")
ax2.text(3e-11, 26, "kinetic ratio", fontsize=9)
ax2.text(2e1, 90, "equilibrium (+40 °C)", fontsize=9)
