"""Shunting versus hyperpolarizing inhibition in a single compartment (steady state).

Leak g_L = 10 nS at E_L = -65 mV; excitatory conductance g_e (E_e = 0 mV); inhibitory
conductance g_i with E_i = -65 mV (shunting, equal to rest) or E_i = -80 mV (hyperpolarizing).
V = (g_L E_L + g_e E_e + g_i E_i) / (g_L + g_e + g_i).
A: depolarization produced by g_e = 2 nS against g_i: shunting inhibition produces no
change by itself but divides the EPSP by (1 + g_i / (g_L + g_e)).
B: depolarization against g_e at several g_i (shunting): the input-output curve is
scaled, i.e. inhibition acts divisively on small inputs.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
gL, EL, Ee = 10.0, -65.0, 0.0


def V(ge, gi, Ei):
    return (gL * EL + ge * Ee + gi * Ei) / (gL + ge + gi)


fig, axs = plt.subplots(1, 2, figsize=(10, 3.9))
ax = axs[0]
gi = np.linspace(0, 60, 300)
ax.plot(gi, V(2.0, gi, -65.0) - EL, color=P.edge("cl"), lw=2.2, label="E + shunting I ($E_i$ = -65 mV)")
ax.plot(gi, V(2.0, gi, -80.0) - EL, color=P.edge("negative"), lw=2.0, label="E + hyperpolarizing I ($E_i$ = -80 mV)")
ax.plot(gi, V(0.0, gi, -65.0) - EL, color=P.edge("cl"), lw=1.2, ls="--", label="shunting I alone")
ax.plot(gi, V(0.0, gi, -80.0) - EL, color=P.edge("negative"), lw=1.2, ls="--", label="hyperpolarizing I alone")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Inhibitory conductance $g_i$ / nS")
ax.set_ylabel("$V - E_L$ / mV")
ax.set_title("A  One excitatory input ($g_e$ = 2 nS)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5, loc="upper right")

ax = axs[1]
ge = np.linspace(0, 10, 300)
for g, c in zip((0, 10, 30), (P.edge("positive"), P.edge("cl"), P.edge("dna"))):
    ax.plot(ge, V(ge, g, -65.0) - EL, color=c, lw=2.0, label=f"$g_i$ = {g} nS")
ax.set_xlabel("Excitatory conductance $g_e$ / nS")
ax.set_ylabel("Depolarization / mV")
ax.set_title("B  Shunting inhibition is divisive", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
