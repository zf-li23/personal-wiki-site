"""The Cahn-Hilliard equation in dimensionless form, d psi/dt = laplacian(psi^3 - psi - laplacian psi)
(double-well free energy f = (psi^2 - 1)^2/4, gradient coefficient and mobility 1, so the interface
width is about 1). A: linear stability of a homogeneous state psi0: growth rate
sigma(q) = q^2 (1 - 3 psi0^2) - q^4; inside the spinodal (|psi0| < 1/sqrt 3) a band of wave numbers
grows, fastest at q_max = [(1 - 3 psi0^2)/2]^(1/2); outside it every mode decays. B, C: a simulation on
a periodic 128 x 128 grid (semi-implicit Fourier scheme) from small random fluctuations about
psi0 = -0.35: dense droplets (dark) form and coarsen. D: the characteristic domain size
L = 2 pi / <q> from the structure factor grows as t^(1/3) at late times (dashed), the Lifshitz-Slyozov
law of diffusion-limited coarsening."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(10.8, 3.1))
gs = fig.add_gridspec(1, 4, width_ratios=[1.15, 0.85, 0.85, 1.15], wspace=0.42, left=0.055, right=0.985,
                      bottom=0.17, top=0.87)

ax = fig.add_subplot(gs[0])
q = np.linspace(0, 1.0, 300)
for psi0, tok in [(0.0, "dna"), (-0.35, "bacterium"), (-0.5, "blood"), (-0.65, "neutral")]:
    s = q ** 2 * (1 - 3 * psi0 ** 2) - q ** 4
    ax.plot(q, s, color=charts.line(tok), lw=1.6, label=rf"$\psi_0 = {psi0:g}$")
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_ylim(-0.12, 0.3)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "wave number $q$", r"growth rate $\sigma(q)$")
charts.title(ax, "A  Linear stability")

# ---- simulation
n = 128
rng = np.random.default_rng(0)
psi = -0.35 + 0.05 * rng.standard_normal((n, n))
k = 2 * np.pi * np.fft.fftfreq(n, d=1.0)
kx, ky = np.meshgrid(k, k)
k2 = kx ** 2 + ky ** 2
A = 2.0  # linear stabilization
t, dt = 0.0, 0.05
snap_times = [60.0, 3000.0]
snaps = {}
ts, Ls = [], []
next_record = 5.0
while t < 3000.0:
    nl = np.fft.fft2(psi ** 3 - (1 + A) * psi)
    ph = np.fft.fft2(psi)
    ph = (ph - dt * k2 * nl) / (1 + dt * (k2 ** 2 + A * k2))
    psi = np.real(np.fft.ifft2(ph))
    t += dt
    dt = min(1.0, dt * 1.004)
    if t >= next_record:
        S = np.abs(np.fft.fft2(psi - psi.mean())) ** 2
        kk = np.sqrt(k2)
        mask = kk > 0
        qmean = np.sum(kk[mask] * S[mask]) / np.sum(S[mask])
        ts.append(t)
        Ls.append(2 * np.pi / qmean)
        next_record *= 1.15
    for st in snap_times:
        if st not in snaps and t >= st:
            snaps[st] = psi.copy()

for i, st in enumerate(snap_times):
    ax = fig.add_subplot(gs[1 + i])
    ax.imshow(-snaps[st], cmap="Greys", vmin=-1.1, vmax=1.1, interpolation="bilinear")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(P.muted())
    charts.title(ax, f"{'BC'[i]}  t = {st:g}")

ax = fig.add_subplot(gs[3])
ts, Ls = np.array(ts), np.array(Ls)
ax.loglog(ts, Ls, "o", ms=3, color=charts.line("protein"))
sel = ts > 300
c = np.exp(np.mean(np.log(Ls[sel]) - np.log(ts[sel]) / 3))
tt = np.logspace(np.log10(100), np.log10(3000), 20)
ax.loglog(tt, c * tt ** (1 / 3), "--", color=P.muted(), lw=1.0)
ax.text(400, c * 400 ** (1 / 3) * 0.7, r"$\propto t^{1/3}$", fontsize=FT["tiny"], color=P.ink())
from matplotlib.ticker import FixedLocator, NullFormatter, ScalarFormatter
ax.yaxis.set_major_locator(FixedLocator([10, 15, 20, 30]))
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
charts.style_axes(ax, "time $t$", "domain size $L(t)$")
charts.title(ax, "D  Coarsening")
