"""Tolerating deception.

A: gain from responding to an alarm rather than ignoring it, (1 - f) L1 - f L2 in units of L2, against the
fraction f of false alarms, for L1/L2 = 3, 10, 50.
B: drongo-meerkat simulation. Meerkat response probability to call type k: after each false alarm of type k it
falls by a factor (1 - 0.35); between attempts every type recovers toward 1 at rate 0.06. Strategy 'repeat'
always uses type 0; 'switch' uses the type with the highest current response. Six call types.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8))
f = np.linspace(0, 1, 200)
for ratio, tok in ((3, "rna"), (10, "positive"), (50, "dna")):
    g = (1 - f) * ratio - f
    a.plot(f, g / ratio, color=P.edge(tok), lw=1.8, label=f"L1/L2 = {ratio}")
    fmax = ratio / (ratio + 1)
    a.scatter([fmax], [0], color=P.edge(tok), s=18, zorder=5)
a.axhline(0, color=P.muted(), lw=0.8)
a.set_xlabel("Proportion of false alarm calls, f")
a.set_ylabel("Gain from responding (relative)")
a.set_ylim(-0.5, 1.05)
a.legend(frameon=False, fontsize=8, loc="lower left")
a.text(0.5, 0.75, "respond", fontsize=8, color=P.muted())
a.text(0.86, -0.35, "ignore", fontsize=8, color=P.muted())
a.set_title("A", loc="left", fontweight="bold")

n_types, T = 6, 40
for strat, tok, lab in (("repeat", "neutral", "repeats one call type"), ("switch", "dna", "switches call types")):
    resp = np.ones(n_types)
    out = []
    for t in range(T):
        k = 0 if strat == "repeat" else int(np.argmax(resp))
        out.append(resp[k])
        resp[k] *= 0.65
        resp += 0.06 * (1 - resp)
    b.plot(range(1, T + 1), out, color=P.edge(tok), lw=1.8, marker="o", ms=2.5, label=f"drongo {lab}")
b.set_xlabel("False alarm number")
b.set_ylabel("Probability meerkat flees")
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=8, loc="lower left")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
