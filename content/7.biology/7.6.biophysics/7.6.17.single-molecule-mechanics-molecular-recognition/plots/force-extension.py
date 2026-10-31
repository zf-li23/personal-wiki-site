# Force-extension curves of single DNA molecules (lambda DNA, 48.5 kbp, contour length 16.5 um, 25 C).
# A: models. Freely jointed chain (Kuhn length b = 2A = 100 nm): x/L = coth(Fb/kT) - kT/(Fb).
#    Worm-like chain, Marko-Siggia interpolation: F A / kT = x/L + 1/(4 (1 - x/L)^2) - 1/4 (A = 50 nm).
#    Extensible WLC (Wang et al. 1997): the same with x/L replaced by x/L - F/S, stretch modulus S = 1200 pN.
#    Overstretching: a plateau near 65 pN to about 1.7 L. Single-stranded DNA: extensible FJC with b = 1.5 nm,
#    contour 0.56 nm per nucleotide, S = 800 pN.
# B: synthetic optical-tweezers data (extensible WLC, A = 50 nm, S = 1200 pN, 0.3 % noise in extension, 2-50 pN)
#    and a least-squares fit for A, S and L.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq, least_squares

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kT, L = 4.11, 16.5  # pN nm, um


def fjc(F, b, S=np.inf):
    u = F * b / kT
    return 1 / np.tanh(u) - 1 / u + F / S


def ewlc(F, A, S=np.inf):
    """Relative extension x/L of the (extensible) Marko-Siggia WLC at force F."""
    def g(r):
        y = r - F / S
        return kT / A * (y + 1 / (4 * (1 - y) ** 2) - 0.25) - F
    return brentq(g, 0, 1 - 1e-12 + F / S)


fig, axs = plt.subplots(1, 2, figsize=(12.5, 4.3))
F = np.logspace(-2, np.log10(64), 300)
axs[0].plot(L * fjc(F, 100.0), F, color=charts.line("neutral"), lw=1.6, label="freely jointed chain, b = 100 nm")
axs[0].plot([L * ewlc(f, 50.0) for f in F], F, color=charts.line("dna"), lw=1.8, label="worm-like chain, A = 50 nm")
xe = np.array([L * ewlc(f, 50.0, 1200.0) for f in F])
axs[0].plot(xe, F, color=charts.line("enzyme"), lw=1.8, ls="--", label="extensible WLC, S = 1200 pN")
xo = np.linspace(xe[-1], 1.7 * L, 50)
axs[0].plot(np.r_[xo, 1.72 * L, 1.75 * L], np.r_[np.full(50, 65.0), 75, 95], color=charts.line("enzyme"), lw=1.8)
Fs = np.logspace(-1, np.log10(95), 200)
Lss = 48502 * 0.56e-3
axs[0].plot(Lss * fjc(Fs, 1.5, 800.0), Fs, color=charts.line("rna"), lw=1.6, label="ssDNA, extensible FJC")
axs[0].text(18, 69, "overstretching\n≈ 65 pN", fontsize=8, color=P.ink())
axs[0].set_xlim(0, 30)
axs[0].set_ylim(0, 100)
charts.style_axes(axs[0], "extension / µm", "force / pN")
axs[0].legend(fontsize=7.5, frameon=False, loc="upper left")
charts.title(axs[0], "A   Entropic and enthalpic elasticity of DNA")

Fd = np.linspace(2, 50, 40)
xd = np.array([L * ewlc(f, 50.0, 1200.0) for f in Fd]) * (1 + rng.normal(0, 0.003, Fd.size))


def resid(p):
    A, S, Lf = p
    return np.array([Lf * ewlc(f, A, S) for f in Fd]) - xd


fit = least_squares(resid, (30.0, 800.0, 15.0), bounds=([5, 100, 10], [200, 1e4, 25]))
A_f, S_f, L_f = fit.x
axs[1].plot(xd, Fd, "o", ms=3.5, color=charts.line("dna"), label="data (simulated)")
ff = np.linspace(0.5, 55, 200)
axs[1].plot([L_f * ewlc(f, A_f, S_f) for f in ff], ff, color=charts.line("enzyme"), lw=1.6,
            label=f"fit: A = {A_f:.0f} nm, S = {S_f:.0f} pN, L = {L_f:.2f} µm")
axs[1].plot([L * ewlc(f, 50.0) for f in ff], ff, color=P.muted(), lw=1.0, ls=":", label="inextensible WLC, A = 50 nm")
charts.style_axes(axs[1], "extension / µm", "force / pN")
axs[1].set_xlim(13.5, 17.8)
axs[1].legend(fontsize=7.5, frameon=False, loc="upper left")
charts.title(axs[1], "B   Fitting the extensible WLC")
fig.tight_layout()
