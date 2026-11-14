"""Sexual conflict over mating rate and the escalation of persistence and resistance (after Arnqvist and Rowe 2005).

A: female fitness as a function of her mating rate m, W_f(m) = 2 (1 - exp(-m)) - 0.5 m (benefits of sperm and
nuptial gifts saturate, harm from mating grows linearly), is maximal at m_f = ln 4. A male gains from every
extra mating with a female, W_m = ln m, so males favor higher rates than females.
B, C: coevolution of a male persistence trait x and a female resistance trait y, with mating rate
m = exp(x - y). Each trait climbs its own fitness gradient minus a cost of the trait (0.5 x^2 / 2 for males,
0.2 y^2 / 2 for females): dx/dt = 1 - 0.5 x, dy/dt = -m W_f'(m) - 0.2 y. Both traits escalate from zero to
costly equilibrium levels (B), while the mating rate changes much less and settles above the female optimum (C).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT


def wf(m):
    return 2 * (1 - np.exp(-m)) - 0.5 * m


def dwf(m):
    return 2 * np.exp(-m) - 0.5


mf = np.log(4)
fig, ax = bio.canvas(33.0, 10.5)

pa = Ch.axes_at(ax, (2.4, 1.8, 7.6, 7.6))
m = np.linspace(0.01, 5, 300)
pa.plot(m, wf(m), color=Ch.line("rna"), lw=1.9)
pa.plot(m, 0.25 * np.log(m) + 0.6, color=Ch.line("dna"), lw=1.9)
pa.axvline(mf, color=Ch.line("rna"), lw=0.8, ls=(0, (3, 2)))
pa.text(mf + 0.08, -0.6, "female optimum $m_f$", fontsize=FS["tiny"], color=Ch.line("rna"))
pa.text(4.9, 0.92, "female fitness", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right", va="top")
pa.text(4.9, 1.1, "male gain (rescaled)", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right", va="bottom")
pa.set_xlim(0, 5)
pa.set_ylim(-0.7, 1.4)
Ch.style_axes(pa, "mating rate $m$", "fitness")
Ch.title(pa, "Conflict over mating rate")
bio.panel(ax, "A", (0.2, 10.2))

dt, n = 0.02, 2500
x = y = 0.0
xs, ys, ms = [], [], []
for _ in range(n):
    mm = np.exp(x - y)
    x, y = x + dt * (1 - 0.5 * x), y + dt * (-mm * dwf(mm) - 0.2 * y)
    xs.append(x)
    ys.append(y)
    ms.append(mm)
t = np.arange(n) * dt

pb = Ch.axes_at(ax, (13.4, 1.8, 7.8, 7.6))
pb.plot(t, xs, color=Ch.line("dna"), lw=1.9, label="male persistence $x$")
pb.plot(t, ys, color=Ch.line("rna"), lw=1.9, label="female resistance $y$")
pb.set_xlim(0, t[-1])
pb.set_ylim(-0.3, 2.4)
Ch.style_axes(pb, "time (arbitrary units)", "trait value")
Ch.title(pb, "Both sexes escalate costly traits")
leg = pb.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
for txt in leg.get_texts():
    txt.set_color(P.ink())
bio.panel(ax, "B", (11.3, 10.2))

pc = Ch.axes_at(ax, (24.6, 1.8, 7.8, 7.6))
pc.plot(t, ms, color=Ch.line("protein"), lw=1.9)
pc.axhline(mf, color=Ch.line("rna"), lw=0.8, ls=(0, (3, 2)))
pc.text(t[-1] * 0.97, mf - 0.05, "female optimum", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right",
        va="top")
pc.set_xlim(0, t[-1])
pc.set_ylim(0, 2.5)
Ch.style_axes(pc, "time (arbitrary units)", "mating rate $m = \\mathrm{e}^{x-y}$")
Ch.title(pc, "Mating rate stays above the female optimum")
bio.panel(ax, "C", (22.5, 10.2))
