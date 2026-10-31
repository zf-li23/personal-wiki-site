# Resolution by Fourier shell correlation.
# A: two half-maps simulated in Fourier space on a 96^3 grid (pixel 1 A): a common signal with power
#    spectrum proportional to exp(-B k^2 / 2) (B = 100 A^2) plus independent white noise in each half-map,
#    scaled so that the signal-to-noise ratio of a half-map at k -> 0 is 400. The FSC computed shell by
#    shell (line) follows the expected FSC = SNR / (1 + SNR) (dashed). The 0.143 threshold for half-maps
#    and the 0.5 threshold are marked with the resolutions they give. Grey: the correlation C_ref of the
#    full map with the true structure, sqrt(2 FSC / (1 + FSC)), which equals 0.5 where FSC = 0.143.
# B: Rosenthal-Henderson plot. If each particle contributes the same signal-to-noise ratio, decaying as
#    exp(-B k^2 / 2), the 0.143 criterion gives ln N = B / (2 d^2) + const: ln N is linear in 1/d^2 with
#    slope B/2. Lines for B = 50, 100 and 150 A^2 (same per-particle SNR at k = 0); a better microscope,
#    detector or specimen (smaller B) needs far fewer particles for the same resolution.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n, B, snr0 = 96, 100.0, 400.0
f = np.fft.fftfreq(n)
KX, KY, KZ = np.meshgrid(f, f, f, indexing="ij")
K = np.sqrt(KX**2 + KY**2 + KZ**2)
amp = np.exp(-B * K**2 / 4)


def cgauss(shape):
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) / np.sqrt(2)


S = amp * cgauss(K.shape)
sn = 1 / np.sqrt(snr0)
F1 = S + sn * cgauss(K.shape)
F2 = S + sn * cgauss(K.shape)
edges = np.arange(0, 0.5 + 1e-9, 1 / n)
idx = np.digitize(K.ravel(), edges)
num = np.bincount(idx, (F1 * np.conj(F2)).real.ravel(), minlength=len(edges) + 1)
d1 = np.bincount(idx, (np.abs(F1) ** 2).ravel(), minlength=len(edges) + 1)
d2 = np.bincount(idx, (np.abs(F2) ** 2).ravel(), minlength=len(edges) + 1)
with np.errstate(invalid="ignore", divide="ignore"):
    fsc = (num / np.sqrt(d1 * d2))[1:len(edges)]
kc = edges[:-1] + 0.5 / n
snr = snr0 * np.exp(-B * kc**2 / 2)
expect = snr / (1 + snr)
cref = np.sqrt(np.clip(2 * fsc / (1 + fsc), 0, None))

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axs[0]
ax.plot(kc, fsc, color=charts.line("protein"), lw=1.8, label="FSC of half-maps (simulated)")
ax.plot(kc, expect, color=charts.line("negative"), lw=1.0, ls="--", label="SNR / (1 + SNR)")
ax.plot(kc, cref, color=charts.line("neutral"), lw=1.0, label="C_ref of full map")
for thr, tok in ((0.5, "dna"), (0.143, "highlight")):
    ax.axhline(thr, color=charts.line(tok), lw=0.8, ls=":")
    kt = np.interp(-thr, -expect, kc)
    ax.plot(kt, thr, "o", color=charts.line(tok), ms=5)
    ax.annotate(f"{thr}: {1 / kt:.2f} Å", (kt, thr), xytext=(6, 4), textcoords="offset points", fontsize=7.5,
                color=P.ink())
ax.set_xlim(0, 0.5)
ax.set_ylim(-0.1, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "spatial frequency k / Å⁻¹", "correlation")
charts.title(ax, "A   Fourier shell correlation (B = 100 Å²)")

ax = axs[1]
inv_d2 = np.linspace(0.02, 0.15, 100)
s1 = 2e-4                                           # per-particle SNR at k = 0 (illustrative)
for Bv, tok in ((50, "positive"), (100, "protein"), (150, "negative")):
    lnN = np.log(2 / (6 * s1)) + Bv * inv_d2 / 2      # 0.143 <=> half-map SNR = 1/6, half-map has N/2 particles
    ax.plot(inv_d2, lnN, color=charts.line(tok), lw=1.8, label=f"B = {Bv} Å²")
for d in (5, 4, 3, 2.6):
    ax.axvline(1 / d**2, color=P.muted(), lw=0.5, ls=":")
    ax.text(1 / d**2, 1.0, f"{d} Å", fontsize=7, color=P.muted(), ha="center")
ax.set_ylim(0, 20)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "1 / d² / Å⁻²", "ln (number of particles N)")
charts.title(ax, "B   Rosenthal–Henderson plot")
fig.tight_layout()
