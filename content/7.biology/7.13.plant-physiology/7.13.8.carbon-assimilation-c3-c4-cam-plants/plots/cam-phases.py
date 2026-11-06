"""The four phases of crassulacean acid metabolism over one day (schematic numerical model).

Time runs from dusk (18 h) to the next dusk. Prescribed stomatal conductance g(t) (relative) and net CO2
uptake A(t): phase I (night) uptake by PEP carboxylase, peak about 6 umol m-2 s-1; phase II (early morning)
a short burst while both PEPC and rubisco are active; phase III (stomata closed) no exchange, malate is
decarboxylated; phase IV (late afternoon) stomata reopen and rubisco fixes CO2 directly. Vacuolar malate
M(t) is integrated from dM/dt = (PEPC uptake)/V - (decarboxylation)/V, with tissue water V = 1.8 L m-2 and
decarboxylation during phase III at the rate that empties the store by its end. The intercellular CO2 in
phase III, behind closed stomata, is drawn as a schematic peak of about 0.6 %. Illustrative values.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t = np.linspace(18, 42, 2401)
dt = (t[1] - t[0]) * 3600


def bump(t, a, b, sharp=0.6):
    return 1 / (1 + np.exp(-(t - a) / sharp)) * (1 - 1 / (1 + np.exp(-(t - b) / sharp)))


night = bump(t, 18.8, 29.6, 0.5)
uI = 6.0 * night * np.clip(np.sin(np.pi * (t - 18) / 12), 0.2, 1) ** 0.5
uII = 8.0 * np.exp(-0.5 * ((t - 30.6) / 0.45) ** 2)
uIV = 6.0 * bump(t, 39.0, 41.6, 0.4)
A = uI + uII + uIV
g = 0.04 + np.clip(A / 8.0, 0, 1) * 0.96
pepc = uI + 0.5 * uII
V = 1.8                                    # L water per m2 leaf
M = np.empty_like(t)
M[0] = 15.0
i3a, i3b = np.searchsorted(t, 31.5), np.searchsorted(t, 39.0)
for i in range(1, len(t)):
    M[i] = M[i - 1] + pepc[i - 1] * dt * 1e-6 / V * 1e3      # mM
Mpeak = M[i3a]
for i in range(i3a, len(t)):
    if t[i] < 39.0:
        M[i] = Mpeak - (Mpeak - 15.0) * (t[i] - t[i3a]) / (39.0 - t[i3a])
    else:
        M[i] = 15.0
ci = 150 + 6000 * bump(t, 32.2, 38.2, 0.7) + 120 * bump(t, 38.8, 42, 0.5)

phases = [(18, 30, "I"), (30, 31.5, "II"), (31.5, 39, "III"), (39, 42, "IV")]
shade = P.mix(P.muted(), P.surface(), 0.8)

fig, (a, b) = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True)
for ax in (a, b):
    ax.axvspan(18, 30, color=shade, lw=0)
    for x0, x1, name in phases:
        ax.axvline(x0, color=P.muted(), lw=0.6, ls=":")
a.plot(t, A, color=P.edge("plant"), lw=2, label="net CO$_2$ uptake $A$")
a2 = a.twinx()
a2.plot(t, g, color=P.edge("dna"), lw=1.6, ls="--", label="stomatal conductance (relative)")
for x0, x1, name in phases:
    a.text((x0 + x1) / 2, 8.6, name, ha="center", fontsize=10, weight="bold", color=P.ink())
a.set_ylim(-0.5, 9.5)
a2.set_ylim(0, 1.2)
a.set_ylabel("$A$ / µmol m$^{-2}$ s$^{-1}$")
a2.set_ylabel("$g_{\\mathrm{s}}$ (relative)", color=P.edge("dna"))
h1, l1 = a.get_legend_handles_labels()
h2, l2 = a2.get_legend_handles_labels()
a.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="center", bbox_to_anchor=(0.66, 0.42))
a.set_title("A  Gas exchange", loc="left", fontsize=10)

b.plot(t, M, color=P.edge("lipid"), lw=2, label="vacuolar malate")
b2 = b.twinx()
b2.plot(t, ci, color=P.edge("rna"), lw=1.6, ls="--", label="intercellular CO$_2$")
b.set_ylim(0, 170)
b2.set_ylim(0, 7000)
b.set_ylabel("Malate / mM")
b2.set_ylabel("$c_{\\mathrm{i}}$ / µmol mol$^{-1}$", color=P.edge("rna"))
h1, l1 = b.get_legend_handles_labels()
h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="upper left")
b.set_title("B  Malate store and internal CO$_2$", loc="left", fontsize=10)
b.set_xlim(18, 42)
b.set_xticks([18, 22, 26, 30, 34, 38, 42])
b.set_xticklabels(["18", "22", "2", "6", "10", "14", "18"])
b.set_xlabel("Time of day / h (shaded: night)")
for ax in (a, b):
    ax.grid(True, alpha=0.3)
fig.tight_layout()
