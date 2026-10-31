"""Dynamic light scattering (Theorems 8.11.1-8.11.2, Formula 8.11.1).

A, B: a direct simulation. N = 400 particles diffuse independently along the scattering vector q;
the scattered field is E(t) = sum_j exp(i q x_j(t)) / sqrt(N) and the intensity I = |E|^2. Time is in
units of the decay time 1/Gamma = 1/(q^2 D); 40 000 steps of 0.02/Gamma, seed 0. A: a stretch of the
fluctuating intensity (a speckle). B: the computed intensity autocorrelation g2 - 1 and field
autocorrelation |g1| against the predictions exp(-2 Gamma tau) and exp(-Gamma tau) (Siegert relation
with beta = 1). C: g2 - 1 for spheres of hydrodynamic radius 2, 7 and 100 nm in water at 25 C
(633 nm laser, 90 degrees, beta = 0.9). D: a mixture of 99.9 % (by mass) 5 nm particles with 0.1 %
of 100 nm aggregates: weights proportional to mass x M x P(q) (sphere form factor); the first two
cumulants of the decay-rate distribution give an intensity-weighted (z-average) radius dominated by the aggregates.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
kT = 1.380649e-23 * 298.15
eta = 0.890e-3
lam, n, theta = 633e-9, 1.332, np.pi / 2
q = 4 * np.pi * n * np.sin(theta / 2) / lam


def gamma(Rh):
    return q ** 2 * kT / (6 * np.pi * eta * Rh)


rng = np.random.default_rng(0)
N, steps, dt = 400, 40000, 0.02
phase = rng.uniform(0, 2 * np.pi, N)
E = np.empty(steps, complex)
for k in range(steps):
    E[k] = np.exp(1j * phase).sum() / np.sqrt(N)
    phase += rng.normal(0, np.sqrt(2 * dt), N)       # q dx has variance 2 q^2 D dt = 2 Gamma dt
I = np.abs(E) ** 2


def autocorr(x, maxlag):
    x = np.asarray(x)
    f = np.fft.fft(np.r_[x, np.zeros_like(x)])
    ac = np.fft.ifft(f * np.conj(f))[:maxlag] / np.arange(len(x), len(x) - maxlag, -1)
    return ac


lags = 200
g2 = (autocorr(I, lags).real / I.mean() ** 2)
g1 = np.abs(autocorr(E, lags)) / np.mean(np.abs(E) ** 2)
tau = np.arange(lags) * dt

fig, ax = bio.canvas(25.0, 8.4)
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.3, 1.3, 4.8, 6.0))
seg = slice(0, 1000)
pa.plot(np.arange(steps)[seg] * dt, I[seg], color=charts.line("channel"), lw=0.8)
charts.style_axes(pa, r"time $t\,\Gamma$", r"intensity $I/\langle I\rangle$")
charts.title(pa, "Simulated speckle intensity")

bio.panel(ax, "B", (6.8, 8.3))
pb = charts.axes_at(ax, (8.0, 1.3, 4.8, 6.0))
pb.plot(tau, g2 - 1, "o", ms=2.2, mfc=charts.line("protein"), mec="none", label="simulated $g_2 - 1$")
pb.plot(tau, g1, "o", ms=2.2, mfc=charts.line("enzyme"), mec="none", label=r"simulated $|g_1|$")
pb.plot(tau, np.exp(-2 * tau), color=charts.line("protein"), lw=1.2, label=r"$\mathrm{e}^{-2\Gamma\tau}$")
pb.plot(tau, np.exp(-tau), color=charts.line("enzyme"), lw=1.2, label=r"$\mathrm{e}^{-\Gamma\tau}$")
pb.set_xlim(0, 4)
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, r"lag $\tau\,\Gamma$", "correlation")
charts.title(pb, "Siegert relation: intensity decays twice as fast")

bio.panel(ax, "C", (13.5, 8.3))
pc = charts.axes_at(ax, (14.7, 1.3, 4.8, 6.0))
tt = np.logspace(-7, -1, 400)
for Rh, tok in ((2e-9, "channel"), (7e-9, "protein"), (100e-9, "receptor")):
    G = gamma(Rh)
    pc.semilogx(tt * 1e6, 0.9 * np.exp(-2 * G * tt), color=charts.line(tok), lw=1.6,
                label=f"{Rh * 1e9:g} nm, " + (f"{1e6 / G:.0f} µs" if G > 1e4 else f"{1e3 / G:.1f} ms"))
pc.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left", title="R$_h$, 1/Γ", title_fontsize=FT["tiny"])
charts.style_axes(pc, r"lag $\tau$ / µs", r"$g_2(\tau) - 1$")
charts.title(pc, "Size sets the decay time")

bio.panel(ax, "D", (20.2, 8.3))
pd = charts.axes_at(ax, (21.4, 1.3, 3.3, 6.0))


def formfactor(R):
    x = q * R
    return (3 * (np.sin(x) - x * np.cos(x)) / x ** 3) ** 2


radii = np.array([5e-9, 100e-9])
mass_frac = np.array([0.999, 0.001])
w = mass_frac * radii ** 3 * formfactor(radii)          # mass fraction x M x P(q)
w /= w.sum()
G = gamma(radii)
Gbar = (w * G).sum()                                      # first cumulant: intensity-weighted mean decay rate
mu2 = (w * (G - Gbar) ** 2).sum()                        # second cumulant
Rz = q ** 2 * kT / (6 * np.pi * eta * Gbar)
pdi = mu2 / Gbar ** 2
labels = ["5 nm", "100 nm"]
x0 = np.arange(2)
pd.bar(x0 - 0.18, mass_frac * 100, width=0.34, color=P.fill("neutral"), edgecolor=P.edge("neutral"), label="mass %")
pd.bar(x0 + 0.18, w * 100, width=0.34, color=P.fill("receptor"), edgecolor=P.edge("receptor"), label="intensity %")
pd.set_xticks(x0)
pd.set_xticklabels(labels)
pd.set_ylim(0, 125)

pd.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pd.text(1.0, 100, f"cumulants:\nR$_z$ = {Rz * 1e9:.0f} nm\nPDI = {pdi:.1f}", fontsize=FT["tiny"], color=P.ink(), va="top", ha="center")
charts.style_axes(pd, None, "percent")
charts.title(pd, "A trace of aggregate")
