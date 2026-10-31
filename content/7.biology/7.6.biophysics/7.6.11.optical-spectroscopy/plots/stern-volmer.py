# Fluorescence quenching analyzed by Stern-Volmer plots (simulated tryptophan data, tau0 = 3 ns).
# A: purely dynamic quenching (kq = 6e9 /(M s), K_D = kq tau0 = 18 /M): F0/F and tau0/tau coincide and are linear.
#    Purely static quenching (K_S = 8 /M): F0/F linear but the lifetime is unchanged.
#    Both together: F0/F = (1 + K_D[Q])(1 + K_S[Q]) curves upward while tau0/tau stays linear.
# B: a protein with two tryptophans, one exposed (K = 15 /M) and one buried (K = 0.05 /M), each contributing half
#    of the fluorescence: the Stern-Volmer plot bends downward; the modified (Lehrer) plot F0/dF against 1/[Q]
#    is linear, with intercept 1/f_a giving the accessible fraction f_a = 0.5.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
Q = np.linspace(0, 0.3, 13)
KD, KS = 18.0, 8.0
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
ax = axs[0]
cases = (("dynamic", 1 + KD * Q, 1 + KD * Q, "dna"),
         ("static", 1 + KS * Q, np.ones_like(Q), "rna"),
         ("dynamic + static", (1 + KD * Q) * (1 + KS * Q), 1 + KD * Q, "protein"))
for name, F, tau, tok in cases:
    ax.plot(Q, F * (1 + rng.normal(0, 0.01, Q.size)), "o", ms=4, color=charts.line(tok), label=f"{name}: F0/F")
    ax.plot(Q, tau, "--", color=charts.line(tok), lw=1.2, label=f"{name}: τ0/τ")
ax.set_ylim(0, 23)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "[Q] / M", "F0/F  or  τ0/τ")
charts.title(ax, "A   Dynamic versus static quenching")

Ka, Kb, fa = 15.0, 0.05, 0.5
Qb = np.linspace(0.0, 0.6, 25)
F = fa / (1 + Ka * Qb) + (1 - fa) / (1 + Kb * Qb)
ax = axs[1]
ax.plot(Qb, 1 / F, "o", ms=4, color=charts.line("dna"))
ax.plot(Qb, 1 + fa * Ka * Qb + (1 - fa) * Kb * Qb, color=P.muted(), lw=0.9, ls=":")
ax.text(0.2, 4.0, "two Trp: exposed + buried", fontsize=8, color=P.ink())
charts.style_axes(ax, "[Q] / M", "F0/F")
charts.title(ax, "B   Downward curvature")

ax = axs[2]
m = Qb > 0
x = 1 / Qb[m]
yv = 1 / (1 - F[m])
ax.plot(x, yv, "o", ms=4, color=charts.line("dna"))
coef = np.polyfit(x[x < 20], yv[x < 20], 1)
xx = np.linspace(0, x.max(), 50)
ax.plot(xx, np.polyval(coef, xx), color=charts.line("positive"), lw=1.3)
ax.text(8, coef[1] + 0.2, f"intercept 1/f_a = {coef[1]:.2f}", fontsize=8, color=P.ink())
ax.set_xlim(0, 25)
charts.style_axes(ax, "1/[Q] / M⁻¹", "F0/ΔF")
charts.title(ax, "C   Lehrer plot")
fig.tight_layout()
