"""Physical limits of concentration sensing. A: flux of ligand to a sphere of radius a = 1 um covered
by N absorbing disks of radius s = 1 nm, relative to a perfectly absorbing sphere: J/J_max =
Ns/(Ns + pi a) (Berg-Purcell), against the naive sum of independent disks Ns/(pi a). B: relative error
of a concentration estimate from one receptor (binding rate k+c = 2/s, unbinding 2/s) against the
averaging time T, from simulated binding histories: time averaging of the occupancy, maximum
likelihood from the unbound intervals, and an ideal absorber that counts every arrival; lines are
the formulas 2/(k+c(1-p)T), 1/(k+c(1-p)T) and 1/(k+cT) for the variance. C: signal-to-noise ratio of
a snapshot comparison of front and back of a cell with M receptors in a 1 % gradient against the
background concentration in units of the dissociation constant."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)

fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.42, left=0.06, right=0.98, bottom=0.17, top=0.88)

# A: receptor patches
a, s = 1.0, 1e-3
N = np.logspace(0, 6, 300)
ax = axs[0]
ax.semilogx(N, N * s / (N * s + np.pi * a), color=charts.line("receptor"), lw=1.6, label="Berg-Purcell")
ax.semilogx(N, np.minimum(N * s / (np.pi * a), 1.2), color=P.muted(), lw=1.0, ls="--", label="independent disks")
Nh = np.pi * a / s
ax.axvline(Nh, color=P.muted(), lw=0.6, ls=":")
ax.plot([Nh], [0.5], "o", color=charts.line("receptor"), ms=4)
cover = Nh * np.pi * s ** 2 / (4 * np.pi * a ** 2)
ax.annotate(rf"$N = \pi a/s$ = {Nh:.0f}"+"\n"+f"coverage {100 * cover:.2f} %", (Nh, 0.5), (12, 0.75), fontsize=7,
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.set_ylim(0, 1.15)
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, "number of receptors N", r"flux $J/J_{\max}$")
charts.title(ax, "A  receptor patches")

# B: single receptor, three estimators
kp, km = 2.0, 2.0          # k+ c and k- (per second)
p = kp / (kp + km)
Ts = np.logspace(0.9, 2.7, 8)
nrep = 400
err_avg, err_ml, err_abs = [], [], []
for T in Ts:
    nmax = int(3 * T * (kp + km) / 2 + 60)
    tu = rng.exponential(1 / kp, size=(nrep, nmax))
    tb = rng.exponential(1 / km, size=(nrep, nmax))
    start = rng.random(nrep) < p            # stationary initial state
    seq = np.empty((nrep, 2 * nmax))
    seq[:, 0::2] = np.where(start[:, None], tb, tu)
    seq[:, 1::2] = np.where(start[:, None], tu, tb)
    ends = np.cumsum(seq, axis=1)
    durs = np.minimum(ends, T) - np.minimum(ends - seq, T)
    bound_first = start[:, None]
    idx = np.arange(2 * nmax)[None, :]
    is_bound = np.where(bound_first, idx % 2 == 0, idx % 2 == 1)
    tbound = np.sum(durs * is_bound, axis=1)
    tfree = T - tbound
    pb = np.clip(tbound / T, 1e-3, 1 - 1e-3)
    c_avg = pb / (1 - pb)                     # c/K from the time average
    # number of completed binding events (ends of unbound intervals inside [0, T])
    nbind = np.sum((~is_bound) & (ends <= T), axis=1)
    c_ml = nbind / np.maximum(tfree, 1e-9) / (kp)   # MLE of k+c, in units of the true value
    c_true = kp / km
    err_avg.append(np.std(c_avg / c_true))
    err_ml.append(np.std(c_ml))
    err_abs.append(np.std(rng.poisson(kp * T, nrep) / (kp * T)))
ax = axs[1]
Tf = np.logspace(0.8, 2.8, 100)
cols = [charts.line("receptor"), charts.line("enzyme"), charts.line("positive")]
ax.loglog(Ts, err_avg, "o", color=cols[0], ms=4, label="time average")
ax.loglog(Tf, np.sqrt(2 / (kp * (1 - p) * Tf)), color=cols[0], lw=1.0)
ax.loglog(Ts, err_ml, "s", color=cols[1], ms=4, label="maximum likelihood")
ax.loglog(Tf, np.sqrt(1 / (kp * (1 - p) * Tf)), color=cols[1], lw=1.0)
ax.loglog(Ts, err_abs, "^", color=cols[2], ms=4, label="ideal absorber")
ax.loglog(Tf, np.sqrt(1 / (kp * Tf)), color=cols[2], lw=1.0)
ax.legend(frameon=False, fontsize=7, loc="lower left")
charts.style_axes(ax, "averaging time T / s", r"relative error $\delta c/c$")
charts.title(ax, "B  one receptor")

# C: spatial gradient sensing by a snapshot
x = np.logspace(-2, 2, 200)      # c/K
ax = axs[2]
for M, tok in ((1e3, "neutral"), (1e4, "receptor"), (1e5, "enzyme")):
    snr = 0.01 * np.sqrt(M * x) / (1 + x)
    ax.loglog(x, snr, color=charts.line(tok), lw=1.4, label=rf"$M = 10^{int(np.log10(M))}$")
ax.axhline(1, color=P.muted(), lw=0.7, ls="--")
ax.axvline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_ylim(1e-2, 5)
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, r"background $c/K_{\mathrm{D}}$", "signal-to-noise ratio")
charts.title(ax, "C  1 % gradient, snapshot")
