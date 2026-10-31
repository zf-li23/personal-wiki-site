# Calibrating an optical trap from the Brownian motion of the trapped bead (simulation).
# A bead of radius 0.5 um in water at 25 C (friction gamma = 6 pi eta a = 8.4e-6 pN s/nm) in a harmonic trap
# of stiffness kappa = 0.05 pN/nm; the overdamped Langevin equation is integrated exactly as an
# Ornstein-Uhlenbeck process and sampled at 100 kHz for 2 s.
# A: 20 ms of the position trace. B: position histogram and the Boltzmann distribution: equipartition gives
#    kappa = kT / <x^2>. C: one-sided power spectral density (averaged over 50 segments) and the Lorentzian
#    S(f) = kT / (pi^2 gamma (fc^2 + f^2)) fitted for fc and gamma; kappa = 2 pi gamma fc.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kT = 4.11                      # pN nm at 298 K
gamma = 6 * np.pi * 0.89e-9 * 500  # pN s / nm  (eta = 0.89e-9 pN s / nm^2, a = 500 nm)
kappa = 0.05                   # pN / nm
fs, T = 1e5, 2.0
n = int(fs * T)
dt = 1 / fs
tau = gamma / kappa
a = np.exp(-dt / tau)
sd = np.sqrt(kT / kappa * (1 - a * a))
x = np.empty(n)
x[0] = 0.0
noise = rng.normal(0, sd, n)
for i in range(1, n):
    x[i] = a * x[i - 1] + noise[i]

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0), gridspec_kw={"width_ratios": [1.3, 0.8, 1.1]})
t = np.arange(n) * dt
axs[0].plot(t[:2000] * 1e3, x[:2000], color=charts.line("neutral"), lw=0.6)
charts.style_axes(axs[0], "time / ms", "bead position x / nm")
charts.title(axs[0], "A   Thermal motion in the trap")

var = x.var()
h, e = np.histogram(x, bins=60, density=True)
c = 0.5 * (e[1:] + e[:-1])
axs[1].barh(c, h, height=e[1] - e[0], color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.3)
xx = np.linspace(e[0], e[-1], 200)
axs[1].plot(np.exp(-kappa * xx**2 / (2 * kT)) / np.sqrt(2 * np.pi * kT / kappa), xx, color=charts.line("rna"), lw=1.5)
axs[1].text(0.002, e[-1] * 0.85, f"κ = kT/⟨x²⟩\n= {kT / var:.4f} pN/nm", fontsize=8, color=P.ink())
charts.style_axes(axs[1], "probability density / nm⁻¹", None)
charts.title(axs[1], "B   Equipartition")

seg = 50
L = n // seg
win = x[: seg * L].reshape(seg, L)
F = np.fft.rfft(win, axis=1)
f = np.fft.rfftfreq(L, dt)
S = (2 * dt / L) * np.mean(np.abs(F) ** 2, axis=0)       # one-sided PSD, nm^2/Hz
m = (f > 5) & (f < fs / 4)


def lorentz(f, fc, D):
    return D / (np.pi**2 * (fc**2 + f**2))


(fc_fit, D_fit), _ = curve_fit(lorentz, f[m], S[m], p0=(500, kT / gamma), sigma=S[m])
g_fit = kT / D_fit
axs[2].loglog(f[1:], S[1:], color=charts.line("neutral"), lw=0.6)
axs[2].loglog(f[m], lorentz(f[m], fc_fit, D_fit), color=charts.line("rna"), lw=1.6)
axs[2].axvline(fc_fit, color=P.muted(), lw=0.7, ls=":")
axs[2].text(fc_fit * 1.15, S[1:].max() * 0.3,
            f"f_c = {fc_fit:.0f} Hz\nκ = 2πγf_c = {2 * np.pi * g_fit * fc_fit:.4f} pN/nm", fontsize=8, color=P.ink())
charts.style_axes(axs[2], "frequency / Hz", "PSD / (nm² Hz⁻¹)")
charts.title(axs[2], "C   Power spectrum and Lorentzian fit")
fig.tight_layout()
