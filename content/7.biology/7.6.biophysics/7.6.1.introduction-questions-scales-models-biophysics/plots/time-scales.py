# Time scales of life on a logarithmic axis from 1 fs to 4 Gyr (seconds on the axis, everyday units on top).
# Molecular events (bond vibration, water hydrogen-bond rearrangement, primary charge separation in a
# photosynthetic reaction centre, side-chain rotation, fast protein folding, enzyme turnover, action potential,
# motor step) lie below the axis; cellular, organismal and evolutionary times above it.
# Values are typical orders of magnitude.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
YEAR = 3.156e7
events_low = [
    (1e-14, "C–H bond\nvibration"),
    (1e-12, "H-bond rearrangement\nin water"),
    (3e-12, "charge separation in\nreaction centre"),
    (1e-9, "side-chain\nrotation"),
    (1e-6, "fastest\nprotein folding"),
    (1e-3, "enzyme turnover,\naction potential"),
    (1e-2, "kinesin step"),
    (1.0, "protein crosses\na eukaryotic cell"),
]
events_high = [
    (60.0, "transcribing\na 2 kb gene"),
    (1.2e3, "E. coli\ndivision"),
    (8.64e4, "human cell cycle,\ncircadian day"),
    (1.0e7, "red blood cell\nlifetime (4 months)"),
    (80 * YEAR, "human\nlifetime"),
    (5e3 * YEAR, "oldest\ntrees"),
    (1e6 * YEAR, "origin of\na species"),
    (3.8e9 * YEAR, "life on\nEarth"),
]

fig, ax = plt.subplots(figsize=(13.5, 3.6))
ax.set_xscale("log")
ax.set_xlim(3e-16, 5e17)
ax.set_ylim(-1.0, 1.0)
ax.axhline(0, color=P.ink(), lw=1.1)
for i, (t, txt) in enumerate(events_low):
    y = -0.35 if i % 2 == 0 else -0.7
    ax.plot([t, t], [0, y + 0.08], color=charts.line("protein"), lw=0.8)
    ax.plot([t], [0], "o", color=charts.line("protein"), ms=4.5, zorder=5)
    ax.text(t, y, txt, ha="center", va="top", fontsize=7, color=P.ink())
for i, (t, txt) in enumerate(events_high):
    y = 0.3 if i % 2 == 0 else 0.62
    ax.plot([t, t], [0, y - 0.04], color=charts.line("positive"), lw=0.8)
    ax.plot([t], [0], "o", color=charts.line("positive"), ms=4.5, zorder=5)
    if txt.startswith("E. coli"):
        ax.text(t, y, "$\\it{E.\\ coli}$\ndivision", ha="center", va="bottom", fontsize=7, color=P.ink())
    else:
        ax.text(t, y, txt, ha="center", va="bottom", fontsize=7, color=P.ink())
ax.set_xticks([1e-15, 1e-12, 1e-9, 1e-6, 1e-3, 1, 1e3, 1e6, 1e9, 1e12, 1e15])
ax.set_xticklabels(["1 fs", "1 ps", "1 ns", "1 µs", "1 ms", "1 s", "17 min", "12 d", "32 yr", "32 kyr", "32 Myr"])
ax.set_yticks([])
for s in ("left", "right", "top"):
    ax.spines[s].set_visible(False)
charts.style_axes(ax, "t (logarithmic scale)")
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.text(4e-16, -0.95, "molecular", fontsize=8, color=charts.line("protein"), weight="bold")
ax.text(4e-16, 0.85, "cellular to evolutionary", fontsize=8, color=charts.line("positive"), weight="bold")
fig.tight_layout()
