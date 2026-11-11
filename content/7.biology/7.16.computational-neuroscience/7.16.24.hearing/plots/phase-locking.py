"""Phase locking of auditory nerve fibres and its high-frequency limit.

Model fibre: at most one spike per stimulus cycle, fired with probability 0.3 per cycle at the
preferred phase plus Gaussian timing jitter of s.d. sigma_t (a crude stand-in for the low-pass
filtering by the hair-cell membrane and the stochastic release at the ribbon synapse).
A: period histograms (spike phase within the cycle, 2 s of stimulation) at 300 Hz, 1 kHz and
3 kHz for sigma_t = 0.1 ms. B: vector strength against frequency for sigma_t = 0.05, 0.1 and
0.2 ms; points from simulation, lines the prediction VS = exp(-(2 pi f sigma_t)^2 / 2).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)


def spikes(f, sigma, dur=2.0, p=0.3):
    n = int(f * dur)
    fire = rng.random(n) < p
    return (np.arange(n)[fire] + 0.25) / f + rng.normal(0, sigma, fire.sum())


def phases(f, ts):
    return np.mod(ts * f, 1.0)


def vs(f, ts):
    return np.abs(np.mean(np.exp(2j * np.pi * f * ts)))


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0), gridspec_kw={"width_ratios": [1.1, 1]})
ax = axs[0]
cols = [P.edge("dna"), P.edge("enzyme"), P.edge("rna")]
bins = np.linspace(0, 1, 33)
for k, (f, c) in enumerate(zip((300, 1000, 3000), cols)):
    ts = spikes(f, 1e-4)
    h, _ = np.histogram(phases(f, ts), bins=bins)
    h = h / h.max()
    ax.bar(bins[:-1] + 1 / 64, h * 0.85, width=1 / 32, bottom=1.1 * k, color=P.fill("dna") if k == 0 else
           (P.fill("enzyme") if k == 1 else P.fill("rna")), edgecolor=c, lw=0.6)
    ax.text(1.02, 1.1 * k + 0.4, f"{f} Hz\nVS = {vs(f, ts):.2f}", fontsize=8, color=c, va="center")
ax.set_xlim(0, 1.25)
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_yticks([])
ax.set_xlabel("Phase of the stimulus cycle / cycles")
ax.set_title("A  Period histograms (jitter 0.1 ms)", loc="left", fontsize=10)
for s in ("left", "top", "right"):
    ax.spines[s].set_visible(False)

ax = axs[1]
fgrid = np.logspace(2, np.log10(1.2e4), 200)
fpts = np.logspace(2, 4, 9)
for sig, c in zip((5e-5, 1e-4, 2e-4), cols):
    ax.semilogx(fgrid, np.exp(-((2 * np.pi * fgrid * sig) ** 2) / 2), color=c, lw=1.6,
                label=f"jitter {sig * 1e3:.2f} ms")
    ax.semilogx(fpts, [vs(f, spikes(f, sig)) for f in fpts], "o", color=c, ms=4)
ax.set_xlabel("Stimulus frequency / Hz")
ax.set_ylabel("Vector strength")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("B  The upper limit of phase locking", loc="left", fontsize=10)
fig.tight_layout()
