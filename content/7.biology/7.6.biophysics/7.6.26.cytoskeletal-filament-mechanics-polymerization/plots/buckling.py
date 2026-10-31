"""Euler buckling of cytoskeletal filaments, free and embedded (Theorem 26.2.1, Formula 26.2.1).

Flexural rigidities: actin EI = 0.07 pN um^2 (lp = 17 um), microtubule 26 pN um^2 (lp = 6 mm).
A: critical compressive force against length for hinged ends, pi^2 EI/L^2 (solid), and for one end
clamped and the other free, pi^2 EI/4L^2 (dashed); horizontal marks: thermodynamic stall force of an
actin filament at c = 100 Cc (7 pN), measured stall force of a growing microtubule (about 4 pN) and the
threshold 2 sqrt(alpha EI) = 320 pN of a microtubule embedded in an elastic medium of modulus
alpha = 1 kPa. B: the buckled shape of a 20 um microtubule with hinged ends, free (one half wave) and
embedded (wavelength 2 pi (EI/alpha)^(1/4) = 2.5 um). C: energy of a bending mode of wave number q,
EI q^4 - F q^2 + alpha (per unit length and squared amplitude, halved), at loads below, at and above the
embedded threshold; the first mode to become negative sets the wavelength."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
EI = {"actin": 0.07, "mt": 26.0}  # pN um^2
ALPHA = 1000.0  # pN/um^2 (1 kPa)

fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.36, left=0.07, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
L = np.logspace(-1.3, 2, 200)
for key, tok, nm in (("actin", "actin", "actin"), ("mt", "channel", "microtubule")):
    ax.plot(L, np.pi ** 2 * EI[key] / L ** 2, color=charts.line(tok), lw=1.4, label=nm)
    ax.plot(L, np.pi ** 2 * EI[key] / (4 * L ** 2), color=charts.line(tok), lw=1.0, ls="--")
fc = 2 * np.sqrt(ALPHA * EI["mt"])
for F, txt in ((7.0, "actin stall force, 7 pN"), (4.0, "microtubule stall, ~4 pN"), (fc, "embedded microtubule, 320 pN")):
    ax.axhline(F, color=P.muted(), lw=0.6, ls=":")
    ax.text(95, F * 1.12, txt, ha="right", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(0.01, 3000)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "filament length L / µm", "critical force / pN")
charts.title(ax, "A  Euler force")

ax = axs[1]
Lm = 20.0
x = np.linspace(0, Lm, 800)
lam = 2 * np.pi * (EI["mt"] / ALPHA) ** 0.25
nwave = round(2 * Lm / lam)
ax.plot(x, 1.0 + 0.6 * np.sin(np.pi * x / Lm), color=charts.line("channel"), lw=1.4)
ax.plot(x, -0.6 + 0.25 * np.sin(nwave * np.pi * x / Lm), color=charts.line("channel"), lw=1.4)
ax.text(10, 1.85, "free: one half wave", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(10, -0.15, f"embedded: wavelength {lam:.1f} µm", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
for y0 in (1.0, -0.6):
    ax.annotate("", xy=(0.2, y0), xytext=(-2.2, y0), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.0))
    ax.annotate("", xy=(Lm - 0.2, y0), xytext=(Lm + 2.2, y0), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.0))
ax.set_xlim(-3, Lm + 3)
ax.set_ylim(-1.2, 2.2)
ax.set_yticks([])
charts.style_axes(ax, "position along a 20 µm microtubule / µm")
ax.spines["left"].set_visible(False)
charts.title(ax, "B  Buckled shapes")

ax = axs[2]
q = np.linspace(0.01, 5, 400)
for F, ls in ((0.6 * fc, ":"), (fc, "-"), (1.3 * fc, "--")):
    ax.plot(q, (EI["mt"] * q ** 4 - F * q ** 2 + ALPHA) / ALPHA, color=charts.line("channel"), lw=1.4, ls=ls,
            label=f"F = {F:.0f} pN")
ax.axhline(0, color=P.muted(), lw=0.6)
qs = (ALPHA / EI["mt"]) ** 0.25
ax.axvline(qs, color=P.muted(), lw=0.6, ls=":")
ax.text(qs + 0.12, 2.7, r"$q^* = (\alpha/EI)^{1/4}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_ylim(-1.2, 3)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"wave number q / µm$^{-1}$", r"mode energy / $\alpha$")
charts.title(ax, "C  Mode selection in a medium")
