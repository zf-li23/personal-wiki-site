"""Run-and-tumble chemotaxis of simulated E. coli in two dimensions. Each cell swims at 20 um/s,
turns by a random angle (mean 68 degrees, sd 25 degrees, either side) at each tumble and diffuses
in angle (D_r = 0.1 rad^2/s) during runs. Its tumble rate is set by an adapting receptor cluster:
the MWC activity of Fig. 35.4 with methylation dynamics dm/dt = k (a0 - a) (adapted activity
a0 = 1/3, k = 0.1 per second) and a motor rate lambda = lambda0 (a/a0)^3 with lambda0 = 1 per second.
A: tracks of five cells for 400 s in uniform attractant. B: the same in an exponential gradient of
MeAsp, c = 0.1 mM exp(x/L) with L = 0.5 mm (attractant increasing to the right). C: mean
displacement along the gradient of 400 cells against time for L = 0.5, 1 and 2 mm, and the drift
speed (inset, um/s) against 1/L: the drift is proportional to the steepness of ln c, the
signature of logarithmic sensing."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(7)
N, KI, KA, alpha, m0 = 6, 18e-3, 3.0, 1.7, 1.0
v, Dr, lam0, a0, kmeth, dt = 20.0, 0.1, 1.0, 1 / 3, 0.1, 0.05


def act(m, c):
    return 1 / (1 + np.exp(N * (alpha * (m0 - m) + np.log((1 + c / KI) / (1 + c / KA)))))


def m_adapted(c):
    return m0 + (np.log((1 + c / KI) / (1 + c / KA)) - np.log(1 / a0 - 1) / N) / alpha


def simulate(ncell, T, L=None, c0=0.1):
    x = np.zeros(ncell)
    y = np.zeros(ncell)
    th = rng.uniform(0, 2 * np.pi, ncell)
    conc = (lambda xx: np.full_like(xx, c0)) if L is None else (lambda xx: c0 * np.exp(xx / L))
    m = m_adapted(conc(x))
    steps = int(T / dt)
    X = np.empty((steps, ncell))
    Y = np.empty((steps, ncell))
    for i in range(steps):
        c = conc(x)
        a = act(m, c)
        m += dt * kmeth * (a0 - a)
        lam = lam0 * (a / a0) ** 3
        tumble = rng.random(ncell) < lam * dt
        turn = np.deg2rad(rng.normal(68, 25, ncell)) * rng.choice([-1, 1], ncell)
        th = th + np.where(tumble, turn, 0.0) + np.sqrt(2 * Dr * dt) * rng.normal(size=ncell)
        run = ~tumble
        x = x + run * v * np.cos(th) * dt
        y = y + run * v * np.sin(th) * dt
        X[i], Y[i] = x, y
    return X, Y


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.4), gridspec_kw=dict(width_ratios=(1, 1, 1.1)))
fig.subplots_adjust(wspace=0.35, left=0.06, right=0.98, bottom=0.16, top=0.88)
toks = ["receptor", "enzyme", "positive", "highlight", "neutral"]
for k, (L, ttl) in enumerate(((None, "A  uniform attractant"), (500.0, r"B  gradient, $L$ = 0.5 mm"))):
    X, Y = simulate(5, 400, L)
    ax = axs[k]
    for j in range(5):
        ax.plot(X[:, j], Y[:, j], color=charts.line(toks[j]), lw=0.6)
        ax.plot(X[-1, j], Y[-1, j], "o", color=charts.line(toks[j]), ms=3)
    ax.plot(0, 0, "+", color=P.ink(), ms=8)
    ax.set_aspect("equal")
    ax.set_xlim(-1000, 2600)
    ax.set_ylim(-1800, 1800)
    charts.style_axes(ax, r"x / $\mu$m", r"y / $\mu$m" if k == 0 else None)
    charts.title(ax, ttl)

ax = axs[2]
Ls = [500.0, 1000.0, 2000.0]
speeds = []
for L, tok in zip(Ls, ["enzyme", "receptor", "neutral"]):
    X, Y = simulate(400, 300, L)
    t = np.arange(X.shape[0]) * dt
    mx = X.mean(axis=1)
    ax.plot(t, mx, color=charts.line(tok), lw=1.3, label=f"L = {L / 1000:g} mm")
    sl = t > 60
    speeds.append(np.polyfit(t[sl], mx[sl], 1)[0])
ax.legend(frameon=False, fontsize=7, loc="lower right", bbox_to_anchor=(1.0, 0.18))
charts.style_axes(ax, "time / s", r"mean displacement / $\mu$m")
charts.title(ax, "C  drift up the gradient")
ins = ax.inset_axes([0.14, 0.6, 0.3, 0.3])
inv = 1000 / np.array(Ls)
ins.plot(inv, speeds, "o", color=charts.line("receptor"), ms=3)
ins.plot([0, 2.1], [0, 2.1 * np.mean(np.array(speeds) / inv)], color=P.muted(), lw=0.8)
ins.set_xlim(0, 2.2)
ins.set_ylim(0, None)
charts.style_axes(ins, "1/L (1/mm)", None)
ins.xaxis.label.set_size(6.5)
