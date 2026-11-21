"""The jamming avoidance response of Eigenmannia (phenomenological model).

A: steady-state frequency shift of the fish against df (neighbor minus own frequency): the fish
moves away from the neighbor, most strongly for |df| of a few hertz; the shift is an odd
function of df, fitted here as -sign(df) A (|df|/f0) exp(1 - |df|/f0) with A = 6 Hz, f0 = 4 Hz.
B: time course when a neighbor mimic at df = +3 Hz is switched on for 60 s: the fish lowers its
EOD frequency with a time constant of about 10 s and drifts back after the stimulus ends.
Shapes and magnitudes are illustrative.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
A, f0 = 6.0, 4.0
df = np.linspace(-20, 20, 801)
shift = -np.sign(df) * A * (np.abs(df) / f0) * np.exp(1 - np.abs(df) / f0)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.7))
a.plot(df, shift, color=P.edge("dna"), lw=2)
a.axhline(0, color=P.muted(), lw=0.6); a.axvline(0, color=P.muted(), lw=0.6)
a.text(7, -5.6, "neighbor higher:\nfish lowers frequency", fontsize=7.5, color=P.ink())
a.text(-19, 4.6, "neighbor lower:\nfish raises frequency", fontsize=7.5, color=P.ink())
a.set_xlabel("Δf = neighbor − own frequency / Hz")
a.set_ylabel("Shift of own frequency / Hz")
a.set_title("A", loc="left", fontweight="bold")
t = np.linspace(0, 150, 1500)
f = np.full_like(t, 400.0)
target = 400 - A * (3 / f0) * np.exp(1 - 3 / f0)
for k in range(1, len(t)):
    on = 20 <= t[k] < 80
    tau = 10.0 if on else 25.0
    goal = target if on else 400.0
    f[k] = f[k - 1] + (goal - f[k - 1]) * (t[k] - t[k - 1]) / tau
b.plot(t, f, color=P.edge("dna"), lw=2, label="own EOD frequency")
b.plot(t, np.where((t >= 20) & (t < 80), 403.0, np.nan), color=P.edge("negative"), lw=2,
       label="neighbor mimic (+3 Hz)")
b.set_xlabel("Time / s"); b.set_ylabel("Frequency / Hz")
b.legend(frameon=False, fontsize=7.5, loc="lower right")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
