"""Interaction energies between molecular groups against distance, in units of kBT at 25 C.
A: magnitudes on log-log axes: two unit charges in vacuum and in water (1/r), a unit charge and a
water dipole aligned in vacuum (1/r^2), two aligned water dipoles in vacuum (1/r^3), the
thermally averaged (Keesom) dipole-dipole attraction and the London dispersion attraction of two
methane molecules (1/r^6); the dotted line marks kBT. B: the Lennard-Jones potential of two
aliphatic carbon atoms (well depth 0.16 kBT at r_m = 0.40 nm) and the attraction of two
opposite unit charges in water, bare and screened by 150 mM salt."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
kT = 1.380649e-23 * 298.15
e = 1.602176634e-19
k_e = 8.9875517923e9
p_w = 1.85 * 3.33564e-30  # water dipole, C m
eps_w = 78.4
lB_vac = e ** 2 * k_e / kT * 1e9  # nm
lD = 0.785  # nm at 150 mM

r = np.logspace(np.log10(0.25), 1, 400)  # nm
rm = r * 1e-9
curves = (
    (lB_vac / r, "blood", r"charge–charge, vacuum ($1/r$)", "-"),
    (lB_vac / eps_w / r, "dna", r"charge–charge, water ($1/r$)", "-"),
    (e * p_w * k_e / (kT * rm ** 2), "drug", r"charge–dipole, vacuum ($1/r^2$)", "-"),
    (2 * p_w ** 2 * k_e / (kT * rm ** 3), "enzyme", r"dipole–dipole aligned ($1/r^3$)", "-"),
    (2 / 3 * (p_w ** 2 * k_e) ** 2 / (kT ** 2 * rm ** 6), "protein", r"dipole–dipole, Keesom ($1/r^6$)", "--"),
    (0.75 * 12.6 * (2.6e-3) ** 2 / 0.025693 / r ** 6, "neutral", r"dispersion, CH$_4$–CH$_4$ ($1/r^6$)", "--"),
)

fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.3), gridspec_kw=dict(width_ratios=(1.25, 1)))
fig.subplots_adjust(wspace=0.3, left=0.07, right=0.98, bottom=0.3, top=0.92)

ax = axs[0]
for u, tok, lab, ls in curves:
    ax.plot(r, u, color=charts.line(tok), lw=1.6, ls=ls, label=lab)
ax.axhline(1, color=P.muted(), lw=0.7, ls=":")
ax.text(5.5, 1.25, r"$k_\mathrm{B}T$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-4, 400)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"] - 0.4, labelcolor=P.ink(), loc="upper center",
          bbox_to_anchor=(0.5, -0.17), ncol=2)
charts.style_axes(ax, r"distance $r$ / nm", r"$|U|$ / $k_\mathrm{B}T$")
charts.title(ax, "A  How fast interactions fall off")

ax = axs[1]
rr = np.linspace(0.3, 1.5, 400)
eps_lj, r_m = 0.16, 0.40
u_lj = eps_lj * ((r_m / rr) ** 12 - 2 * (r_m / rr) ** 6)
ax.plot(rr, u_lj * 10, color=charts.line("neutral"), lw=1.8, label=r"Lennard-Jones C$\cdots$C ($\times 10$)")
ax.plot(rr, -lB_vac / eps_w / rr, color=charts.line("dna"), lw=1.6, label="opposite charges, water")
ax.plot(rr, -lB_vac / eps_w / rr * np.exp(-rr / lD), color=charts.line("dna"), lw=1.2, ls="--", label="screened, 150 mM")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.axhline(-1, color=P.muted(), lw=0.6, ls=":")
ax.axvline(r_m, color=P.muted(), lw=0.5, ls=":")
ax.text(r_m + 0.01, 1.6, r"$r_\mathrm{m}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(1.25, -0.88, r"$-k_\mathrm{B}T$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_ylim(-3, 2)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper center",
          bbox_to_anchor=(0.5, -0.17), ncol=1)
charts.style_axes(ax, r"$r$ / nm", r"$U$ / $k_\mathrm{B}T$")
charts.title(ax, "B  Contact versus long range")
