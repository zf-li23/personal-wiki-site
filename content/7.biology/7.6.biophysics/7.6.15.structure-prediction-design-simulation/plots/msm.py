# A Markov state model built from simulated trajectories.
# Overdamped Brownian dynamics (D = 1, dt = 1e-3, energies in k_B T) in a triple-well potential
# U(x) = 0.35 x^2 (x^2 - 4)^2 + 0.4 x, with minima near x = -2, 0, 2 (states A, B, C) separated by
# barriers of about 3-4 k_B T;
# 20 independent trajectories of 50 000 steps. The coordinate is divided into 40 bins (microstates);
# transitions are counted at a lag time tau, the count matrix is symmetrized (detailed balance), and
# the transition matrix T(tau) is diagonalized.
# A: the potential and a stretch of one trajectory, hopping between the three wells.
# B: implied time scales t_i = -tau / ln lambda_i(tau) of the two slowest processes against the lag time:
#    they level off once tau exceeds the fast relaxation inside the wells, the test of Markovian behaviour.
# C: the stationary distribution of the model (first eigenvector) compared with exp(-U) (line), and the
#    second and third left eigenvectors divided by it: each is nearly constant within a well and changes
#    sign across the barriers, identifying which wells exchange population in each slow process
#    (process 2 mainly A against C, process 3 B against A and C).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(6)


def U(x):
    return 0.35 * x**2 * (x**2 - 4) ** 2 + 0.4 * x


def dU(x, h=1e-5):
    return (U(x + h) - U(x - h)) / (2 * h)


dt, D, ntraj, steps = 1e-3, 1.0, 20, 50000
x = rng.choice([-2.0, 0.0, 2.0], ntraj)
traj = np.empty((steps, ntraj))
for s in range(steps):
    x = x - D * dU(x) * dt + np.sqrt(2 * D * dt) * rng.standard_normal(ntraj)
    traj[s] = x
edges = np.linspace(-3.0, 3.0, 41)
xc = 0.5 * (edges[1:] + edges[:-1])
lab = np.clip(np.digitize(traj, edges) - 1, 0, 39)
nb = 40


def tmatrix(lag):
    C = np.zeros((nb, nb))
    for j in range(ntraj):
        np.add.at(C, (lab[:-lag, j], lab[lag:, j]), 1)
    C = C + C.T + 1e-12
    return C / C.sum(1, keepdims=True), C.sum(1) / C.sum()


lags = np.array([1, 2, 5, 10, 20, 50, 100, 200, 400, 800])
its = []
for lag in lags:
    T, pi = tmatrix(lag)
    ev = np.sort(np.linalg.eigvals(T).real)[::-1]
    its.append(-lag * dt / np.log(ev[1:3]))
its = np.array(its)

fig, axs = plt.subplots(1, 3, figsize=(14, 4.0))
ax = axs[0]
xx = np.linspace(-3, 3, 300)
ax.plot(xx, U(xx), color=charts.line("protein"), lw=1.8)
ax.set_ylim(-1.6, 8)
for x0, name in ((-2, "A"), (0, "B"), (2, "C")):
    ax.text(x0, U(x0) - 0.25, name, ha="center", va="top", fontsize=9, color=P.ink(), weight="bold")
charts.style_axes(ax, "coordinate x", "U / k_B T")
inset = ax.inset_axes([0.3, 0.62, 0.42, 0.33])
tt = np.arange(steps) * dt
inset.plot(tt[::20], traj[::20, 0], color=charts.line("dna"), lw=0.5)
inset.set_xticks([0, 25, 50])
charts.style_axes(inset, "time", "x")
charts.title(ax, "A   Triple well and a trajectory")

ax = axs[1]
for i, tok in ((0, "negative"), (1, "dna")):
    ax.loglog(lags * dt, its[:, i], "o-", color=charts.line(tok), lw=1.2, ms=4, label=f"process {i + 2}")
ax.loglog(lags * dt, lags * dt, color=P.muted(), lw=0.8, ls=":", label="t = τ")
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "lag time τ", "implied time scale")
charts.title(ax, "B   Implied time scales")

ax = axs[2]
T, pi = tmatrix(100)
w, vl = np.linalg.eig(T.T)
order = np.argsort(-w.real)
stat = np.abs(vl[:, order[0]].real)
stat /= stat.sum()
boltz = np.exp(-U(xc))
boltz /= boltz.sum()
ax.bar(xc, stat, width=0.13, color=P.light("protein"), edgecolor=P.edge("protein"), lw=0.5, label="π (MSM)")
ax.plot(xc, boltz, color=charts.line("protein"), lw=1.2, label="exp(−U) / Z")
ax2 = ax.twinx()
for k, tok in ((1, "negative"), (2, "dna")):
    psi = vl[:, order[k]].real / np.where(stat > 1e-6, stat, np.nan)
    psi /= np.nanmax(np.abs(psi))
    ax2.plot(xc, psi, color=charts.line(tok), lw=1.2, ls="--", label=f"eigenvector {k + 1} / π")
ax2.axhline(0, color=P.muted(), lw=0.5)
ax2.set_ylim(-1.2, 1.2)
ax2.tick_params(colors=P.muted(), labelcolor=P.muted(), labelsize=7)
for name, sp in ax2.spines.items():
    sp.set_visible(name == "right")
    sp.set_color(P.muted())
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "coordinate x", "probability")
charts.title(ax, "C   Stationary distribution and slow modes")
fig.tight_layout()
