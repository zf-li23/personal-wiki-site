"""Thermal undulations of a fluid membrane (bending rigidity kappa = 20 kB T). A: mean squared
amplitude of the Fourier mode of wavevector q of a patch of area A, <|h_q|^2> = kB T /
[A (kappa q^4 + sigma q^2)], for membrane tensions sigma = 0, 1e-6, 1e-5 and 1e-4 N/m: bending
dominates at short wavelengths (slope -4), tension at long wavelengths (slope -2), with the
crossover at q_c = sqrt(sigma/kappa). B, C: height fields of a 4 um x 4 um patch synthesized from
these spectra with random phases (same random numbers), for sigma = 1e-7 and 1e-4 N/m: tension
irons out the long-wavelength undulations. D: tension against apparent area strain of a vesicle in
micropipette aspiration, alpha = (kB T / 8 pi kappa) ln(sigma / sigma_0) + sigma / K_A (Evans and
Rawicz 1990; K_A = 0.24 N/m, sigma_0 = 1e-6 N/m): at low tension, pulling out the undulations
(logarithmic regime) gives kappa; at high tension the bilayer stretches elastically, which gives
K_A, until it ruptures at a few percent strain (lysis tension about 10 mN/m)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
kT = 4.1e-21
kap = 20 * kT
fig, axs = plt.subplots(1, 4, figsize=(12.0, 3.1), gridspec_kw=dict(width_ratios=[1.25, 0.9, 0.9, 1.25]))
fig.subplots_adjust(wspace=0.42, left=0.05, right=0.98, bottom=0.19, top=0.86)

ax = axs[0]
q = np.logspace(5, 9, 300)  # 1/m
for s, tok in ((0, "neutral"), (1e-6, "dna"), (1e-5, "bacterium"), (1e-4, "blood")):
    S = kT / (kap * q**4 + s * q**2)  # times 1/A
    ax.plot(q * 1e-6, S * 1e36, color=charts.line(tok), lw=1.6, label=r"$\sigma = 0$" if s == 0 else rf"$\sigma = 10^{{{int(np.log10(s))}}}$ N/m")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"wavevector q / $\mu$m$^{-1}$", r"$A\langle|h_q|^2\rangle$ / nm$^4$")
charts.title(ax, "A  Fluctuation spectrum")

rng = np.random.default_rng(1)
n, Lp = 128, 4e-6
kx = 2 * np.pi * np.fft.fftfreq(n, d=Lp / n)
KX, KY = np.meshgrid(kx, kx)
Q2 = KX**2 + KY**2
Q2[0, 0] = np.inf
noise = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
fields = []
for s in (1e-7, 1e-4):
    amp = np.sqrt(kT / (kap * Q2**2 + s * Q2) / Lp**2)
    h = np.fft.ifft2(noise * amp).real * n * n / np.sqrt(2)
    fields.append(h * 1e9)
vmax = np.max(np.abs(fields[0]))
for ax, h, ttl in ((axs[1], fields[0], r"B  $\sigma = 10^{-7}$ N/m"), (axs[2], fields[1], r"C  $\sigma = 10^{-4}$ N/m")):
    im = ax.imshow(h, cmap="RdBu_r", vmin=-vmax, vmax=vmax, extent=(0, 4, 0, 4), origin="lower")
    charts.style_axes(ax, r"x / $\mu$m", None)
    charts.title(ax, ttl)
    ax.text(0.15, 0.25, f"rms {h.std():.0f} nm", fontsize=bio.core.FONT["tiny"], color=P.ink(),
            bbox=dict(facecolor=P.surface(), edgecolor="none", pad=1.5))

ax = axs[3]
KA, s0 = 0.24, 1e-6
sig = np.logspace(-6, -2, 300)
alpha = kT / (8 * np.pi * kap) * np.log(sig / s0) + sig / KA
ax.plot(alpha * 100, sig * 1e3, color=charts.line("lipid_head"), lw=1.8)
ax.axhline(10, color=charts.line("negative"), lw=0.8, ls=":")
ax.text(0.05, 12, "lysis", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(0.2, 2e-3, "entropic:\nslope gives $\\kappa$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(2.0, 0.3, "elastic:\nslope gives $K_A$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_yscale("log")
charts.style_axes(ax, "apparent area strain / %", "tension / (mN/m)")
charts.title(ax, "D  Micropipette aspiration")
