"""Free induction decay of two resonances (offsets 40 Hz and 100 Hz from the carrier,
intensity ratio 1:2) and the spectra obtained by a fast Fourier transform, for T2 = 0.5 s
and T2 = 0.05 s. The linewidth (full width at half height) of the Lorentzian lines is
1/(pi T2): 0.64 Hz and 6.4 Hz."""

import numpy as np
import matplotlib.pyplot as plt

sw = 1000.0  # spectral width / Hz (complex sampling interval 1 ms)
n = 8192
t = np.arange(n) / sw
rng = np.random.default_rng(0)

fig, axes = plt.subplots(2, 2, figsize=(10, 5.8))
for i, T2 in enumerate([0.5, 0.05]):
    fid = (1.0 * np.exp(2j * np.pi * 40 * t) + 2.0 * np.exp(2j * np.pi * 100 * t)) \
        * np.exp(-t / T2)
    fid += 0.02 * (rng.standard_normal(n) + 1j * rng.standard_normal(n))
    ax = axes[i, 0]
    m = t <= 0.6
    ax.plot(t[m], fid.real[m], color="C0", lw=0.7)
    ax.plot(t[m], 3 * np.exp(-t[m] / T2), color="C3", lw=1.0, ls="--")
    ax.text(0.98, 0.85, rf"$T_2$ = {T2} s", transform=ax.transAxes, ha="right", fontsize=9)
    ax.set_ylabel("signal (real part)")
    ax.set_yticks([])
    if i == 1:
        ax.set_xlabel(r"time $t$ / s")
    spec = np.fft.fftshift(np.fft.fft(fid))
    f = np.fft.fftshift(np.fft.fftfreq(n, d=1 / sw))
    ax = axes[i, 1]
    ax.plot(f, spec.real / np.abs(spec.real).max(), color="k", lw=1.0)
    ax.set_xlim(140, 0)
    ax.set_yticks([])
    ax.set_ylabel("spectrum (real part)")
    fwhm = 1 / (np.pi * T2)
    ax.text(0.03, 0.8, f"linewidth = 1/($\\pi T_2$) = {fwhm:.2g} Hz", transform=ax.transAxes,
            fontsize=9)
    if i == 1:
        ax.set_xlabel("frequency offset / Hz")
axes[0, 0].set_title("FID (dashed: envelope exp(-t/$T_2$))", fontsize=10)
axes[0, 1].set_title("after Fourier transform", fontsize=10)
fig.tight_layout()
