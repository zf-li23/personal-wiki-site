"""Optimal retinal filter for natural images with noise (Atick and Redlich 1990, 1992; Dayan and Abbott 4.2).

Signal power spectrum Q_ss(k) = A / k^2 (natural images), white input noise Q_nn = N.
Optimal filter = whitening filter of the noisy signal times a Wiener noise filter:
    |D(k)| = Q_ss / (Q_ss + Q_nn)^(3/2).
A: |D(k)| for signal-to-noise ratios A/N = 1e4, 1e2, 1 (bright to dim light), normalized to their
maxima; at high SNR the filter rises as k (whitening) over most frequencies, at low SNR it is low pass.
B: the corresponding radial spatial profiles (inverse 2D Fourier transform, Hankel transform with
J0), normalized to the center value; the inhibitory surround weakens and disappears as light dims.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import j0

import wikibio as bio

P = bio.P
k = np.linspace(1e-3, 40, 8000)
dk = k[1] - k[0]
r = np.linspace(0, 1.5, 300)
cols = [P.edge("dna"), P.edge("rna"), P.edge("positive")]
fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
for snr, col in zip((1e4, 1e2, 1.0), cols):
    Qss = snr / k**2
    D = Qss / (Qss + 1.0) ** 1.5 * np.exp(-(k / 30) ** 2)
    axs[0].plot(k, D / D.max(), color=col, lw=1.8, label=f"A/N = {snr:g}")
    prof = np.array([(D * j0(2 * np.pi * k * rr) * 2 * np.pi * k).sum() * dk for rr in r])
    axs[1].plot(r, prof / prof[0], color=col, lw=1.8, label=f"A/N = {snr:g}")
axs[0].set_xscale("log")
axs[0].set_xlim(0.01, 40)
axs[0].set_xlabel("Spatial frequency k (arbitrary units)")
axs[0].set_ylabel("Filter gain |D(k)| (normalized)")
axs[0].legend(frameon=False, fontsize=8, loc="upper left")
axs[0].set_title("A  From whitening to smoothing as noise grows", loc="left", fontsize=10)
axs[1].axhline(0, color=P.muted(), lw=0.6)
axs[1].set_xlabel("Distance from receptive field center (units of 1/k)")
axs[1].set_ylabel("Spatial weight (normalized)")
axs[1].set_ylim(-0.35, 1.05)
axs[1].legend(frameon=False, fontsize=8, loc="upper right")
axs[1].set_title("B  Receptive field profile: the surround fades in dim light", loc="left", fontsize=10)
fig.tight_layout()
