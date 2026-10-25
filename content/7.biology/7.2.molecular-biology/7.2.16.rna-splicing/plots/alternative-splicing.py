# Patterns of alternative splicing and the kinetic coupling of splicing to elongation.
# A: each row is a pre-mRNA; constitutive exons are dark, alternatively used regions light (highlight); the
# junctions drawn above the row give one isoform, those below the other. Alternative first and last exons
# (alternative promoters and polyadenylation sites) are not drawn.
# B: "window of opportunity" model. The weak 3' splice site of a cassette exon is transcribed first and is
# committed to splicing with rate constant k; the competing strong 3' splice site downstream is transcribed
# d = 2 kb later, after a delay d/v, after which the two sites compete with rate constants k and ks = 0.1 /s.
# Inclusion Psi = 1 - exp(-k d/v) + exp(-k d/v) k/(k + ks). Curves for k = 0.005 and 0.02 /s; the band marks
# typical Pol II elongation rates (1-4 kb/min); a mutant polymerase about twofold slower raises inclusion.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)

bio.panel(ax, "A", (0.1, 11.85))
H = 0.42


def ex(x0, x1, yy, alt=False):
    bio.box(ax, ((x0 + x1) / 2, yy), x1 - x0, H, token="highlight" if alt else "mrna", radius=0.05, zorder=6)


def junction(xa, xb, yy, up=True):
    h = 0.42 if up else -0.42
    ym = yy + (H / 2 if up else -H / 2)
    ax.plot([xa, (xa + xb) / 2, xb], [ym, ym + h, ym], color=P.edge("rna") if up else P.edge("dna"), lw=1.1, zorder=5)


rows = []
yy = 10.4
dy = 1.62
x0 = 4.3
# constitutive
y_ = yy
bio.label(ax, (0.3, y_), "Constitutive", size="small", ha="left")
ax.plot([x0, x0 + 7.6], [y_, y_], color=P.muted(), lw=0.9, zorder=3)
for a, b in ((x0, x0 + 1.3), (x0 + 3.2, x0 + 4.4), (x0 + 6.3, x0 + 7.6)):
    ex(a, b, y_)
junction(x0 + 1.3, x0 + 3.2, y_)
junction(x0 + 4.4, x0 + 6.3, y_)
# cassette exon
y_ = yy - dy
bio.label(ax, (0.3, y_), "Cassette exon", size="small", ha="left")
ax.plot([x0, x0 + 7.6], [y_, y_], color=P.muted(), lw=0.9, zorder=3)
ex(x0, x0 + 1.3, y_)
ex(x0 + 3.2, x0 + 4.4, y_, alt=True)
ex(x0 + 6.3, x0 + 7.6, y_)
junction(x0 + 1.3, x0 + 3.2, y_)
junction(x0 + 4.4, x0 + 6.3, y_)
junction(x0 + 1.3, x0 + 6.3, y_, up=False)
# mutually exclusive
y_ = yy - 2 * dy
bio.label(ax, (0.3, y_), "Mutually exclusive", size="small", ha="left")
ax.plot([x0, x0 + 7.6], [y_, y_], color=P.muted(), lw=0.9, zorder=3)
ex(x0, x0 + 1.3, y_)
ex(x0 + 2.4, x0 + 3.4, y_, alt=True)
ex(x0 + 4.4, x0 + 5.4, y_, alt=True)
ex(x0 + 6.3, x0 + 7.6, y_)
junction(x0 + 1.3, x0 + 2.4, y_)
junction(x0 + 3.4, x0 + 6.3, y_)
junction(x0 + 1.3, x0 + 4.4, y_, up=False)
junction(x0 + 5.4, x0 + 6.3, y_, up=False)
# alternative 5' splice site
y_ = yy - 3 * dy
bio.label(ax, (0.3, y_), "Alternative 5′ site", size="small", ha="left")
ax.plot([x0, x0 + 7.6], [y_, y_], color=P.muted(), lw=0.9, zorder=3)
ex(x0, x0 + 2.2, y_)
ex(x0 + 2.2, x0 + 3.2, y_, alt=True)
ex(x0 + 6.3, x0 + 7.6, y_)
junction(x0 + 3.2, x0 + 6.3, y_)
junction(x0 + 2.2, x0 + 6.3, y_, up=False)
# alternative 3' splice site
y_ = yy - 4 * dy
bio.label(ax, (0.3, y_), "Alternative 3′ site", size="small", ha="left")
ax.plot([x0, x0 + 7.6], [y_, y_], color=P.muted(), lw=0.9, zorder=3)
ex(x0, x0 + 1.3, y_)
ex(x0 + 4.4, x0 + 5.4, y_, alt=True)
ex(x0 + 5.4, x0 + 7.6, y_)
junction(x0 + 1.3, x0 + 4.4, y_)
junction(x0 + 1.3, x0 + 5.4, y_, up=False)
# intron retention
y_ = yy - 5 * dy
bio.label(ax, (0.3, y_), "Intron retention", size="small", ha="left")
ex(x0, x0 + 2.4, y_)
ex(x0 + 2.4, x0 + 5.2, y_, alt=True)
ex(x0 + 5.2, x0 + 7.6, y_)
junction(x0 + 2.4, x0 + 5.2, y_, up=False)
bio.label(ax, (x0 + 3.8, y_ + 0.55), "retained (no junction)", size="tiny", color=P.edge("rna"))
bio.label(ax, (x0 + 3.8, yy + 1.05), "isoform 1 (above)  ·  isoform 2 (below)", size="tiny", color=P.muted())

# --- B: kinetic coupling --------------------------------------------------------------------------------------
bio.panel(ax, "B", (13.3, 11.85))
d, ks = 2000.0, 0.1
v = np.linspace(0.25, 6.0, 300)  # kb/min
vs = v * 1000 / 60  # nt/s
pl = Q.Plot(ax, (15.2, 2.2, 7.8, 7.8), xlim=(0, 6), ylim=(0, 1.0), xlabel="Pol II elongation rate / (kb min⁻¹)",
            ylabel="exon inclusion Ψ", ylabel_offset=1.0, xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[0, 0.25, 0.5, 0.75, 1])
pl.span(1, 4, "neutral", text="typical in vivo", strength=0.6)
for k, tok, at in ((0.02, "positive", 0.5), (0.005, "rna", 0.4)):
    w = np.exp(-k * d / vs)
    psi = 1 - w + w * k / (k + ks)
    pl.line(v, psi, tok, text=f"k = {k:g} s⁻¹", at=at, dy=0.28)
    for vv, mk in ((3.0, False), (1.5, True)):
        ww = np.exp(-k * d / (vv * 1000 / 60))
        pl.points([vv], [1 - ww + ww * k / (k + ks)], tok, hollow=mk)
pl.text(1.55, 0.06, "○ slow Pol II mutant (≈2× slower)", ha="left")
bio.label(ax, (19.1, 10.85), "Window of opportunity", size="normal", bold=True)
