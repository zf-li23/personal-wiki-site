"""Amino acid differences in alpha-globin between shark, carp, dog and human (percent of sites; data from
Futuyma & Kirkpatrick (2017), Fig. 7.17) against the age of the common ancestor given there (440 Mya for
shark versus bony vertebrates, 400 Mya for carp versus tetrapods, 70 Mya for dog versus human). Open dots:
proportion p of differing sites; filled dots: Poisson-corrected distance -ln(1 - p); line: least-squares line
through the origin for the corrected distance."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
pairs = [("shark-human", 440, 0.53), ("shark-dog", 440, 0.57), ("shark-carp", 440, 0.59),
         ("carp-human", 400, 0.49), ("carp-dog", 400, 0.48), ("dog-human", 70, 0.16)]
fig, ax = plt.subplots(figsize=(6.4, 4.0))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.14, top=0.9)
t = np.array([x[1] for x in pairs], float)
p = np.array([x[2] for x in pairs])
d = -np.log(1 - p)
ax.scatter(t, p, s=30, facecolor=P.surface(), edgecolor=charts.line("dna"), lw=1.2, zorder=4,
           label="proportion different, $p$")
ax.scatter(t, d, s=30, color=charts.line("rna"), zorder=4, label="Poisson distance $-\\ln(1 - p)$")
slope = (t @ d) / (t @ t)
tt = np.linspace(0, 480, 10)
ax.plot(tt, slope * tt, color=charts.line("rna"), lw=1, ls="--")
for name, ti, pi in pairs:
    if name in ("shark-carp", "carp-dog", "dog-human"):
        ax.annotate(name.replace("-", "–"), (ti, -np.log(1 - pi)), xytext=(6, 2), textcoords="offset points",
                    fontsize=FT["tiny"], color=P.ink())
ax.set_xlim(0, 480)
ax.set_ylim(0, 1.0)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "age of common ancestor (Mya)", "difference per site")
charts.title(ax, "Alpha-globin divergence and time")
