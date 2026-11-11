"""Voltage dependence of NMDA and AMPA receptor currents.

Mg2+ block of the NMDA receptor follows Jahr and Stevens (1990):
B(V) = 1 / (1 + [Mg2+]_o / 3.57 mM * exp(-0.062 V / mV)).
A: unblocked fraction B(V) at 0, 0.1, 1 and 2 mM external Mg2+.
B: peak current-voltage relations, I = g B(V) (V - E_rev) with E_rev = 0 mV, for an NMDA
conductance of 1 nS at 1 mM Mg2+ (region of negative slope conductance below about -30 mV)
and in Mg2+-free solution, and for an AMPA conductance of 1 nS (linear).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
V = np.linspace(-100, 60, 400)


def B(V, mg):
    return 1.0 / (1.0 + mg / 3.57 * np.exp(-0.062 * V))


fig, axs = plt.subplots(1, 2, figsize=(10, 3.9))
ax = axs[0]
cols = [P.muted(), P.edge("dna"), P.edge("mg"), P.edge("negative")]
for mg, c in zip((0.0, 0.1, 1.0, 2.0), cols):
    ax.plot(V, B(V, mg), color=c, lw=2.0, label=f"[Mg$^{{2+}}$]$_o$ = {mg} mM")
ax.axvline(-65, color=P.muted(), lw=0.8, ls=":")
ax.text(-64, 0.9, "rest", fontsize=8, color=P.muted())
ax.set_xlabel("Membrane potential / mV")
ax.set_ylabel("Unblocked fraction B(V)")
ax.set_title("A  Mg$^{2+}$ block", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="center right")

ax = axs[1]
ax.plot(V, B(V, 1.0) * V, color=P.edge("mg"), lw=2.2, label="NMDA, 1 mM Mg$^{2+}$")
ax.plot(V, B(V, 0.0) * V, color=P.muted(), lw=1.4, ls="--", label="NMDA, no Mg$^{2+}$")
ax.plot(V, V, color=P.edge("positive"), lw=1.6, label="AMPA")
ax.axhline(0, color=P.ink(), lw=0.6)
ax.axvline(0, color=P.ink(), lw=0.6)
ax.set_ylim(-110, 70)
ax.set_xlabel("Membrane potential / mV")
ax.set_ylabel("Peak current / pA (g = 1 nS)")
ax.set_title("B  Current-voltage relations", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
