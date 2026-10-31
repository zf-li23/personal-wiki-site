# Buffer subtraction and first checks of SAXS data (simulated, absolute scale in cm^-1).
# Protein: a 14.3 kDa globular protein at c = 2 mg/mL, modelled as spheres of mean radius 18.7 A
# (Rg = 14.5 A) with a 10 % spread of radii (Guinier fit: the z-average Rg, 15.4 A);
# I(0) = MW c / 1385 = 0.0207 cm^-1 (Formula 9.10.1).
# Buffer: water (0.0163 cm^-1) plus capillary and parasitic scattering, 0.030 + 2e-8 q^-3 cm^-1.
# Sample = buffer (attenuated by the displaced volume, 0.15 %) + protein; Poisson-like noise.
# A: sample, buffer and their difference: at q = 0.3 A^-1 the protein is about 0.3 % of the measured signal.
# B: Kratky representation q^2 I(q) of the difference after correct subtraction and after scaling the buffer
#    by 0.997 or 1.003 (a 0.3 % mismatch, e.g. from a transmission error): under-subtraction produces a
#    rising tail that mimics unfolding, over-subtraction a tail that falls below zero.
# C: Guinier plots ln I against q^2 for the monodisperse protein, the same with 1 % (by mass) of
#    aggregates (50-mers, Rg = 55 A), and with repulsive interparticle interference (S(q) < 1 at small q).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)
q = np.linspace(0.008, 0.35, 400)


def sphere_pd(q, R, spread=0.1, n=41):
    r = R * (1 + spread * np.linspace(-2.5, 2.5, n))
    w = np.exp(-0.5 * np.linspace(-2.5, 2.5, n) ** 2) * r**6
    x = np.outer(q, r)
    F = 3 * (np.sin(x) - x * np.cos(x)) / x**3
    return (F**2 @ w) / w.sum()


MW, c = 14.3, 2.0
I0 = MW * c / 1385
Ip = I0 * sphere_pd(q, 18.7)
Ib = 0.030 + 2e-8 * q**-3
Is = Ib * (1 - 0.0015) + Ip
sig = 2e-4 * np.sqrt(Is * 0.03) + 1e-6
Is_n = Is + sig * rng.normal(size=q.size)
Ib_n = Ib + sig * rng.normal(size=q.size)
diff = Is_n - Ib_n * (1 - 0.0015)

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
ax.semilogy(q, Is_n, color=charts.line("protein"), lw=1.4, label="sample")
ax.semilogy(q, Ib_n, color=charts.line("neutral"), lw=1.4, ls="--", label="buffer")
ax.semilogy(q, np.clip(diff, 1e-6, None), color=charts.line("dna"), lw=1.4, label="difference (protein)")
ax.set_ylim(1e-5, 0.2)
ax.set_xlim(0, 0.35)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q / Å⁻¹", "I(q) / cm⁻¹")
charts.title(ax, "A   Sample minus buffer")

ax = axs[1]
for f, lab, tok in ((1.0, "correct", "dna"), (0.997, "buffer × 0.997", "negative"),
                    (1.003, "buffer × 1.003", "positive")):
    d = Is_n - f * Ib_n * (1 - 0.0015)
    ax.plot(q, q**2 * d * 1e4, color=charts.line(tok), lw=1.4, label=lab)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlim(0, 0.35)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "q / Å⁻¹", "q² I(q)  /  (10⁻⁴ cm⁻¹ Å⁻²)")
charts.title(ax, "B   A 0.3 % error in subtraction")

ax = axs[2]
rg = np.sqrt(0.6) * 18.7          # nominal Rg of the mean sphere
qg = np.linspace(0.008, 1.3 / rg, 60)
Ig = I0 * sphere_pd(qg, 18.7)
agg = 0.01 * 50 * I0 * np.exp(-(qg * 55.0) ** 2 / 3)
Sq = 1 - 0.18 * np.exp(-(qg * 30.0) ** 2)
cases = (("monodisperse", Ig, "dna"), ("+ 1 % aggregates", 0.99 * Ig + agg, "negative"),
         ("repulsion, S(q) < 1", Ig * Sq, "positive"))
for lab, y, tok in cases:
    ax.plot(qg**2 * 1e3, np.log(y), "o", ms=2.6, color=charts.line(tok), label=lab)
sl, ic = np.polyfit(qg[:30] ** 2, np.log(Ig[:30]), 1)
ax.plot(qg**2 * 1e3, ic + sl * qg**2, color=P.muted(), lw=0.9, ls=(0, (3, 2)),
        label=f"Guinier fit, Rg = {np.sqrt(-3 * sl):.1f} Å")
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q² / (10⁻³ Å⁻²)", "ln[I(q) / cm⁻¹]")
charts.title(ax, "C   Guinier diagnostics")
fig.tight_layout()
