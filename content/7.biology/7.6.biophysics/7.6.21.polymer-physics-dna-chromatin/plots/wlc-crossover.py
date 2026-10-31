"""Tangent correlations and the rod-to-coil crossover of the worm-like chain.

Discrete worm-like chains as in the conformation figure (segment ds = 0.1 lp, Boltzmann-distributed
bending angles). A: tangent correlation <t(0).t(s)> along chains of length 4 lp (20000 chains, dots)
against exp(-s/lp) (line); the semilogarithmic plot is straight with slope -1/lp. B: mean squared
end-to-end distance relative to L^2 (rod limit 1) and to 2 lp L (coil limit 1) against L/lp, from
Monte Carlo (dots, 1500 chains per length) and from Formula 21.3.2 (lines). Top axis: the same
lengths for DNA in base pairs (lp = 50 nm = 147 bp); the nucleosome (147 bp), the lac loop between
O1 and O2 (401 bp) and the lambda genome (48.5 kb) are marked."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
DS = 0.1  # segment length in units of lp
# stiffness per joint chosen so that <cos theta> = coth(K) - 1/K equals exp(-ds/lp) exactly
KAPPA = 1.0 / DS
for _ in range(50):
    KAPPA = 1.0 / (1.0 / np.tanh(KAPPA) - np.exp(-DS))


def sample_cos(n):
    u = rng.random(n)
    return 1.0 + np.log(u + (1.0 - u) * np.exp(-2.0 * KAPPA)) / KAPPA


def chains(M, nseg, keep=False):
    """Positions (M, nseg+1, 3) if keep, else end vectors (M, 3)."""
    t = rng.normal(size=(M, 3))
    t /= np.linalg.norm(t, axis=1)[:, None]
    r = np.zeros((M, 3))
    path = [r.copy()] if keep else None
    for _ in range(nseg):
        r = r + DS * t
        if keep:
            path.append(r.copy())
        c = sample_cos(M)
        s = np.sqrt(np.clip(1.0 - c * c, 0.0, None))
        phi = rng.random(M) * 2.0 * np.pi
        a = np.where(np.abs(t[:, [0]]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
        e1 = np.cross(t, a)
        e1 /= np.linalg.norm(e1, axis=1)[:, None]
        e2 = np.cross(t, e1)
        t = c[:, None] * t + s[:, None] * (np.cos(phi)[:, None] * e1 + np.sin(phi)[:, None] * e2)
    return np.stack(path, axis=1) if keep else r


def r2_wlc(L):
    return 2.0 * L - 2.0 * (1.0 - np.exp(-L))




def tangents(M, nseg):
    t = np.zeros((M, 3))
    t[:, 2] = 1.0
    out = [t[:, 2].copy()]
    for _ in range(nseg):
        c = sample_cos(M)
        s = np.sqrt(np.clip(1.0 - c * c, 0.0, None))
        phi = rng.random(M) * 2.0 * np.pi
        a = np.where(np.abs(t[:, [0]]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
        e1 = np.cross(t, a)
        e1 /= np.linalg.norm(e1, axis=1)[:, None]
        e2 = np.cross(t, e1)
        t = c[:, None] * t + s[:, None] * (np.cos(phi)[:, None] * e1 + np.sin(phi)[:, None] * e2)
        out.append(t[:, 2].copy())
    return np.array(out)


fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.97, bottom=0.16, top=0.80)

ax = axs[0]
tz = tangents(20000, 40)
s = np.arange(41) * DS
corr = tz.mean(axis=1)
ax.plot(s[::2], corr[::2], "o", color=charts.line("dna"), ms=3.5, label="Monte Carlo")
ss = np.linspace(0, 4, 200)
ax.plot(ss, np.exp(-ss), color=P.ink(), lw=1.1, label=r"$\mathrm{e}^{-s/\ell_{\mathrm{p}}}$")
ax.set_yscale("log")
ax.set_ylim(1e-2, 1.3)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, r"contour separation $s/\ell_{\mathrm{p}}$", r"$\langle \boldsymbol{t}(0)\cdot\boldsymbol{t}(s)\rangle$")
charts.title(ax, "A  Tangent correlation")

ax = axs[1]
Ls = np.logspace(-1.5, 2.5, 300)
ax.plot(Ls, r2_wlc(Ls) / Ls ** 2, color=charts.line("protein"), lw=1.3, label=r"$\langle R^2\rangle/L^2$")
ax.plot(Ls, r2_wlc(Ls) / (2 * Ls), color=charts.line("dna"), lw=1.3, label=r"$\langle R^2\rangle/2\ell_{\mathrm{p}}L$")
for L in (0.3, 1, 3, 10, 30):
    R2 = (chains(1500, max(3, int(round(L / DS)))) ** 2).sum(axis=1).mean()
    ax.plot(L, R2 / L ** 2, "o", color=charts.line("protein"), ms=3.5)
    ax.plot(L, R2 / (2 * L), "o", color=charts.line("dna"), ms=3.5)
ax.set_xscale("log")
ax.set_ylim(0, 1.08)
ax.axvline(1, color=P.muted(), lw=0.6, ls=":")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, r"$L/\ell_{\mathrm{p}}$", "ratio")
charts.title(ax, "B  From rod to coil")
top = ax.secondary_xaxis("top", functions=(lambda x: x * 147.0, lambda b: b / 147.0))
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
top.set_xlabel("DNA length / bp", fontsize=bio.core.FONT["tiny"], color=P.ink())
for bp, name, h in ((147, "nucleosome", 0.2), (401, "lac O1-O2", 0.3), (48500, "lambda genome", 0.2)):
    ax.annotate(name, (bp / 147.0, 0.03), xytext=(bp / 147.0, h), fontsize=bio.core.FONT["tiny"],
                color=P.ink(), ha="center", arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
