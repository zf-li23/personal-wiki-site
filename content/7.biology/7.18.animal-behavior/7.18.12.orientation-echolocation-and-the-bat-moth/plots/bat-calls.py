"""An FM bat closing in on an insect: call design follows the geometry of echoes.

The bat flies at 5 m/s toward an insect 4.5 m away. Each call must end before its echo
returns (duration < 2 d / c) and the next call should wait for the echo (interval > 2 d / c
plus processing); simple rules of this kind reproduce the search, approach and terminal-buzz
phases recorded from hunting bats (values illustrative, after the patterns in Eptesicus).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c = 343.0
v = 5.0
d0 = 4.5
calls = []
t = 0.0
while True:
    d = d0 - v * t
    if d < 0.06:
        break
    delay = 2 * d / c
    dur = min(8e-3, 0.45 * delay)
    dur = max(dur, 0.2e-3)
    phase = "search" if d > 2.5 else ("approach" if d > 0.5 else "buzz")
    interval = min(0.11, 0.045 * d) if phase != "buzz" else 0.005
    f_hi = 55e3 if phase == "search" else (70e3 if phase == "approach" else 45e3)
    f_lo = 25e3 if phase == "search" else (28e3 if phase == "approach" else 20e3)
    calls.append((t, dur, f_hi, f_lo, d, interval, phase))
    t += interval
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw={"width_ratios": [1.5, 1]})
col = {"search": P.edge("dna"), "approach": P.edge("rna"), "buzz": P.edge("negative")}
for (t0, dur, fh, fl, d, itv, ph) in calls:
    tt = np.linspace(0, dur, 20)
    f = fh * (fl / fh) ** (tt / dur)  # exponential (hyperbolic-like) downward sweep
    w = 2.0 if ph != "buzz" else 1.2
    a.plot((t0 + tt) * 1e3, f / 1e3, color=col[ph], lw=w)
tc = calls[-1][0]
for ph, x in (("search", 150), ("approach", 560), ("buzz", 840)):
    a.text(x, 78, ph if ph != "buzz" else "terminal buzz", color=col[ph], fontsize=8.5, ha="center")
a.set_xlim(-20, tc * 1e3 + 30)
a.set_ylim(15, 85)
a.set_xlabel("Time / ms")
a.set_ylabel("Frequency / kHz")
a.set_title("A", loc="left", fontweight="bold")
ds = np.array([cl[4] for cl in calls])
durs = np.array([cl[1] for cl in calls]) * 1e3
itvs = np.array([cl[5] for cl in calls]) * 1e3
dd = np.logspace(-1.3, 0.7, 100)
b.fill_between(dd, 2 * dd / c * 1e3, 200, color=P.light("negative"), alpha=0.3, lw=0)
b.text(0.3, 70, "a call this long would\noverlap its own echo", fontsize=7.5, color=P.edge("negative"))
b.plot(dd, 2 * dd / c * 1e3, color=P.edge("negative"), lw=1)
b.plot(ds, durs, "o", ms=3, color=P.edge("dna"), label="call duration")
b.plot(ds, itvs, "s", ms=3, color=P.edge("rna"), label="call interval")
b.set_xscale("log"); b.set_yscale("log")
b.set_xlim(0.05, 5); b.set_ylim(0.2, 200)
b.invert_xaxis()
b.set_xlabel("Distance to target / m")
b.set_ylabel("Time / ms")
b.legend(frameon=False, fontsize=8, loc="lower left")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
