"""Simple eutectic system Bi-Cd at constant pressure. Left: liquidus curves from the ideal
solubility equation ln x_i = -(Delta_fus H_i / R)(1/T - 1/T_i*), with Bi: 544.55 K,
11.30 kJ/mol and Cd: 594.22 K, 6.21 kJ/mol (the measured eutectic is about 419 K at
x(Cd) = 0.55; the ideal model gives 408 K). Right: cooling curves simulated by Newtonian
cooling with latent heat released according to the lever rule."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

R = 8.314462618
TBi, HBi = 544.55, 11.30e3
TCd, HCd = 594.22, 6.21e3


def xs(T, Tm, H):
    return np.exp(-H / R * (1 / T - 1 / Tm))


TE = brentq(lambda T: xs(T, TBi, HBi) + xs(T, TCd, HCd) - 1, 300, 540)
xE = xs(TE, TCd, HCd)          # mole fraction of Cd at the eutectic

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 4.0), gridspec_kw=dict(width_ratios=[1.1, 1]))
T = np.linspace(TE, TBi, 200)
ax1.plot(1 - xs(T, TBi, HBi), T, color="C0", lw=1.8)
T = np.linspace(TE, TCd, 200)
ax1.plot(xs(T, TCd, HCd), T, color="C0", lw=1.8)
ax1.plot([0, 1], [TE, TE], color="C0", lw=1.8)
ax1.plot([xE], [TE], "o", color="C3", ms=5)
ax1.text(xE, TE - 14, "E", ha="center", fontsize=10)
ax1.text(0.45, 580, "l", fontsize=12)
ax1.text(0.05, 470, "l + Bi(s)", fontsize=9)
ax1.text(0.7, 470, "l + Cd(s)", fontsize=9)
ax1.text(0.5, 380, "Bi(s) + Cd(s)", ha="center", fontsize=9)
ax1.text(0.02, TBi + 5, "Bi", fontsize=8)
ax1.text(0.92, TCd + 5, "Cd", fontsize=8)
comps = [0.0, 0.2, xE, 0.8, 1.0]
for X in comps[1:-1]:
    ax1.axvline(X, color="0.75", lw=0.8, ls=":")
ax1.set_xlabel(r"$x(\mathrm{Cd})$")
ax1.set_ylabel(r"$T\,/\,\mathrm{K}$")
ax1.set_xlim(0, 1)
ax1.set_ylim(340, 640)


def enthalpy_curve(X, Cp=30.0):
    """Molar enthalpy H(T) for overall Cd mole fraction X (liquid fully above the liquidus)."""
    Ts = np.linspace(330, 650, 3201)
    H = np.empty_like(Ts)
    for k, Tk in enumerate(Ts):
        if X in (0.0, 1.0):
            Tm, L = (TBi, HBi) if X == 0.0 else (TCd, HCd)
            H[k] = Cp * Tk + (L if Tk >= Tm else 0.0)
            continue
        if X < xE:
            xl = 1 - xs(Tk, TBi, HBi) if Tk > TE else xE
            fl = X / xl if Tk > TE else 0.0      # Bi(s) is pure: X = fl * xl
            fl = min(fl, 1.0)
        else:
            xl = xs(Tk, TCd, HCd) if Tk > TE else xE
            fl = (1 - X) / (1 - xl) if Tk > TE else 0.0
            fl = min(fl, 1.0)
        H[k] = Cp * Tk + fl * (xl * HCd + (1 - xl) * HBi)
    return Ts, H


def cool(X, T0=630.0, Tenv=330.0, k=1.0, dt=0.02, tmax=60.0):
    Ts, Hs = enthalpy_curve(X)
    # make H strictly increasing so it can be inverted (plateaus become steep steps)
    Hs = np.maximum.accumulate(Hs + 1e-6 * np.arange(Hs.size))
    H = np.interp(T0, Ts, Hs)
    t, out = 0.0, []
    while t < tmax:
        T = np.interp(H, Hs, Ts)
        out.append((t, T))
        H -= k * (T - Tenv) * dt * 30.0
        t += dt
    return np.array(out)


off = 0.0
for X, c in zip(comps, ["C0", "C1", "C3", "C2", "C4"]):
    tr = cool(X)
    ax2.plot(tr[:, 0] + off, tr[:, 1], color=c, lw=1.5)
    lab = {0.0: "Bi", 1.0: "Cd"}.get(X, f"{X:.2f}")
    ax2.text(off + 0.5, 636, lab, fontsize=8, color=c)
    off += 7.0
ax2.axhline(TE, color="0.7", lw=0.8, ls=":")
ax2.set_xlabel("time (arbitrary units, curves offset)")
ax2.set_ylabel(r"$T\,/\,\mathrm{K}$")
ax2.set_xticks([])
ax2.set_ylim(340, 650)
ax2.set_xlim(-1, 45)
fig.tight_layout()
