# The nuclear Dorsal gradient and its readout. A: a transverse section of the blastoderm at cycle 14 (dorsal up);
# nuclear Dorsal (blue) is highest at the ventral midline. Bands outside the embryo: twist/snail (mesoderm, red),
# vnd and rhomboid (ventral neuroectoderm, orange), sog (lateral neuroectoderm, purple), dpp and zen (dorsal
# ectoderm, yellow), which Dorsal represses. B: the gradient fitted as a Gaussian, c(s) = exp(-s^2 / 2 sigma^2) + B
# with sigma = 0.15 and baseline B = 0.05 (s = 0 ventral, 1 dorsal midline), on a log scale; each target is switched on
# above its own threshold (high for snail, low for sog), and dpp/zen are repressed wherever Dorsal is present above a
# low threshold. The positions of the boundaries follow Formula 14.5.1.
import numpy as np
import wikibio as bio
from wikibio import bodyaxes as BA
from wikibio import charts as C

P = bio.P
sig, B = 0.15, 0.05
g = lambda s: np.exp(-s ** 2 / (2 * sig ** 2)) + B
fig, ax = bio.canvas(22.0, 9.4)
bio.panel(ax, "A", (0.2, 9.2))
xs = BA.FlyCrossSection(ax, (4.8, 4.6), 2.5, n=44, values=lambda s: (g(s) - B) / 1.0, token="dna", cells=True)
xs.domain(0.0, 0.22, "muscle", ring=0)
xs.domain(0.22, 0.34, "drug", ring=0)
xs.domain(0.22, 0.55, "protein", ring=1)
xs.domain(0.6, 1.0, "highlight", ring=0)
bio.label(ax, (4.8, 8.55), "Dorsal side", size="small", color=P.muted())
bio.label(ax, (4.8, 0.45), "Ventral midline", size="small", color=P.muted())
keys = [("muscle", "twist, snail"), ("drug", "vnd, rhomboid"), ("protein", "sog"), ("highlight", "dpp, zen, tolloid")]
for k, (tok, txt) in enumerate(keys):
    y = 8.4 - k * 0.55
    ax.add_patch(bio.core.FancyBboxPatch((9.0, y - 0.15), 0.5, 0.3, boxstyle="round,pad=0,rounding_size=0.06",
                                         facecolor=P.fill(tok), edgecolor=P.edge(tok), zorder=12))
    bio.label(ax, (9.7, y), txt, size="tiny", italic=True, ha="left")

bio.panel(ax, "B", (12.0, 9.2))
pa = C.axes_at(ax, (13.4, 1.4, 7.8, 6.4))
s = np.linspace(0, 1, 300)
pa.semilogy(s, g(s), color=C.line("dna"), lw=2.0)
for th, tok, name in [(0.38, "muscle", "snail"), (0.12, "drug", "vnd"), (0.054, "protein", "sog")]:
    pa.axhline(th, color=C.line(tok), lw=0.9, ls=(0, (3, 2)))
    sb = sig * np.sqrt(2 * np.log(1 / (th - B)))
    pa.plot([sb], [th], "o", color=C.line(tok), ms=4)
    pa.text(0.98, th * 1.08, name + " on above", fontsize=bio.core.FONT["tiny"], color=C.line(tok), ha="right", style="italic")
pa.set_xlim(0, 1)
pa.set_ylim(0.03, 1.3)
C.style_axes(pa, "s (ventral midline 0 → dorsal midline 1)", "nuclear Dorsal (relative)")
