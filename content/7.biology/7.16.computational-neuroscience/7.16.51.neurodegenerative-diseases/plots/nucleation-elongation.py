"""Aggregation kinetics of amyloid proteins: primary and secondary nucleation, elongation and seeding.

Moment equations (Knowles et al. 2009; Cohen et al. 2013) for the fibril number concentration P and the
fibril mass concentration M, with free monomer m = m_tot - M:
  dP/dt = k_n m^n_c + k_2 m^n_2 M,      dM/dt = 2 k_+ m P,
n_c = n_2 = 2, m_tot = 5 uM, k_+ = 3e6 /M/s and k_2 = 1e4 /M^2/s (of the order measured for Abeta42),
k_n = 3e-6 /M/s (lowered about 100-fold so that primary nucleation is rate-limiting); time in hours. Seeding: an initial fibril mass M0 (fraction of m_tot) with fibrils
of average length 5000 monomers, P0 = M0 / 5000.
A: normalized fibril mass for unseeded aggregation with and without secondary nucleation, and with seeds.
B: half-time against seed fraction (log-log).
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio

P_ = bio.P
mt = 5e-6
kp, kn, k2 = 3e6, 3e-6, 1e4


def rhs(t, y, k2v):
    Pn, M = y
    m = max(mt - M, 0.0)
    return [kn * m ** 2 + k2v * m ** 2 * M, 2 * kp * m * Pn]


def run(seed=0.0, k2v=k2, tmax=60 * 3600):
    M0 = seed * mt
    y0 = [M0 / 5000.0, M0]
    t = np.linspace(0, tmax, 2000)
    sol = solve_ivp(rhs, (0, tmax), y0, t_eval=t, args=(k2v,), method="LSODA", rtol=1e-8, atol=1e-20)
    return t / 3600, sol.y[1] / mt


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axs[0]
t, f = run(0.0)
ax.plot(t, f, color=P_.edge("negative"), lw=2.0, label="unseeded")
t, f = run(0.0, k2v=0.0, tmax=4000 * 3600)
ax.plot(t, f, color=P_.muted(), lw=1.6, ls="--", label="no secondary nucleation")
for s, col in ((1e-4, P_.edge("protein")), (1e-2, P_.edge("dna"))):
    t, f = run(s)
    ax.plot(t, f, color=col, lw=1.8, label=f"seeded, {100 * s:g} % preformed fibrils")
ax.set_xlim(0, 12)
ax.set_xlabel("Time / h")
ax.set_ylabel("Fibril mass / total protein")
ax.legend(frameon=False, fontsize=7.5, loc="center right")
ax.set_title("A  Sigmoidal aggregation", loc="left", fontsize=10)

ax = axs[1]
seeds = np.logspace(-6, -1, 11)
th = []
for s in seeds:
    t, f = run(s)
    th.append(np.interp(0.5, f, t))
ax.loglog(seeds * 100, th, "o-", color=P_.edge("dna"), lw=1.6, ms=4)
t, f = run(0.0)
ax.axhline(np.interp(0.5, f, t), color=P_.edge("negative"), lw=1.0, ls="--")
ax.text(1.2e-4, np.interp(0.5, f, t) * 0.9, "unseeded", fontsize=8, color=P_.edge("negative"))
ax.set_xlabel("Seed / % of total protein")
ax.set_ylabel("Half-time / h")
ax.set_title("B  Seeds shorten the lag", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3, which="both")
fig.tight_layout()
