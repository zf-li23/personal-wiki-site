"""Goldman rectification: the GHK current-voltage relation of a single permeant ion against the
ohmic approximation I = g (V - E) with g the slope of the GHK curve at V = E (37 C, RT/F = 26.7 mV).
Currents are in units of P z^2 F^2 / (RT) times mM, so that I(V) = V ([C]i - [C]o exp(-zFV/RT)) /
(1 - exp(-zFV/RT)). A: K+ (140 mM inside, 5 mM outside, E = -89 mV). B: Na+ (12 mM inside, 145 mM
outside, E = +66 mV). C: the ratio of the GHK current to the ohmic current for the two ions (and for K+ with 20 mM outside),
as a function of the driving force V - E."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
RTF = 26.7
V = np.linspace(-120, 80, 2001)


def ghk(V, ci, co):
    v = V / RTF
    with np.errstate(divide="ignore", invalid="ignore"):
        I = V * (ci - co * np.exp(-v)) / (1 - np.exp(-v))
    return np.where(np.abs(v) < 1e-9, ci - co, I)


def ohmic(V, ci, co):
    E = RTF * np.log(co / ci)
    h = 1e-3
    g = (ghk(np.array([E + h]), ci, co) - ghk(np.array([E - h]), ci, co)) / (2 * h)
    return g * (V - E), E


fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.5))
fig.subplots_adjust(wspace=0.36, left=0.07, right=0.99, bottom=0.17, top=0.9)
for ax, (name, ci, co, tok, lim) in zip(axs[:2], [("K⁺", 140, 5, "k", 700), ("Na⁺", 12, 145, "na", 700)]):
    I = ghk(V, ci, co)
    Io, E = ohmic(V, ci, co)
    ax.axhline(0, color=P.muted(), lw=0.6)
    ax.plot(V, Io, color=P.muted(), lw=1.2, ls="--", label="ohmic, slope at $E$")
    ax.plot(V, I, color=charts.line(tok), lw=1.9, label="GHK")
    ax.plot([E], [0], "o", ms=4, color=P.ink())
    ax.text(E, -0.08 * lim, f"$E$ = {E:.0f} mV", ha="center", va="top", fontsize=FT["tiny"], color=P.ink())
    ax.set_ylim(-lim * 0.6, lim)
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(ax, "V / mV", "current (a.u.)")
    charts.title(ax, ("A  " if name == "K⁺" else "B  ") + name + " current")
ax = axs[2]
for name, ci, co, tok, ls in [("K⁺, 5 mM out", 140, 5, "k", "-"), ("K⁺, 20 mM out", 140, 20, "k", ":"), ("Na⁺", 12, 145, "na", "-")]:
    Io, E = ohmic(V, ci, co)
    d = V - E
    m = np.abs(d) > 3
    ax.plot(d[m], (ghk(V, ci, co)[m] / Io[m]), color=charts.line(tok), lw=1.7, ls=ls, label=name)
ax.axhline(1, color=P.muted(), lw=0.6)
ax.set_ylim(0, 6)
ax.set_xlim(-60, 80)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "driving force $V - E$ / mV", "GHK current / ohmic current")
charts.title(ax, "C  Error of the ohmic approximation")
