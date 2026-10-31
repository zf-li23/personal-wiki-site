# Data-quality statistics in resolution shells, from simulated diffraction data.
# True intensities: acentric Wilson statistics (exponential distribution) with mean
# <I>(s) = 2000 exp(-2 B s^2), B = 34 A^2, in 16 shells of equal reciprocal volume from 20 A to 1.5 A
# (2000 unique reflections per shell). Each reflection is measured m times with Poisson counting noise
# on signal plus a constant background of 40 counts (sigma^2 = I + 2 * 40), and with a 3 % random
# scale error per observation (absorption, beam fluctuations).
# A: per shell, the merged signal-to-noise <I/sigma(I)> (m = 4), the half-set correlation CC_1/2 and
#    CC* = sqrt(2 CC_1/2 / (1 + CC_1/2)) (right axis). The resolution limit is usually placed where
#    CC_1/2 is still significant (about 0.3) and <I/sigma> falls to about 1-2 (dashed lines).
# B: R_merge, R_meas and R_pim of the lowest-resolution shell against the multiplicity m: R_merge grows
#    with m (it measures the spread of single observations, with a bias at small m), R_meas is
#    multiplicity-independent, and R_pim (precision of the merged mean) falls as 1/sqrt(m - 1).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
rng = np.random.default_rng(0)

B, nsh, nref, bg = 34.0, 16, 2000, 40.0
dmax, dmin = 20.0, 1.5
s3 = np.linspace((1 / dmax) ** 3, (1 / dmin) ** 3, nsh + 1)
s_edges = s3 ** (1 / 3)                                   # 1/d, equal reciprocal volume per shell
s_mid = 0.5 * (s_edges[:-1] + s_edges[1:])
d_mid = 1 / s_mid


def observe(I, m):
    sig2 = I[:, None] + 2 * bg
    obs = I[:, None] * (1 + 0.03 * rng.normal(size=(len(I), m))) + np.sqrt(sig2) * rng.normal(size=(len(I), m))
    return obs, np.sqrt(sig2)


def stats(I, m):
    obs, sig = observe(I, m)
    mean = obs.mean(axis=1)
    dev = np.abs(obs - mean[:, None]).sum(axis=1)
    rmerge = dev.sum() / obs.sum()
    rmeas = (np.sqrt(m / (m - 1)) * dev).sum() / obs.sum()
    rpim = (np.sqrt(1 / (m - 1)) * dev).sum() / obs.sum()
    sig_mean = sig[:, 0] / np.sqrt(m)
    isig = np.mean(mean / sig_mean)
    perm = rng.permuted(np.tile(np.arange(m), (len(I), 1)), axis=1)
    half1 = np.take_along_axis(obs, perm[:, : m // 2], axis=1).mean(axis=1)
    half2 = np.take_along_axis(obs, perm[:, m // 2:], axis=1).mean(axis=1)
    cc = np.corrcoef(half1, half2)[0, 1]
    return rmerge, rmeas, rpim, isig, cc


rows = []
for s in s_mid:
    I = rng.exponential(2000 * np.exp(-2 * B * (s / 2) ** 2), size=nref)    # (sin theta / lambda) = s/2
    rows.append(stats(I, 4))
rows = np.array(rows)

fig, axs = plt.subplots(1, 2, figsize=(12, 4.3))
ax = axs[0]
x = s_mid**2
ax.plot(x, rows[:, 3], "o-", color=charts.line("dna"), lw=1.6, ms=4, label=r"$\langle I/\sigma(I)\rangle$")
ax.axhline(1.5, color=muted, lw=0.8, ls=(0, (3, 2)))
ax.set_yscale("log")
ax.set_ylim(0.3, 300)
charts.style_axes(ax, "resolution d / Å", r"$\langle I/\sigma(I)\rangle$")
ticks = np.array([8, 4, 3, 2.5, 2.0, 1.8, 1.6, 1.5])
ax.set_xticks(1 / ticks**2)
ax.set_xticklabels([f"{t:g}" for t in ticks])
ax2 = ax.twinx()
ax2.plot(x, rows[:, 4], "s-", color=charts.line("negative"), lw=1.6, ms=4, label=r"$CC_{1/2}$")
ccs = np.sqrt(2 * np.clip(rows[:, 4], 0, 1) / (1 + np.clip(rows[:, 4], 0, 1)))
ax2.plot(x, ccs, "^-", color=charts.line("highlight"), lw=1.2, ms=4, label=r"$CC^*$")
ax2.axhline(0.3, color=charts.line("negative"), lw=0.8, ls=(0, (3, 2)))
ax2.set_ylim(0, 1.05)
for sp in ("top",):
    ax2.spines[sp].set_visible(False)
ax2.tick_params(colors=muted, labelsize=8)
ax2.set_ylabel("correlation", color=ink, fontsize=8)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=8, frameon=False, loc="lower left")
ax.set_title("A  statistics in resolution shells (m = 4)", fontsize=9, loc="left", color=ink)

ax = axs[1]
I0 = rng.exponential(2000 * np.exp(-2 * B * (s_mid[0] / 2) ** 2), size=nref)
ms = np.arange(2, 21)
res = np.array([stats(I0, m)[:3] for m in ms])
for j, (tok, name) in enumerate((("dna", r"$R_{\mathrm{merge}}$"), ("protein", r"$R_{\mathrm{meas}}$"),
                                 ("highlight", r"$R_{\mathrm{pim}}$"))):
    ax.plot(ms, 100 * res[:, j], "o-", color=charts.line(tok), lw=1.6, ms=4, label=name)
ax.legend(fontsize=9, frameon=False)
ax.set_title(f"B  R values against multiplicity (d = {d_mid[0]:.0f} Å shell)", fontsize=9, loc="left",
             color=ink)
charts.style_axes(ax, "multiplicity m", "R / %")
ax.set_ylim(0, None)
fig.tight_layout()
