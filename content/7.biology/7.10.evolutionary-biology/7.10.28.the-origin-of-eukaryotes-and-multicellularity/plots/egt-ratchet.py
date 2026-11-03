"""Endosymbiotic gene transfer as a one-way ratchet (simulated, illustrative parameters): 1000 genes; per Myr
each lost with p 0.002 or transferred to the nucleus (organelle copy lost) with p 0.0005; 40 genes cannot leave."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
G, KEEP, T, RUNS = 1000, 40, 3000, 200
pl, pt = 0.002, 0.0005
t = np.arange(T + 1)
org = np.zeros((RUNS, T + 1)); nuc = np.zeros_like(org); lost = np.zeros_like(org)
for r in range(RUNS):
    state = np.zeros(G, int)            # 0 organelle, 1 nucleus, 2 lost
    movable = np.arange(G) >= KEEP
    org[r, 0] = G
    for k in range(1, T + 1):
        inorg = (state == 0) & movable
        u = rng.random(G)
        state[inorg & (u < pl)] = 2
        state[inorg & (u >= pl) & (u < pl + pt)] = 1
        org[r, k] = np.sum(state == 0); nuc[r, k] = np.sum(state == 1); lost[r, k] = np.sum(state == 2)
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8)); bio.panel(ax, "B", (12.2, 8.8))
pa = charts.axes_at(ax, (2.0, 1.6, 9.2, 6.6)); pb = charts.axes_at(ax, (14.2, 1.6, 9.2, 6.6))
for arr, tok, lab in ((org, "chloroplast", "in organelle"), (nuc, "nucleus", "transferred to nucleus"),
                      (lost, "neutral", "lost")):
    pa.plot(t, arr.mean(0), color=charts.line(tok), lw=1.8, label=lab)
pa.set_xlim(0, T); pa.set_ylim(0, G)
charts.style_axes(pa, "time since endosymbiosis (Myr)", "number of genes")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
for r in range(12):
    pb.plot(t, org[r], color=charts.line("chloroplast"), lw=0.6, alpha=0.6)
pb.axhline(KEEP, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.text(T, KEEP * 1.15, "genes that cannot leave (40)", fontsize=FT["tiny"], color=P.muted(), ha="right")
pb.set_yscale("log"); pb.set_xlim(0, T); pb.set_ylim(20, 1200)
charts.style_axes(pb, "time since endosymbiosis (Myr)", "genes in organelle (log scale)")
