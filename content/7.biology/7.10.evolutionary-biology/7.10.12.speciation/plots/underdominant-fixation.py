"""Fixation of an underdominant chromosomal rearrangement by drift. A new rearrangement arises as a single
copy (frequency 1/2N) in a deme of N diploids; heterozygotes have fertility 1 - s and both homozygotes 1.
Line: diffusion approximation u = int_0^{1/2N} G / int_0^1 G with G(y) = exp(4 N s y (1 - y)), relative to
the neutral probability 1/2N; dots: Wright-Fisher simulations with N = 25 (200 000 replicates each,
seed 0, 95 % Wilson intervals). Dashed: exp(-N s). Fixation is plausible only when N s is below about 10."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
N = 25


def u_diff(Ns, N):
    s = Ns / N
    G = lambda y: np.exp(4 * N * s * y * (1 - y))
    num = integrate.quad(G, 0, 1 / (2 * N))[0]
    den = integrate.quad(G, 0, 1, limit=200)[0]
    return num / den


Nsg = np.linspace(0, 14, 80)
rel = [u_diff(v, N) * 2 * N for v in Nsg]
fig, ax = plt.subplots(figsize=(6.5, 4.0))
fig.subplots_adjust(left=0.14, right=0.97, bottom=0.14, top=0.92)
ax.semilogy(Nsg, rel, color=charts.line("dna"), lw=2, label="diffusion approximation")
ax.semilogy(Nsg, np.exp(-Nsg), color=P.muted(), lw=1.2, ls="--", label="$\\mathrm{e}^{-Ns}$")
rng = np.random.default_rng(0)
reps = 200000
for Ns in (0, 1, 2, 3, 4):
    s = Ns / N
    k = np.ones(reps, dtype=int)
    fixed = 0
    while len(k):
        p = k / (2 * N)
        q = 1 - p
        pp = (p * p + p * q * (1 - s)) / (1 - 2 * p * q * s)
        k = rng.binomial(2 * N, pp)
        fixed += int((k == 2 * N).sum())
        k = k[(k > 0) & (k < 2 * N)]
    lo, hi = evo.wilson(fixed, reps)
    est = fixed / reps * 2 * N
    ax.errorbar([Ns], [est], yerr=[[est - lo * 2 * N], [hi * 2 * N - est]], fmt="o", ms=4,
                color=charts.line("rna"), lw=1, label="simulation, $N = 25$" if Ns == 0 else None)
ax.set_ylim(1e-6, 2)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "$Ns$ (selection against heterozygotes $\\times$ deme size)", "fixation probability / neutral")
