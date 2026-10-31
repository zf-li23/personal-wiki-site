"""Strain stiffening of a cross-linked semiflexible network (affine thermal model, Formula 26.6.1).

Each segment between cross-links (contour length lc, persistence length lp) stores the length
dl(f) = (lc^2/pi^2 lp) sum_n 1/(n^2 + phi), phi = f lc^2/(kappa pi^2), in its transverse undulations.
The network is deformed affinely by simple shear gamma: a segment along n, of end-to-end distance
lc - dl(0), is stretched or compressed to |(I + gamma e_x e_z^T) n| (lc - dl(0)), and its tension f
follows by inverting dl(f) (compressed segments carry at most the Euler load). The shear stress
sigma = (rho/lc) <f t_x r_z> is averaged over 3000 isotropic orientations; actin, lp = 17 um, at
1 mg/mL (rho = 39 um of filament per um^3), for three cross-link spacings. A: stress against strain.
B: differential modulus K = d sigma/d gamma against stress: a plateau G0, then K ~ sigma^(3/2) (dotted
slope), as the undulations of the segments are pulled out."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
KBT = 4.1e-3  # pN um
LP = 17.0
KAP = LP * KBT
RHO = 39.0
M = 3000
i = np.arange(M) + 0.5
th = np.arccos(1 - 2 * i / M)
ph = np.pi * (1 + 5 ** 0.5) * i
N = np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], axis=1)


def S(phi):
    out = np.empty_like(phi)
    pos = phi > 1e-8
    neg = phi < -1e-8
    z = np.sqrt(phi[pos]) * np.pi
    out[pos] = (z / np.tanh(z) - 1) / (2 * phi[pos])
    z = np.sqrt(-phi[neg]) * np.pi
    out[neg] = (z / np.tan(z) - 1) / (2 * phi[neg])
    out[~(pos | neg)] = np.pi ** 2 / 6
    return out


def network(lc, gammas):
    phis = np.concatenate([np.linspace(-0.995, 0, 400)[:-1], np.logspace(-6, 8, 3000)])
    dl = lc ** 2 / (np.pi ** 2 * LP) * S(phis)  # decreasing in phi
    f_of = phis * KAP * np.pi ** 2 / lc ** 2
    r0 = lc - dl[np.argmin(np.abs(phis))]
    sig = []
    for g in gammas:
        if sig and np.isnan(sig[-1]):
            sig.append(np.nan)
            continue
        v = N.copy()
        v[:, 0] += g * N[:, 2]
        lam = np.linalg.norm(v, axis=1)
        need = lc - lam * r0
        if need.min() <= dl[-1] * 1.5:
            sig.append(np.nan)
            continue
        need = np.minimum(need, dl[0])
        f = np.interp(need, dl[::-1], f_of[::-1])
        sig.append(RHO / lc * np.mean(f * v[:, 0] * v[:, 2] / lam * r0))
    return np.array(sig)


fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.86)
gam = np.linspace(0, 0.045, 3000)
for lc, tok in ((0.5, "channel"), (1.0, "actin"), (2.0, "lipid_head")):
    s = network(lc, gam)
    axs[0].plot(gam, s, color=charts.line(tok), lw=1.4, label=rf"$\ell_{{\mathrm{{c}}}} = {lc:g}$ µm")
    K = np.gradient(s, gam)
    ok = (s > 1e-2) & (K > 0) & np.isfinite(K)
    axs[1].plot(s[ok], K[ok], color=charts.line(tok), lw=1.4, label=rf"$\ell_{{\mathrm{{c}}}} = {lc:g}$ µm")
ax = axs[0]
ax.set_yscale("log")
ax.set_ylim(1e-1, 1e4)
ax.set_xlim(0, 0.045)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"shear strain $\gamma$", "shear stress / Pa")
charts.title(ax, "A  Stress rises steeply with strain")
ax = axs[1]
ss = np.logspace(0, 3.5, 10)
ax.plot(ss, 30 * ss ** 1.5, ":", color=P.muted(), lw=1.0)
ax.text(40, 30 * 40 ** 1.5 * 0.25, r"$K \propto \sigma^{3/2}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-2, 1e4)
ax.set_ylim(10, 1e7)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "shear stress / Pa", "differential modulus K / Pa")
charts.title(ax, "B  Linear plateau, then stiffening")
