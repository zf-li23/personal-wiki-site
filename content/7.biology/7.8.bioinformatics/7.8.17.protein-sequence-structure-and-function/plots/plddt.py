# Per-residue confidence of an AlphaFold model: the human N-glycanase NGLY1 (UniProt Q96IV0, 654 residues,
# AlphaFold DB model AF-Q96IV0-F1, pLDDT values in ngly1-plddt.csv, data available under CC BY 4.0).
# A: pLDDT along the sequence, with the UniProt annotations of the two structured domains (PUB 30-91,
# PAW 454-654), of the region annotated as disordered (112-163) and of the catalytic triad (309, 336, 353);
# the usual confidence bands are drawn as background. B: the fraction of residues above each pLDDT value
# for the whole chain. C: the mean pLDDT of the annotated segments.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
D = np.loadtxt("ngly1-plddt.csv", delimiter=",", skiprows=1)
res, plddt = D[:, 0], D[:, 1]
bands = [(90, 100, "positive", "very high"), (70, 90, "dna", "confident"), (50, 70, "rna", "low"),
         (0, 50, "negative", "very low")]
segs = [("PUB domain", 30, 91), ("disordered (112-163)", 112, 163), ("catalytic core", 164, 453),
        ("PAW domain", 454, 654)]

fig, ax = bio.canvas(28.0, 10.0)
a = C.axes_at(ax, (2.0, 1.2, 16.0, 7.6))
for lo, hi, tok, name in bands:
    a.axhspan(lo, hi, color=P.mix(P.light(tok), P.surface(), 0.62), lw=0)
    a.text(660, (lo + hi) / 2, name, fontsize=FT["tiny"], color=C.line(tok), va="center")
a.plot(res, plddt, color=P.ink(), lw=1.0)
for name, lo, hi in segs:
    if "disordered" in name:
        a.annotate("", xy=(lo, 8), xytext=(hi, 8), arrowprops=dict(arrowstyle="-", color=C.line("negative"), lw=2.5))
        a.text((lo + hi) / 2, 13, "disordered", ha="center", fontsize=FT["tiny"], color=C.line("negative"))
    else:
        a.annotate("", xy=(lo, 8), xytext=(hi, 8), arrowprops=dict(arrowstyle="-", color=C.line("dna"), lw=2.5))
        a.text((lo + hi) / 2, 13, name, ha="center", fontsize=FT["tiny"], color=C.line("dna"))
for site in (309, 336, 353):
    a.scatter([site], [plddt[int(site) - 1]], s=14, color=C.line("enzyme"), zorder=5)
a.text(330, 103, "catalytic triad", ha="center", fontsize=FT["tiny"], color=C.line("enzyme"))
a.set_xlim(0, 700)
a.set_ylim(0, 108)
C.style_axes(a, "residue", "pLDDT")
bio.panel(ax, "A", (0.2, 9.6))
b = C.axes_at(ax, (20.8, 5.5, 6.0, 3.3))
xs = np.linspace(0, 100, 201)
b.plot(xs, [(plddt >= v).mean() for v in xs], color=C.line("dna"), lw=1.4)
for v, tok in ((90, "positive"), (70, "dna"), (50, "rna")):
    b.axvline(v, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    b.text(v - 2, 0.9, f"{(plddt >= v).mean():.0%} ≥ {v}", rotation=90, ha="right", va="top",
           fontsize=FT["tiny"], color=P.ink())
b.set_ylim(0, 1.05)
C.style_axes(b, "pLDDT", "fraction of residues above")
bio.panel(ax, "B", (19.8, 9.6))
c = C.axes_at(ax, (20.8, 1.2, 6.0, 2.8))
ys = np.arange(len(segs))[::-1]
means = [plddt[int(lo) - 1:int(hi)].mean() for _, lo, hi in segs]
c.barh(ys, means, height=0.6,
       color=[C.line("negative") if m < 70 else C.line("dna") for m in means])
c.set_yticks(ys)
c.set_yticklabels([s[0] for s in segs], fontsize=FT["tiny"])
c.set_xlim(0, 100)
for y_, m in zip(ys, means):
    c.text(m + 2, y_, f"{m:.0f}", va="center", fontsize=FT["tiny"], color=P.ink())
C.style_axes(c, "mean pLDDT", None)
bio.panel(ax, "C", (19.8, 4.6))
