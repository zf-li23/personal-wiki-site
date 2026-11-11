"""Recruitment by the size principle in a motor-unit pool (after Fuglevand, Winter and Patla, 1993).

N = 120 motor units. Recruitment thresholds RT_i rise exponentially over a 30-fold range of the
excitatory drive E (in % of maximum); peak twitch forces P_i rise exponentially over a 100-fold range
in the same order (small units have low thresholds). Above threshold a unit fires at
f_i = 8 Hz + 1 Hz per % of drive above threshold, up to 35 Hz. Force of a unit:
F_i = P_i (1 - exp(-f_i / 12 Hz)) (fusion of twitches into tetanus).
Force fluctuations: each spike adds a twitch, so the variance of unit i is ~ c f_i P_i^2 (shot noise).
A: firing rate of every tenth unit against drive (orderly recruitment, then rate coding).
B: total force against drive, and the number of active units.
C: coefficient of variation (s.d. / mean) of force against mean force for the size-ordered pool
   and for a pool of equal units with the same total force: size ordering keeps the CV nearly
   constant over most of the range (signal-dependent noise), equal units give s.d. ~ sqrt(force).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N = 120
i = np.arange(N)
RT = np.exp(np.log(30) * i / (N - 1))  # 1 .. 30 % of max drive
RT = RT / RT[-1] * 50  # largest unit recruited at 50 % drive
Pk = np.exp(np.log(100) * i / (N - 1))
E = np.linspace(0, 100, 600)


def rates(E):
    f = 8 + 1.0 * (E[:, None] - RT[None, :])
    f = np.clip(f, 0, 35)
    f[E[:, None] < RT[None, :]] = 0
    return f


f = rates(E)
F = Pk[None, :] * (1 - np.exp(-f / 12))
Ftot = F.sum(1)
var_ord = (f * Pk[None, :] ** 2).sum(1)
Peq = Pk.mean() * np.ones(N)
# equal units: same recruitment thresholds but equal size
Feq = (Peq[None, :] * (1 - np.exp(-f / 12))).sum(1)
var_eq = (f * Peq[None, :] ** 2).sum(1)

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
cmap = plt.get_cmap("viridis")
for k in range(0, N, 10):
    ax.plot(E, f[:, k], color=cmap(k / N), lw=1.5)
ax.set_xlabel("Excitatory drive / % of maximum")
ax.set_ylabel("Firing rate / Hz")
ax.set_title("A  Recruitment and rate coding", loc="left", fontsize=10)
ax.text(55, 5, "small units first,\nlarge units last", fontsize=8, color=P.muted())
ax = axs[1]
ax.plot(E, 100 * Ftot / Ftot[-1], color=P.edge("dna"), lw=2.2)
ax.set_xlabel("Excitatory drive / % of maximum")
ax.set_ylabel("Force / % of maximum", color=P.edge("dna"))
ax2 = ax.twinx()
ax2.plot(E, (f > 0).sum(1), color=P.edge("rna"), lw=1.6, ls="--")
ax2.set_ylabel("Active units", color=P.edge("rna"))
ax.set_title("B  Force and recruitment", loc="left", fontsize=10)
ax = axs[2]
m = E > 2
ax.plot(100 * Ftot[m] / Ftot[-1], np.sqrt(var_ord[m]) / Ftot[m], color=P.edge("dna"), lw=2.0, label="size-ordered pool")
ax.plot(100 * Feq[m] / Feq[-1], np.sqrt(var_eq[m]) / Feq[m], color=P.muted(), lw=2.0, ls="--", label="equal units")
ax.set_yscale("log")
ax.set_xlabel("Mean force / % of maximum")
ax.set_ylabel("Coefficient of variation (relative)")
ax.set_title("C  Force variability", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
