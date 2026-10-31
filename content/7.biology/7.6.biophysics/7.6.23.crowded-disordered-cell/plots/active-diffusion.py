"""A particle held in an elastic medium and stirred by active forces (overdamped Langevin
dynamics, gamma dx/dt = -k x + xi(t) + f_a(t); units gamma = k = kB T = 1, so the relaxation time
tau = gamma/k = 1). The thermal noise xi has strength 2 gamma kB T. The active force f_a, the sum
of many motors pulling on the network, is modeled as an Ornstein-Uhlenbeck process with
correlation time tau_a = 300 and variance s^2 = 20 kB T k, starting from the stationary state.
A: MSD of passive (thermal only) and active particles: both start diffusively; the passive
particle saturates at 2 kB T/k (twice the equipartition variance), while the active particle's MSD keeps
growing, nearly linearly, for tau < t < tau_a, because the active force itself wanders like a
random walk on these times; it saturates only beyond tau_a. Simulation (dots, 200 particles)
and theory (lines). B: ratio of the measured fluctuation spectrum S_x(omega) to the spectrum
2 kB T Im chi(omega)/omega predicted from the response function chi = 1/(k - i gamma omega) by the
fluctuation-dissipation theorem: one for the passive particle, far above one at low
frequencies for the active one (an "effective temperature")."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
dt, nsteps, M = 0.05, 40000, 200
ta, s2 = 300.0, 20.0
lam = 1 / ta
x_p = rng.normal(size=M); fa = rng.normal(size=M) * np.sqrt(s2)
x_a = fa / (1 + lam) + rng.normal(size=M)
for i in range(int(3 * ta / dt)):  # burn-in to the stationary state
    xi = rng.normal(size=M) * np.sqrt(2 / dt)
    x_p += (-x_p + xi) * dt
    x_a += (-x_a + xi + fa) * dt
    fa += -fa * lam * dt + np.sqrt(2 * s2 * lam * dt) * rng.normal(size=M)
x0p, x0a = x_p.copy(), x_a.copy()
rec = set(np.unique(np.logspace(0, np.log10(nsteps), 40).astype(int)).tolist())
t, msd_p, msd_a = [], [], []
for i in range(1, nsteps + 1):
    xi = rng.normal(size=M) * np.sqrt(2 / dt)
    x_p += (-x_p + xi) * dt
    x_a += (-x_a + xi + fa) * dt
    fa += -fa * lam * dt + np.sqrt(2 * s2 * lam * dt) * rng.normal(size=M)
    if i in rec:
        t.append(i * dt)
        msd_p.append(np.mean((x_p - x0p) ** 2)); msd_a.append(np.mean((x_a - x0a) ** 2))
t = np.array(t)

fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.17, top=0.87)
ax = axs[0]
tt = np.logspace(np.log10(t[0]), np.log10(t[-1]), 300)
th_p = 2 * (1 - np.exp(-tt))
act = 2 * s2 / (1 - lam**2) * ((1 - lam) - np.exp(-lam * tt) + lam * np.exp(-tt))
ax.plot(t, msd_p, "o", ms=3, color=charts.line("dna"), label="passive (simulation)")
ax.plot(t, msd_a, "o", ms=3, color=charts.line("blood"), label="active (simulation)")
ax.plot(tt, th_p, color=charts.line("dna"), lw=1.2)
ax.plot(tt, th_p + act, color=charts.line("blood"), lw=1.2)
ax.plot(tt, 2 * tt, color=P.muted(), lw=0.8, ls=":", label=r"free diffusion $2Dt$")
ax.axvline(1, color=P.muted(), lw=0.5); ax.axvline(ta, color=P.muted(), lw=0.5)
ax.text(1.1, 2e-2, r"$\tau$", fontsize=bio.core.FONT["small"], color=P.ink())
ax.text(ta * 1.1, 2e-2, r"$\tau_a$", fontsize=bio.core.FONT["small"], color=P.ink())
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(1e-2, 2e2)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"time $t/\tau$", r"$\langle x^2\rangle$ / $(k_{\mathrm{B}}T/k)$")
charts.title(ax, "A  Active forces unpin the particle")

ax = axs[1]
w = np.logspace(-4, 2, 300)
chi2 = 1 / (1 + w**2)
S_th = 2 * chi2  # 2 kT gamma |chi|^2
S_act = chi2 * 2 * s2 * ta / (1 + (w * ta) ** 2)
ax.plot(w, S_th / S_th, color=charts.line("dna"), lw=1.7, label="passive")
ax.plot(w, (S_th + S_act) / S_th, color=charts.line("blood"), lw=1.7, label="active")
ax.axvline(1 / ta, color=P.muted(), lw=0.5)
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"frequency $\omega\tau$", r"$S_x / [2k_{\mathrm{B}}T\,\mathrm{Im}\,\chi/\omega]$")
charts.title(ax, "B  Violation of fluctuation-dissipation")
