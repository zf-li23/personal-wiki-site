# Gametophytic versus sporophytic self-incompatibility for a pistil of genotype S1S2. Pollen comes from
# plants S1S2 (self), S1S3 and S3S4. In GSI the haploid genotype of each pollen grain matters: grains
# carrying S1 or S2 are stopped in the style, S3 and S4 grains reach the ovary. In SSI the pollen phenotype
# is that of the diploid parent (here S alleles codominant): every grain from an S1S3 parent carries S1
# and S3 products and is rejected on the stigma surface, while all S3S4 pollen is accepted.
from matplotlib.patches import Polygon, Ellipse, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28.0, 11.0)
OK, NO = P.edge("positive"), P.edge("negative")


def pistil(x):
    ax.add_patch(Polygon([(x - 0.35, 2.6), (x + 0.35, 2.6), (x + 0.3, 7.6), (x - 0.3, 7.6)], closed=True,
                         facecolor=P.light("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=4))
    ax.add_patch(Ellipse((x, 8.0), 1.9, 0.9, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=5))
    ax.add_patch(Ellipse((x, 1.8), 2.1, 1.9, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=5))
    bio.label(ax, (x, 1.8), "S1S2", size="tiny")


def grain(x, y, text, accepted, stop):
    c = OK if accepted else NO
    ax.add_patch(Circle((x, y), 0.3, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9, zorder=8))
    bio.label(ax, (x, y + 0.55), text, size="tiny")
    if stop is None:
        return
    ax.plot([x, x * 0.0 + x], [y - 0.3, stop], color=c, lw=1.6, zorder=7)
    if not accepted:
        ax.plot([x - 0.18, x + 0.18], [stop, stop], color=c, lw=2.2, zorder=7)


def panel(x0, title, mode):
    bio.label(ax, (x0 + 6.0, 10.6), title, size="normal", bold=True)
    for k, (par, grains) in enumerate((("self S1S2", ("S1", "S2")), ("S1S3", ("S1", "S3")), ("S3S4", ("S3", "S4")))):
        x = x0 + 2.0 + 4.0 * k
        pistil(x)
        bio.label(ax, (x, 9.85), "pollen from " + par, size="tiny", color=P.muted())
        for j, g in enumerate(grains):
            gx = x - 0.4 + 0.8 * j
            if mode == "gsi":
                acc = g not in ("S1", "S2")
                grain(gx, 8.5, g, acc, 2.4 if acc else 5.2)
            else:
                parent = par.replace("self ", "")
                acc = not any(a in parent for a in ("S1", "S2"))
                grain(gx, 8.5, g, acc, 2.4 if acc else 8.05)
        if mode == "ssi":
            bio.label(ax, (x, 9.45), "coat: " + par.replace("self ", "") + " products", size="tiny", color=P.muted())


bio.panel(ax, "A", (0.2, 10.9))
panel(0.3, "Gametophytic SI: pollen phenotype = its own haploid S allele", "gsi")
bio.panel(ax, "B", (14.2, 10.9))
panel(14.2, "Sporophytic SI: pollen phenotype = S alleles of the parent", "ssi")
bio.label(ax, (7.0, 0.45), "pollen tubes stopped in the style", size="tiny", color=P.muted())
bio.label(ax, (21.0, 0.45), "pollen rejected on the stigma (no hydration or germination)", size="tiny", color=P.muted())
