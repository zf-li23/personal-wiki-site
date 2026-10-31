"""Equilibrium polymers and seeded growth (Theorem 26.3.1, Formula 26.3.1).

A, B: equilibrium of monomers with polymers whose concentrations are c_n = sigma Cc x^n (n >= 2),
x = c1/Cc, solved for the total subunit concentration cT. sigma = 1 is the single-stranded polymer
(every bond equivalent); small sigma is the nucleation penalty of a multistranded filament.
A: number-averaged length of the polymers; dashed, the approximation sqrt((cT - Cc)/(sigma Cc)).
B: fraction of subunits in polymers: for small sigma a sharp critical concentration appears.
C: growth of 50 seeded actin filaments (plus-end rates 11.6 uM^-1 s^-1 and 1.4 s^-1, 2 uM actin,
1 nM seeds) simulated with the Gillespie algorithm (gray: five filaments; thick: mean) against the
rate equation with monomer depletion (dashed). The mean saturates at (c0 - Cc)/c_seeds while the
lengths keep spreading diffusively."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)


def solve(cT, sigma):
    """Return (mean length, polymer fraction) for total cT in units of Cc."""
    def total(x):
        return x + sigma * (x ** 2 * (2 - x) / (1 - x) ** 2)  # sum_{n>=2} n x^n
    x = brentq(lambda v: total(v) - cT, 1e-12, 1 - 1e-12)
    num = sigma * x ** 2 / (1 - x)
    mass = sigma * x ** 2 * (2 - x) / (1 - x) ** 2
    return mass / num, mass / cT


fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.86)
cts = np.logspace(-1, 3, 300)
for sigma, tok, nm in ((1.0, "neutral", r"$\sigma = 1$ (single strand)"), (1e-3, "lipid_head", r"$\sigma = 10^{-3}$"),
                       (1e-5, "actin", r"$\sigma = 10^{-5}$")):
    res = np.array([solve(c, sigma) for c in cts])
    axs[0].plot(cts, res[:, 0], color=charts.line(tok), lw=1.4, label=nm)
    ok = cts > 1.5
    axs[0].plot(cts[ok], np.sqrt((cts[ok] - 1) / sigma), color=charts.line(tok), lw=0.8, ls="--")
    axs[1].plot(cts, res[:, 1], color=charts.line(tok), lw=1.4, label=nm)
ax = axs[0]
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1.5, 1e6)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"total subunits $c_{\mathrm{T}}/C_{\mathrm{c}}$", "mean polymer length / subunits")
charts.title(ax, "A  Mean length")
ax = axs[1]
ax.set_xscale("log")
ax.axvline(1, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(ax, r"total subunits $c_{\mathrm{T}}/C_{\mathrm{c}}$", "fraction in polymers")
charts.title(ax, "B  A critical concentration")

# C: seeded growth, Gillespie
KON, KOFF, C0, CS, M = 11.6, 1.4, 2.0, 1e-3, 50  # uM^-1 s^-1, s^-1, uM, uM, filaments
VOL = M / CS  # volume in units where 1 uM = 1 molecule
free = int(round(C0 * VOL))
L = np.zeros(M, dtype=int)
T_END = 600.0
t, rec_t, rec = 0.0, [0.0], [L.copy()]
next_rec = 5.0
while t < T_END:
    c = free / VOL
    a_on = KON * c * M
    a_off = KOFF * np.count_nonzero(L)
    a = a_on + a_off
    t += rng.exponential(1 / a)
    while t > next_rec and next_rec <= T_END:
        rec_t.append(next_rec)
        rec.append(L.copy())
        next_rec += 5.0
    if rng.random() * a < a_on:
        L[rng.integers(M)] += 1
        free -= 1
    else:
        idx = np.flatnonzero(L)
        L[idx[rng.integers(idx.size)]] -= 1
        free += 1
rec_t, rec = np.array(rec_t), np.array(rec)
ax = axs[2]
for i in range(5):
    ax.plot(rec_t, rec[:, i] * 2.7e-3, color=P.muted(), lw=0.7)
ax.plot(rec_t, rec.mean(axis=1) * 2.7e-3, color=charts.line("actin"), lw=1.8, label="mean of 50 (simulation)")
tt = np.linspace(0, T_END, 300)
cc = KOFF / KON
ninf = (C0 - cc) / CS
ax.plot(tt, ninf * (1 - np.exp(-KON * CS * tt)) * 2.7e-3, color=P.ink(), lw=1.0, ls="--", label="rate equation")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "time / s", "filament length / µm")
charts.title(ax, "C  Seeded growth")
