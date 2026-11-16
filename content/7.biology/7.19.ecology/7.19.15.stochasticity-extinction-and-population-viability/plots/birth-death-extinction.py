"""Demographic stochasticity in the linear birth-death process.

Each individual gives birth at rate b = 1 and dies at rate d = 0.8 (time in units of 1/b); the deterministic
model N(t) = N0 exp((b - d) t) grows. A: 25 realizations (Gillespie algorithm, seed 0) started from N0 = 5,
with the deterministic expectation (black); several die out early. B: probability of ultimate extinction
against N0: exact value (d/b)^N0 (line) and the fraction of 4000 simulations that went extinct before
reaching 200 individuals (points); also, for discrete generations, the Galton-Watson process with Poisson
offspring of mean R0 = 1.25 (= b/d), whose extinction probability q^N0 solves q = exp(R0 (q - 1)).
C: probability of extinction by time t for N0 = 1, 2, 5 (formula of the linear birth-death process).
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
b, d = 1.0, 0.8
rng = np.random.default_rng(0)


def path(n0, t_end):
    t, n = 0.0, n0
    ts, ns = [0.0], [n0]
    while n > 0 and t < t_end and n < 2000:
        t += rng.exponential(1.0 / ((b + d) * n))
        n += 1 if rng.random() < b / (b + d) else -1
        ts.append(t)
        ns.append(n)
    return np.array(ts), np.array(ns)


def extinct(n0, cap=200):
    n = n0
    while 0 < n < cap:
        n += 1 if rng.random() < b / (b + d) else -1
    return n == 0


fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
for k in range(25):
    ts, ns = path(5, 15.0)
    pa.step(ts, ns, where="post", color=Q.line_color("dna" if ns[-1] > 0 else "negative"), lw=0.8, alpha=0.8)
tt = np.linspace(0, 15, 100)
pa.plot(tt, 5 * np.exp((b - d) * tt), color=P.ink(), lw=1.8)
pa.set_yscale("symlog", linthresh=10)
pa.set_xlim(0, 15)
pa.set_ylim(0, 300)
C.style_axes(pa, "time (units of 1/b)", "population size N")
pa.text(0.4, 220, "red: extinct by t = 15", fontsize=FS["tiny"], color=Q.line_color("negative"))
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Sample paths, N0 = 5, b = 1, d = 0.8", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
N0 = np.arange(1, 21)
pb.plot(N0, (d / b) ** N0, color=Q.line_color("dna"), lw=1.6, label="birth-death: (d/b)^N0")
sim_n = [1, 2, 3, 5, 8, 12, 16, 20]
pb.plot(sim_n, [np.mean([extinct(n) for _ in range(4000)]) for n in sim_n], "o", ms=3.5,
        color=Q.line_color("negative"), label="simulation")
R0 = b / d
q = brentq(lambda x: np.exp(R0 * (x - 1)) - x, 1e-9, 1 - 1e-9)
pb.plot(N0, q ** N0, color=Q.line_color("protein"), lw=1.3, ls=(0, (4, 2)), label=f"Galton-Watson, Poisson R0 = {R0}")
pb.set_ylim(0, 1)
pb.set_xlim(0, 20.5)
C.style_axes(pb, "initial size N0", "probability of extinction")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Extinction despite growth", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.0, 1.6, 7.0, 6.8))
t = np.linspace(0.01, 30, 300)
E = np.exp((b - d) * t)
p0 = d * (1 - 1 / E) / (b - d / E)
for n0, tok in [(1, "negative"), (2, "atp"), (5, "dna")]:
    pc.plot(t, p0 ** n0, color=Q.line_color(tok), lw=1.6, label=f"N0 = {n0}")
    pc.axhline((d / b) ** n0, color=Q.line_color(tok), lw=0.6, ls=(0, (3, 2)))
pc.set_ylim(0, 1)
pc.set_xlim(0, 30)
C.style_axes(pc, "time (units of 1/b)", "P(extinct by t)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "C", (20.5, 9.6))
bio.label(ax, (22.0, 9.2), "Extinction happens early", size="small", bold=True, ha="left")
