# Fluorescence correlation spectroscopy.
# A: theoretical autocorrelation G(tau) = (1/N)(1 + tau/tau_D)^-1 (1 + tau/(omega^2 tau_D))^-1/2 for a confocal
#    volume with w0 = 0.25 um, omega = z0/w0 = 5 and N = 5: a free dye (D = 414 um^2/s), GFP (87 um^2/s) and an
#    antibody-sized complex (40 um^2/s); the dye curve is also shown with a 15 % triplet fraction
#    (tau_T = 2 us), and the GFP curve for N = 3 and 10 (dotted).
# B: Brownian dynamics check of the formula: 720 particles diffusing (D = 10 um^2/s) in a periodic box of
#    3 x 3 x 12 um^3 around a Gaussian detection volume with w0 = 0.3 um and z0 = 1.5 um (mean N about 5),
#    100 000 steps of 50 us; the intensity trace is the sum of exp(-2(x^2+y^2)/w0^2 - 2 z^2/z0^2).
# C: the simulated intensity trace (first 0.2 s) and its fluctuations about the mean.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def G(tau, N, tD, om):
    return (1 / N) / (1 + tau / tD) / np.sqrt(1 + tau / (om**2 * tD))


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2), gridspec_kw={"width_ratios": [1.2, 1.2, 1]})
ax = axs[0]
tau = np.logspace(-7, 0, 400)
w0, om = 0.25, 5.0
for D, tok, lab in ((414, "positive", "dye"), (87, "dna", "GFP"), (40, "rna", "IgG-sized complex")):
    tD = w0**2 / (4 * D)
    ax.semilogx(tau, G(tau, 5, tD, om), color=charts.line(tok), lw=1.8, label=f"{lab}: τ_D = {tD * 1e6:.0f} µs")
tD = w0**2 / (4 * 414)
FT, tT = 0.15, 2e-6
ax.semilogx(tau, G(tau, 5, tD, om) * (1 - FT + FT * np.exp(-tau / tT)) / (1 - FT), color=charts.line("positive"),
            lw=1.0, ls="--", label="dye with triplet blinking")
tD = w0**2 / (4 * 87)
for N in (3, 10):
    ax.semilogx(tau, G(tau, N, tD, om), color=charts.line("dna"), lw=0.8, ls=":")
ax.text(2e-7, 0.115, "GFP, N = 10", fontsize=7, color=P.ink())
ax.text(2e-7, 0.345, "GFP, N = 3", fontsize=7, color=P.ink())
ax.set_ylim(0, 0.37)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "lag time τ / s", "G(τ)")
charts.title(ax, "A   Diffusion, blinking and concentration")

# Brownian dynamics
D, w0s, z0s = 10.0, 0.3, 1.5
Lx, Lz = 3.0, 12.0
npart, nstep, dt = 720, 100000, 5e-5
pos = np.column_stack([rng.uniform(-Lx / 2, Lx / 2, npart), rng.uniform(-Lx / 2, Lx / 2, npart),
                       rng.uniform(-Lz / 2, Lz / 2, npart)])
box = np.array([Lx, Lx, Lz])
step = np.sqrt(2 * D * dt)
F = np.empty(nstep)
for i in range(nstep):
    pos += step * rng.standard_normal((npart, 3))
    pos -= box * np.round(pos / box)
    F[i] = np.exp(-2 * (pos[:, 0] ** 2 + pos[:, 1] ** 2) / w0s**2 - 2 * pos[:, 2] ** 2 / z0s**2).sum()
dF = F - F.mean()
nfft = 1 << (2 * nstep - 1).bit_length()
fx = np.fft.rfft(dF, nfft)
ac = np.fft.irfft(fx * np.conj(fx), nfft)[:nstep] / np.arange(nstep, 0, -1)
Gs = ac / F.mean() ** 2
lags = np.arange(nstep) * dt
sel = np.unique(np.logspace(0, np.log10(nstep / 10), 60).astype(int))
Veff = np.pi**1.5 * w0s**2 * z0s
Nmean = npart / (Lx * Lx * Lz) * Veff
tDs = w0s**2 / (4 * D)
ax = axs[1]
ax.semilogx(lags[sel], Gs[sel], "o", ms=3.5, color=charts.line("dna"), label="simulation")
tt = np.logspace(np.log10(dt), np.log10(lags[sel[-1]]), 200)
ax.semilogx(tt, G(tt, Nmean, tDs, z0s / w0s), color=charts.line("negative"), lw=1.5,
            label=f"theory, ⟨N⟩ = {Nmean:.1f}, τ_D = {tDs * 1e3:.2f} ms")
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "lag time τ / s", "G(τ)")
charts.title(ax, "B   Simulation confirms the formula")
ax = axs[2]
m = int(0.2 / dt)
ax.plot(np.arange(m) * dt, F[:m], color=charts.line("dna"), lw=0.6)
ax.axhline(F.mean(), color=charts.line("negative"), lw=1.0)
charts.style_axes(ax, "time / s", "detected intensity (a.u.)")
charts.title(ax, "C   Fluctuations of a few molecules")
fig.tight_layout()
