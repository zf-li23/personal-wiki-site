"""Two codes for interaural time difference (ITD) in a small mammal.

Stimulus: 500 Hz tone; physiological ITD range +-135 us (gerbil-sized head). Tuning to ITD:
r(ITD) = r0 + r1 exp(kappa (cos 2 pi f (ITD - d) - 1)), r0 = 5 Hz, r1 = 100 Hz, kappa = 1.5.
Place code (Jeffress): 20 neurons with best delays d spread evenly over the physiological range.
Two-channel code: 10 neurons per hemisphere, best interaural phase difference +-pi/4 (best delays
+-250 us, outside the physiological range), as found by Brand et al. (2002) and argued for by
Harper and McAlpine (2004). A: tuning curves (grey band: physiological range). B: difference of the
mean rates of the two channels, a monotonic read-out of ITD. C: Fisher information of the whole
population for Poisson spike counts in 100 ms, I_F = T sum r'^2 / r, and the corresponding
Cramer-Rao bound on the standard deviation of an unbiased ITD estimate.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
f, r0, r1, kap, T = 500.0, 5.0, 100.0, 1.5, 0.1
itd = np.linspace(-500e-6, 500e-6, 801)
phys = 135e-6


def tune(x, d):
    return r0 + r1 * np.exp(kap * (np.cos(2 * np.pi * f * (x - d)) - 1))


def dtune(x, d):
    ph = 2 * np.pi * f * (x - d)
    return -r1 * kap * 2 * np.pi * f * np.sin(ph) * np.exp(kap * (np.cos(ph) - 1))


place = np.linspace(-phys, phys, 20)
two = np.array([250e-6] * 10 + [-250e-6] * 10)

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
for a in axs:
    a.axvspan(-phys * 1e6, phys * 1e6, color=P.muted(), alpha=0.15, lw=0)
for d in place[::3]:
    ax.plot(itd * 1e6, tune(itd, d), color=P.edge("dna"), lw=1.0)
for d, c in ((250e-6, P.edge("rna")), (-250e-6, P.edge("enzyme"))):
    ax.plot(itd * 1e6, tune(itd, d), color=c, lw=2.2)
ax.plot([], [], color=P.edge("dna"), lw=1.0, label="place code (some of 20)")
ax.plot([], [], color=P.edge("rna"), lw=2.2, label="channel: best ITD +250 us")
ax.plot([], [], color=P.edge("enzyme"), lw=2.2, label="channel: best ITD -250 us")
ax.set_xlabel("ITD / us")
ax.set_ylabel("Rate / Hz")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_ylim(0, 150)
ax.set_title("A  Tuning to ITD at 500 Hz", loc="left", fontsize=10)

ax = axs[1]
diff = tune(itd, 250e-6) - tune(itd, -250e-6)
ax.plot(itd * 1e6, diff, color=P.edge("protein"), lw=2)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("ITD / us")
ax.set_ylabel("Rate difference of the channels / Hz")
ax.set_title("B  Hemispheric difference", loc="left", fontsize=10)

ax = axs[2]
for ds, c, lab in ((place, P.edge("dna"), "place code"), (two, P.edge("rna"), "two-channel code")):
    I = T * sum(dtune(itd, d) ** 2 / tune(itd, d) for d in ds)
    sel = np.abs(itd) <= 300e-6
    ax.plot(itd[sel] * 1e6, 1e6 / np.sqrt(I[sel]), color=c, lw=2, label=lab)
ax.set_xlabel("ITD / us")
ax.set_ylabel("Cramer-Rao bound on s.d. / us")
ax.set_ylim(0, 80)
ax.legend(frameon=False, fontsize=8, loc="lower center")
ax.set_title("C  Precision of the two codes", loc="left", fontsize=10)
fig.tight_layout()
