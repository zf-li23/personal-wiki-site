"""Force from polymerization: the Brownian ratchet in its limits and the elastic ratchet (26.5).

A: velocity against the dimensionless load omega = F delta/kBT. Reaction-limited ratchet (fast load
diffusion), v = delta (kon c e^-omega - koff), for actin at 10 uM (kon c = 116 s^-1, koff = 1.4 s^-1,
stall at omega = ln(c/Cc) = 4.4), normalized by its unloaded value; diffusion-limited ideal ratchet
(instant addition when a gap opens), v = (D/delta) omega^2/(e^omega - 1 - omega), normalized by 2D/delta.
B: elastic Brownian ratchet: a filament at angle theta to the load normal advances the load by
delta cos(theta) per subunit, v = delta cos(theta) (kon c e^(-omega cos theta) - koff), with
delta = 2.7 nm; at high load, inclined filaments push faster. C: thermal lateral fluctuation of the free
tip of an actin filament of free length l (clamped at its base, rms sqrt(kBT l^3/3EI)) against the step
2.7 nm, and the largest free length that does not buckle under 1 or 5 pN, (pi/2) sqrt(EI/F): filaments
can push only in the window between."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
KBT, DELTA = 4.1, 2.7  # pN nm, nm
KONC, KOFF = 116.0, 1.4
EI = 0.07e6  # pN nm^2

fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.36, left=0.07, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
w = np.linspace(1e-4, 6, 300)
v_r = (KONC * np.exp(-w) - KOFF) / (KONC - KOFF)
v_d = w ** 2 / (np.expm1(w) - w) / 2.0
ax.plot(w, v_r, color=charts.line("actin"), lw=1.4, label="reaction-limited (actin, 10 µM)")
ax.plot(w, v_d, color=charts.line("channel"), lw=1.4, ls="--", label="diffusion-limited ideal ratchet")
ws = np.log(KONC / KOFF)
ax.axvline(ws, color=P.muted(), lw=0.6, ls=":")
ax.text(ws + 0.08, 0.6, "stall\n" + r"$\ln(c/C_{\mathrm{c}})$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-0.08, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"load $F\delta/k_{\mathrm{B}}T$", "velocity / unloaded velocity")
charts.title(ax, "A  Two limits of the ratchet")

ax = axs[1]
F = np.linspace(0, 16, 300)
for th, ls in ((0, "-"), (30, "--"), (60, "-."), (75, ":")):
    c = np.cos(np.radians(th))
    v = DELTA * c * (KONC * np.exp(-F * DELTA * c / KBT) - KOFF)  # nm/s
    ax.plot(F, v / 1000 * 60, color=charts.line("actin"), lw=1.4, ls=ls, label=rf"$\theta = {th}^\circ$")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-0.5, 19.5)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "load per filament F / pN", r"load velocity / (µm min$^{-1}$)")
charts.title(ax, "B  Inclined filaments")

ax = axs[2]
l = np.logspace(0.7, 3.2, 300)  # nm
rms = np.sqrt(KBT * l ** 3 / (3 * EI))
ax.plot(l, rms, color=charts.line("actin"), lw=1.4, label="rms tip fluctuation")
ax.axhline(DELTA, color=P.muted(), lw=0.8, ls=":")
ax.text(6, DELTA * 1.15, r"step $\delta$ = 2.7 nm", fontsize=bio.core.FONT["tiny"], color=P.ink())
lmin = (3 * EI * DELTA ** 2 / KBT) ** (1 / 3)
for Fb, ls, f, ha in ((1.0, "--", 1.06, "left"), (5.0, "-.", 0.94, "right")):
    lb = np.pi / 2 * np.sqrt(EI / Fb)
    ax.axvline(lb, color=charts.line("negative"), lw=1.0, ls=ls)
    ax.text(lb * f, 0.15, f"buckles\nat {Fb:g} pN", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha=ha)
ax.axvspan(lmin, np.pi / 2 * np.sqrt(EI / 1.0), color=P.light("positive"), lw=0)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(0.1, 300)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "free length of the filament l / nm", "lateral fluctuation / nm")
charts.title(ax, "C  A window of free lengths")
