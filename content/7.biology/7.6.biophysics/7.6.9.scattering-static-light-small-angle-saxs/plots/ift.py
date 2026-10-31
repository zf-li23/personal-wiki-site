# Indirect Fourier transformation (IFT) of noisy SAXS data with Tikhonov regularization.
# Test particle: a two-domain protein modelled as two touching spheres of radii 22 and 16 A (centres 38 A
# apart, Dmax = 76 A); its true p(r) is the distance histogram of 6000 random points (grey).
# Data: I(q) = 4 pi int p(r) sinc(qr) dr on 0.012 <= q <= 0.30 A^-1 (250 points), with noise of 0.5 % of
# I at low q rising to about 10 % at q_max (sigma = 0.005 I + 2e-4 I(0)).
# IFT: p(r) on 60 points in (0, Dmax) with p(0) = p(Dmax) = 0; I = T p with T_ik = 4 pi dr sinc(q_i r_k);
# minimize chi^2 = sum ((I_i - (T p)_i) / sigma_i)^2 + lambda |L p|^2 (L: second differences),
# solved as a stacked linear least-squares problem, for three values of lambda (A, B) and a scan (C).
# A: data with the fits; B: the recovered p(r) compared with the truth, and the naive transform of the
#    truncated data, p(r) = (r / 2 pi^2) int_{q_min}^{q_max} q I(q) sin(qr) dq (dotted), which has a
#    negative tail; C: the misfit chi^2/N stays near 1 over many decades of lambda while the error of p(r)
#    (known only in a simulation) falls; the best lambda is the largest one that does not yet raise chi^2.
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(4)


def ball(n, R, z0):
    v = rng.normal(size=(n, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    v *= R * rng.random(n)[:, None] ** (1 / 3)
    v[:, 2] += z0
    return v


R1, R2 = 22.0, 16.0
n1 = int(6000 * R1**3 / (R1**3 + R2**3))
pts = np.vstack([ball(n1, R1, 0.0), ball(6000 - n1, R2, R1 + R2)])
dmax = 2 * (R1 + R2)
edges = np.linspace(0, dmax + 4, 161)
rt = 0.5 * (edges[1:] + edges[:-1])
pt = np.histogram(pdist(pts), bins=edges)[0].astype(float)
pt /= pt.sum() * (edges[1] - edges[0])

q = np.linspace(0.012, 0.30, 250)
Itrue = 4 * np.pi * (pt * np.sinc(np.outer(q, rt) / np.pi)).sum(axis=1) * (edges[1] - edges[0])
sig = 0.005 * Itrue + 2e-4 * Itrue[0]
Iobs = Itrue + sig * rng.normal(size=q.size)

K = 60
r = np.linspace(0, dmax, K + 2)[1:-1]
dr = r[1] - r[0]
T = 4 * np.pi * dr * np.sinc(np.outer(q, r) / np.pi)
L = np.diff(np.eye(K + 2), 2, axis=0)[:, 1:-1]
W = 1 / sig


def ift(lam):
    A = np.vstack([T * W[:, None], np.sqrt(lam) * L])
    b = np.concatenate([Iobs * W, np.zeros(L.shape[0])])
    p = np.linalg.lstsq(A, b, rcond=None)[0]
    chi2 = (((T @ p - Iobs) * W) ** 2).mean()
    return p, chi2


lams = ((1e2, "λ = 10² (too small)", "negative"), (1e7, "λ = 10⁷", "dna"), (1e12, "λ = 10¹² (too large)", "positive"))
fits = [(ift(lam), lab, tok, lam) for lam, lab, tok in lams]

fig, axs = plt.subplots(1, 3, figsize=(14.5, 4.3), gridspec_kw={"width_ratios": [1.0, 1.0, 0.8]})
ax = axs[0]
ax.errorbar(q, Iobs / Itrue[0], yerr=sig / Itrue[0], fmt="o", ms=1.8, color=P.muted(), elinewidth=0.5,
            label="simulated data")
for (p, chi2), lab, tok, lam in fits:
    ax.plot(q, T @ p / Itrue[0], color=charts.line(tok), lw=1.4, label=f"{lab}: χ²/N = {chi2:.2f}")
ax.set_yscale("log")
ax.set_xlim(0, 0.3)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q / Å⁻¹", "I(q) / I(0)")
charts.title(ax, "A   Data and fits")

ax = axs[1]
ax.plot(rt, pt * 100, color=P.muted(), lw=3.5, alpha=0.6, label="true p(r)")
for (p, chi2), lab, tok, lam in fits:
    norm = p.sum() * dr
    ax.plot(np.r_[0, r, dmax], np.r_[0, p, 0] / norm * 100, color=charts.line(tok), lw=1.5, label=lab)
pn = r / (2 * np.pi**2) * (q * Iobs * np.sin(np.outer(r, q))).sum(axis=1) * (q[1] - q[0])
ax.plot(r, pn / (pn.sum() * dr) * 100, color=P.ink(), lw=0.9, ls=":", label="direct transform, truncated")
ax.axvline(dmax, color=P.muted(), lw=0.6, ls=(0, (3, 2)))
ax.text(dmax - 1, 3.1, "Dmax", color=P.muted(), fontsize=7.5, ha="right")
ax.set_xlim(0, dmax + 6)
ax.set_ylim(-0.8, 3.4)
ax.legend(fontsize=7, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.92))
charts.style_axes(ax, "r / Å", "p(r)  (% per Å)")
charts.title(ax, "B   Recovered distance distribution")

ax = axs[2]
lam_scan = 10.0 ** np.arange(0, 13.5, 0.5)
ptrue = np.interp(r, rt, pt)
chis, errs = [], []
for lam in lam_scan:
    p, chi2 = ift(lam)
    chis.append(chi2)
    errs.append(np.sqrt(((p / (p.sum() * dr) - ptrue) ** 2).mean()) / ptrue.max())
ax.loglog(lam_scan, chis, color=charts.line("dna"), lw=1.6, label="χ²/N (data misfit)")
ax.loglog(lam_scan, errs, color=charts.line("negative"), lw=1.6, ls="--", label="error of p(r) vs truth")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=7, frameon=False, loc="upper center")
charts.style_axes(ax, "regularization weight λ", "")
charts.title(ax, "C   Choosing λ")
fig.tight_layout()
