"""Monte Carlo conformations of a discrete worm-like chain in three dimensions.

Segments of length ds = 0.1 lp; the angle between successive tangents is drawn from the Boltzmann
weight exp(kappa cos theta) with kappa fixed by <cos theta> = exp(-ds/lp), so that <t(0).t(s)> = exp(-s/lp).
A: one conformation each of contour length L = 2, 20 and 200 lp (projected on the x-y plane, each
drawn at its own scale, with a bar of length lp). For DNA (lp = 50 nm) these are 300 bp, 3 kb and
30 kb. B: distribution of the end-to-end distance R for L = 1, 5 and 50 lp from 4000 chains each,
compared with the Gaussian distribution 4 pi R^2 (3/(2 pi <R^2>))^(3/2) exp(-3 R^2 / 2 <R^2>) that
has the worm-like-chain value of <R^2>: the Gaussian fails for short, stiff chains and becomes
accurate once L >> lp."""

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


fig, axs = plt.subplots(1, 4, figsize=(11.0, 3.2), gridspec_kw={"width_ratios": [1, 1, 1, 1.6]})
fig.subplots_adjust(wspace=0.35, left=0.03, right=0.98, bottom=0.17, top=0.86)
for ax, L, tok in zip(axs[:3], (2, 20, 200), ("protein", "dna", "enzyme")):
    pos = chains(1, int(round(L / DS)), keep=True)[0]
    ax.plot(pos[:, 0], pos[:, 1], color=charts.line(tok), lw=0.9)
    ax.plot(*pos[0, :2], "o", color=P.ink(), ms=3)
    ax.plot(*pos[-1, :2], "s", color=P.ink(), ms=3)
    ax.set_aspect("equal")
    ax.axis("off")
    xmin, xmax = pos[:, 0].min(), pos[:, 0].max()
    ymin = pos[:, 1].min()
    span = max(xmax - xmin, pos[:, 1].max() - ymin)
    y0 = ymin - 0.08 * span
    ax.plot([xmin, xmin + 1.0], [y0, y0], color=P.ink(), lw=1.6)
    ax.text(xmin + 0.5, y0 - 0.05 * span, r"$\ell_{\mathrm{p}}$", ha="center", va="top",
            fontsize=bio.core.FONT["tiny"], color=P.ink())
    ax.set_title(f"L = {L} " + r"$\ell_{\mathrm{p}}$", fontsize=bio.core.FONT["small"], color=P.ink())
axs[0].text(0.0, 1.13, "A  Conformations", transform=axs[0].transAxes, fontsize=bio.core.FONT["small"],
            color=P.ink(), weight="bold")

ax = axs[3]
for L, tok in ((1, "protein"), (5, "rna"), (50, "dna")):
    R = np.linalg.norm(chains(4000, int(round(L / DS))), axis=1)
    m2 = r2_wlc(L)
    x = R / np.sqrt(m2)
    ax.hist(x, bins=40, range=(0, 2.6), density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.4,
            alpha=0.7, label=f"L = {L} " + r"$\ell_{\mathrm{p}}$")
xs = np.linspace(0, 2.6, 300)
gauss = 4 * np.pi * xs ** 2 * (3 / (2 * np.pi)) ** 1.5 * np.exp(-1.5 * xs ** 2)
ax.plot(xs, gauss, color=P.ink(), lw=1.2, label="Gaussian chain")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"$R/\langle R^2\rangle^{1/2}$", "probability density")
charts.title(ax, "B  End-to-end distance")
