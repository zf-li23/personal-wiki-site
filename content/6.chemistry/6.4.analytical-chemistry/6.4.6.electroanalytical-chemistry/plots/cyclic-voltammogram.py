"""Cyclic voltammetry of a reversible one-electron couple O + e- <=> R at a planar electrode.

Semi-infinite linear diffusion is solved with an explicit finite-difference scheme for the
diffusion equation c_t = D c_xx (equal diffusion coefficients, so c_O + c_R = c* everywhere and
only c_O has to be computed). The Nernst equation fixes the surface concentration at every
potential. Current density follows IUPAC sign convention (cathodic current negative).
Left: voltammograms at three scan rates. Right: cathodic peak current against v^(1/2)
compared with the Randles-Sevcik equation."""

import numpy as np
import matplotlib.pyplot as plt

F, R, T = 96485.33212, 8.314462618, 298.15
f = F / (R * T)
D = 1.0e-9           # m2/s
cstar = 1.0          # mol/m3 (1 mmol/L)
E0 = 0.0             # formal potential, V
E_start, E_switch = 0.30, -0.30
dE = 0.5e-3          # potential increment per time step, V
lam = 0.45           # D dt / dx^2 (stability of the explicit scheme needs < 0.5)


def simulate(v):
    dt = dE / v
    dx = np.sqrt(D * dt / lam)
    t_total = 2 * (E_start - E_switch) / v
    L = 6 * np.sqrt(D * t_total)
    n = int(L / dx) + 2
    c = np.full(n, cstar)
    n_half = int(round((E_start - E_switch) / dE))
    E = np.concatenate([E_start - dE * np.arange(1, n_half + 1),
                        E_switch + dE * np.arange(1, n_half + 1)])
    j = np.empty_like(E)
    for k, Ek in enumerate(E):
        c[1:-1] = c[1:-1] + lam * (c[2:] - 2 * c[1:-1] + c[:-2])
        xi = np.exp(f * (Ek - E0))
        c[0] = cstar * xi / (1 + xi)
        grad = (-3 * c[0] + 4 * c[1] - c[2]) / (2 * dx)
        j[k] = -F * D * grad  # reduction of O gives a negative (cathodic) current
    return E, j


fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axes[0]
rates = [0.025, 0.1, 0.4]
peaks = []
for v, col in zip(rates, ["C0", "C1", "C3"]):
    E, j = simulate(v)
    ax.plot(E * 1e3, j / 10, color=col, lw=1.6, label=f"v = {v * 1e3:g} mV/s")  # A/m2 -> mA/cm2
    kc, ka = np.argmin(j), np.argmax(j)
    peaks.append((v, -j[kc], E[kc], E[ka]))
v, jp, Epc, Epa = peaks[1]
ax.annotate("", xy=(Epa * 1e3, -0.32), xytext=(Epc * 1e3, -0.32),
            arrowprops=dict(arrowstyle="<->", color="0.3", lw=1))
ax.text(Epa * 1e3 + 8, -0.32, rf"$\Delta E_{{\mathrm{{p}}}}$ = {(Epa - Epc) * 1e3:.0f} mV (100 mV/s)",
        ha="left", va="center", fontsize=9)
ax.axhline(0, color="0.6", lw=0.6)
ax.axvline(E0 * 1e3, color="0.6", lw=0.6, ls=":")
ax.set_xlim(-300, 300)
ax.set_xlabel(r"$E - E^{\circ\prime}$ / mV")
ax.set_ylabel(r"$j$ / (mA cm$^{-2}$)   (cathodic negative)")
ax.set_title(r"reversible O + e$^-$ $\rightleftharpoons$ R, $c^*$ = 1 mmol/L, $D$ = 1e-5 cm$^2$/s",
             fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper left")

ax = axes[1]
vv = np.linspace(0, 0.45, 100)
rs = 0.4463 * F * cstar * np.sqrt(f * vv * D) / 10
ax.plot(np.sqrt(vv), rs, color="k", lw=1.2, label="Randles-Sevcik")
ax.plot([np.sqrt(p[0]) for p in peaks], [p[1] / 10 for p in peaks], "o", color="C3",
        label="simulation")
ax.set_xlabel(r"$v^{1/2}$ / (V s$^{-1}$)$^{1/2}$")
ax.set_ylabel(r"$|j_{\mathrm{pc}}|$ / (mA cm$^{-2}$)")
ax.set_xlim(0, 0.7)
ax.set_ylim(0, 0.6)
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
