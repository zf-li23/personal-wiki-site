"""Life cycle of a plasmodial slime mold (Stemonitis, Physarum). Blue: diploid phase; orange: haploid.
Left: the cycle. Right: a stalked sporangium of Stemonitis in section (peridium, columella, capillitium
with spores)."""
import numpy as np
from matplotlib.patches import Ellipse, Circle

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(26, 13)


def st(t, bold=False):
    return dict(text=t, size="small", bold=bold)


nodes = plant.alternation_of_generations(ax, (7.5, 6.4), 4.0, [
    st("Plasmodium (2n)\nmultinucleate, no wall", True), st("Sporangia form\n(stalk, columella)"),
    st("Spores (n)\nwith walls"), st("Myxamoebae or\nswarm cells (n)"), st("Zygote (2n)")],
    meiosis=1, fertilization=3, gap=0.2,
    arrow_labels=[None, None, "Germination", None, "Growth"],
    chords=[(0, 0, dict())] if False else None)
# sclerotium side loop
p0 = nodes[0].xy
bio.box(ax, (p0[0] + 5.6, p0[1] + 0.9), 2.6, 1.1, token="neutral", text="Sclerotium\n(dry, dormant)", size="small")
bio.arrow(ax, (p0[0] + 1.9, p0[1] + 0.45), (p0[0] + 4.25, p0[1] + 1.05), kind="process")
bio.arrow(ax, (p0[0] + 4.25, p0[1] + 0.65), (p0[0] + 1.9, p0[1] + 0.05), kind="process")

# sporangium drawing
bio.panel(ax, "B", (16.2, 12.7))
cx, base = 20.5, 1.2
stalk = np.array([[cx - 0.12, base], [cx - 0.08, base + 3.2], [cx + 0.08, base + 3.2], [cx + 0.12, base]])
bio.shape(ax, stalk, token="bone")
ax.add_patch(Ellipse((cx, base + 6.6), 3.0, 7.0, facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=1.3, zorder=5))
ax.plot([cx, cx], [base + 3.2, base + 9.4], color=P.edge("bone"), lw=3.0, zorder=6, solid_capstyle="round")
rng = np.random.default_rng(1)
for k in range(26):  # capillitium threads
    y0 = rng.uniform(base + 3.6, base + 9.4)
    ang = rng.uniform(-1, 1)
    xs = np.linspace(cx, cx + np.sign(ang + 1e-3) * 1.35 * np.sqrt(max(0.05, 1 - ((y0 - base - 6.6) / 3.5) ** 2)), 12)
    ys = y0 + 0.25 * np.sin(np.linspace(0, 3, 12)) + ang * 0.3
    ax.plot(xs, ys, color=P.edge("lipid_tail"), lw=0.6, zorder=6.5)
for k in range(140):  # spores
    t = rng.uniform(0, 2 * np.pi); r = np.sqrt(rng.uniform(0.02, 0.95))
    x, y = cx + 1.38 * r * np.cos(t), base + 6.6 + 3.3 * r * np.sin(t)
    if abs(x - cx) > 0.18:
        ax.add_patch(Circle((x, y), 0.07, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.3, zorder=7))
bio.callout(ax, (cx + 1.5, base + 7.6), (23.2, base + 9.6), "Peridium")
bio.callout(ax, (cx, base + 8.6), (23.2, base + 8.4), "Columella")
bio.callout(ax, (cx + 0.9, base + 5.2), (23.2, base + 5.0), "Capillitium")
bio.callout(ax, (cx - 0.9, base + 6.2), (17.0, base + 6.4), "Spores (n)")
bio.callout(ax, (cx, base + 1.6), (17.4, base + 1.6), "Stalk")
bio.label(ax, (cx - 0.1, 0.5), "Sporangium of", size="small", ha="right")
bio.label(ax, (cx + 0.1, 0.5), "Stemonitis", size="small", ha="left", italic=True)
bio.panel(ax, "A", (0.2, 12.7))
