# Three classes of phytochrome responses, from a minimal photoconversion model.
# A red (660 nm) pulse of fluence F converts Pr to Pfr: p(F) = phi_R (1 - exp(-s F)), phi_R = 0.87,
# s = sigma_r / phi_R with sigma_r = 4.1e-3 m2/umol (eps about 1.2e5 L/(mol cm), quantum yield 0.15).
# VLFR: hyperbolic response to p with half-saturation at p = 2e-5 (0.002 % Pfr).
# LFR: Hill response to p (n = 2, half-saturation at p = 0.12).
# A far-red pulse after the red pulse resets p to 0.025: this reverses the LFR, but not the VLFR.
# HIR: under continuous light of fluence rate I the response grows with time (tau = 3 h) towards
# a plateau that depends on I, so curves for different I do not superimpose when plotted against
# fluence (no reciprocity). Response parameters are illustrative.
import matplotlib.pyplot as plt
import numpy as np

PHI_R, SIG_R = 0.87, 4.1e-3
S = SIG_R / PHI_R
F = np.logspace(-5, 4, 400)  # umol m-2
p = PHI_R * (1 - np.exp(-S * F))
p_fr = 0.025


def vlfr(x):
    return x / (x + 2e-5)


def lfr(x):
    return x**2 / (x**2 + 0.12**2)


fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.0))
a.loglog(F, p * 100, color="black", lw=2.2)
a.axhline(0.02, color="#7a5cc8", lw=1.0, ls="--")
a.text(1.5e-5, 0.045, "0.02 % (VLFR saturated)", fontsize=8.5, color="#7a5cc8")
a.axhline(PHI_R * 100, color="#d9463b", lw=1.0, ls="--")
a.text(1.5e-5, 140, "87 % (photostationary state)", fontsize=8.5, color="#d9463b")
a.axhline(p_fr * 100, color="#8b1e3f", lw=1.0, ls=":")
a.text(1.5e-5, 4.5, "2.5 % (after far-red)", fontsize=8.5, color="#8b1e3f")
a.set_xlabel(r"Red fluence / $\mu$mol m$^{-2}$")
a.set_ylabel("Pfr / % of total phytochrome")
a.set_ylim(1e-7, 600)
a.set_title("A   Pfr formed by a red pulse", loc="left", fontsize=10)

b.semilogx(F, vlfr(p), color="#7a5cc8", lw=2.2, label="VLFR")
b.semilogx(F, lfr(p), color="#d9463b", lw=2.2, label="LFR")
b.axvspan(1e-4, 5e-2, color="#7a5cc8", alpha=0.10, lw=0)
b.axvspan(1, 1e3, color="#d9463b", alpha=0.10, lw=0)
for y, col, lab in ((vlfr(p_fr), "#7a5cc8", "VLFR after R + FR"), (lfr(p_fr), "#d9463b", "LFR after R + FR")):
    b.plot([5e3], [y], marker="o", mfc="none", mec=col, mew=1.8, ms=8, ls="none")
    b.annotate(lab, xy=(5e3, y), xytext=(150, 0.22 if y < 0.5 else 0.74), fontsize=8.5, color=col,
               arrowprops=dict(arrowstyle="->", lw=0.8, color=col))
b.set_xlabel(r"Red fluence / $\mu$mol m$^{-2}$")
b.set_ylabel("Relative response")
b.set_ylim(-0.03, 1.12)
b.legend(frameon=False, fontsize=9, loc="upper left")
b.set_title("B   Pulse responses: VLFR and LFR", loc="left", fontsize=10)

tau = 3 * 3600.0
c.set_xlim(1e1, 1e7)
F2 = np.logspace(1, 7, 300)
for I, col in ((100, "#1f5fa8"), (10, "#4c8fd6"), (1, "#9cc2ea")):
    t = F2 / I
    c.semilogx(F2, I / (I + 20) * (1 - np.exp(-t / tau)), color=col, lw=2.2,
               label=rf"$I$ = {I} $\mu$mol m$^{{-2}}$ s$^{{-1}}$")
c.set_xlabel(r"Fluence of continuous light / $\mu$mol m$^{-2}$")
c.set_ylabel("Relative response")
c.set_ylim(-0.03, 1.12)
c.legend(frameon=False, fontsize=8.5, loc="upper left")
c.set_title("C   HIR: depends on fluence rate", loc="left", fontsize=10)
for ax in (a, b, c):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
