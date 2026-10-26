# Two ways of dissecting a class II promoter (idealized values, not measured data).
# A: linker scanning of the HSV thymidine kinase promoter (after McKnight and Kingsbury 1982). Each bar is one
# mutant in which a 10 bp block is replaced by a linker; height = transcription relative to wild type. Blocks
# overlapping the TATA box (about -30), the proximal GC box (about -50), the CCAAT box (about -85) and the distal
# GC box (about -105) reduce transcription; the others do not. Values are rounded illustrations.
# B: start sites mapped by S1 protection for the SV40 early promoter with and without the TATA box (after
# Benoist and Chambon 1981). Wild type: a sharp peak at +1; TATA deleted: the same total signal spread over
# tens of base pairs (modeled as a broad distribution with a few weak preferred sites).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19.0, 8.2)

# ---- A: linker scan
a = C.axes_at(ax, (1.5, 2.1, 7.4, 4.6))
starts = np.arange(-120, 10, 10)
rel = {-120: 100, -110: 38, -100: 45, -90: 30, -80: 72, -70: 95, -60: 28, -50: 40, -40: 90, -30: 6, -20: 85,
       -10: 100, 0: 95}
vals = np.array([rel[s] for s in starts])
cols = [P.fill("negative") if v < 60 else P.fill("neutral") for v in vals]
edges = [C.line("negative") if v < 60 else C.line("neutral") for v in vals]
a.bar(starts + 5, vals, width=8.6, color=cols, edgecolor=edges, lw=0.8)
a.axhline(100, color=P.muted(), lw=0.7, ls=(0, (2, 2)))
a.set_xlim(-122, 12)
a.set_ylim(0, 118)
a.set_xticks([-120, -100, -80, -60, -40, -20, 0], ["−120", "−100", "−80", "−60", "−40", "−20", "+1"])
C.style_axes(a, "position of the substituted 10 bp block", "transcription / % of wild type")
# element boxes drawn on the canvas below the axes, on the same position scale
for lo, hi, name, tok in [(-112, -100, "GC", "antibody"), (-92, -80, "CCAAT", "receptor"), (-62, -48, "GC", "antibody"),
                          (-31, -24, "TATA", "highlight")]:
    def cx(p):
        return 1.5 + (p + 122) / 134 * 7.4
    bio.box(ax, ((cx(lo) + cx(hi)) / 2, 0.55), cx(hi) - cx(lo), 0.34, tok, None, radius=0.05)
    bio.label(ax, ((cx(lo) + cx(hi)) / 2, 0.12), name, size="tiny")
ax.plot([1.5 + 2 / 134 * 7.4, 8.9], [0.55, 0.55], color=P.ink(), lw=1.2, zorder=5)
bio.panel(ax, "A", (0.1, 8.1))
bio.label(ax, (0.6, 7.75), "Linker scanning (tk promoter)", size="normal", bold=True, ha="left")

# ---- B: start-site distributions
b = C.axes_at(ax, (11.3, 2.1, 7.2, 4.6))
x = np.arange(-30, 61)
wt = np.exp(-0.5 * (x / 1.2) ** 2)
wt /= wt.sum()
rng = np.random.default_rng(0)
broad = np.exp(-0.5 * ((x - 12) / 18) ** 2) * (1 + 0.9 * rng.random(x.size))
for site in (-8, 3, 19, 34):
    broad += 1.6 * np.exp(-0.5 * ((x - site) / 1.0) ** 2)
broad /= broad.sum()
b.bar(x, wt, width=0.9, color=P.fill("dna"), edgecolor=C.line("dna"), lw=0.4, label="wild type")
b.bar(x, broad, width=0.9, color=P.fill("negative"), edgecolor=C.line("negative"), lw=0.4, alpha=0.85,
      label="TATA box deleted")
b.set_xlim(-31, 61)
b.set_ylim(0, 0.36)
b.set_yticks([0, 0.1, 0.2, 0.3])
b.set_xticks([-20, 0, 20, 40, 60], ["−20", "+1", "+20", "+40", "+60"])
C.style_axes(b, "start site (relative to wild-type +1)", "fraction of transcripts")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
b.text(58, 0.2, "same total signal,\nscattered start sites", ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "B", (10.0, 8.1))
bio.label(ax, (10.5, 7.75), "TATA deletion (SV40 early promoter)", size="normal", bold=True, ha="left")
