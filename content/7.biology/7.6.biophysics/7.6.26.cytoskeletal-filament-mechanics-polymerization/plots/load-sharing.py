"""Several filaments pushing one load (26.5.4): Monte Carlo of the ratchet with rapid load equilibration.

N filaments grow against a wall loaded with force F. The wall equilibrates fast, so given the tips x_i
its distance above the leading tip is exponential with mean kBT/F; filament i can add a subunit of
length delta only if the wall is at least delta above its tip, which happens with probability
exp(-F max(0, x_i + delta - x_max)/kBT). Subunits add at rate kon c times that probability and leave
at rate koff (kon c = 116 s^-1, koff = 1.4 s^-1: actin at 10 uM, delta = 2.7 nm). Each filament's
lattice offset is fixed: perfectly staggered (offsets j delta/N), aligned (all equal) or random.
A: load velocity against force for N = 1 and N = 4, with the equal-sharing formula
v = delta (kon c e^(-F delta/N kBT) - koff) (lines). B: the same against force per filament for
N = 1, 2, 4, 8 random arrays: all stall at N times the single-filament stall force (dotted)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)
KONC, KOFF, KBT, DELTA = 116.0, 1.4, 4.1, 2.7
FS = KBT / DELTA * np.log(KONC / KOFF)


def velocity(offsets, F, events=12000):
    x = np.array(offsets, dtype=float)
    w = F * DELTA / KBT
    t = 0.0
    x0 = x.max()
    n = len(x)
    for _ in range(events):
        xm = x.max()
        pa = np.exp(-w * np.maximum(0.0, x + 1.0 - xm))
        ra = KONC * pa
        tot = ra.sum() + KOFF * n
        t += rng.exponential(1.0 / tot)
        u = rng.random() * tot
        cs = np.cumsum(ra)
        if u < cs[-1]:
            x[np.searchsorted(cs, u)] += 1.0
        else:
            x[rng.integers(n)] -= 1.0
    return (x.max() - x0) * DELTA / t * 60 / 1000  # um/min


def sharing(F, N):
    return DELTA * (KONC * np.exp(-F * DELTA / (N * KBT)) - KOFF) * 60 / 1000


fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
Fg = np.linspace(0, 30, 200)
ax.plot(Fg, sharing(Fg, 1), color=charts.line("neutral"), lw=1.0)
ax.plot(Fg, sharing(Fg, 4), color=charts.line("actin"), lw=1.0)
Fp = np.linspace(0, 28, 9)
cfgs = (([0.0], "neutral", "o", "N = 1"),
        (list(np.arange(4) / 4), "actin", "o", "N = 4, staggered"),
        ([0.0] * 4, "channel", "s", "N = 4, aligned"))
for off, tok, mk, lab in cfgs:
    v = [velocity(off, F) for F in Fp]
    ax.plot(Fp, v, mk, color=charts.line(tok), ms=4, label=lab, mfc="none" if mk == "s" else None)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-1, 20)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "total load F / pN", r"load velocity / (µm min$^{-1}$)")
charts.title(ax, "A  Staggering helps")

ax = axs[1]
for N, tok in ((1, "neutral"), (2, "lipid_head"), (4, "actin"), (8, "channel")):
    fpf = np.linspace(0, 8, 9)
    v = [np.mean([velocity(rng.random(N), f * N, events=6000) for _ in range(2)]) for f in fpf]
    ax.plot(fpf, v, "o-", color=charts.line(tok), ms=3.5, lw=1.0, label=f"N = {N}")
ax.axvline(FS, color=P.muted(), lw=0.6, ls=":")
ax.text(FS + 0.1, 12, "single-filament\nstall force", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-1, 20)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "load per filament F/N / pN", r"load velocity / (µm min$^{-1}$)")
charts.title(ax, "B  Stall at N times the single force")
