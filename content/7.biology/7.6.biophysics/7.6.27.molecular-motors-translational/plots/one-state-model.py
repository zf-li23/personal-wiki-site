# The one-state motor. A: 30 stochastic trajectories (Gillespie simulation) of a motor that steps a = 8 nm
# forward at k+ = 100 /s and backward at k- = 10 /s; the mean moves at V = a(k+ - k-) and the spread grows as
# sqrt(2Dt) with D = a^2 (k+ + k-)/2 (band: mean +/- one standard deviation). B: velocity against load for the
# generalized detailed balance k+/k- = exp[(dmu - F a)/kBT] with dmu = 8 kBT (stall force dmu/a = 4.1 pN; small, so that all three curves stay visible) and
# k+(0) = 100 /s, when the load acts only on the forward rate (theta = 1), equally (theta = 0.5) or only on the
# backward rate (theta = 0); negative forces assist the motor. The velocity axis is linear within +/- 10 nm/s
# and logarithmic outside.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
a, kp, km = 8.0, 100.0, 10.0
T = 1.0
fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
for i in range(30):
    t, x, ts, xs = 0.0, 0.0, [0.0], [0.0]
    while t < T:
        t += rng.exponential(1 / (kp + km))
        x += a if rng.random() < kp / (kp + km) else -a
        ts.append(t); xs.append(x)
    ax.step(ts, xs, where="post", color=charts.line("enzyme"), lw=0.6, alpha=0.6)
tt = np.linspace(0, T, 200)
V, D = a * (kp - km), a * a * (kp + km) / 2
ax.plot(tt, V * tt, color=charts.line("negative"), lw=1.8, label="$Vt$")
ax.fill_between(tt, V * tt - np.sqrt(2 * D * tt), V * tt + np.sqrt(2 * D * tt), color=P.fill("negative"), alpha=0.3, lw=0,
                label="$Vt \\pm \\sqrt{2Dt}$")
ax.set_xlim(0, T); ax.set_ylim(-20, 850)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "$t$ / s", "position / nm")
charts.title(ax, "A   Drift and spreading of a biased hopper")

ax = axs[1]
kT, dmu, k0 = 4.1, 8 * 4.1, 100.0
F = np.linspace(-3, 7, 400)
for th, tok in ((1.0, "dna"), (0.5, "enzyme"), (0.0, "rna")):
    kf = k0 * np.exp(-th * F * a / kT)
    kb = k0 * np.exp(-dmu / kT) * np.exp((1 - th) * F * a / kT)
    ax.plot(F, a * (kf - kb), color=charts.line(tok), lw=1.8, label=f"$\\theta$ = {th:g}")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(dmu / a, color=P.muted(), lw=0.8, ls="--")
ax.set_yscale("symlog", linthresh=10)
ax.text(dmu / a + 0.9, -15, "stall\n$F_\\mathrm{s} = \\Delta\\mu/a$", fontsize=7.5, color=P.ink(), va="top")
ax.axvspan(-3, 0, color=P.fill("positive"), alpha=0.25, lw=0)
ax.text(-2.9, -300, "assisting\nload", fontsize=7.5, color=P.ink(), va="top")
ax.set_ylim(-3000, 3e4); ax.set_xlim(-3, 7)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "load $F$ / pN", "$V$ / (nm s$^{-1}$)")
charts.title(ax, "B   Where the load acts sets the curve's shape")
fig.tight_layout()
