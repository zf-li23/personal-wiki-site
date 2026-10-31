# The flashing ratchet: overdamped Brownian particles in an asymmetric sawtooth potential that is switched
# on (duration t_on) and off (duration t_off). Units: period L = 1, diffusion coefficient D = 1, energies in kBT.
# Barrier U0 = 8 kBT; from each minimum (at the integers) the potential rises steeply over alpha L = 0.2 L to its
# maximum and falls gently over (1 - alpha) L to the next minimum, so a particle released from a minimum has
# to diffuse only alpha L forward but (1 - alpha) L backward to be captured by a neighboring well.
# A: the potential and the particle distributions just before switching off and just before switching on.
# B: mean drift velocity (Euler-Maruyama simulation of 400 particles, dt = 4e-4) against t_off at t_on = 0.3,
#    compared with Formula 27.2.1 (line), evaluated with the committor of the frozen potential.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
U0, alpha, D = 8.0, 0.2, 1.0
xm = alpha  # position of the maximum within each period; minima at integers


def force(x):
    s = np.mod(x, 1.0)
    return np.where(s < xm, -U0 / xm, U0 / (1 - xm))  # F = -dU/dx


def U(x):
    s = np.mod(x, 1.0)
    return np.where(s < xm, U0 * s / xm, U0 * (1 - s) / (1 - xm))


dt = 4e-4
t_on = 0.3


def run(t_off, cycles, n=400, keep=False):
    x = np.zeros(n)
    snaps = []
    on_steps, off_steps = int(t_on / dt), int(t_off / dt)
    sq = np.sqrt(2 * D * dt)
    for c in range(cycles):
        for _ in range(on_steps):
            x += force(x) * dt + sq * rng.standard_normal(n)
        if keep and c == cycles - 1:
            snaps.append(x.copy())
        x += np.sqrt(2 * D * t_off) * rng.standard_normal(n)  # free diffusion while off (exact)
        if keep and c == cycles - 1:
            snaps.append(x.copy())
    return x.mean() / (cycles * (t_on + t_off)), snaps


toffs = np.array([0.002, 0.005, 0.01, 0.02, 0.04, 0.07, 0.12, 0.2, 0.35])
vs = [run(to, 25)[0] for to in toffs]
tt = np.logspace(-3, np.log10(0.5), 50)
# estimate: start from the Boltzmann distribution in one well, spread by free diffusion for t_off; a particle at
# y is then recaptured by the well to its right with the committor probability q of the frozen potential,
# q(s) = int_0^s exp(U) / int_0^1 exp(U) for s = y mod L (the barrier top is crossed by diffusion, not deterministically)
x0 = np.linspace(-(1 - alpha), alpha, 201)
w0 = np.exp(-U(x0))
w0 /= w0.sum()
sg = np.linspace(0, 1, 2001)
eU = np.exp(U(sg))
q_tab = np.concatenate([[0], np.cumsum(0.5 * (eU[1:] + eU[:-1]))])
q_tab /= q_tab[-1]
y = np.linspace(-4, 4, 1601)
fate = np.floor(y) + np.interp(np.mod(y, 1.0), sg, q_tab)


def mean_jump(t):
    s = np.sqrt(2 * D * t)
    dens = np.exp(-(y[:, None] - x0[None, :]) ** 2 / (2 * s * s)) @ w0
    dens /= dens.sum()
    return np.sum(dens * fate)


v_est = np.array([mean_jump(t) for t in tt]) / (t_on + tt)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
xx = np.linspace(-1.5, 2.5, 800)
ax.plot(xx, U(xx), color=charts.line("enzyme"), lw=1.8)
_, snaps = run(0.04, 3, n=4000, keep=True)
bins = np.linspace(-1.5, 2.5, 161)
for sn, tok, lab in ((snaps[0], "dna", "end of on phase"), (snaps[1], "rna", "end of off phase")):
    h, e = np.histogram(sn, bins, density=True)
    ax.plot(0.5 * (e[1:] + e[:-1]), h * 1.2, color=charts.line(tok), lw=1.2, drawstyle="steps-mid", label=lab)
ax.annotate("", xy=(xm + 1, U0 + 0.6), xytext=(1, U0 + 0.6), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(1 + xm / 2, U0 + 0.9, "$\\alpha L$", ha="center", fontsize=8, color=P.ink())
ax.annotate("", xy=(2, U0 + 0.6), xytext=(xm + 1, U0 + 0.6), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(1.6, U0 + 0.9, "$(1-\\alpha)L$", ha="center", fontsize=8, color=P.ink())
ax.set_ylim(0, 11); ax.set_xlim(-1.5, 2.5)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "position $x / L$", "$U / k_\\mathrm{B}T$  (densities scaled)")
charts.title(ax, "A   Sawtooth potential and particle densities")

ax = axs[1]
ax.semilogx(tt, v_est, color=charts.line("neutral"), lw=1.4, label="estimate (Formula 27.2.1)")
ax.semilogx(toffs, vs, "o", color=charts.line("enzyme"), ms=5, label="Langevin simulation")
ax.axhline(0, color=P.muted(), lw=0.6)
charts.style_axes(ax, "off time $t_\\mathrm{off}$ / ($L^2/D$)", "drift velocity / ($D/L$)")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.title(ax, "B   Too short: no escape; too long: wasted time")
fig.tight_layout()
