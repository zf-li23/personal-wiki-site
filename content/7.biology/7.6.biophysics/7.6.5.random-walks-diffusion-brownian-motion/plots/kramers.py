"""Barrier crossing in a double-well potential U(x) = dU (x^2 - 1)^2 (overdamped Langevin dynamics,
gamma = kBT = 1). A: the potential for dU = 4 kBT: minima at x = +-1 with curvature
U''(a) = 8 dU, barrier at x = 0 with U''(b) = -4 dU. B: a trajectory for dU = 4 kBT: long dwells
in each well and fast jumps between them. C: escape rate (inverse mean first-passage time from
x = -1 to x = +1) from 400 simulated particles per barrier (dots), from the exact first-passage
integral (line) and from Kramers' formula k = sqrt(U''(a)|U''(b)|) / (2 pi gamma) e^{-dU/kBT}
(dashed), which becomes accurate once the barrier exceeds a few kBT."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)
U = lambda x, h: h * (x ** 2 - 1) ** 2
F = lambda x, h: -4 * h * x * (x ** 2 - 1)

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3), gridspec_kw=dict(width_ratios=(0.8, 1.3, 1)))
fig.subplots_adjust(wspace=0.36, left=0.06, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
x = np.linspace(-1.7, 1.7, 400)
ax.plot(x, U(x, 4), color=charts.line("protein"), lw=1.8)
ax.annotate("", (0, 4), (0, 0), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
ax.text(0.08, 1.8, r"$\Delta U$", fontsize=bio.core.FONT["small"], color=P.ink())
ax.plot([-1, 1], [0, 0], "o", color=charts.line("protein"), ms=4)
ax.text(-1, -0.9, "a", fontsize=bio.core.FONT["small"], color=P.ink(), ha="center")
ax.text(0, 4.4, "b", fontsize=bio.core.FONT["small"], color=P.ink(), ha="center")
ax.set_ylim(-1.5, 8)
charts.style_axes(ax, "x", r"$U$ / $k_\mathrm{B}T$")
charts.title(ax, r"A  $\Delta U = 4\,k_\mathrm{B}T$")

ax = axs[1]
dt = 0.002
n = 100000
xs = np.empty(n)
xx = -1.0
noise = rng.normal(0, np.sqrt(2 * dt), n)
for i in range(n):
    xx = xx + F(xx, 4.0) * dt + noise[i]
    xs[i] = xx
ax.plot(np.arange(n)[::5] * dt, xs[::5], color=charts.line("protein"), lw=0.5)
charts.style_axes(ax, r"$t$", "x")
charts.title(ax, "B  Dwell, jump, dwell")

ax = axs[2]
H = np.arange(1.0, 7.0)
Mw = 400
pos = np.full((H.size, Mw), -1.0)
done = np.zeros((H.size, Mw), bool)
tfp = np.zeros((H.size, Mw))
step = 0
while not done.all() and step < 400000:
    act = ~done
    pos[act] = pos[act] + F(pos[act], np.broadcast_to(H[:, None], pos.shape)[act]) * dt + \
        rng.normal(0, np.sqrt(2 * dt), act.sum())
    step += 1
    hit = act & (pos > 1.0)
    tfp[hit] = step * dt
    done |= hit
k_sim = 1 / tfp.mean(axis=1)


def mfpt(h):
    z = np.linspace(-3.0, 1.0, 40001)
    inner = cumulative_trapezoid(np.exp(-U(z, h)), z, initial=0)
    m = z >= -1.0
    return np.trapezoid(np.exp(U(z[m], h)) * inner[m], z[m])


Hc = np.linspace(0.5, 7, 60)
ax.plot(Hc, [1 / mfpt(h) for h in Hc], color=charts.line("protein"), lw=1.6, label="exact first passage")
ax.plot(Hc, np.sqrt(32) * Hc / (2 * np.pi) * np.exp(-Hc), color=P.ink(), lw=1.0, ls="--", label="Kramers")
ax.plot(H, k_sim, "o", color=charts.line("blood"), ms=4, label="simulation")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"barrier $\Delta U$ / $k_\mathrm{B}T$", r"escape rate $k$")
charts.title(ax, r"C  $k \propto \mathrm{e}^{-\Delta U/k_\mathrm{B}T}$")
