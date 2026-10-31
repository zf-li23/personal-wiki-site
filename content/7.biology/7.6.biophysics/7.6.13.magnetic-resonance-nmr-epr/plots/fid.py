# Free induction decay, Fourier transform and line width.
# A: quadrature-detected FID (real and imaginary parts) of two resonances at offsets of 50 and 120 Hz with
#    T2 = 50 ms and 20 ms.
# B: real (absorption) and imaginary (dispersion) parts of its Fourier transform: Lorentzian lines whose full
#    width at half height is 1/(pi T2) = 6.4 Hz and 15.9 Hz; the two peaks have equal areas.
# C: simulated amide region of the 1H spectrum of folded proteins of 8, 25, 50 and 100 kDa at 600 MHz.
#    One amide proton per 110 Da, shifts drawn from a normal distribution (mean 8.2 ppm, s.d. 0.6 ppm, seed 0);
#    tau_c = 0.5 ns per kDa; R2 of each HN from dipolar relaxation by its 15N (1.02 A) and two protons at 2.4 A
#    in the rigid-sphere model (Lorentzian lines; each trace scaled to the same maximum).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9), gridspec_kw=dict(width_ratios=[1, 1, 1.25]))

dt = 1e-4
t = np.arange(0, 0.25, dt)
lines = ((50.0, 0.050), (120.0, 0.020))
fid = sum(np.exp(2j * np.pi * nu * t - t / T2) for nu, T2 in lines)
ax = axs[0]
ax.plot(t * 1e3, fid.real, color=charts.line("protein"), lw=0.9, label="real (x)")
ax.plot(t * 1e3, fid.imag - 2.6, color=charts.line("rna"), lw=0.9, label="imaginary (y)")
ax.set_xlim(0, 150)
ax.set_yticks([])
ax.legend(fontsize=7.5, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 1.12))
charts.style_axes(ax, "t / ms", "signal")
charts.title(ax, "A   FID (quadrature detection)")

ax = axs[1]
n = 2**16
spec = np.fft.fftshift(np.fft.fft(fid, n)) * dt
f = np.fft.fftshift(np.fft.fftfreq(n, dt))
sel = (f > 0) & (f < 170)
ax.plot(f[sel], spec.real[sel], color=charts.line("protein"), lw=1.6, label="absorption (real)")
ax.plot(f[sel], spec.imag[sel], color=P.muted(), lw=0.9, ls="--", label="dispersion (imaginary)")
for nu, T2 in lines:
    w = 1 / (np.pi * T2)
    h = spec.real[np.argmin(abs(f - nu))] / 2
    ax.annotate("", xy=(nu - w / 2, h), xytext=(nu + w / 2, h),
                arrowprops=dict(arrowstyle="<->", color=charts.line("rna"), lw=1.0))
    ax.text(nu + w / 2 + 3, h, f"1/(πT₂)\n= {w:.1f} Hz", ha="left", va="center", fontsize=7.5, color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_xlim(0, 170)
ax.set_yticks([])
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "frequency offset / Hz", "spectrum")
charts.title(ax, "B   Fourier transform: Lorentzian lines")

ax = axs[2]
hb, mu0 = 1.054571817e-34, 1.25663706e-6
gH, gN = 2.6752218744e8, -2.71261804e7
B0 = 14.09
wH, wN = gH * B0, gN * B0


def J(w, tc):
    return 0.4 * tc / (1 + (w * tc) ** 2)


def r2_hn(tc):
    b = mu0 / (4 * np.pi) * gH**2 * hb / 2.4e-10**3
    r_hh = 2 * 0.15 * b**2 * (3 * tc + 5 * tc / (1 + (wH * tc) ** 2) + 2 * tc / (1 + 4 * (wH * tc) ** 2))
    d = mu0 * hb * gH * gN / (4 * np.pi * 1.02e-10**3)
    r_hn = d**2 / 8 * (4 * J(0, tc) + J(wH - wN, tc) + 3 * J(wH, tc) + 6 * J(wN, tc) + 6 * J(wH + wN, tc))
    return r_hh + r_hn


rng = np.random.default_rng(0)
ppm = np.linspace(6.3, 10.3, 4000)
for k, M in enumerate((8, 25, 50, 100)):
    nres = int(M * 1000 / 110)
    shifts = rng.normal(8.2, 0.6, nres)
    lw_hz = r2_hn(0.5e-9 * M) / np.pi
    g = lw_hz / 2 / 600.0                        # half width in ppm at 600 MHz
    y = sum(g**2 / ((ppm - s) ** 2 + g**2) for s in shifts)
    y = 0.85 * y / y.max()
    ax.plot(ppm, y + 1.15 * k, color=charts.line("protein"), lw=0.8)
    ax.text(10.25, 1.15 * k + 0.9, f"{M} kDa   τc ≈ {0.5 * M:.0f} ns   Δν ≈ {lw_hz:.0f} Hz",
            fontsize=7.5, color=P.ink(), ha="left")
ax.set_xlim(10.3, 6.3)
ax.set_ylim(-0.05, 4.65)
ax.set_yticks([])
charts.style_axes(ax, "¹H chemical shift / ppm", None)
charts.title(ax, "C   Amide region at 600 MHz (simulated)")
fig.tight_layout()
