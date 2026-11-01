"""One law, many switches: two-state systems of the course driven by their conjugate variables.

Each curve is p = 1/(1 + exp(beta*dG)) with dG = dG0 - qX (Theorem 4.1.1), using the parameters of
the chapters. A: MscL opened by membrane tension, dG0 = 50 kBT, dA = 20 nm^2 (half-open near
10 mN/m, 7.6.4, 7.6.25). B: a voltage-gated channel with the Shaker gating charge z = 13 at 25 C,
against V - V_1/2 (7.6.4, 7.6.30). C: a TRPV1-like heat sensor with dH = 420 kJ/mol, half-open at
42 C (7.6.4). D: the P5ab RNA hairpin under force, transition near 14.5 pN with dx = 18 nm
(7.6.17). E: ligand binding as a two-state system in the variable ln c: a single site (Hill n = 1)
and an all-or-none tetramer (n = 4), 7.6.3-7.6.4. The 10-90 % widths 4.4 kBT/q are marked. F: all
curves fall on one logistic when plotted against the free-energy bias -beta*dG (for ligands, n ln(c/K)):
the conjugate charge q (area, gating charge, enthalpy/T, extension, number of ligands) sets the
sensitivity in physical units, and nothing else differs."""

import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT
kT = 4.1  # pN nm
R = 8.314


def logistic(x):
    return 1.0 / (1.0 + np.exp(-x))


fig, axs = plt.subplots(2, 3, figsize=(10.2, 6.0))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.09, top=0.93, wspace=0.32, hspace=0.55)
axs = axs.ravel()
collapse = []


def width_mark(ax, x50, w, unit, tok):
    ax.annotate("", (x50 - w / 2, 0.5), (x50 + w / 2, 0.5),
                arrowprops=dict(arrowstyle="<->", color=charts.line(tok), lw=0.8))
    ax.text(x50 + w / 2 + 0.05 * w, 0.42, f"10–90 %: {w:.1f} {unit}", fontsize=F["tiny"], color=P.ink(), va="top")


# A: tension
tau = np.linspace(6, 14, 300)
b = (20 * tau - 50 * kT) / kT  # -beta dG with tau in pN/nm = mN/m
ax = axs[0]
ax.plot(tau, logistic(b), color=charts.line("channel"), lw=1.6)
width_mark(ax, 50 * kT / 20, 4.4 * kT / 20, "mN/m", "channel")
charts.style_axes(ax, "membrane tension / (mN m⁻¹)", "open probability")
charts.title(ax, "A  MscL: tension")
collapse.append(("tension (MscL)", b[::25], "channel"))

# B: voltage
dV = np.linspace(-30, 30, 300)
b = 13 * dV / 25.7
ax = axs[1]
ax.plot(dV, logistic(b), color=charts.line("na"), lw=1.6)
width_mark(ax, 0.0, 4.4 * 25.7 / 13, "mV", "na")
charts.style_axes(ax, "V − V₁/₂ / mV", "open probability")
charts.title(ax, "B  Gating charge: voltage")
collapse.append(("voltage (z = 13)", b[::25], "na"))

# C: temperature
tC = np.linspace(28, 56, 300)
T = tC + 273.15
dH = 420e3
dS = dH / 315.15
b = -(dH - T * dS) / (R * T)
ax = axs[2]
ax.plot(tC, logistic(b), color=charts.line("drug"), lw=1.6)
width_mark(ax, 42.0, 4.4 * R * 315.15 ** 2 / dH, "K", "drug")
charts.style_axes(ax, "temperature / °C", "open probability")
charts.title(ax, "C  TRPV1-like: temperature")
collapse.append(("temperature (TRPV1)", b[::25], "drug"))

# D: force
f = np.linspace(11, 18, 300)
b = 18 * (f - 14.5) / kT
ax = axs[3]
ax.plot(f, logistic(b), color=charts.line("rna"), lw=1.6)
width_mark(ax, 14.5, 4.4 * kT / 18, "pN", "rna")
charts.style_axes(ax, "force / pN", "probability unfolded")
charts.title(ax, "D  RNA hairpin: force")
collapse.append(("force (P5ab)", b[::25], "rna"))

# E: ligand
c = np.logspace(-2, 2, 300)
ax = axs[4]
for n, ls in ((1, "-"), (4, "--")):
    ax.plot(c, c ** n / (1 + c ** n), color=charts.line("receptor"), lw=1.6, ls=ls, label=f"n = {n}: 10–90 % over {81 ** (1 / n):.0f}-fold")
    collapse.append((f"ligand, n = {n}", (n * np.log(c))[::25], "receptor"))
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=F["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "c / K", "fraction bound")
charts.title(ax, "E  Binding: ligand concentration")

# F: collapse
ax = axs[5]
x = np.linspace(-8, 8, 300)
ax.plot(x, logistic(x), color=P.ink(), lw=1.2, zorder=2)
marks = ["o", "s", "^", "D", "v", "P"]
for (lab, bb, tok), mk in zip(collapse, marks):
    sel = np.abs(bb) < 8
    ax.plot(bb[sel], logistic(bb[sel]), mk, ms=3.5, mfc=P.fill(tok), mec=P.edge(tok), mew=0.7, ls="none",
            label=lab, zorder=3)
ax.legend(frameon=False, fontsize=F["tiny"], labelcolor=P.ink(), loc="upper left", handletextpad=0.2)
charts.style_axes(ax, "bias −βΔG = β(qX − ΔG₀)", "probability")
charts.title(ax, "F  One curve")
for a in axs:
    a.set_ylim(-0.03, 1.03)
