"""Doppler-shift compensation in the greater horseshoe bat (Rhinolophus ferrumequinum).

A bat flying at speed v toward a stationary reflector hears its echo at
f_echo = f_emit (c + v) / (c - v). To keep the echo at its reference frequency f_ref
(about 83 kHz, where the cochlea is most sharply tuned) it must emit f_emit = f_ref (c - v) / (c + v).
B simulates a 0.9 s flight between perches with a compensation loop of gain 0.95 and a
lag of 20 ms. C sketches the cochlear place map: an "acoustic fovea" in which a few kHz
around f_ref occupy a long stretch of basilar membrane (illustrative shape).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c = 343.0
fref = 83.0
fig, (a, b, cc) = plt.subplots(1, 3, figsize=(11.5, 3.6))
v = np.linspace(0, 8, 100)
a.plot(v, fref * (c + v) / (c - v), color=P.edge("negative"), lw=2, label="echo if call held at 83 kHz")
a.plot(v, fref * (c - v) / (c + v), color=P.edge("dna"), lw=2, label="call needed to keep echo at 83 kHz")
a.axhline(fref, color=P.muted(), ls="--", lw=0.8)
a.set_xlabel("Flight speed / m s$^{-1}$")
a.set_ylabel("Frequency / kHz")
a.legend(frameon=False, fontsize=7.5, loc="upper left")
a.set_ylim(78.5, 88)
a.set_title("A", loc="left", fontweight="bold")

t = np.linspace(0, 1.0, 1000)
vt = np.where((t > 0.05) & (t < 0.95), 5.5 * np.sin(np.pi * (t - 0.05) / 0.9) ** 2, 0.0)
dt = t[1] - t[0]
lag = int(0.02 / dt)
femit = np.full_like(t, fref)
for k in range(1, len(t)):
    j = max(0, k - lag)
    target = fref * (c - vt[j]) / (c + vt[j])
    femit[k] = fref + 0.95 * (target - fref)
fecho = femit * (c + vt) / (c - vt)
b.plot(t, femit, color=P.edge("dna"), lw=1.8, label="emitted CF")
b.plot(t, fecho, color=P.edge("rna"), lw=1.8, label="echo CF")
b.axhline(fref, color=P.muted(), ls="--", lw=0.8)
b2 = b.twinx()
b2.fill_between(t, 0, vt, color=P.light("neutral"), alpha=0.5, lw=0)
b2.set_ylim(0, 25)
b2.set_yticks([0, 5])
b2.set_ylabel("Speed / m s$^{-1}$", fontsize=8)
b.set_zorder(b2.get_zorder() + 1); b.patch.set_visible(False)
b.set_xlabel("Time / s")
b.set_ylabel("Frequency / kHz")
b.set_ylim(80.5, 83.8)
b.legend(frameon=False, fontsize=7.5, loc="upper right")
b.set_title("B", loc="left", fontweight="bold")

f = np.linspace(10, 105, 800)
x_generic = np.log(f / 10) / np.log(105 / 10)
fovea = 0.33 * (1 / (1 + np.exp(-(f - fref + 0.3) / 0.6)))
x_bat = 0.67 * x_generic + fovea
x_bat = x_bat / x_bat.max()
cc.plot(f, 1 - x_generic, color=P.edge("neutral"), lw=1.6, ls="--", label="typical mammal (log map)")
cc.plot(f, 1 - x_bat, color=P.edge("dna"), lw=2, label="horseshoe bat")
cc.axvspan(fref - 1, fref + 3, color=P.light("highlight"), alpha=0.6, lw=0)
cc.text(fref - 2, 0.85, "acoustic\nfovea", fontsize=8, ha="right", color=P.ink())
cc.set_xlabel("Frequency / kHz")
cc.set_ylabel("Distance from base (0) to apex (1)")
cc.legend(frameon=False, fontsize=7.5, loc="lower left")
cc.set_title("C", loc="left", fontweight="bold")
for ax in (a, b, cc):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
b2.spines["top"].set_visible(False)
fig.tight_layout()
