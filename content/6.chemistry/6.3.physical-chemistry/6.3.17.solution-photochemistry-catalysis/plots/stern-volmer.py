"""Stern-Volmer plots. Dynamic (collisional) quenching gives linear F0/F = tau0/tau = 1 + K_SV[Q];
adding static quenching (ground-state complex, constant Ks) makes F0/F curve upwards while
the lifetime ratio stays linear. Simulated intensities with 2 % noise, fitted by least squares."""

import numpy as np
import matplotlib.pyplot as plt

kq, tau0, Ks = 1.0e10, 4.0e-9, 20.0          # L mol^-1 s^-1, s, L mol^-1
KSV = kq * tau0
Q = np.linspace(0, 0.05, 11)                  # mol L^-1
rng = np.random.default_rng(0)
F_dyn = (1 + KSV * Q) * (1 + 0.02 * rng.standard_normal(Q.size))
F_both = (1 + KSV * Q) * (1 + Ks * Q) * (1 + 0.02 * rng.standard_normal(Q.size))
slope = np.polyfit(Q, F_dyn - 1, 1)[0]

fig, ax = plt.subplots(figsize=(6, 4))
qq = np.linspace(0, 0.05, 100)
ax.plot(Q * 1e3, F_dyn, "o", color="C0", ms=4, label=r"$F_0/F$, dynamic only")
ax.plot(qq * 1e3, 1 + slope * qq, color="C0", lw=1)
ax.plot(Q * 1e3, F_both, "s", color="C3", ms=4, label=r"$F_0/F$, dynamic + static")
ax.plot(qq * 1e3, (1 + KSV * qq) * (1 + Ks * qq), color="C3", lw=1)
ax.plot(qq * 1e3, 1 + KSV * qq, color="C2", ls="--", label=r"$\tau_0/\tau$ (both cases)")
ax.set_xlabel(r"[Q] / (mmol L$^{-1}$)")
ax.set_ylabel("ratio")
ax.set_title(rf"fitted $K_{{\mathrm{{SV}}}}$ = {slope:.1f} L/mol (true {KSV:.0f})", fontsize=10)
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
