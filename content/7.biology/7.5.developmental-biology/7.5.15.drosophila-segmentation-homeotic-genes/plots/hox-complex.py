# The homeotic complex of Drosophila (HOM-C) and the colinearity of its genes. Top: the eight Hox genes on chromosome
# arm 3R in their chromosomal order, the Antennapedia complex (labial, proboscipedia, Deformed, Sex combs reduced,
# Antennapedia) and the bithorax complex (Ultrabithorax, abdominal-A, Abdominal-B), separated by about 10 Mb; the
# direction of transcription is not shown. Bottom: the segments of the embryo with the anterior limit of each gene's
# domain (schematic, after Akam 1987 and later work): the order of the genes along the chromosome matches the order
# of their domains along the body (spatial colinearity). Each gene is expressed from its anterior limit backwards,
# usually at a lower level in more posterior segments where a more posterior Hox gene dominates.
import wikibio as bio

fig, ax = bio.canvas(24.0, 10.0)
P = bio.P
genes = [("lab", "channel"), ("pb", "dna2"), ("Dfd", "positive"), ("Scr", "cl"), ("Antp", "highlight"), ("Ubx", "drug"),
         ("abd-A", "receptor"), ("Abd-B", "protein")]
x = 1.5
gx = {}
for k, (g, t) in enumerate(genes):
    if k == 5:
        ax.plot([x + 0.1, x + 1.3], [8.6, 8.6], color=P.muted(), lw=1.2, ls=(0, (2, 2)))
        bio.label(ax, (x + 0.7, 9.05), "about 10 Mb", size="tiny", color=P.muted())
        x += 1.4
    bio.box(ax, (x + 0.95, 8.6), 1.8, 0.7, token=t, text=g, size="small", italic=True)
    gx[g] = x + 0.95
    x += 2.2
ax.plot([0.8, x + 0.2], [8.6, 8.6], color=P.edge("dna"), lw=2.5, zorder=5)
bio.label(ax, (gx["Scr"] - 1.0, 9.6), "Antennapedia complex", size="small", bold=True)
bio.label(ax, (gx["abd-A"], 9.6), "bithorax complex", size="small", bold=True)
segs = ["Ic", "Md", "Mx", "Lb", "T1", "T2", "T3", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
x0, sw, y = 1.2, 1.45, 3.0
sx = {s: x0 + i * sw for i, s in enumerate(segs)}
for s in segs:
    ax.add_patch(bio.core.FancyBboxPatch((sx[s], y - 0.4), sw - 0.08, 0.8, boxstyle="round,pad=0,rounding_size=0.1",
                                         facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=6))
    bio.label(ax, (sx[s] + sw / 2, y), s, size="tiny")
# anterior limits and main domains
dom = {"lab": ("Ic", "Ic"), "pb": ("Mx", "Lb"), "Dfd": ("Md", "Mx"), "Scr": ("Lb", "T1"), "Antp": ("T1", "T3"),
       "Ubx": ("T3", "A1"), "abd-A": ("A2", "A7"), "Abd-B": ("A5", "A8")}
for k, (g, t) in enumerate(genes):
    a, b = dom[g]
    yy = 4.2 + (k % 4) * 0.55
    xa, xb = sx[a], sx[b] + sw - 0.08
    ax.add_patch(bio.core.FancyBboxPatch((xa, yy - 0.18), xb - xa, 0.36, boxstyle="round,pad=0,rounding_size=0.08",
                                         facecolor=P.fill(t), edgecolor=P.edge(t), lw=0.8, zorder=7))
    # weaker extension to the posterior
    if g in ("Antp", "Ubx", "Scr"):
        ax.add_patch(bio.core.FancyBboxPatch((xb, yy - 0.1), min(sx["A8"] + sw, xb + 3 * sw) - xb, 0.2,
                                             boxstyle="round,pad=0,rounding_size=0.05", facecolor=P.light(t),
                                             edgecolor="none", zorder=6.5))
    bio.arrow(ax, (gx[g], 8.2), (xa + 0.2, yy + 0.22), kind="link", color=P.mix(P.edge(t), P.surface(), 0.3), lw=0.8)
bio.label(ax, (sx["T1"], 1.9), "head", size="small", color=P.muted(), ha="right")
bio.label(ax, (sx["T2"] + sw / 2, 1.9), "thorax", size="small", color=P.muted())
bio.label(ax, (sx["A4"] + sw, 1.9), "abdomen", size="small", color=P.muted())
bio.label(ax, (12.0, 0.8), "chromosome 3′ → 5′ order = anterior → posterior order of expression domains", size="small")
