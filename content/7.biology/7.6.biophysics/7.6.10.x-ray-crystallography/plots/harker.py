# Isomorphous replacement: the Harker construction and the phase probability.
# One reflection of a protein, F_P = 100 exp(i 60 deg) (unknown phase), and two heavy-atom derivatives
# whose heavy-atom contributions F_H1 = 30 exp(i 200 deg) and F_H2 = 25 exp(i 320 deg) are known from
# the heavy-atom substructure; measured amplitudes |F_PH| = |F_P + F_H|.
# A: Harker construction. The protein circle (radius |F_P|, centre 0) and each derivative circle
#    (radius |F_PH|, centre -F_H) intersect where F_P + F_H has the measured length. A single derivative
#    gives two intersections (two phases, SIR ambiguity); the second derivative selects the true one.
# B: Blow-Crick phase probabilities P(phi) ~ exp(-eps(phi)^2 / (2 E^2)) with the lack of closure
#    eps(phi) = |F_PH| - |F_P exp(i phi) + F_H| and E = 6 (a combined error of measurement and of the
#    heavy-atom model); SIR from derivative 1 alone is bimodal, MIR is the product. The figure of merit
#    m = |<exp(i phi)>| and the "best" phase (the centroid) are given for each.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

FP = 100 * np.exp(1j * np.deg2rad(60))
FH = [30 * np.exp(1j * np.deg2rad(200)), 25 * np.exp(1j * np.deg2rad(320))]
FPH = [abs(FP + h) for h in FH]
toks = ["dna", "highlight"]

fig, axs = plt.subplots(1, 2, figsize=(11.5, 5.0), gridspec_kw={"width_ratios": [1, 1.15]})
ax = axs[0]
ax.add_patch(Circle((0, 0), abs(FP), fill=False, edgecolor=charts.line("protein"), lw=1.8))
for h, r, tok, k in zip(FH, FPH, toks, (1, 2)):
    c = -h
    ax.add_patch(Circle((c.real, c.imag), r, fill=False, edgecolor=charts.line(tok), lw=1.4,
                        ls="-" if k == 1 else (0, (5, 2))))
    ax.add_patch(FancyArrowPatch((c.real, c.imag), (0, 0), arrowstyle="-|>", mutation_scale=10,
                                 color=charts.line(tok), lw=1.3))
    ax.text(c.real * 1.12 - 6, c.imag * 1.12 - 4, rf"$-\boldsymbol{{F}}_{{\mathrm{{H}}{k}}}$", fontsize=10,
            color=charts.line(tok))
    # intersections of |z| = |FP| and |z - c| = r
    phis = np.linspace(0, 2 * np.pi, 3600, endpoint=False)
    z = abs(FP) * np.exp(1j * phis)
    d = np.abs(np.abs(z - c) - r)
    idx = [i for i in range(len(d)) if d[i] < d[i - 1] and d[i] <= d[(i + 1) % len(d)] and d[i] < 0.5]
    for i in idx:
        ax.plot(z[i].real, z[i].imag, "o", ms=8 if k == 1 else 6, mfc="none", mec=charts.line(tok), mew=1.6)
ax.add_patch(FancyArrowPatch((0, 0), (FP.real, FP.imag), arrowstyle="-|>", mutation_scale=12, color=ink,
                             lw=1.8))
ax.text(FP.real + 4, FP.imag + 3, r"$\boldsymbol{F}_{\mathrm{P}}$ (true)", fontsize=10, color=ink)
ax.text(-128, 108, "protein circle", fontsize=8, color=charts.line("protein"))
ax.text(-128, 96, "derivative 1", fontsize=8, color=charts.line("dna"))
ax.text(-128, 84, "derivative 2", fontsize=8, color=charts.line("highlight"))
ax.axhline(0, color=muted, lw=0.5)
ax.axvline(0, color=muted, lw=0.5)
ax.set_xlim(-135, 135)
ax.set_ylim(-135, 135)
ax.set_aspect("equal")
ax.set_title("A  Harker construction", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "Re F", "Im F", box=True)

ax = axs[1]
phi = np.linspace(-np.pi, np.pi, 1441)
E = 6.0


def prob(k):
    eps = FPH[k] - np.abs(abs(FP) * np.exp(1j * phi) + FH[k])
    return np.exp(-(eps**2) / (2 * E**2))


p1 = prob(0)
p12 = p1 * prob(1)
for p, tok, name in ((p1, "dna", "SIR (derivative 1)"), (p12, "highlight", "MIR (derivatives 1 + 2)")):
    p = p / np.trapezoid(p, phi)
    cent = np.trapezoid(p * np.exp(1j * phi), phi)
    m, best = abs(cent), np.rad2deg(np.angle(cent))
    ax.plot(np.rad2deg(phi), p, color=charts.line(tok), lw=1.8,
            label=rf"{name}: $m$ = {m:.2f}, $\varphi_{{\mathrm{{best}}}}$ = {best:.0f}°")
ax.axvline(60, color=ink, lw=1.0, ls=(0, (3, 2)))
ax.text(70, 1.3, "true phase 60°", fontsize=8, color=ink)
ax.legend(fontsize=8, frameon=False, loc="upper left")
ax.set_xlim(-180, 180)
ax.set_xticks(range(-180, 181, 60))
ax.set_title("B  phase probability", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, r"protein phase $\varphi$ / deg", r"$P(\varphi)$ / rad$^{-1}$")
fig.tight_layout()
