# The two transesterifications of nuclear pre-mRNA splicing and the kinetics of the lariat intermediate.
# A: step 1, the 2'-OH of the branch-point adenosine attacks the phosphate at the 5' splice site, releasing
# exon 1 with a 3'-OH and forming the lariat intron-exon 2 intermediate (the 5'-terminal G of the intron is
# joined 2'-5' to the branch A, which is also linked 3'-5' to its neighbour: a branched nucleotide with
# 2', 3' and 5' phosphodiester bonds); step 2, the 3'-OH of exon 1 attacks the phosphate at the 3' splice
# site, joining the exons and releasing the lariat intron with a 3'-OH. The phosphate that ends up between the
# exons (red) is the one that was at the 3' splice site.
# B: sequential first-order model P -> I -> S with k1 = 0.05 /min and k2 = 0.1 /min (illustrative values that
# reproduce the lag and the transient intermediate seen in in vitro splicing time courses).
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(24.0, 10.5)

EX_H = 0.62


def exon(cx, cy, w, text):
    bio.box(ax, (cx, cy), w, EX_H, token="mrna", text=text, size="tiny", radius=0.08, zorder=8)


def dot(xy, token="negative", r=0.13, text="p"):
    ax.add_patch(bio.core.Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=12))
    bio.label(ax, xy, text, size="tiny", color=P.on_fill(), zorder=13)


def lariat(cx, cy, r, tail_to):
    # loop of the intron closed at the branch A (rightmost point), tail from A to tail_to
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(cx + r * np.cos(th), cy + r * np.sin(th), color=P.edge("rna"), lw=1.8, zorder=6)
    a = (cx + r, cy)
    if tail_to is not None:
        ax.plot([a[0], tail_to[0]], [a[1], tail_to[1]], color=P.edge("rna"), lw=1.8, zorder=6)
    ax.add_patch(bio.core.Circle(a, 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=11))
    bio.label(ax, a, "A", size="tiny", bold=True, color=P.on_fill(), zorder=12)
    return a


bio.panel(ax, "A", (0.1, 10.35))
# --- row 1: precursor ---
y1 = 8.6
exon(1.9, y1, 2.2, "Exon 1")
exon(11.6, y1, 2.2, "Exon 2")
ax.plot([3.0, 10.5], [y1, y1], color=P.edge("rna"), lw=1.8, zorder=6)
dot((3.15, y1), "neutral")
dot((10.35, y1), "negative")
bio.label(ax, (3.7, y1 - 0.38), "GU", size="tiny", bold=True, color=P.edge("rna"))
bio.label(ax, (9.9, y1 - 0.38), "AG", size="tiny", bold=True, color=P.edge("rna"))
ax.add_patch(bio.core.Circle((8.0, y1), 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=11))
bio.label(ax, (8.0, y1), "A", size="tiny", bold=True, color=P.on_fill(), zorder=12)
bio.label(ax, (8.0, y1 - 0.45), "2′-OH", size="tiny", color=P.edge("highlight"))
bio.arrow(ax, (7.85, y1 + 0.25), (3.3, y1 + 0.2), kind="process", bend=-0.35, color=P.edge("negative"))
bio.label(ax, (5.6, y1 + 1.15), "step 1: 2′-OH of branch A attacks 5′ splice-site phosphate", size="tiny",
          color=P.edge("negative"))
bio.label(ax, (0.55, y1), "5′", size="tiny", bold=True)
bio.label(ax, (12.95, y1), "3′", size="tiny", bold=True)
bio.label(ax, (14.0, y1), "pre-mRNA", size="small", bold=True, ha="left")

# --- row 2: intermediates ---
y2 = 5.55
exon(1.9, y2, 2.2, "Exon 1")
bio.label(ax, (3.35, y2 + 0.32), "3′-OH", size="tiny", color=P.edge("highlight"))
ax.add_patch(bio.core.Circle((3.15, y2), 0.09, color=P.edge("highlight"), zorder=12))
a = lariat(6.6, y2, 0.95, (10.5, y2))
dot((6.6 - 0.95 * np.cos(np.pi / 5), y2 + 0.95 * np.sin(np.pi / 5)), "neutral")
bio.callout(ax, (6.6 - 0.95 * np.cos(np.pi / 5) + 0.1, y2 + 0.95 * np.sin(np.pi / 5) + 0.1), (5.4, y2 + 1.55),
            "G joined 2′→5′ to A")
dot((10.35, y2), "negative")
exon(11.6, y2, 2.2, "Exon 2")
bio.arrow(ax, (3.25, y2 - 0.25), (10.25, y2 - 0.28), kind="process", bend=-0.25, color=P.edge("negative"))
bio.label(ax, (6.6, y2 - 1.75), "step 2: 3′-OH of exon 1 attacks 3′ splice-site phosphate", size="tiny",
          color=P.edge("negative"))
bio.label(ax, (14.0, y2), "lariat intermediate", size="small", bold=True, ha="left")

# --- row 3: products ---
y3 = 2.05
exon(1.9, y3, 2.2, "Exon 1")
dot((3.15, y3), "negative")
exon(4.4, y3, 2.2, "Exon 2")
bio.label(ax, (2.9, y3 - 0.6), "mRNA: exons joined by the phosphate of the 3′ splice site", size="tiny",
          color=P.muted(), ha="left")
a = lariat(9.6, y3 + 0.1, 0.9, (11.3, y3 + 0.1))
dot((9.6 - 0.9 * np.cos(np.pi / 5), y3 + 0.1 + 0.9 * np.sin(np.pi / 5)), "neutral")
bio.label(ax, (11.75, y3 + 0.1), "3′-OH", size="tiny", color=P.edge("highlight"))
bio.label(ax, (14.0, y3), "spliced mRNA + lariat intron", size="small", bold=True, ha="left")
for ya, yb in ((y1 - 0.5, y2 + 0.5), (y2 - 0.5, y3 + 0.5)):
    bio.arrow(ax, (14.6, ya), (14.6, yb), kind="process")

# --- B: kinetics ---
bio.panel(ax, "B", (17.4, 10.35))
k1, k2 = 0.05, 0.1
t = np.linspace(0, 120, 400)
p = np.exp(-k1 * t)
i = k1 / (k2 - k1) * (np.exp(-k1 * t) - np.exp(-k2 * t))
s = 1 - p - i
pl = Q.Plot(ax, (19.2, 1.6, 4.4, 7.2), xlim=(0, 120), ylim=(0, 1.02), xlabel="t / min", ylabel="fraction of RNA",
            xticks=[0, 30, 60, 90, 120], yticks=[0, 0.5, 1])
pl.line(t, p, "rna", text="pre-mRNA", at=0.03, dx=0.25, dy=0.1)
pl.line(t, i, "highlight", text="intermediates", at=0.55, dy=0.25)
pl.line(t, s, "positive", text="mRNA + lariat", at=0.62, dy=-0.5)
tmax = np.log(k2 / k1) / (k2 - k1)
pl.vline(tmax, text=r"$t_{\max}$", top=True)
bio.label(ax, (21.2, 9.65), "P → I → S", size="small", bold=True)
