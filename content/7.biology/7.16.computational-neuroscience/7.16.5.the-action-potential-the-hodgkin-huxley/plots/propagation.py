"""Conduction in a compartmental axon with Hodgkin-Huxley kinetics (20 C: rates x 4.5 from 6.3 C; axial
resistivity R_i = 100 ohm cm). Unmyelinated: HH membrane everywhere, compartments of 20 um (d = 2 um),
a depolarized segment at the left end launches a pulse. Myelinated: nodes of Ranvier 1 um long with
g_Na = 1000, g_K = 36 mS/cm2 (HH gates), internodes of length 100 d with N = 10 d (d in um) myelin lamellae
(capacitance 1/(2N) uF/cm2, leak 0.3/(2N) mS/cm2), 6 passive compartments each. The voltage is advanced
with a semi-implicit scheme (backward Euler for V, tridiagonal solve; exponential Euler for the gates).
A: V(x) at 1 ms intervals for the unmyelinated fiber (d = 2 um): a constant-shape pulse. B: V(t) at
successive nodes of a myelinated fiber (d = 4 um): the pulse jumps from node to node, each node
delayed by about 0.03 ms. C: conduction velocity against fiber diameter (log-log): unmyelinated
slope 1/2, myelinated slope 1."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
import wikibio as bio
from wikibio import charts, neuro

P = bio.P
FT = bio.core.FONT
p = neuro.HH
Q = 3.0 ** ((20 - 6.3) / 10)
RI, GNODE = 100.0, 1000.0


def build(d_um, myel):
    d = d_um * 1e-4
    ra = 4 * RI / (np.pi * d * d)  # ohm / cm
    if myel:
        lnode, L, nseg, nn = 1e-4, 100 * d, 6, 12
        lens, kind = [], []
        for k in range(nn):
            lens.append(lnode); kind.append(1)
            if k < nn - 1:
                lens += [L / nseg] * nseg; kind += [0] * nseg
        lens, kind = np.array(lens), np.array(kind)
    else:
        dx = 0.002 * np.sqrt(d_um / 2)
        lens = np.full(int(1.2 * np.sqrt(d_um / 2) / dx), dx); kind = np.ones(len(lens), int)
    return d, ra, lens, kind


def simulate(d_um, myel, T, dt, every=0.02):
    d, ra, lens, kind = build(d_um, myel)
    n = len(lens); area = np.pi * d * lens
    Nm = 10.0 * d_um
    Cu = np.where(kind == 1, 1.0, 1.0 / (2 * Nm)) * area  # uF
    gax = 1e3 / (ra * 0.5 * (lens[:-1] + lens[1:]))  # mS
    gNa = np.where(kind == 1, GNODE if myel else p["gNa"], 0.0) * area
    gK = np.where(kind == 1, p["gK"], 0.0) * area
    gL = np.where(kind == 1, p["gL"], p["gL"] / (2 * Nm)) * area
    x = np.concatenate([[0], np.cumsum(0.5 * (lens[:-1] + lens[1:]))])
    V = np.full(n, -65.0)
    m0, h0, n0 = [float(v) for v in neuro.hh_steady(-65.0)]
    m, h, nk = np.full(n, m0), np.full(n, h0), np.full(n, n0)
    base = np.zeros((3, n)); dg = Cu / dt; dg[:-1] += gax; dg[1:] += gax
    base[1] = dg; base[0, 1:] = -gax; base[2, :-1] = -gax
    V[:7] = 0.0 if myel else V[:7]
    if not myel:
        V[x < 0.3 * np.sqrt(d_um / 2)] = 0.0
    rec = []; k_every = int(round(every / dt))
    for s in range(int(T / dt)):
        am, bm, ah, bh, an, bn = [Q * a for a in neuro.hh_rates(V)]
        for var, a_, b_ in ((m, am, bm), (h, ah, bh), (nk, an, bn)):
            var += (a_ / (a_ + b_) - var) * (1 - np.exp(-dt * (a_ + b_)))
        gn, gk = gNa * m**3 * h, gK * nk**4
        ab = base.copy(); ab[1] += gn + gk + gL
        V = solve_banded((1, 1), ab, Cu / dt * V + gn * p["ENa"] + gk * p["EK"] + gL * p["EL"])
        if s % k_every == 0:
            rec.append(V.copy())
    return x, kind, np.arange(len(rec)) * every, np.array(rec)


def cross(ts, v, th=-20.0):
    k = np.where((v[:-1] < th) & (v[1:] >= th))[0]
    if not len(k):
        return np.nan
    k = k[0]
    return ts[k] + (th - v[k]) / (v[k + 1] - v[k]) * (ts[k + 1] - ts[k])


fig = plt.figure(figsize=(10.4, 3.4))
gs = fig.add_gridspec(1, 3, wspace=0.32, left=0.06, right=0.99, bottom=0.17, top=0.88)

ax = fig.add_subplot(gs[0, 0])
x, kind, ts, Vs = simulate(2, False, 8.0, 0.01)
for j, k in enumerate(range(100, 400, 50)):
    ax.plot(x * 10, Vs[k], color=charts.line("neuron"), lw=1.2, alpha=0.35 + 0.65 * j / 5)
    ax.text(x[np.argmax(Vs[k])] * 10, Vs[k].max() + 3, f"{ts[k]:.0f}", ha="center", fontsize=FT["tiny"], color=P.muted())
ax.set_xlim(0, 12); ax.set_ylim(-80, 50)
charts.style_axes(ax, "position / mm", "$V$ / mV")
charts.title(ax, "A  Unmyelinated, $d = 2\\,\\mu$m")

ax = fig.add_subplot(gs[0, 1])
x, kind, ts, Vs = simulate(4, True, 1.6, 0.004, every=0.008)
idx = np.where(kind == 1)[0]
for j, i in enumerate(idx[1:9]):
    ax.plot(ts, Vs[:, i] + 0 * j, color=charts.line("neuron"), lw=1.1)
ax.set_xlim(0, 0.8); ax.set_ylim(-75, 55)
charts.style_axes(ax, "t / ms", "$V$ / mV (nodes 2-9)")
charts.title(ax, "B  Myelinated, $d = 4\\,\\mu$m")

ax = fig.add_subplot(gs[0, 2])
du = np.array([0.5, 1.0, 2.0, 4.0, 8.0]); vu = []
for d in du:
    x, kind, ts, Vs = simulate(d, False, 40 / np.sqrt(d / 0.5) if d > 0.5 else 40.0, 0.01)
    idx = np.where(kind == 1)[0]
    a, b = idx[int(len(idx) * 0.45)], idx[int(len(idx) * 0.7)]
    vu.append((x[b] - x[a]) * 1e-2 / ((cross(ts, Vs[:, b]) - cross(ts, Vs[:, a])) * 1e-3))
dm = np.array([1.0, 2.0, 4.0, 8.0, 16.0]); vm = []
for d in dm:
    x, kind, ts, Vs = simulate(d, True, 1.6, 0.004)
    idx = np.where(kind == 1)[0]
    a, b = idx[3], idx[-3]
    vm.append((x[b] - x[a]) * 1e-2 / ((cross(ts, Vs[:, b]) - cross(ts, Vs[:, a])) * 1e-3))
ax.loglog(du, vu, "o-", color=charts.line("neuron"), lw=1.3, label="unmyelinated")
ax.loglog(dm, vm, "s-", color=charts.line("highlight"), lw=1.3, label="myelinated")
ax.loglog(du, vu[0] * (du / du[0]) ** 0.5, ":", color=P.muted(), lw=0.8)
ax.loglog(dm, vm[0] * (dm / dm[0]), ":", color=P.muted(), lw=0.8)
ax.text(0.5, 0.62, "slope 1/2", fontsize=FT["tiny"], color=P.muted()); ax.text(1.1, 6, "slope 1", fontsize=FT["tiny"], color=P.muted())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "diameter $d$ / $\\mu$m", "velocity / m s$^{-1}$")
charts.title(ax, "C  Velocity against diameter")
