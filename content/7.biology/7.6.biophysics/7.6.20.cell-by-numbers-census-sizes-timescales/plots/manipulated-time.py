"""How cells beat the intrinsic time scales of diffusion and chemistry.

A: time to travel a distance x by diffusion, t = x^2/(2D) along one coordinate, for a small molecule
(D = 1000 um^2/s), a protein in cytoplasm (10 um^2/s) and a vesicle (0.1 um^2/s), and by directed
transport at constant speed, t = x/v, for kinesin-driven fast axonal transport (1 um/s) and slow
axonal transport (about 1 mm per day). Diffusion wins over short distances and loses over long ones;
the crossover x* = 2D/v is 20 um for a protein against a motor at 1 um/s. Vertical lines: a synaptic
cleft (20 nm), E. coli (2 um), a eukaryotic cell (20 um), the squid giant axon (10 cm) and a human
motor axon (1 m). B: half-lives of six reactions in water without enzyme (open circles) and with the
enzyme (ln 2 / kcat, filled circles), after Radzicka and Wolfenden (1995) and Wolfenden (2011); the
rate enhancements range from 10^6 to 10^17."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.8), gridspec_kw={"width_ratios": [1.2, 1]})
fig.subplots_adjust(wspace=0.6, left=0.07, right=0.98, bottom=0.15, top=0.88)

ax = axs[0]
x = np.logspace(-2, 6, 300)  # um
for D, name, tok in ((1000, "small molecule", "neutral"), (10, "protein in cytoplasm", "protein"),
                     (0.1, "vesicle", "vesicle")):
    ax.plot(x, x ** 2 / (2 * D), color=charts.line(tok), lw=1.4, label=f"diffusion, {name}")
for v, name, ls in ((1.0, "fast axonal transport (1 um/s)", "-"), (1e3 / 86400, "slow axonal transport (1 mm/day)", "--")):
    ax.plot(x, x / v, color=charts.line("dna"), lw=1.4, ls=ls, label=name)
marks = ((0.02, "synapse"), (2, "E. coli"), (20, "cell"), (1e5, "squid axon"), (1e6, "human axon"))
for xm, name in marks:
    ax.axvline(xm, color=P.muted(), lw=0.5, ls=":")
    lab = r"$\it{E.\ coli}$" if name == "E. coli" else name
    ax.text(xm * 1.15, 3e-7, lab, rotation=90, fontsize=bio.core.FONT["tiny"], color=P.ink(), va="bottom")
for t, lab in ((1, "1 s"), (3600, "1 h"), (86400 * 365, "1 yr")):
    ax.axhline(t, color=P.muted(), lw=0.5, ls=":")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-7, 1e13)
rt = ax.secondary_yaxis("right")
rt.set_yticks([1, 3600, 86400 * 365])
rt.set_yticklabels(["1 s", "1 h", "1 yr"])
rt.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "distance / µm", "time / s")
charts.title(ax, "A  Diffusion versus motors")

ax = axs[1]
rx = [  # name, uncatalyzed half-life (s), kcat (s^-1)
    ("OMP decarboxylase", 78e6 * 3.15e7, 39),
    ("staphylococcal nuclease", 1.3e5 * 3.15e7, 95),
    ("adenosine deaminase", 120 * 3.15e7, 370),
    ("triose phosphate isomerase", 1.9 * 86400, 4300),
    ("chorismate mutase", 7.4 * 3600, 50),
    ("carbonic anhydrase", 5.0, 1e6),
]
ys = np.arange(len(rx))[::-1]
for y, (name, t0, kcat) in zip(ys, rx):
    t1 = np.log(2) / kcat
    ax.plot([t1, t0], [y, y], color=P.muted(), lw=0.8)
    ax.plot(t0, y, "o", mfc="none", mec=charts.line("enzyme"), ms=6, mew=1.2)
    ax.plot(t1, y, "o", color=charts.line("enzyme"), ms=6)
    ax.text(np.sqrt(t0 * t1), y + 0.18, "10" + str(int(round(np.log10(t0 / t1)))).translate(
        str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")), ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_yticks(ys)
ax.set_yticklabels([r[0] for r in rx], fontsize=bio.core.FONT["tiny"])
ax.set_xscale("log")
ax.set_xlim(1e-7, 1e17)
ax.set_ylim(-0.6, len(rx) - 0.3)
ax.plot([], [], "o", mfc="none", mec=charts.line("enzyme"), ls="none", label="without enzyme")
ax.plot([], [], "o", color=charts.line("enzyme"), ls="none", label="with enzyme")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "half-life / s")
charts.title(ax, "B  Enzymes compress time")
