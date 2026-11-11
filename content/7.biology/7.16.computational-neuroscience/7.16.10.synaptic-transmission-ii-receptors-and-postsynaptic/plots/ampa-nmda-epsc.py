"""AMPA and NMDA components of a glutamatergic EPSC under voltage clamp.

Each conductance is a difference of exponentials normalized to a peak of 1:
AMPA tau_rise 0.2 ms, tau_decay 2 ms, peak 1 nS; NMDA tau_rise 3 ms, tau_decay 80 ms,
peak 0.5 nS, multiplied by the Jahr-Stevens block at 1 mM Mg2+. E_rev = 0 mV.
At -70 mV the EPSC is almost purely AMPA (inward, fast); at +40 mV it is outward and the
slow NMDA component dominates late times. The usual NMDA/AMPA ratio measurement takes the
current at +40 mV, 50 ms after the stimulus (dotted line), when the AMPA current has decayed.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t = np.linspace(-5, 200, 2000)


def kern(tr, td):
    s = np.clip(t, 0, None)
    k = (np.exp(-s / td) - np.exp(-s / tr)) * (t >= 0)
    return k / k.max()


def B(V):
    return 1.0 / (1.0 + 1.0 / 3.57 * np.exp(-0.062 * V))


ga, gn = 1.0 * kern(0.2, 2.0), 0.5 * kern(3.0, 80.0)
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
for ax, V, tl in zip(axs, (-70.0, 40.0), ("A  Held at -70 mV", "B  Held at +40 mV")):
    ia, inn = ga * V, gn * B(V) * V
    ax.plot(t, ia, color=P.edge("positive"), lw=1.4, ls="--", label="AMPA component")
    ax.plot(t, inn, color=P.edge("mg"), lw=1.4, ls="--", label="NMDA component")
    ax.plot(t, ia + inn, color=P.ink(), lw=2.0, label="total EPSC")
    ax.axhline(0, color=P.muted(), lw=0.6)
    ax.set_xlabel("Time after stimulus / ms")
    ax.set_title(tl, loc="left", fontsize=10)
    ax.legend(frameon=False, fontsize=8, loc="lower right" if V < 0 else "upper right")
    ax.grid(True, alpha=0.3)
axs[1].axvline(50, color=P.muted(), lw=0.8, ls=":")
axs[0].set_ylabel("Current / pA (outward positive)")
axs[0].set_xlim(-5, 60)
axs[1].set_xlim(-5, 200)
fig.tight_layout()
