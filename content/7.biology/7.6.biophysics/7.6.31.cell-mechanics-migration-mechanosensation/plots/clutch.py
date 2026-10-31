"""The molecular-clutch model of stiffness sensing (Chan and Odde 2008), simulated stochastically.
Myosin motors pull an actin bundle rearward at the unloaded speed v_u = 120 nm/s, slowed by load as
v = v_u (1 - F_sub/(n_m F_m)) (n_m = 75 motors of stall force 2 pN). Clutches (n_c = 75 molecular
springs of stiffness k_c = 5 pN/nm, the integrin-talin-actin linkage) bind at rate k_on = 1/s and
unbind as slip bonds at k_off = 0.1/s * exp(F/F_b), F_b = 2 pN; bound clutches stretch between the
moving actin and the substrate, a spring of stiffness k_sub. A: mean traction force and retrograde flow
against substrate stiffness: traction is maximal at an optimal stiffness. B: traction against time on
a soft substrate (0.1 pN/nm): load-and-fail cycles, slow loading engages many clutches, which then fail
together; C: on a stiff substrate (100 pN/nm): fast loading breaks clutches one by one before others
engage (frictional slippage), with low traction and fast retrograde flow."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
nm_, Fm, vu = 75, 2.0, 120.0
nc, kc, kon, koff0, Fb = 75, 5.0, 1.0, 0.1, 2.0


def simulate(ksub, T=60.0, dt=1e-3, seed=0):
    rng = np.random.default_rng(seed)
    bound = np.zeros(nc, bool)
    xc = np.zeros(nc)  # position of each bound clutch's actin attachment
    xsub = 0.0
    ts, Fs, vs = [], [], []
    nsteps = int(T / dt)
    for i in range(nsteps):
        nb = bound.sum()
        xsub = kc * xc[bound].sum() / (ksub + nb * kc) if nb else 0.0
        Fsub = ksub * xsub
        v = vu * max(0.0, 1 - Fsub / (nm_ * Fm))
        xc[bound] += v * dt
        F = kc * (xc - xsub)
        off = bound & (rng.random(nc) < 1 - np.exp(-koff0 * np.exp(np.clip(F, 0, 60) / Fb) * dt))
        on = (~bound) & (rng.random(nc) < kon * dt)
        bound[off] = False
        bound[on] = True
        xc[on] = xsub
        if i % 20 == 0:
            ts.append(i * dt); Fs.append(Fsub); vs.append(v)
    return np.array(ts), np.array(Fs), np.array(vs)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.4, left=0.07, right=0.93, bottom=0.17, top=0.87)
ks = np.logspace(-2, 2, 11)
mF, mv = [], []
for k in ks:
    t, F, v = simulate(k, T=40.0)
    sel = t > 5
    mF.append(F[sel].mean()); mv.append(v[sel].mean())
ax = axs[0]
ax.semilogx(ks, mF, "o-", ms=3.5, color=charts.line("blood"), lw=1.5, label="traction")
ax2 = ax.twinx()
ax2.semilogx(ks, mv, "s--", ms=3, color=charts.line("dna"), lw=1.2, label="retrograde flow")
charts.style_axes(ax2, None, None, box=True)
ax2.set_ylabel("retrograde flow / nm s$^{-1}$ (dashed)", fontsize=FT["small"], color=P.ink())
charts.style_axes(ax, "substrate stiffness / pN nm$^{-1}$", "mean traction / pN")
charts.title(ax, "A  Optimal stiffness")
for ax, k, title, tok in [(axs[1], 0.1, "B  Soft: load and fail", "blood"), (axs[2], 100.0, "C  Stiff: slippage", "dna")]:
    t, F, v = simulate(k, T=60.0, seed=1)
    ax.plot(t, F, color=charts.line(tok), lw=1.0)
    ax.set_ylim(0, max(F.max() * 1.1, 10))
    charts.style_axes(ax, "time / s", "traction / pN")
    charts.title(ax, title)
