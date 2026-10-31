"""Reynolds numbers of swimmers and the coasting distance of a sphere in water.
A: Re = vL/nu (nu = 1e-6 m^2/s) for swimmers from bacteria to whales, against body length;
the shaded band separates the viscous (Re < 1) from the inertial world.
B: coasting distance (valid while Re << 1, a below about 100 um) d = v0 * tau of a sphere of radius a and the density of water, started at
v0 = 2a per second and slowed by Stokes drag, tau = m / (6 pi eta a) = 2 rho a^2 / (9 eta)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
nu, eta, rho = 1e-6, 1e-3, 1e3
sw = [  # name, length (m), speed (m/s)
    ("E. coli", 2e-6, 3e-5, True), ("sperm (human)", 5e-5, 6e-5, False),
    ("Chlamydomonas", 1e-5, 1e-4, True), ("Paramecium", 2e-4, 1e-3, True),
    ("copepod", 1e-3, 1e-2, False), ("zebrafish larva", 4e-3, 2e-2, False),
    ("tadpole", 1e-2, 5e-2, False), ("goldfish", 0.1, 0.5, False),
    ("human swimmer", 1.8, 1.5, False), ("dolphin", 2.5, 8.0, False), ("blue whale", 25.0, 8.0, False),
]

fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.5))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.97, bottom=0.16, top=0.89)

ax = axs[0]
L = np.logspace(-6.5, 1.8, 50)
ax.axhspan(1e-7, 1, color=P.fill("bacterium"), alpha=0.3, lw=0)
for nm, l, v, it in sw:
    re = v * l / nu
    ax.plot(l, re, "o", ms=4.5, color=charts.line("animal" if l > 1e-3 else "bacterium"))
    lab = rf"$\it{{{nm.replace(' ', r'\ ').replace('.', '.')}}}$" if it else nm
    ax.text(l * 1.35, re / 1.6, lab, fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_ylim(1e-6, 1e9); ax.set_xlim(3e-7, 3e2)
ax.axhline(1, color=P.muted(), lw=0.7, ls="--")
ax.text(4e-7, 2, "Re = 1", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.text(1e-1, 1e-4, "viscous world", fontsize=bio.core.FONT["small"], color=P.ink(), ha="center")
charts.style_axes(ax, "body length L / m", r"Reynolds number $vL/\nu$")
charts.title(ax, r"A  From $10^{-5}$ to $10^{8}$")

ax = axs[1]
a = np.logspace(-9.5, -4, 200)
tau = 2 * rho * a**2 / (9 * eta)
d = 2 * a * tau
ax.plot(a * 1e6, d * 1e9, color=charts.line("dna"), lw=1.7)
for r, txt in ((1e-6, "bacterium"), (2.5e-9, "protein"), (1e-4, "Paramecium")):
    dd = 2 * r * 2 * rho * r**2 / (9 * eta)
    ax.plot(r * 1e6, dd * 1e9, "o", color=charts.line("blood"), ms=4)
    ax.text(r * 1e6 * 1.4, dd * 1e9 / 3, txt, fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axhline(0.1, color=P.muted(), lw=0.6, ls=":")
ax.text(2e-2, 0.15, "size of a water molecule (0.1 nm)", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.set_xscale("log"); ax.set_yscale("log")
charts.style_axes(ax, r"radius a / $\mu$m", "coasting distance / nm")
charts.title(ax, r"B  Stopping after the motor stops ($v_0 = 2a$ per s)")
