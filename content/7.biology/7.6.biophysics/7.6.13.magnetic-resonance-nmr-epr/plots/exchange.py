# Two-site chemical exchange A <-> B computed from the Bloch-McConnell equations for the transverse
# magnetization m = (m_A, m_B): dm/dt = L m with L = [[i W_A - R2 - k_AB, k_BA], [k_AB, i W_B - R2 - k_BA]],
# k_ex = k_AB + k_BA, populations p_A = k_BA / k_ex, p_B = k_AB / k_ex, intrinsic R2 = 10 s^-1.
# A: spectra (absorption, real part of (i w - L)^-1 p) for equal populations and a shift difference of
#    Delta nu = 200 Hz as k_ex increases from slow (two lines) through coalescence (k_AB = k_BA = pi Delta nu /
#    sqrt 2, that is k_ex = sqrt 2 pi Delta nu = 888 s^-1) to fast exchange (one line at the average position).
# B: a titration (p_B rising from 0 to 1, as when a ligand is added) in the slow (k_ex = 50 s^-1), intermediate
#    (1000 s^-1) and fast (20000 s^-1) regimes, Delta nu = 200 Hz.
# C: CPMG relaxation dispersion: the effective R2 after a constant-time train of 180 degree pulses (40 ms)
#    against the pulsing rate nu_CPMG = 1 / (2 tau_cp), computed by propagating the Bloch-McConnell equations
#    with ideal pulses, for p_B = 5 %, Delta nu = 150 Hz and three exchange rates.
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio
from wikibio import charts

P = bio.P
R2 = 10.0


def L_matrix(wa, wb, kex, pb):
    kab, kba = kex * pb, kex * (1 - pb)
    return np.array([[1j * wa - R2 - kab, kba], [kab, 1j * wb - R2 - kba]])


def spectrum(nu, dnu, kex, pb):
    L = L_matrix(-np.pi * dnu, np.pi * dnu, kex, pb)
    p = np.array([1 - pb, pb])
    out = []
    for f in nu:
        out.append(np.linalg.solve(1j * 2 * np.pi * f * np.eye(2) - L, p).sum().real)
    return np.array(out)


fig, axs = plt.subplots(1, 3, figsize=(13.0, 4.6), gridspec_kw=dict(width_ratios=[1, 1.35, 1.1]))
nu = np.linspace(-250, 250, 1200)

ax = axs[0]
for k, kex in enumerate((20, 150, 888, 3000, 20000)):
    y = spectrum(nu, 200.0, kex, 0.5)
    ax.plot(nu, y / y.max() * 0.9 + 1.1 * k, color=charts.line("protein"), lw=1.2)
    ax.text(250, 1.1 * k + 0.45, f"k_ex = {kex} s⁻¹", fontsize=7.5, color=P.ink(), ha="right")
ax.set_yticks([])
ax.set_xlim(-250, 250)
charts.style_axes(ax, "frequency / Hz", None)
charts.title(ax, "A   Exchange broadening, Δν = 200 Hz")

ax = axs[1]
nu2 = np.linspace(-170, 170, 900)
for col, (kex, name) in enumerate(((50, "slow"), (1000, "intermediate"), (20000, "fast"))):
    ymax = None
    for k, pb in enumerate((0.0, 0.25, 0.5, 0.75, 1.0)):
        y = spectrum(nu2, 200.0, kex, pb)
        if ymax is None:
            ymax = y.max()
        ax.plot(nu2 / 170 * 0.6 + 1.4 * col, y / ymax * 0.85 + 1.0 * (4 - k), color=charts.line("enzyme"), lw=1.0)
        if col == 0:
            ax.text(-0.65, 1.0 * (4 - k) + 0.15, f"p_B = {pb:.2f}", fontsize=7, color=P.ink(), ha="right")
    ax.text(1.4 * col, 5.05, f"{name}\nk_ex = {kex} s⁻¹", ha="center", fontsize=7.5, color=P.ink())
ax.set_xlim(-1.3, 3.5)
ax.set_ylim(-0.1, 5.7)
ax.axis("off")
charts.title(ax, "B   Titration: free → bound")

ax = axs[2]
Tcp = 0.040
dnu, pb = 150.0, 0.05
for kex, tok in ((300, "protein"), (1000, "rna"), (3000, "enzyme")):
    L = L_matrix(-2 * np.pi * dnu * pb, 2 * np.pi * dnu * (1 - pb), kex, pb)   # average frequency at zero
    p = np.array([1 - pb, pb], complex)
    nus, r2s = [], []
    for ncyc in (1, 2, 3, 4, 6, 8, 10, 14, 20, 26, 32, 40):
        tau = Tcp / (4 * ncyc)                 # each cycle: tau - 180 - 2 tau - 180 - tau
        E = expm(L * tau)
        m = p.copy()
        for _ in range(2 * ncyc):
            m = E @ np.conj(E @ m)
        r2s.append(-np.log(abs(m.sum()) / abs(p.sum())) / Tcp)
        nus.append(1 / (4 * tau))
    ax.plot(nus, r2s, "o-", color=charts.line(tok), lw=1.2, ms=3.5, label=f"k_ex = {kex} s⁻¹")
ax.axhline(R2, color=P.muted(), lw=0.7, ls="--")
ax.text(700, R2 + 0.5, "R₂⁰ (no exchange)", fontsize=7.5, color=P.muted())
ax.set_xlim(0, 1050)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "ν_CPMG / Hz", "R₂,eff / s⁻¹")
charts.title(ax, "C   CPMG dispersion, p_B = 5 %, Δν = 150 Hz")
fig.tight_layout()
