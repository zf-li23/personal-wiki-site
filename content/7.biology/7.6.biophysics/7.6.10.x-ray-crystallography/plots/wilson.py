# Wilson statistics from a random-atom model.
# 400 carbon atoms at random positions in an orthorhombic cell of 40 x 50 x 60 A (space group P1), all
# with an isotropic temperature factor B = 20 A^2; carbon scattering factors from the Cromer-Mann
# coefficients. Structure factors are computed for all reflections to d = 2.5 A.
# A: Wilson plot. ln(<I> / sum f0^2) in thin resolution shells against s^2 = (sin theta / lambda)^2 is a
#    straight line of slope -2B (dashed: the input B), so the overall temperature factor and the scale
#    of the data follow from a straight-line fit (fitted B printed).
# B: cumulative distribution N(z) of the normalized intensity z = I / <I> (shell averages), compared with
#    the acentric law 1 - exp(-z); the same atoms related by an inversion centre (P-1) follow the centric
#    law erf(sqrt(z/2)); averaging each intensity with an independent partner of the same shell mimics a
#    perfect hemihedral twin, 1 - (1 + 2z) exp(-2z), with too few weak reflections.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
rng = np.random.default_rng(0)

a, b, c = 40.0, 50.0, 60.0
dmin = 2.5
N = 400
B = 20.0
xyz = rng.uniform(0, 1, size=(N, 3))

cm_a = np.array([2.31, 1.02, 1.5886, 0.865])
cm_b = np.array([20.8439, 10.2075, 0.5687, 51.6512])
cm_c = 0.2156


def f_carbon(s2):
    return (cm_a[None, :] * np.exp(-cm_b[None, :] * s2[:, None])).sum(axis=1) + cm_c


hm, km, lm = int(a / dmin), int(b / dmin), int(c / dmin)
hkl = np.array([(h, k, l) for h in range(0, hm + 1) for k in range(-km, km + 1) for l in range(-lm, lm + 1)])
hkl = hkl[(hkl[:, 0] > 0) | ((hkl[:, 0] == 0) & ((hkl[:, 1] > 0) | ((hkl[:, 1] == 0) & (hkl[:, 2] > 0))))]
s2 = ((hkl[:, 0] / a) ** 2 + (hkl[:, 1] / b) ** 2 + (hkl[:, 2] / c) ** 2) / 4      # (sin theta / lambda)^2
keep = s2 <= 1 / (4 * dmin**2)
hkl, s2 = hkl[keep], s2[keep]


def structure_factors(frac, centric=False):
    F = np.zeros(len(hkl), complex)
    for i in range(0, len(frac), 50):
        ph = 2 * np.pi * hkl @ frac[i:i + 50].T
        F += (np.cos(ph) if centric else np.exp(1j * ph)).sum(axis=1) * (2 if centric else 1)
    return F


f0 = f_carbon(s2)
T = np.exp(-2 * B * s2)                       # exp(-B s^2) on F, squared on I
Iac = np.abs(structure_factors(xyz)) ** 2 * f0**2 * T
Ice = np.abs(structure_factors(xyz[: N // 2], centric=True)) ** 2 * f0**2 * T

edges = np.quantile(s2, np.linspace(0, 1, 21))
shell = np.clip(np.digitize(s2, edges) - 1, 0, 19)
sig = N * f0**2
mean_s2 = np.array([s2[shell == j].mean() for j in range(20)])
w_ac = np.array([(Iac / sig)[shell == j].mean() for j in range(20)])
yfit = np.log(w_ac)
sel = mean_s2 > 0.008
slope, icpt = np.polyfit(mean_s2[sel], yfit[sel], 1)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axs[0]
ax.plot(mean_s2, yfit, "o", color=charts.line("protein"), ms=5, label="shell averages")
xx = np.linspace(0, mean_s2.max() * 1.02, 50)
ax.plot(xx, icpt + slope * xx, color=charts.line("protein"), lw=1.3, label=f"fit: B = {-slope / 2:.1f} Å²")
ax.plot(xx, -2 * B * xx, color=muted, lw=1.0, ls=(0, (4, 2)), label="input: B = 20 Å²")
ax.legend(fontsize=8, frameon=False)
ax.set_title("A  Wilson plot", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, r"$s^2 = (\sin\theta/\lambda)^2$ / Å$^{-2}$", r"$\ln(\langle I\rangle / \sum f_0^2)$")


def normalize(I):
    z = np.empty_like(I)
    for j in range(20):
        m = shell == j
        z[m] = I[m] / I[m].mean()
    return z


z_ac = normalize(Iac)
z_ce = normalize(Ice)
z_tw = np.empty_like(z_ac)
for j in range(20):
    idx = np.flatnonzero(shell == j)
    partner = rng.permutation(idx)
    z_tw[idx] = 0.5 * (z_ac[idx] + z_ac[partner])
zz = np.linspace(0, 1, 101)
ax = axs[1]
for z, tok, name in ((z_ce, "dna", r"centric ($P\bar{1}$)"), (z_ac, "protein", r"acentric ($P1$)"),
                     (z_tw, "highlight", "perfect twin")):
    emp = np.array([(z <= q).mean() for q in zz])
    ax.plot(zz, emp, "o", ms=3, color=charts.line(tok), label=name)
ax.plot(zz, erf(np.sqrt(zz / 2)), color=charts.line("dna"), lw=1.2)
ax.plot(zz, 1 - np.exp(-zz), color=charts.line("protein"), lw=1.2)
ax.plot(zz, 1 - (1 + 2 * zz) * np.exp(-2 * zz), color=charts.line("highlight"), lw=1.2)
ax.legend(fontsize=8, frameon=False, loc="lower right")
ax.set_title("B  cumulative intensity distribution N(z)", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, r"$z = I/\langle I\rangle$", "N(z)")
fig.tight_layout()
