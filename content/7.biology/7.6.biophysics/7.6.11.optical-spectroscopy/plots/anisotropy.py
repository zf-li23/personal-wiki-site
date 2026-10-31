# Fluorescence anisotropy and rotational diffusion (water, 20 C, eta = 1.0 mPa s; spheres with hydrated volume
# V = M (v + h)/N_A, v = 0.73 mL/g, h = 0.3 g/g, so tau_rot = eta V / kB T = 0.42 ns per kDa).
# A: photoselection: the excited population is distributed as cos^2 theta about the excitation polarization
#    (polar plot), which gives the fundamental anisotropy r0 = 0.4; r0 for an angle beta between absorption
#    and emission dipoles, r0 = 0.4 P2(cos beta), is noted.
# B: time-resolved anisotropy r(t) = r0 exp(-t / tau_rot) for a 25 kDa monomer (tau_rot = 10.6 ns) and its
#    dimer, with the fluorescence decay (tau = 4 ns) for comparison, and a label that wobbles in a cone
#    (fast 0.5 ns component, order parameter S^2 = 0.5) on the monomer.
# C: steady-state anisotropy (Perrin equation r = r0 / (1 + tau / tau_rot)) for a fluorescein-labeled peptide
#    (2 kDa) titrated with a 50 kDa protein, KD = 100 nM, label at 5 nM: the bound fraction is read from r.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(13.5, 4.3))
ax = fig.add_subplot(1, 3, 1, projection="polar")
th = np.linspace(0, 2 * np.pi, 400)
ax.plot(th, np.cos(th) ** 2, color=charts.line("rna"), lw=2.0)
ax.fill(th, np.cos(th) ** 2, color=P.light("rna"), alpha=0.8)
ax.set_theta_zero_location("N")
ax.set_yticks([])
ax.set_xticks(np.radians([0, 54.7, 90, 180]), ["E (pol.)", "54.7°", "90°", ""], fontsize=7.5, color=P.ink())
ax.tick_params(colors=P.muted())
ax.set_title("A   Photoselection: P(θ) ∝ cos²θ", fontsize=9, color=P.ink(), loc="left", fontweight="bold", pad=18)
fig.text(0.04, 0.03, "r0 = 0.4 P2(cos β): 0.4 (β = 0), 0 (54.7°), -0.2 (90°)", fontsize=7.5, color=P.ink())

kT = 1.380649e-23 * 293.15
tau_per_kDa = 1.0e-3 * 1000 * 1.03 / 6.02214e23 * 1e-6 / kT * 1e9
ax = fig.add_subplot(1, 3, 2)
t = np.linspace(0, 40, 400)
tm, td = 25 * tau_per_kDa, 50 * tau_per_kDa
ax.plot(t, 0.38 * np.exp(-t / tm), color=charts.line("dna"), lw=1.8, label=f"monomer, τ_rot = {tm:.1f} ns")
ax.plot(t, 0.38 * np.exp(-t / td), color=charts.line("rna"), lw=1.8, label=f"dimer, τ_rot = {td:.1f} ns")
ax.plot(t, 0.38 * (0.5 * np.exp(-t / 0.5) + 0.5) * np.exp(-t / tm), color=charts.line("protein"), lw=1.4,
        ls="--", label="monomer, wobbling label")
ax.plot(t, 0.38 * np.exp(-t / 4.0), color=P.muted(), lw=1.0, ls=":", label="intensity decay, τ = 4 ns (scaled)")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "time / ns", "r(t)")
charts.title(ax, "B   Time-resolved anisotropy")

ax = fig.add_subplot(1, 3, 3)
tau = 4.0
rF = 0.38 / (1 + tau / (2 * tau_per_kDa))
rB = 0.38 / (1 + tau / (52 * tau_per_kDa))
KD, L0 = 100.0, 5.0
Pt = np.logspace(-1, 4, 200)
b_ = L0 + Pt + KD
fb = (b_ - np.sqrt(b_**2 - 4 * L0 * Pt)) / (2 * L0)
r = fb * rB + (1 - fb) * rF
ax.semilogx(Pt, r, color=charts.line("dna"), lw=1.8)
ax.axhline(rF, color=P.muted(), lw=0.7, ls=":")
ax.axhline(rB, color=P.muted(), lw=0.7, ls=":")
ax.text(0.12, rF + 0.006, f"free peptide r = {rF:.3f}", fontsize=8, color=P.ink())
ax.text(0.12, rB + 0.006, f"bound r = {rB:.3f}", fontsize=8, color=P.ink())
ax.axvline(KD, color=P.muted(), lw=0.7, ls="--")
ax.text(KD * 1.15, 0.12, "K_D", fontsize=8, color=P.muted())
charts.style_axes(ax, "[protein] / nM", "steady-state anisotropy r")
charts.title(ax, "C   Fluorescence polarization binding assay")
fig.tight_layout()
