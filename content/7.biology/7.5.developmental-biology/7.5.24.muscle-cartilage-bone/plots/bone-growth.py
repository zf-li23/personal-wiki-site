"""Height and height velocity of a boy (Preece-Baines model 1), and the growth-plate relation v = n l."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
h1, ht, s0, s1, th = 175.0, 163.0, 0.11, 1.24, 14.6
t = np.linspace(2, 20, 400)
h = h1 - 2 * (h1 - ht) / (np.exp(s0 * (t - th)) + np.exp(s1 * (t - th)))
v = np.gradient(h, t)
fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.6))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.86, wspace=0.32)
a = axs[0]
a.plot(t, h, color=charts.line("dna"), lw=1.8)
charts.style_axes(a, "age (years)", "height (cm)")
charts.title(a, "A  Height")
b = axs[1]
b.plot(t, v, color=charts.line("drug"), lw=1.8)
i = np.argmax(v * (t > 10))
b.plot(t[i], v[i], "o", color=charts.line("drug"), ms=4)
b.text(t[i] + 0.4, v[i], "peak %.1f cm/yr at %.1f yr" % (v[i], t[i]), fontsize=FT["tiny"], color=P_.ink(), va="center")
b.set_ylim(0, 12)
charts.style_axes(b, "age (years)", "velocity (cm/yr)")
charts.title(b, "B  Height velocity")
c = axs[2]
n = np.linspace(0, 3, 50)
for l, tok in ((20, "dna"), (30, "protein"), (40, "drug")):
    c.plot(n, n * l * 365 / 1e4, color=charts.line(tok), lw=1.6, label="l = %d $\\mu$m" % l)
c.axhspan(0.8, 2.0, color=P_.light("highlight"), lw=0)
c.text(0.1, 1.4, "distal femur", fontsize=FT["tiny"], color=P_.ink())
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(c, "new cells per column per day n", "growth of one plate (cm/yr)")
charts.title(c, "C  v = n l")
