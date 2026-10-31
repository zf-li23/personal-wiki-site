"""Osmotic pressure and activity of concentrated hemoglobin (0 degC; M = 64.5 kDa, hard-sphere
diameter 5.8 nm, volume V = 102 nm^3). A: osmotic pressure against concentration: ideal (van 't
Hoff), lattice model Pi = -(kB T/nu) ln(1 - c nu) with lattice cell volume nu = 2V and 3V, and the
hard-sphere fluid (Carnahan-Starling equation of state, equivalent to Boltzmann's virial series
for these densities), which describes the measurements of Ross and Minton (1977) with this single
size parameter. B: activity coefficient of hemoglobin in its own solution from the same hard-sphere
model, ln gamma = (8 phi - 9 phi^2 + 3 phi^3)/(1 - phi)^3: at the 330 g/L of the red-cell interior
the effective concentration is one to two hundred times the actual one."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
kT = 1.380649e-23 * 273.15
NA = 6.02214076e23
M, d = 64.5, 5.8e-9
V = np.pi * d**3 / 6
c = np.linspace(1, 350, 300)  # g/L
n = c / (M * 1e3) * NA * 1e3  # c g/L = c kg/m^3; M kg/mol = 64.5
phi = n * V

fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.17, top=0.87)
ax = axs[0]
ax.plot(c, n * kT / 1e3, color=P.muted(), lw=1.0, ls="--", label="ideal (van 't Hoff)")
for f, ls in ((2, ":"), (3, "-.")):
    nu = f * V
    x = np.where(n * nu < 0.999, n * nu, np.nan)
    ax.plot(c, -kT / nu * np.log(1 - x) / 1e3, color=charts.line("dna"), lw=1.1, ls=ls, label=rf"lattice, $\nu = {f}V$")
Z = (1 + phi + phi**2 - phi**3) / (1 - phi) ** 3
ax.plot(c, n * kT * Z / 1e3, color=charts.line("blood"), lw=1.9, label="hard spheres")
ax.set_ylim(0, 60)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "hemoglobin / (g/L)", "osmotic pressure / kPa")
charts.title(ax, "A  Nonideal osmotic pressure")

ax = axs[1]
lng = (8 * phi - 9 * phi**2 + 3 * phi**3) / (1 - phi) ** 3
ax.plot(c, np.exp(lng), color=charts.line("blood"), lw=1.9)
ax.axvline(330, color=P.muted(), lw=0.7, ls=":")
ax.text(320, 2, "red cell", rotation=90, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="right")
ax.set_yscale("log")
charts.style_axes(ax, "hemoglobin / (g/L)", r"activity coefficient $\gamma$")
charts.title(ax, "B  Effective concentration")
