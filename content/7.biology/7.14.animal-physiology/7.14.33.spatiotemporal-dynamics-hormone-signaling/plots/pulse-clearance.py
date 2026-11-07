# One-compartment pulse-clearance model: dC/dt = sum_n A delta(t - n T) - k C, k = ln 2 / t_half.
# A: the same mean secretion rate (A / T fixed) delivered as pulses at T / t_half = 1, 2 and 8; the
#    dotted line is the steady level of a continuous infusion at that rate, A / (k T).
#    Time is in units of the half-life.
# B: trough-to-peak ratio exp(-k T) = 2^(-T / t_half) and peak-to-mean ratio k T / (1 - exp(-k T)).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
k = np.log(2.0)  # half-life = 1 time unit
fig, ax = bio.canvas(24.0, 9.6)


def train(T, t, mean=1.0):
    A = mean * k * T  # keeps the mean concentration at `mean`
    n_last = np.floor(t / T)
    tau = t - n_last * T
    # periodic steady state reached from many earlier pulses
    return A * np.exp(-k * tau) / (1.0 - np.exp(-k * T))


bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 9.0, 6.9))
t = np.linspace(0, 24, 4000)
for T, tok in ((1, "dna"), (2, "positive"), (8, "rna")):
    pa.plot(t, train(T, t), color=charts.line(tok), lw=1.5)
pa.axhline(1.0, color=P.ink(), lw=0.9, ls=":")
pa.text(23.8, 1.06, "continuous infusion", fontsize=7.2, color=P.ink(), ha="right", va="bottom")
pa.text(0.3, 2.2, "T = t½", color=charts.line("dna"), fontsize=7.5)
pa.text(2.2, 3.15, "T = 2 t½", color=charts.line("positive"), fontsize=7.5)
pa.text(8.4, 5.4, "T = 8 t½", color=charts.line("rna"), fontsize=7.5)
pa.set_xlim(0, 24)
pa.set_ylim(0, 6.2)
charts.style_axes(pa, "time / t½", "C / mean")
charts.title(pa, "Same mean, different waveforms")

bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.9))
x = np.linspace(0.05, 10, 400)
pb.plot(x, 2.0 ** (-x), color=charts.line("dna"), lw=1.8)
pk = k * x / (1 - np.exp(-k * x))
pb2 = pb.twinx()
pb2.plot(x, pk, color=charts.line("rna"), lw=1.8, ls="--")
for xv in (1, 2, 8):
    pb.scatter([xv], [2.0 ** (-xv)], s=24, color=charts.line("dna"), zorder=5)
    pb.text(xv + 0.2, 2.0 ** (-xv) + 0.03, f"{2.0 ** (-xv):.3g}", fontsize=7.2, color=charts.line("dna"))
pb.text(3.2, 0.32, "trough / peak = 2^(−T/t½)", color=charts.line("dna"), fontsize=7.5)
pb2.text(9.8, 6.3, "peak / mean", color=charts.line("rna"), fontsize=7.5, ha="right", va="bottom")
pb.set_xlim(0, 10)
pb.set_ylim(0, 1.0)
pb2.set_ylim(0, 8)
charts.style_axes(pb, "pulse interval T / t½", "trough / peak")
charts.style_axes(pb2, None, "peak / mean", box=True)
pb2.spines["top"].set_visible(False)
pb2.spines["left"].set_visible(False)
charts.title(pb, "Pulsatility is set by T / t½")
