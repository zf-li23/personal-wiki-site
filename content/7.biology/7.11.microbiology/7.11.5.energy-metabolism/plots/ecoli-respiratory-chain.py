"""The branched aerobic respiratory chain of E. coli (periplasm on top). NADH dehydrogenase I (NDH-1,
nuo; Complex I homolog, 4 H+ pumped per 2 e-), NADH dehydrogenase II (NDH-2, ndh; no pumping) and
succinate dehydrogenase (SDH, Complex II) reduce the quinone pool (ubiquinone-8 aerobically,
menaquinone-8 anoxically). Quinol oxidases: cytochrome bo3 (cyo; heme-copper, 4 H+ per 2 e-, low O2
affinity) and cytochrome bd-I (cyd; 2 H+ per 2 e-, high O2 affinity). Anoxic alternatives (dashed):
nitrate reductase and fumarate reductase. Electrons blue, protons red."""

from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 11.0)
y = 5.6
ax.add_patch(Rectangle((0.3, y), 26.4, 4.6, facecolor=P.mix(P.fill("extracellular"), P.fill("vacuole"), 0.6),
                       edgecolor="none", zorder=1))
ax.add_patch(Rectangle((0.3, 0.3), 26.4, y - 0.3, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
bio.bilayer(ax, [(0.3, y), (26.7, y)])
bio.label(ax, (0.6, 9.85), "Periplasm (P side)", size="small", ha="left", color=P.muted())
bio.label(ax, (0.6, 0.7), "Cytoplasm (N side)", size="small", ha="left", color=P.muted())
E, H = P.edge("dna"), P.edge("h")


def tm(x, w, token, text, h=1.25, dy=0.0):
    bio.protein(ax, (x, y + dy), w, h, token, text=text, size="tiny", zorder=12)


def e_arrow(a, b, bend=0.0):
    bio.arrow(ax, a, b, kind="process", color=E, lw=1.8, head=0.2, bend=bend, zorder=16)


def h_arrow(x, n):
    bio.arrow(ax, (x, y - 1.0), (x, y + 1.9), kind="process", color=H, lw=1.4, head=0.18, zorder=17)
    bio.ion(ax, (x + 0.35, y + 2.05), "h", r=0.15, text=False)
    bio.label(ax, (x + 0.58, y + 2.05), n, size="tiny", ha="left", color=H)


def quinone(x):
    ax.add_patch(Ellipse((x, y), 0.6, 0.3, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=14))
    bio.label(ax, (x, y), "Q", size="tiny", zorder=15)


# NDH-1 (L-shaped)
x = 3.0
tm(x, 1.9, "protein", "NDH-1")
bio.protein(ax, (x - 0.35, y - 1.55), 1.0, 1.4, "protein", zorder=11)
bio.label(ax, (x - 1.7, 2.4), "NADH → NAD⁺", size="tiny")
e_arrow((x - 1.6, 2.75), (x - 0.6, y - 1.6))
h_arrow(x + 0.55, "4 H⁺")
quinone(4.6)
e_arrow((x + 0.95, y - 0.3), (4.4, y - 0.15))
# NDH-2 (monotopic, cytoplasmic face)
x = 7.6
bio.protein(ax, (x, y - 0.85), 1.6, 0.9, "enzyme", text="NDH-2", size="tiny", zorder=12)
bio.label(ax, (x, 2.55), "NADH → NAD⁺", size="tiny")
e_arrow((x, 2.85), (x, y - 1.35))
quinone(x + 0.9)
e_arrow((x + 0.5, y - 0.45), (x + 0.85, y - 0.17))
bio.label(ax, (x + 0.95, y - 1.5), "no H⁺ pumped", size="tiny", color=P.muted(), ha="left")
# SDH
x = 11.4
tm(x, 1.1, "channel", "SDH")
bio.protein(ax, (x, y - 1.45), 1.3, 1.0, "channel", zorder=11)
bio.label(ax, (x, 2.4), "succinate → fumarate", size="tiny")
e_arrow((x, 2.75), (x, y - 1.95))
quinone(x + 1.0)
e_arrow((x + 0.5, y), (x + 0.68, y))
# pool bracket
ax.plot([4.3, 4.3, 21.0, 21.0], [y + 0.75, y + 1.0, y + 1.0, y + 0.75], color=P.edge("lipid"), lw=1.2, zorder=12)
bio.label(ax, (12.6, y + 1.35), "quinone pool, diffusing in the membrane: ubiquinone-8 (aerobic), menaquinone-8 (anoxic)",
          size="tiny", color=P.ink())
# cytochrome bo3
x = 17.6
tm(x, 1.9, "receptor", "cyt bo₃", h=1.4)
quinone(x - 1.5)
e_arrow((x - 1.2, y), (x - 0.95, y))
bio.label(ax, (x, 2.0), "½O₂ + 2H⁺ → H₂O", size="tiny")
e_arrow((x, y - 0.75), (x, 2.35))
h_arrow(x + 0.55, "4 H⁺/2e⁻")
bio.label(ax, (x, y + 3.2), "low O₂ affinity", size="tiny", color=P.muted())
# cytochrome bd
x = 22.4
tm(x, 1.6, "atp", "cyt bd", h=1.3)
quinone(x - 1.4)
e_arrow((x - 1.1, y), (x - 0.82, y))
bio.label(ax, (x, 2.0), "½O₂ + 2H⁺ → H₂O", size="tiny")
e_arrow((x, y - 0.7), (x, 2.35))
h_arrow(x + 0.5, "2 H⁺/2e⁻")
bio.label(ax, (x, y + 3.2), "high O₂ affinity", size="tiny", color=P.muted())
# anaerobic reductases (dashed)
x = 25.4
ax.add_patch(FancyBboxPatch((x - 0.85, 1.2), 1.7, 2.3, boxstyle="round,pad=0,rounding_size=0.2", facecolor="none",
                            edgecolor=P.muted(), lw=1.0, ls="--", zorder=10))
bio.label(ax, (x, 2.35), "anoxic:\nnitrate\nreductase,\nfumarate\nreductase", size="tiny", color=P.muted())
bio.label(ax, (x, 4.1), "replace the\noxidases", size="tiny", color=P.muted())
