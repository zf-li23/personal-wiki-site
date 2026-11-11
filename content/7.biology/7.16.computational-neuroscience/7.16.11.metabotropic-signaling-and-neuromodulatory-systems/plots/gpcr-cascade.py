"""Time scales and amplification of a GPCR cascade compared with an ionotropic response.

Minimal three-stage model of beta-adrenergic signaling (time in s, concentrations normalized):
receptor occupancy R = A / (A + Kd) follows the agonist A (a 2 s application, or a steady dose);
G* (active Gs-GTP):   dG/dt = kG R (1 - G) - G / tauG,   kG = 2 /s, tauG = 1 s (GTP hydrolysis)
cAMP:                 dc/dt = kC G - c / tauC,            kC = 5 /s, tauC = 2 s (phosphodiesterase)
PKA activity:         P = c^2 / (c^2 + Kp^2),             Kp = 0.5
For comparison an ionotropic EPSC (difference of exponentials, 0.5 ms and 5 ms).
A: normalized time courses on a logarithmic time axis: each stage is slower than the previous.
B: steady-state dose-response of each stage (agonist in units of Kd): every stage saturates at
lower agonist, so the cascade is both amplifying (left shift) and steeper (Hill-like).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
kG, tauG, kC, tauC, Kp = 2.0, 1.0, 5.0, 2.0, 0.5
dt = 1e-4
t = np.arange(0, 40, dt)


def run(Afun):
    G = c = 0.0
    out = np.zeros((len(t), 4))
    for k, tk in enumerate(t):
        A = Afun(tk)
        R = A / (A + 1.0)
        G += dt * (kG * R * (1 - G) - G / tauG)
        c += dt * (kC * G - c / tauC)
        out[k] = (R, G, c, c**2 / (c**2 + Kp**2))
    return out


fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
o = run(lambda s: 1.0 if s < 2.0 else 0.0)
names = ["receptor occupancy", "G$\\alpha_s$-GTP", "cAMP", "PKA activity"]
cols = [P.edge("receptor"), P.edge("dna"), P.edge("rna"), P.edge("enzyme")]
ts = t[1:]
for j in range(4):
    y = o[1:, j]
    ax.plot(ts, y / y.max(), color=cols[j], lw=2.0, label=names[j])
te = np.logspace(-4, 1.6, 400)
epsc = np.exp(-te / 5e-3) - np.exp(-te / 5e-4)
ax.plot(te, epsc / epsc.max(), color=P.edge("positive"), lw=1.6, ls="--", label="ionotropic EPSC")
ax.set_xscale("log")
ax.set_xlim(1e-4, 40)
ax.axvspan(1e-4, 2.0, color=P.light("highlight"), zorder=0)
ax.text(0.6, 1.03, "agonist", fontsize=8, ha="center", color=P.ink())
ax.set_xlabel("Time / s")
ax.set_ylabel("Normalized response")
ax.set_title("A  Each stage is slower", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5, loc="center left")
ax.set_ylim(0, 1.12)

ax = axs[1]
A = np.logspace(-4, 1, 60)
R = A / (A + 1)
G = kG * R / (kG * R + 1 / tauG)
c = kC * G * tauC
Pk = c**2 / (c**2 + Kp**2)
for y, nm, col in zip((R, G, c / c.max(), Pk), names, cols):
    ax.semilogx(A, y / y.max(), color=col, lw=2.0, label=nm)
ax.set_xlabel("Agonist concentration / $K_d$")
ax.set_ylabel("Steady-state response (normalized)")
ax.set_title("B  Amplification shifts sensitivity", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
