"""The Levins metapopulation model and habitat destruction.

dp/dt = c p (1 - D - p) - e p, with p the fraction of all patches occupied, c the colonization and e the
extinction rate (time in units of 1/c) and D the fraction of patches destroyed (D = 0 in A and B).
A: dp/dt against p for four values of e/c: the stable equilibrium p* = 1 - e/c (filled points) exists only
for e/c < 1. B: deterministic trajectories for e/c = 0.5 from p0 = 0.05 and 0.95 (lines), and one
realization of a stochastic patch-occupancy model with 50 patches (each occupied patch goes extinct at
rate e; each empty patch is colonized at rate c times the fraction occupied; Gillespie algorithm, seed 2):
a finite network fluctuates around p*; it must eventually go extinct, but the mean time grows exponentially with the number of patches. C: equilibrium occupancy
p* = 1 - D - e/c against D for e/c = 0.2 and 0.4 (lines) and the fraction of patches that are suitable but
empty, which stays equal to e/c (dashed) until the metapopulation collapses at D = 1 - e/c.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
p = np.linspace(0, 1, 300)
for ec, tok in [(0.2, "dna"), (0.5, "enzyme"), (0.8, "protein"), (1.2, "negative")]:
    pa.plot(p, p * (1 - p) - ec * p, color=Q.line_color(tok), lw=1.6, label=f"e/c = {ec}")
    if ec < 1:
        pa.plot([1 - ec], [0], "o", ms=4.5, color=Q.line_color(tok))
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 1)
pa.set_ylim(-0.6, 0.45)
C.style_axes(pa, "fraction of patches occupied p", "dp/dt (units of c)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Phase line", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.5, 6.8))
ec = 0.5
t = np.linspace(0, 120, 600)
r = 1 - ec
for p0 in (0.05, 0.95):
    pt = (1 - ec) / (1 + ((1 - ec) / p0 - 1) * np.exp(-r * t))
    pb.plot(t, pt, color=Q.line_color("enzyme"), lw=1.6)
rng = np.random.default_rng(2)
n, k, tt = 50, 5, 0.0
ts, ks = [0.0], [k]
while tt < 400 and k > 0:
    col = (n - k) * k / n
    ext = ec * k
    tt += rng.exponential(1 / (col + ext))
    k += 1 if rng.random() < col / (col + ext) else -1
    ts.append(tt)
    ks.append(k)
pb.step(ts, np.array(ks) / n, where="post", color=Q.line_color("negative"), lw=0.8)
pb.axhline(1 - ec, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.set_xlim(0, 120)
pb.set_ylim(0, 1)
C.style_axes(pb, "time (units of 1/c)", "fraction occupied p")
pb.text(118, 0.93, "50 patches, stochastic", fontsize=FS["tiny"], color=Q.line_color("negative"), ha="right")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Approach to p* = 1 - e/c", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
D = np.linspace(0, 1, 300)
for ec, tok in [(0.2, "dna"), (0.4, "protein")]:
    ps = np.clip(1 - D - ec, 0, None)
    pc.plot(D, ps, color=Q.line_color(tok), lw=1.7, label=f"occupied, e/c = {ec}")
    empty = np.where(ps > 0, ec, 1 - D)
    pc.plot(D, empty, color=Q.line_color(tok), lw=1.0, ls=(0, (4, 2)), label=f"suitable but empty, e/c = {ec}")
pc.set_xlim(0, 1)
pc.set_ylim(0, 1)
C.style_axes(pc, "fraction of habitat destroyed D", "fraction of all patches")
pc.legend(frameon=False, fontsize=FS["tiny"] - 1, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Habitat destruction", size="small", bold=True, ha="left")
