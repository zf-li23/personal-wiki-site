"""Migration pathways of trunk neural crest cells. (A) Transverse section (dorsal up). Cells taking the ventral
pathway (between the neural tube and the somite, then through the sclerotome) form the dorsal root ganglia beside
the tube, the sympathetic ganglia beside the dorsal aorta and the chromaffin cells of the adrenal medulla; cells
taking the later dorsolateral pathway (between the epidermis and the dermomyotome) become melanocytes. (B) Dorsal
view of the same region (anterior up). Ventral-pathway cells enter only the anterior half of each sclerotome,
because the posterior half expresses repellent ephrin-B and semaphorin-3F; the dorsal root ganglia and the motor
axons are therefore segmented in register with the somites, and rotating a strip of somites by 180 degrees
leaves the crest in the (original) anterior halves."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N
from matplotlib.patches import Circle, Ellipse, Rectangle

fig, ax = bio.canvas(23, 10.5)
P = bio.P
T = N.TISSUE
bio.panel(ax, "A", (0.2, 10.3))
cx, cy = 6.0, 6.2
# epidermis
ax.add_patch(Rectangle((0.6, 9.0), 10.8, 0.25, facecolor=P.fill(T["epidermis"]), edgecolor=P.edge(T["epidermis"]), lw=1.0))
# neural tube, notochord, aorta
ax.add_patch(Ellipse((cx, cy + 0.9), 1.9, 3.0, facecolor=P.fill(T["neural"]), edgecolor=P.edge(T["neural"]), lw=1.1))
ax.add_patch(Ellipse((cx, cy + 0.9), 0.15, 1.8, facecolor=P.fill("extracellular"), edgecolor=P.edge(T["neural"]), lw=0.7))
ax.add_patch(Circle((cx, cy - 1.3), 0.45, facecolor=P.fill(T["notochord"]), edgecolor=P.edge(T["notochord"]), lw=1.0))
for s in (-1, 1):
    ax.add_patch(Circle((cx + s * 0.9, cy - 2.6), 0.5, facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=1.0))
    # dermomyotome: curved epithelial sheet dorso-laterally; sclerotome: mesenchyme ventro-medially
    th = np.linspace(np.radians(40), np.radians(140), 40) if s < 0 else np.linspace(np.radians(40), np.radians(140), 40)
    x0 = cx + s * 3.3
    dm = np.c_[x0 + 1.5 * np.cos(th) * (-s), cy + 0.6 + 1.0 * np.sin(th)]
    poly, _, _ = __import__("wikibio").neurodev._band(dm, 0.18, 0.18)
    bio.shape(ax, poly, T["somite"], lw=1.0)
    bio.shape(ax, bio.blob((cx + s * 2.6, cy - 0.6), 1.3, 0.95, wobble=0.05, seed=3 + s, k=9), T["somite"], lw=0.9, alpha=0.6)
    # crest paths
    crest = P.edge(T["crest"])
    bio.arrow(ax, (cx + s * 0.4, cy + 2.6), (cx + s * 4.6, cy + 2.15), kind="process", color=crest, lw=1.6, bend=0.15 * s, head=0.18)
    bio.arrow(ax, (cx + s * 0.6, cy + 2.4), (cx + s * 1.25, cy - 1.6), kind="process", color=crest, lw=1.6, bend=-0.1 * s, head=0.18)
    ax.add_patch(Ellipse((cx + s * 1.45, cy + 0.6), 0.6, 0.9, facecolor=P.fill(T["crest"]), edgecolor=crest, lw=0.9, zorder=6))
    ax.add_patch(Ellipse((cx + s * 1.8, cy - 2.3), 0.5, 0.55, facecolor=P.fill(T["crest"]), edgecolor=crest, lw=0.9, zorder=6))
for k in range(6):
    ax.add_patch(Circle((cx - 0.35 + 0.14 * k, cy + 2.55 + 0.08 * (k % 2)), 0.1, facecolor=P.fill(T["crest"]), edgecolor=P.edge(T["crest"]), lw=0.6, zorder=7))
bio.callout(ax, (cx + 4.2, cy + 2.2), (cx + 3.6, 9.8), "dorsolateral pathway: melanocytes")
bio.callout(ax, (cx + 1.45, cy + 0.6), (cx + 4.0, cy + 1.0), "dorsal root ganglion")
bio.callout(ax, (cx + 1.8, cy - 2.3), (cx + 4.0, cy - 2.0), "sympathetic ganglion")
bio.callout(ax, (cx - 3.5, cy + 1.3), (0.7, cy + 3.0), "dermomyotome")
bio.callout(ax, (cx - 2.6, cy - 0.8), (0.7, cy - 2.2), "sclerotome")
bio.callout(ax, (cx - 0.9, cy - 2.6), (cx - 2.5, cy - 3.4), "dorsal aorta")
bio.callout(ax, (cx - 1.15, cy - 0.6), (0.7, cy - 0.4), "ventral pathway")

# (B) dorsal view
bio.panel(ax, "B", (12.3, 10.3))
x0 = 17.4
ax.add_patch(Rectangle((x0 - 0.5, 1.2), 1.0, 8.1, facecolor=P.fill(T["neural"]), edgecolor=P.edge(T["neural"]), lw=1.0))
for k in range(4):
    y = 8.6 - k * 1.85
    for s in (-1, 1):
        xa = x0 + s * 0.65 + (0 if s > 0 else -2.4)
        ax.add_patch(Rectangle((xa, y - 0.75), 2.4, 0.75, facecolor=P.light(T["somite"]), edgecolor=P.edge(T["somite"]), lw=0.8))
        ax.add_patch(Rectangle((xa, y - 1.5), 2.4, 0.75, facecolor=P.fill(T["somite"]), edgecolor=P.edge(T["somite"]), lw=0.8, hatch="///"))
        for j in range(5):
            ax.add_patch(Circle((x0 + s * (0.85 + 0.45 * j), y - 0.38 + 0.12 * ((j % 2) - 0.5)), 0.12,
                                facecolor=P.fill(T["crest"]), edgecolor=P.edge(T["crest"]), lw=0.6, zorder=6))
bio.label(ax, (x0, 9.75), "anterior", size="tiny", color=P.muted())
bio.label(ax, (x0 - 2.3, 0.9), "posterior", size="tiny", color=P.muted())
bio.label(ax, (21.4, 7.8), "anterior half:", size="tiny", ha="left")
bio.label(ax, (21.4, 7.45), "permissive", size="tiny", ha="left", color=P.muted())
bio.label(ax, (21.4, 7.05), "posterior half:", size="tiny", ha="left")
bio.label(ax, (21.4, 6.7), "ephrin-B, Sema3F", size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0 + 0.9, 0.9), "neural tube", size="tiny", color=P.muted())
