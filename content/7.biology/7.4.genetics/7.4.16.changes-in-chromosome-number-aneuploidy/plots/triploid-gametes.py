"""Fertility of triploids. Each of the x trivalents sends one or two of its three homologues to a pole at
random; a gamete is euploid (x or 2x chromosomes) only if all trivalents send the same number, with
probability 2 (1/2)^x. Circles: simulation of 100 000 meioses for each x."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
x = np.arange(1, 16)
fig, ax = plt.subplots(figsize=(6.4, 3.8))
fig.subplots_adjust(left=0.14, right=0.97, bottom=0.16, top=0.93)
ax.semilogy(x, 2 * 0.5 ** x, color=charts.line("dna"), lw=1.5, label="2 (1/2)^x")
sim = []
for xx in x:
    k = rng.integers(1, 3, size=(100000, xx))
    s = k.sum(axis=1)
    sim.append(np.mean((s == xx) | (s == 2 * xx)))
ax.semilogy(x, np.maximum(sim, 1e-6), "o", mfc="none", color=charts.line("dna"), ms=4, label="simulation")
for xx, name in ((7, "wheat x = 7"), (11, "banana, watermelon x = 11")):
    ax.annotate(name, (xx, 2 * 0.5 ** xx), xytext=(8, 10), textcoords="offset points",
                fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xlim(0.5, 15.5)
charts.style_axes(ax, "basic chromosome number x", "fraction of euploid gametes")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
