# Magnetic flux densities relevant to biology, on one logarithmic axis (approximate ranges).
# Biological sources: brain (MEG, at the scalp), heart (MCG, at the chest), a single axon (measured close to
# a giant axon). Environment: geomagnetic field, its daily variation, power-line and household fields,
# a refrigerator magnet, MRI scanners, the strongest continuous laboratory fields.
# Biological sensing: the radio-frequency amplitude reported to disorient robins, the geomagnetic window of
# the robin compass. Sensors: SQUID, optically pumped magnetometers (OPM) and NV-diamond magnetometers
# (sensitivity per root hertz, shown as a field).
# Upper axis: Zeeman energy of a free electron spin, g muB B, in units of kT at 310 K.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rows = [
    ("brain (MEG)", 3e-14, 1e-12, "neuron"),
    ("heart (MCG)", 1e-11, 1e-10, "muscle"),
    ("giant axon, at 1 mm", 1e-11, 1e-9, "neuron"),
    ("SQUID / OPM noise (1 s)", 1e-15, 2e-14, "neutral"),
    ("NV diamond noise (1 s)", 1e-13, 1e-11, "neutral"),
    ("RF field disrupting robins", 1.5e-8, 5e-8, "highlight"),
    ("daily geomagnetic variation", 1e-8, 1e-7, "plant"),
    ("power lines, households", 1e-7, 1e-5, "neutral"),
    ("geomagnetic field", 2.5e-5, 6.5e-5, "plant"),
    ("refrigerator magnet", 3e-3, 1e-2, "neutral"),
    ("MRI scanners", 1.5, 11.7, "dna"),
    ("strongest static fields", 30, 45, "dna"),
]
fig, ax = plt.subplots(figsize=(10.5, 4.6))
y = np.arange(len(rows))[::-1]
for yi, (name, lo, hi, tok) in zip(y, rows):
    ax.barh(yi, np.log10(hi) - np.log10(lo), left=np.log10(lo), height=0.6, color=P.fill(tok), edgecolor=P.edge(tok),
            lw=0.8)
ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in rows], fontsize=7.5)
ticks = np.arange(-15, 3)
ax.set_xticks(ticks)
names = {-15: "1 fT", -12: "1 pT", -9: "1 nT", -6: "1 μT", -3: "1 mT", 0: "1 T"}
ax.set_xticklabels([names.get(t, "") for t in ticks])
ax.set_xlim(-15.3, 2.3)
charts.style_axes(ax, "magnetic flux density B (logarithmic)")
gmuB, kT = 2.0023 * 9.2740e-24, 1.380649e-23 * 310
top = ax.secondary_xaxis("top", functions=(lambda x: x + np.log10(gmuB / kT), lambda z: z - np.log10(gmuB / kT)))
top.set_xticks(np.arange(-18, 1, 3))
top.set_xticklabels([f"$10^{{{k}}}$" if k != 0 else "1" for k in np.arange(-18, 1, 3)])
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=7)
top.set_xlabel("electron Zeeman energy g μB B / kBT (310 K)", fontsize=7.5, color=P.ink())
fig.tight_layout()
