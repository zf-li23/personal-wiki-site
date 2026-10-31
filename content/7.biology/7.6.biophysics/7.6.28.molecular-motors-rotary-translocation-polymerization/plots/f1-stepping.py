# Rotation of F1-ATPase (alpha3 beta3 gamma) with a 40 nm gold bead on gamma, as in dark-field experiments.
# Kinetic scheme per 120 degrees: ATP binding at k_on [ATP] (k_on = 3e7 /(M s)) at the binding dwell, then an
# 80 degree substep; at the catalytic dwell two sequential ~1 ms events (hydrolysis k_h = 1000 /s, phosphate
# release k_p = 700 /s), then a 40 degree substep. The bead follows with a 0.1 ms relaxation time and Brownian
# fluctuations of 6 degrees; sampling at 20 kHz.
# A: angle against time at 2 uM, 20 uM and 2 mM ATP (offset in time). B: histograms of the two dwells at
# 2 uM ATP: binding dwells are exponential, catalytic dwells rise from zero (two hidden steps, Formula 27.4.1 of
# 7.6.27). C: rotation rate against [ATP]: Michaelis-Menten with Vmax = 1/(3 (1/k_h + 1/k_p)) and
# K_M = Vmax*3/k_on; for comparison a 1 um actin filament, whose viscous drag limits the speed.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
kon, kh, kp = 3e7, 1000.0, 700.0
fs = 20000.0


def trace(atp, T):
    t_ev, ang, a, t = [0.0], [0.0], 0.0, 0.0
    bind, cat = [], []
    while t < T:
        d1 = rng.exponential(1 / (kon * atp)); t += d1; a += 80; t_ev.append(t); ang.append(a); bind.append(d1)
        d2 = rng.exponential(1 / kh) + rng.exponential(1 / kp); t += d2; a += 40; t_ev.append(t); ang.append(a); cat.append(d2)
    tt = np.arange(0, T, 1 / fs)
    target = np.array(ang)[np.searchsorted(t_ev, tt, side="right") - 1]
    # first-order relaxation of the bead (0.1 ms) plus Ornstein-Uhlenbeck noise
    al = np.exp(-1 / (fs * 1e-4))
    x = np.empty_like(tt); n = np.empty_like(tt); x[0] = n[0] = 0.0
    e = rng.standard_normal(tt.size) * 6.0 * np.sqrt(1 - al * al)
    for i in range(1, tt.size):
        x[i] = al * x[i - 1] + (1 - al) * target[i]
        n[i] = al * n[i - 1] + e[i]
    return tt, x + n, np.array(bind), np.array(cat)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0), gridspec_kw={"width_ratios": [1.3, 1, 1]})
ax = axs[0]
for atp, tok, T, lab in ((2e-6, "dna", 0.12, "2 µM"), (20e-6, "enzyme", 0.06, "20 µM"), (2e-3, "rna", 0.03, "2 mM")):
    tt, x, _, _ = trace(atp, T)
    ax.plot(tt * 1e3, x, color=charts.line(tok), lw=0.8, label=f"[ATP] = {lab}")
for k in range(0, 1200, 120):
    ax.axhline(k, color=P.muted(), lw=0.3)
    ax.axhline(k + 80, color=P.muted(), lw=0.3, ls=":")
ax.set_xlim(0, 120); ax.set_ylim(-20, 1100)
ax.set_yticks(range(0, 1200, 240))
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "$t$ / ms", "angle / degrees")
charts.title(ax, "A   120° steps split into 80° and 40°")

ax = axs[1]
_, _, b, c = trace(2e-6, 6.0)
bins = np.linspace(0, 0.06, 31)
ax.hist(b, bins, density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, alpha=0.8, label="binding dwell (0°)")
ax.hist(c, np.linspace(0, 0.012, 25), density=True, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.4, alpha=0.6,
        label="catalytic dwell (80°)")
tt = np.linspace(1e-5, 0.06, 300)
k1 = kon * 2e-6
ax.plot(tt, k1 * np.exp(-k1 * tt), color=charts.line("dna"), lw=1.5)
ax.plot(tt, kh * kp / (kh - kp) * (np.exp(-kp * tt) - np.exp(-kh * tt)), color=charts.line("rna"), lw=1.5)
ax.set_yscale("log"); ax.set_ylim(1, 1000); ax.set_xlim(0, 0.06)
ax.set_xticks([0, 0.02, 0.04, 0.06]); ax.set_xticklabels(["0", "20", "40", "60"])
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "dwell time / ms", "density / s$^{-1}$")
charts.title(ax, "B   Two dwells at 2 µM ATP")

ax = axs[2]
A = np.logspace(-8, -2, 200)
vmax = 1 / (3 * (1 / kh + 1 / kp))
v = 1 / (3 * (1 / (kon * A) + 1 / kh + 1 / kp))
ax.loglog(A * 1e6, v, color=charts.line("enzyme"), lw=1.8, label="40 nm bead (kinetics limits)")
zeta = 4 * np.pi * 1e-3 * (1e-6) ** 3 / (3 * (np.log(1e-6 / 10e-9) - 0.45))
w_drag = 40e-21 / zeta / (2 * np.pi)
ax.loglog(A * 1e6, 1 / (1 / v + 1 / w_drag), color=charts.line("actin"), lw=1.8, label="1 µm actin filament (drag limits)")
KM = vmax * 3 / kon
ax.axvline(KM * 1e6, color=P.muted(), lw=0.8, ls="--")
ax.text(KM * 1e6 * 1.2, 0.05, f"$K_\\mathrm{{M}}$ = {KM * 1e6:.0f} µM", fontsize=7.5, color=P.ink())
ax.text(0.012, vmax * 1.3, f"$V_\\max$ = {vmax:.0f} rev/s", fontsize=7.5, color=P.ink())
ax.set_ylim(0.01, 400)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "[ATP] / µM", "rotation rate / (rev s$^{-1}$)")
charts.title(ax, "C   Rate against ATP")
fig.tight_layout()
