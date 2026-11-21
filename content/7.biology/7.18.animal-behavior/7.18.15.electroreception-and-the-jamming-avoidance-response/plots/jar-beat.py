"""What the fish feels when a neighbor discharges at a nearby frequency.

The fish's own EOD (amplitude 1, frequency f) mixes with a weaker neighbor signal (amplitude m)
at f + df. Relative to the fish's own signal, the mixture z = 1 + m exp(i 2 pi df t) has amplitude
|z| (amplitude modulation at the beat frequency |df|) and phase arg z (phase modulation).
A: the summed waveform for df = +4 Hz, m = 0.3 (carrier drawn at 60 Hz for visibility).
B: amplitude against phase over one beat cycle (two neighbor strengths m): the loop runs clockwise for df > 0 (neighbor higher)
and counter-clockwise for df < 0. Rule: if amplitude rises while the phase lags, the neighbor is
higher and the fish should lower its frequency.
C: the fish has no pure copy of its own signal, so it compares the phase at two body regions with
different contamination (m = 0.3 near the neighbor, m = 0.05 elsewhere): the differential phase
plotted against amplitude gives the same sense of rotation.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.7), gridspec_kw={"width_ratios": [1.4, 1, 1]})
a = axs[0]
t = np.linspace(0, 0.5, 6000)
f, df, m = 60.0, 4.0, 0.3
s = np.sin(2 * np.pi * f * t) + m * np.sin(2 * np.pi * (f + df) * t)
a.plot(t * 1e3, s, color=P.edge("dna"), lw=0.6)
env = np.abs(1 + m * np.exp(2j * np.pi * df * t))
a.plot(t * 1e3, env, color=P.edge("negative"), lw=1.5)
a.plot(t * 1e3, -env, color=P.edge("negative"), lw=1.5)
a.set_xlabel("Time / ms")
a.set_ylabel("Field at the skin (rel.)")
a.text(10, 1.45, "beat: amplitude modulation at |Δf| = 4 Hz", fontsize=7.5, color=P.edge("negative"))
a.set_ylim(-1.6, 1.7)
a.set_title("A", loc="left", fontweight="bold")
tt = np.linspace(0, 1, 400)
for d, col, lab, mm in ((4.0, P.edge("rna"), "Δf = +4 Hz (m = 0.3)", 0.3), (-4.0, P.edge("dna"), "Δf = −4 Hz (m = 0.15)", 0.15)):
    z = 1 + mm * np.exp(2j * np.pi * np.sign(d) * tt)
    ph = np.degrees(np.angle(z)); am = np.abs(z)
    axs[1].plot(ph, am, color=col, lw=1.8, label=lab)
    for k in (40, 140, 240, 340):
        axs[1].annotate("", (ph[k + 3], am[k + 3]), (ph[k], am[k]),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.2, mutation_scale=12))
    z1 = 1 + 2 * mm / 2 * np.exp(2j * np.pi * np.sign(d) * tt)
    z2 = 1 + 0.05 * np.exp(2j * np.pi * np.sign(d) * tt + 1.0j)
    dph = np.degrees(np.angle(z1 / z2))
    axs[2].plot(dph, np.abs(z1), color=col, lw=1.8, label=lab)
    for k in (40, 140, 240, 340):
        axs[2].annotate("", (dph[k + 3], np.abs(z1)[k + 3]), (dph[k], np.abs(z1)[k]),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.2, mutation_scale=12))
axs[1].set_xlabel("Phase relative to own EOD / deg")
axs[1].set_ylabel("Amplitude (rel.)")
axs[1].legend(frameon=False, fontsize=7.5, loc="center")
axs[1].set_title("B", loc="left", fontweight="bold")
axs[2].set_xlabel("Differential phase, region 1 − region 2 / deg")
axs[2].set_ylabel("Amplitude in region 1 (rel.)")
axs[2].set_title("C", loc="left", fontweight="bold")
for ax in axs:
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
