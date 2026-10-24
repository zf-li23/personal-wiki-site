# The secretory (biosynthetic) pathway. Proteins made on ribosomes of the rough ER enter its lumen, leave
# the ER in COPII-coated vesicles for the cis face of the Golgi (COPI vesicles return escaped ER proteins),
# move through the cisternae and are sorted at the trans-Golgi network into constitutive secretory vesicles
# (continuous exocytosis), regulated secretory granules (stored until a signal such as a rise in Ca2+
# triggers fusion), and vesicles carrying mannose 6-phosphate-tagged hydrolases to endosomes and lysosomes.
import numpy as np
import wikibio as bio

fig, ax = bio.canvas(18, 11)
P = bio.P
cell = bio.cell(ax, (4.0, 5.5), 12.4, 8.0, kind="animal", seed=6)
bio.nucleus(ax, (1.6, 5.4), 2.3, pores=14)
bio.label(ax, (1.0, 5.4), "Nucleus", size="small", bold=True)
bio.er(ax, (4.85, 5.4), 4.2, 1.9, sheets=4, angle=90)
bio.golgi(ax, (9.6, 5.4), 3.4, cisternae=5, curve=0.35, angle=-90)
cargo = "highlight"


def membrane_x(yy):
    # x of the plasma membrane on the right side at height yy
    right = cell[cell[:, 0] > 10]
    return float(np.interp(yy, *zip(*sorted(zip(right[:, 1], right[:, 0])))))


def vesicle(xy, r=0.22, token="vesicle", k=3, coat=None):
    bio.vesicle(ax, xy, r, token=token)
    rng = np.random.default_rng(int(xy[0] * 37 + xy[1] * 11))
    for _ in range(k):
        a, d = rng.uniform(0, 2 * np.pi), r * 0.5 * np.sqrt(rng.uniform())
        ax.add_patch(bio.core.Circle((xy[0] + d * np.cos(a), xy[1] + d * np.sin(a)), r * 0.2, facecolor=P.fill(cargo),
                                     edgecolor=P.edge(cargo), lw=0.4, zorder=9))
    if coat:
        for t in np.linspace(0, 2 * np.pi, 14, endpoint=False):
            p = (xy[0] + (r + 0.05) * np.cos(t), xy[1] + (r + 0.05) * np.sin(t))
            ax.add_patch(bio.core.Circle(p, 0.035, color=P.edge(coat), lw=0, zorder=9))


# ER -> cis Golgi (COPII) and back (COPI)
vesicle((7.35, 6.0), coat="positive")
vesicle((7.35, 4.8), coat="channel", k=1)
bio.arrow(ax, (6.65, 6.15), (8.25, 6.15), kind="process", shrink=0.05)
bio.arrow(ax, (8.25, 4.65), (6.65, 4.65), kind="process", dashed=True, color=P.muted())
bio.label(ax, (7.45, 6.65), "COPII", size="tiny", color=P.edge("positive"), bold=True)
bio.label(ax, (7.45, 4.15), "COPI", size="tiny", color=P.edge("channel"), bold=True)

# trans-Golgi network -> three destinations
tgn = np.array([11.0, 5.4])
xm = membrane_x(8.0)
vesicle((12.6, 7.7))
bio.arrow(ax, tgn + (0.2, 0.7), (12.35, 7.55), kind="process", bend=-0.15)
fuse_y = 8.4
fx = membrane_x(fuse_y)
bio.arrow(ax, (12.85, 7.85), (fx - 0.35, fuse_y), kind="process")
bio.vesicle(ax, (fx - 0.05, fuse_y), 0.24, token="vesicle")
for k, d in enumerate((0.35, 0.7, 0.5)):
    ax.add_patch(bio.core.Circle((fx + d, fuse_y + (k - 1) * 0.3), 0.055, facecolor=P.fill(cargo), edgecolor=P.edge(cargo), lw=0.4, zorder=9))

for k, (xy) in enumerate(((12.4, 5.6), (13.1, 5.15), (12.9, 6.05))):
    bio.vesicle(ax, xy, 0.28, token="golgi")
    ax.add_patch(bio.core.Circle(xy, 0.16, facecolor=P.edge(cargo), edgecolor="none", zorder=9))
bio.arrow(ax, tgn + (0.3, 0.1), (12.05, 5.5), kind="process")
gy = 5.4
gx = membrane_x(gy)
bio.arrow(ax, (13.5, 5.45), (gx - 0.4, gy), kind="process", dashed=True)
bio.ion(ax, (gx - 0.9, gy + 0.65), "ca", r=0.13, text=False)
bio.label(ax, (gx - 0.7, gy + 0.65), "Ca²⁺ signal", size="tiny", ha="left")

vesicle((12.4, 3.2), token="lysosome", k=2)
bio.arrow(ax, tgn + (0.2, -0.75), (12.15, 3.35), kind="process", bend=0.15)
bio.lysosome(ax, (13.15, 2.1), 0.55)
bio.arrow(ax, (12.55, 2.95), (12.85, 2.6), kind="process", head=0.16)

# labels
bio.callout(ax, (4.6, 6.9), (4.0, 9.4), "Rough ER")
bio.callout(ax, (8.52, 5.6), (8.0, 9.4), "cis face")
bio.callout(ax, (10.35, 6.6), (10.6, 9.6), "trans face (TGN)")
bio.label(ax, (fx - 0.3, fuse_y + 0.55), "Constitutive secretion", size="small", ha="right")
bio.label(ax, (12.9, 4.6), "Regulated secretion\n(secretory granules)", size="small", va="top")
bio.label(ax, (12.45, 1.55), "Lysosome", size="small", ha="right")
bio.label(ax, (11.6, 3.2), "M6P-tagged\nhydrolases", size="tiny", ha="right", color=P.muted())
bio.label(ax, (gx + 0.35, 9.9), "Extracellular\nspace", size="small", ha="left", color=P.muted())
bio.label(ax, (gx + 0.35, gy - 0.2), "Plasma\nmembrane", size="tiny", ha="left", color=P.muted())
bio.label(ax, (9.0, 0.75), "Cytosol", size="small", color=P.muted(), bold=True)
bio.label(ax, (7.45, 1.7), "Cargo protein", size="tiny", ha="left")
ax.add_patch(bio.core.Circle((7.3, 1.7), 0.06, facecolor=P.fill(cargo), edgecolor=P.edge(cargo), lw=0.4, zorder=9))
