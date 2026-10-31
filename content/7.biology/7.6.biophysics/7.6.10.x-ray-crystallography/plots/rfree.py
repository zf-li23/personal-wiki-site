# Overfitting and the free R value in a toy refinement.
# "Observed" data: structure factors of 18 Gaussian atoms (B = 15 A^2) at random positions in a
# two-dimensional 20 x 20 A cell, for all reflections to d = 2.0 A (about 160 unique), with complex
# Gaussian noise of 8 % of the rms amplitude. A random 10 % of the reflections are set aside as the test
# set. The model is a density of M atoms (B = 15 A^2) with free amplitudes (occupancies), fitted
# by linear least squares to the working reflections (phases taken as known, as after phasing): first
# 2, 4, ..., 18 blobs at the true atom positions (an incomplete, then complete model), then the complete
# model plus an increasing number of blobs at random positions (spurious "waters" or alternative
# conformations). R = sum ||F_obs| - |F_calc|| / sum |F_obs| for the working and test sets, averaged over
# 6 random test sets. Adding real structure lowers both R values; adding spurious parameters lowers
# R_work towards 0 as M approaches the number of working observations, while R_free rises: the extra
# parameters fit the noise. The gap R_free - R_work measures overfitting.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
rng = np.random.default_rng(0)

cell, dmin = 20.0, 2.0
hm = int(cell / dmin)
hk = np.array([(h, k) for h in range(0, hm + 1) for k in range(-hm, hm + 1)
               if (h > 0 or k > 0) and (h * h + k * k) <= (cell / dmin) ** 2])
s2 = (hk**2).sum(axis=1) / cell**2
atoms = rng.uniform(0, 1, size=(18, 2))
Ftrue = np.exp(-15 / 4 * s2) * np.exp(2j * np.pi * hk @ atoms.T).sum(axis=1)
noise = 0.08 * np.sqrt(np.mean(np.abs(Ftrue) ** 2))
Fobs = Ftrue + noise * (rng.normal(size=len(hk)) + 1j * rng.normal(size=len(hk))) / np.sqrt(2)


extra = rng.uniform(0, 1, size=(300, 2))


def design(n_true, n_extra):
    """Model: atoms with B = 15 A^2 at the first n_true true atom positions plus n_extra random
    positions; the blob amplitudes (occupancies) are the free parameters."""
    pos = np.vstack([atoms[:n_true], extra[:n_extra]])
    blob = np.exp(-15 / 4 * s2)            # same B as the true atoms
    return blob[:, None] * np.exp(2j * np.pi * hk @ pos.T)


def R(Fo, Fc):
    return np.sum(np.abs(np.abs(Fo) - np.abs(Fc))) / np.sum(np.abs(Fo))


models = [(k, 0) for k in range(2, 19, 2)] + [(18, e) for e in (4, 8, 16, 32, 64, 96, 128, 160, 200, 240, 270)]
Ms = np.array([k + e for k, e in models])
rw, rf = np.zeros(len(Ms)), np.zeros(len(Ms))
n_trials = 6
for t in range(n_trials):
    test = rng.random(len(hk)) < 0.10
    for i, (k, e) in enumerate(models):
        A = design(k, e)
        Aw = np.vstack([A[~test].real, A[~test].imag])
        bw = np.concatenate([Fobs[~test].real, Fobs[~test].imag])
        c, *_ = np.linalg.lstsq(Aw, bw, rcond=None)
        Fc = A @ c
        rw[i] += R(Fobs[~test], Fc[~test]) / n_trials
        rf[i] += R(Fobs[test], Fc[test]) / n_trials

nobs = 2 * 0.9 * len(hk)
fig, ax = plt.subplots(figsize=(6.8, 4.2))
ax.plot(Ms, 100 * rw, "o-", color=charts.line("dna"), ms=4, lw=1.6, label=r"$R_{\mathrm{work}}$")
ax.plot(Ms, 100 * rf, "o-", color=charts.line("negative"), ms=4, lw=1.6, label=r"$R_{\mathrm{free}}$")
ax.text(60, 14, "overfitting:\nR$_{\\mathrm{free}}$ rises,\nR$_{\\mathrm{work}}$ falls", fontsize=8, color=ink)
ax.text(5, 30, "incomplete\nmodel", fontsize=8, color=ink)
ax.axvline(nobs, color=muted, lw=0.9, ls=(0, (3, 2)))
ax.axvline(18, color=muted, lw=0.6, ls=(0, (1, 2)))
ax.text(19, 56, "all 18 true atoms", fontsize=8, color=muted)
ax.text(nobs * 0.55, 44, "parameters =\nworking\nobservations", fontsize=8, color=muted)
ax.set_xscale("log")
ax.set_ylim(0, 60)
ax.legend(fontsize=9, frameon=False, loc="upper left", bbox_to_anchor=(0.62, 1.0))
charts.style_axes(ax, "number of model parameters M", "R / %")
fig.tight_layout()
