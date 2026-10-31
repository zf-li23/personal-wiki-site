"""Polarity from a mass-conserved reaction-diffusion system: the wave-pinning model of a small
GTPase (Formula 15.4.1 of 7.3.15), active membrane form a (D_a = 0.02 um^2/s) and inactive cytosolic
form b (D_b = 10 um^2/s), f(a, b) = b(k0 + a^2/(1 + a^2)) - a with k0 = 0.067, in a cell of length
10 um with no-flux ends. A: the reactive nullcline f = 0 in the (a, b) plane and lines of constant
total density n = a + b; where the nullcline slope db/da is below -D_a/D_b (thick part) the uniform
state is laterally unstable (Theorem 36.4.1); the two points mark the uniform states used in B and C.
B: kymograph of a(x, t) from small noise around the uniform state with n = 2.5, inside the unstable
window: noise alone is amplified into a single domain of active GTPase, whose size is set by the
total amount of protein because the cytosolic pool is shared.
C: with n = 2.2 the uniform state is laterally stable and noise decays (thin line, final profile),
but a transient local stimulus at the left end (activation 0.5 b per second for 20 s) leaves a pinned domain
(thick line): polarization requires a threshold."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.fft import dct, idct
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(11)
k0, Da, Db, L, nx = 0.067, 0.02, 10.0, 10.0, 200
dx = L / nx
x = (np.arange(nx) + 0.5) * dx
lam = -(np.pi * np.arange(nx) / L) ** 2
cmap = LinearSegmentedColormap.from_list("gtp", [P.surface(), P.fill("enzyme"), P.edge("enzyme")])


def f(a, b):
    return b * (k0 + a ** 2 / (1 + a ** 2)) - a


def uniform(n):
    return brentq(lambda a: f(a, n - a), 1e-6, n - 1e-6)


def simulate(n, T, dt=0.02, noise=0.01, stim=None):
    a0 = uniform(n)
    a = a0 * (1 + noise * rng.standard_normal(nx))
    b = (n - a0) * np.ones(nx)
    rec = []
    for i in range(int(T / dt)):
        r = f(a, b)
        if stim is not None and i * dt < stim:
            r = r + 0.5 * b * (x < 1.0)
        ah = dct(a + dt * r, norm="ortho") / (1 - dt * Da * lam)
        bh = dct(b - dt * r, norm="ortho")
        bh = bh / (1 - dt * Db * lam)
        a, b = idct(ah, norm="ortho"), idct(bh, norm="ortho")
        if i % int(5 / dt) == 0:
            rec.append(a.copy())
    return np.array(rec), a


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.4), gridspec_kw=dict(width_ratios=(1, 1.15, 1)))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.98, bottom=0.16, top=0.88)

ax = axs[0]
aa = np.linspace(0.001, 3, 600)
bb = aa / (k0 + aa ** 2 / (1 + aa ** 2))
slope = np.gradient(bb, aa)
ax.plot(aa, bb, color=charts.line("enzyme"), lw=1.0)
uns = slope < -Da / Db
ax.plot(np.where(uns, aa, np.nan), np.where(uns, bb, np.nan), color=charts.line("enzyme"), lw=3.0)
for n in (1.5, 2.0, 2.5, 3.0):
    ax.plot(aa, n - aa, color=P.muted(), lw=0.6, ls="--")
for n, tok in ((2.5, "enzyme"), (2.2, "receptor")):
    a0 = uniform(n)
    ax.plot(a0, n - a0, "o", color=charts.line(tok), ms=4)
ax.set_xlim(0, 3)
ax.set_ylim(0, 3.2)
charts.style_axes(ax, "active, membrane a", "inactive, cytosol b")
charts.title(ax, "A  nullcline and mass lines")

rec, _ = simulate(2.5, 1500)
ax = axs[1]
ax.imshow(rec, aspect="auto", origin="lower", extent=(0, L, 0, 5 * rec.shape[0]), cmap=cmap, interpolation="bilinear")
charts.style_axes(ax, r"position / $\mu$m", "time / s", box=True)
charts.title(ax, "B  polarization from noise")

ax = axs[2]
_, a_noise = simulate(2.2, 300)
_, a_stim = simulate(2.2, 300, stim=20.0)
ax.plot(x, a_noise, color=charts.line("receptor"), lw=1.0, label="noise only")
ax.plot(x, a_stim, color=charts.line("enzyme"), lw=1.8, label="after local stimulus")
ax.legend(frameon=False, fontsize=7, loc="upper right")
charts.style_axes(ax, r"position / $\mu$m", "active GTPase a")
charts.title(ax, "C  threshold for polarity")
