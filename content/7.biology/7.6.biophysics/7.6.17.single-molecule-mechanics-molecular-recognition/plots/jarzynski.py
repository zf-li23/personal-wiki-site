# Free energies from irreversible pulling: the Jarzynski equality and the Crooks theorem (simulation).
# A molecule with a double-well landscape U(x) = 3 (x^2 - 1)^2 (barrier 3 kT; units kT = 1, friction 1) is
# held by a harmonic trap of stiffness k = 5 whose centre lambda moves at constant speed from -1.5 to 2.0
# in a time 2 (forward) and back (reverse). Overdamped Langevin dynamics, dt = 1e-3, 3000 trajectories in
# each direction, started from equilibrium. Work W = integral of dH/dlambda dlambda = -k (x - lambda) dlambda.
# The exact free-energy difference dF follows from the partition functions Z(lambda) = int exp(-H) dx.
# A: forward work and minus the reverse work: the distributions cross at W = dF (Crooks).
# B: ln[P_F(W) / P_R(-W)] is a straight line of slope 1 through W = dF.
# C: the Jarzynski estimate -ln <exp(-W)> from N trajectories (median and 10-90 % range of 200 resamplings)
#    converges to dF, with a bias at small N; the mean work exceeds dF by the dissipated work.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
k, l0, l1, tau, dt, n = 5.0, -1.5, 2.0, 2.0, 1e-3, 3000
U = lambda x: 3.0 * (x**2 - 1) ** 2
dU = lambda x: 12.0 * x * (x**2 - 1)
xg = np.linspace(-4, 5, 20001)


def lnZ(lam):
    H = U(xg) + 0.5 * k * (xg - lam) ** 2
    m = H.min()
    return -m + np.log(np.trapezoid(np.exp(-(H - m)), xg))


dF = -(lnZ(l1) - lnZ(l0))


def equilibrium(lam, size):
    w = np.exp(-(U(xg) + 0.5 * k * (xg - lam) ** 2))
    c = np.cumsum(w)
    return np.interp(rng.random(size) * c[-1], c, xg)


def pull(la, lb):
    steps = int(tau / dt)
    dl = (lb - la) / steps
    x = equilibrium(la, n)
    lam, W = la, np.zeros(n)
    for _ in range(steps):
        W += -k * (x - lam) * dl
        lam += dl
        x += (-dU(x) - k * (x - lam)) * dt + np.sqrt(2 * dt) * rng.normal(size=n)
    return W


WF = pull(l0, l1)
WR = pull(l1, l0)
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
bins = np.linspace(min(WF.min(), -WR.max()), max(WF.max(), -WR.min()), 50)
hF, _ = np.histogram(WF, bins, density=True)
hR, _ = np.histogram(-WR, bins, density=True)
c = 0.5 * (bins[1:] + bins[:-1])
axs[0].bar(c, hF, width=bins[1] - bins[0], color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3, alpha=0.7, label="forward W")
axs[0].bar(c, hR, width=bins[1] - bins[0], color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.3, alpha=0.7, label="reverse −W")
axs[0].axvline(dF, color=P.ink(), lw=1.0, ls="--")
axs[0].text(dF + 0.2, max(hF.max(), hR.max()) * 0.95, f"ΔF = {dF:.2f} kT", fontsize=8, color=P.ink())
charts.style_axes(axs[0], "work / kT", "probability density")
axs[0].legend(fontsize=7.5, frameon=False, loc="upper left")
charts.title(axs[0], "A   Work distributions")

ok = (hF > 0) & (hR > 0)
counts_ok = ok & (np.histogram(WF, bins)[0] >= 10) & (np.histogram(-WR, bins)[0] >= 10)
axs[1].plot(c[counts_ok], np.log(hF[counts_ok] / hR[counts_ok]), "o", ms=4, color=charts.line("enzyme"))
ww = np.linspace(c[counts_ok].min(), c[counts_ok].max(), 10)
axs[1].plot(ww, ww - dF, color=P.muted(), lw=1.0, ls="--", label="slope 1 through ΔF")
axs[1].axhline(0, color=P.muted(), lw=0.5)
charts.style_axes(axs[1], "work W / kT", "ln [P_F(W) / P_R(−W)]")
axs[1].legend(fontsize=7.5, frameon=False, loc="upper left")
charts.title(axs[1], "B   Crooks fluctuation theorem")

Ns = np.unique(np.logspace(0, np.log10(n), 25).astype(int))
med, lo, hi = [], [], []
for N in Ns:
    est = []
    for _ in range(200):
        w = rng.choice(WF, N, replace=False)
        est.append(-(np.log(np.mean(np.exp(-(w - w.min())))) - w.min()))
    q = np.percentile(est, [10, 50, 90])
    lo.append(q[0]); med.append(q[1]); hi.append(q[2])
axs[2].fill_between(Ns, lo, hi, color=P.fill("dna"), alpha=0.5, lw=0)
axs[2].semilogx(Ns, med, color=charts.line("dna"), lw=1.8, label="Jarzynski estimate")
axs[2].axhline(dF, color=P.ink(), lw=1.0, ls="--", label="exact ΔF")
axs[2].axhline(WF.mean(), color=charts.line("rna"), lw=1.0, ls=":", label=f"mean work ⟨W⟩ = {WF.mean():.2f}")
charts.style_axes(axs[2], "number of trajectories N", "free-energy estimate / kT")
axs[2].legend(fontsize=7.5, frameon=False, loc="upper right")
charts.title(axs[2], "C   Convergence of the exponential average")
fig.tight_layout()
