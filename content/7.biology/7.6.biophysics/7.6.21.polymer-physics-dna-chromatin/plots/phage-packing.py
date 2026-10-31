"""Packing DNA into a phage capsid: the inverse-spool model.

The packed DNA is a spool of hoops wound from the capsid wall inward, hexagonally packed with
interaxial spacing d_s, in a cylindrical capsid of inner radius R and height z. Free energy
G(d_s, L) = G_bend + G_int: bending, G_bend = -(pi lp kBT z/(sqrt(3) d_s^2)) ln(1 - sqrt(3) d_s^2 L /
(2 pi z R^2)) with lp = 50 nm, and the measured repulsion between hexagonally packed DNA helices,
an osmotic pressure Pi = F0 exp(-d_s/c) with c = 0.27 nm and F0 = 55000 pN/nm^2 (Rau and Parsegian;
monovalent salt with a little Mg2+), which integrates to G_int = sqrt(3) F0 (c^2 + c d_s) L exp(-d_s/c).
For each packed length L, d_s minimizes G; the resisting force is F = dG/dL. Capsids:
phi29 (19.3 kb; R = 19.4 nm, z = 34 nm) and lambda (48.5 kb; R = 27.5 nm, z = 36.7 nm, a cylinder of
the volume of its roughly spherical capsid). A: DNA packing fraction (genome volume at 1 nm^3 per bp
over container volume) for a phage, the E. coli nucleoid, a human sperm head and a human nucleus.
B: interaxial spacing against the fraction packed. C: force resisting packaging and internal pressure
(right axis, at full packing); the dotted line marks the stall force of the phi29 motor (about 57 pN)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import wikibio as bio
from wikibio import charts

P = bio.P
KT, LP, F0, C = 4.11, 50.0, 55000.0, 0.27


def G(ds, L, R, z):
    arg = 1 - np.sqrt(3) * ds ** 2 * L / (2 * np.pi * z * R ** 2)
    gb = -np.pi * LP * KT * z / (np.sqrt(3) * ds) * np.log(arg)
    gc = np.sqrt(3) * F0 * (C ** 2 + C * ds) * L * np.exp(-ds / C)
    return gb + gc


def model(R, z, bp):
    Ls = np.linspace(0.04, 1.0, 60) * bp * 0.34
    res = []
    for L in Ls:
        dmax = np.sqrt(2 * np.pi * z * R ** 2 / (np.sqrt(3) * L)) * 0.9999
        r = minimize_scalar(lambda d: G(d, L, R, z), bounds=(1.5, min(dmax, 20.0)), method="bounded")
        res.append((r.x, r.fun))
    ds, g = np.array(res).T
    return Ls / Ls[-1], ds, np.gradient(g, Ls)


fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.5), gridspec_kw={"width_ratios": [1.0, 1.0, 1.15]})
fig.subplots_adjust(wspace=0.42, left=0.07, right=0.93, bottom=0.2, top=0.87)
ax = axs[0]
names = ["phage lambda", r"$\it{E.\ coli}$ nucleoid", "human sperm", "human nucleus"]
nu = [0.6, 0.1, 0.02, 0.002]
ax.barh(range(4)[::-1], nu, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8)
ax.set_yticks(range(4)[::-1])
ax.set_yticklabels(names, fontsize=bio.core.FONT["tiny"])
ax.set_xscale("log")
ax.set_xlim(1e-3, 1)
charts.style_axes(ax, "packing fraction")
charts.title(ax, "A  Compaction")

for name, R, z, bp, tok in (("phi29", 19.4, 34.0, 19300, "protein"), ("lambda", 27.5, 36.7, 48500, "dna")):
    f, ds, F = model(R, z, bp)
    axs[1].plot(100 * f, ds, color=charts.line(tok), lw=1.4, label=name)
    axs[2].plot(100 * f, F, color=charts.line(tok), lw=1.4, label=name)
    p_atm = F[-1] / (np.sqrt(3) / 2 * ds[-1] ** 2) * 1e6 / 101325
    axs[2].text(101, F[-1], f"{p_atm:.0f} atm", fontsize=bio.core.FONT["tiny"], color=charts.line(tok), va="center")
axs[1].set_ylim(2, 8)
axs[1].legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(axs[1], "genome packaged / %", r"interaxial spacing $d_{\mathrm{s}}$ / nm")
charts.title(axs[1], "B  Spacing")
axs[2].axhline(57, color=P.muted(), lw=0.7, ls=":")
axs[2].text(3, 59, "phi29 motor stall force", fontsize=bio.core.FONT["tiny"], color=P.ink())
axs[2].set_xlim(0, 100)
axs[2].set_ylim(0, 70)
axs[2].legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(axs[2], "genome packaged / %", "resisting force / pN")
charts.title(axs[2], "C  Force on the motor")
