"""State-energy-weight tables for three two-state systems. A: a tension-gated channel (open state
enlarges the channel footprint by dA, and tension tau lowers its energy by tau*dA). B: a
voltage-gated channel (z gating charges cross the membrane field on opening). C: a receptor that
is empty or holds one ligand taken from a solution of chemical potential mu. In each case the open
(or bound) probability is the weight of that state divided by the sum of the two weights."""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
import wikibio as bio
from wikibio import neuro

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)

COLS = (0.0, 8.1, 16.2)
TITLES = ("Tension-gated channel", "Voltage-gated channel", "Ligand-receptor binding")
ENERGY = (
    (r"$\varepsilon_\mathrm{c}$", r"$\varepsilon_\mathrm{o} - \tau\,\Delta A$"),
    (r"$\varepsilon_\mathrm{c}$", r"$\varepsilon_\mathrm{o} - z e V$"),
    (r"$0$", r"$\varepsilon_\mathrm{b} - \mu$"),
)
WEIGHT = (
    (r"$\mathrm{e}^{-\beta\varepsilon_\mathrm{c}}$", r"$\mathrm{e}^{-\beta(\varepsilon_\mathrm{o} - \tau\Delta A)}$"),
    (r"$\mathrm{e}^{-\beta\varepsilon_\mathrm{c}}$", r"$\mathrm{e}^{-\beta(\varepsilon_\mathrm{o} - zeV)}$"),
    (r"$1$", "$\\mathrm{e}^{-\\beta(\\varepsilon_\\mathrm{b}-\\mu)}$\n$= c/K_\\mathrm{d}$"),
)
RESULT = (
    r"$p_\mathrm{o} = \dfrac{1}{1 + \mathrm{e}^{\beta(\Delta\varepsilon - \tau\Delta A)}}$",
    r"$p_\mathrm{o} = \dfrac{1}{1 + \mathrm{e}^{-ze(V - V_{1/2})/k_\mathrm{B}T}}$",
    r"$p_\mathrm{b} = \dfrac{c/K_\mathrm{d}}{1 + c/K_\mathrm{d}}$",
)
STATES = (("closed", "open"), ("closed", "open"), ("empty", "bound"))
ROW_Y = (6.2, 3.4)


def tension_channel(x, y, open_):
    neuro.patch(ax, x - 1.5, x + 1.5, y, labels=False, depth=0.85)
    neuro.channel(ax, x, y, ion=None, open=open_, token="channel", width=1.25 if open_ else 0.8, show_ion=False)
    for s in (-1, 1):
        bio.arrow(ax, (x + s * 1.15, y), (x + s * 1.85, y), kind="process", lw=1.1, head=0.16)
    bio.label(ax, (x + 1.95, y + 0.45), r"$\tau$", size="small", ha="left")


def voltage_channel(x, y, open_):
    neuro.patch(ax, x - 1.5, x + 1.5, y, labels=False, depth=0.85)
    neuro.channel(ax, x, y, ion="k", open=open_, show_ion=open_)
    yy = y + 0.33 if open_ else y - 0.33
    for s in (-1, 1):
        ax.add_patch(Circle((x + s * 0.62, yy), 0.15, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.7,
                            zorder=14))
        bio.label(ax, (x + s * 0.62, yy), "+", size="tiny", color=P.on_fill(), zorder=15)
    bio.label(ax, (x + 1.62, y + 0.6), "out", size="tiny", color=P.muted(), ha="left")
    bio.label(ax, (x + 1.62, y - 0.6), "in", size="tiny", color=P.muted(), ha="left")


def receptor(x, y, bound):
    ax.add_patch(FancyBboxPatch((x - 0.55, y - 0.75), 1.1, 1.0, boxstyle="round,pad=0,rounding_size=0.2",
                                facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.9, zorder=10))
    # binding pocket
    ax.add_patch(Circle((x, y + 0.25), 0.26, facecolor=P.surface(), edgecolor=P.edge("receptor"), lw=0.9, zorder=11))
    rng = np.random.default_rng(3)
    for _ in range(5):
        px, py = x + rng.uniform(-1.4, 1.4), y + rng.uniform(0.75, 1.05)
        ax.add_patch(Circle((px, py), 0.12, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"), lw=0.6, zorder=9))
    if bound:
        ax.add_patch(Circle((x, y + 0.25), 0.2, facecolor=P.fill("metabolite"), edgecolor=P.edge("metabolite"), lw=0.8,
                            zorder=12))


DRAW = (tension_channel, voltage_channel, receptor)

for k, x0 in enumerate(COLS):
    bio.panel(ax, "ABC"[k], (x0 + 0.1, 9.4))
    bio.label(ax, (x0 + 0.65, 9.4), TITLES[k], size="small", bold=True, ha="left")
    for head, xx in (("state", 1.9), ("energy", 4.6), ("weight", 6.6)):
        bio.label(ax, (x0 + xx, 8.55), head, size="tiny", color=P.muted())
    ax.plot([x0 + 0.3, x0 + 7.6], [8.25, 8.25], color=P.muted(), lw=0.6)
    for j, y in enumerate(ROW_Y):
        DRAW[k](x0 + 1.9, y, j == 1)
        bio.label(ax, (x0 + 0.2, y + 1.1), STATES[k][j], size="tiny", ha="left", color=P.muted())
        bio.label(ax, (x0 + 4.6, y), ENERGY[k][j], size="small")
        bio.label(ax, (x0 + 6.6, y), WEIGHT[k][j], size="small")
    ax.plot([x0 + 0.3, x0 + 7.6], [1.75, 1.75], color=P.muted(), lw=0.6)
    bio.label(ax, (x0 + 3.95, 0.85), RESULT[k], size="small")
