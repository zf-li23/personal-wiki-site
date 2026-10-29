# From the follicle cells to the nucleus: the dorsal-ventral signalling cascade of the Drosophila egg (left) and the
# homologous Toll-like receptor pathway of mammalian innate immunity (right). Gurken-EGFR signalling represses pipe
# in dorsal follicle cells, so Pipe sulfates vitelline-membrane proteins only ventrally; the sulfated proteins
# localize a protease cascade (Nudel, Gastrulation defective, Snake, Easter) in the perivitelline space that cleaves
# Spatzle; Spatzle activates Toll; Toll recruits MyD88, Tube and the kinase Pelle, Cactus is phosphorylated and
# degraded, and Dorsal enters ventral nuclei. Grey boxes on the right are the mammalian counterparts.
import wikibio as bio

fig, ax = bio.canvas(21.0, 15.0)
P = bio.P


def node(xy, text, tok, w=3.6, italic=False):
    bio.box(ax, xy, w, 0.75, token=tok, text=text, size="small", italic=italic)


# compartments
regions = [("Dorsal follicle cell", 13.0, 14.6, "mg"), ("Ventral follicle cell", 10.6, 12.2, "mg"),
           ("Perivitelline space", 6.6, 10.2, "extracellular"), ("Embryo (ventral side)", 0.3, 6.2, "cytoplasm")]
for name, y0, y1, tok in regions:
    ax.add_patch(bio.core.FancyBboxPatch((0.4, y0), 12.4, y1 - y0, boxstyle="round,pad=0,rounding_size=0.25",
                                         facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=2))
    bio.label(ax, (0.7, y1 - 0.3), name, size="tiny", ha="left", color=P.muted())
x1, x2 = 3.6, 9.2
node((x1, 13.7), "Gurken → Torpedo", "highlight")
node((x2, 13.7), "pipe off", "negative", w=2.6, italic=False)
bio.arrow(ax, (x1 + 1.85, 13.7), (x2 - 1.35, 13.7), kind="inhibition")
node((x2, 11.4), "Pipe (sulfotransferase)", "enzyme", w=4.2)
node((x1, 11.4), "pipe on", "positive", w=2.6)
bio.arrow(ax, (x1 + 1.35, 11.4), (x2 - 2.15, 11.4), kind="process")
node((x2, 9.4), "sulfated vitelline proteins", "neutral", w=4.6)
bio.arrow(ax, (x2, 11.0), (x2, 9.8), kind="process")
node((x1, 8.3), "Ndl, GD → Snake → Easter", "enzyme", w=4.6)
bio.arrow(ax, (x2 - 1.6, 9.0), (x1 + 1.3, 8.7), kind="activation", bend=0.1)
node((x2, 7.3), "Spätzle → cleaved Spätzle", "receptor", w=4.8)
bio.arrow(ax, (x1 + 2.35, 8.1), (x2 - 2.45, 7.5), kind="catalysis")
node((x2, 5.3), "Toll", "receptor", w=2.4)
bio.arrow(ax, (x2, 6.9), (x2, 5.7), kind="activation")
node((x1, 5.3), "MyD88 · Tube · Pelle", "protein", w=4.0)
bio.arrow(ax, (x2 - 1.25, 5.3), (x1 + 2.05, 5.3), kind="activation")
node((x1, 3.5), "Cactus · Dorsal", "protein", w=3.4)
bio.arrow(ax, (x1, 4.9), (x1, 3.9), kind="catalysis")
bio.label(ax, (x1 + 2.0, 4.4), "phosphorylation,\ndegradation of Cactus", size="tiny", color=P.muted(), ha="left")
node((x1, 1.4), "Dorsal in the nucleus", "dna", w=4.0)
bio.arrow(ax, (x1, 3.1), (x1, 1.8), kind="process")
node((x2, 1.4), "twist, snail on; dpp, zen off", "dna2", w=5.0, italic=False)
bio.arrow(ax, (x1 + 2.05, 1.4), (x2 - 2.55, 1.4), kind="activation")

# mammalian homologues
X = 16.8
bio.label(ax, (X, 14.4), "Mammalian innate immunity", size="small", bold=True)
pairs = [(7.3, "microbial ligand (e.g. LPS)"), (5.3, "Toll-like receptor"), (4.4, "MyD88 · IRAK"), (3.5, "IκB · NF-κB"),
         (1.4, "NF-κB in the nucleus")]
for y, txt in pairs:
    node((X, y), txt, "neutral", w=6.2)
for (ya, _), (yb, _) in zip(pairs[:-1], pairs[1:]):
    bio.arrow(ax, (X, ya - 0.4), (X, yb + 0.4), kind="activation")
for y in (5.3, 3.5, 1.4):
    ax.plot([12.9, 13.6], [y, y], color=P.muted(), lw=0.8, ls=(0, (2, 2)))
bio.label(ax, (X, 0.3), "homologous steps: Toll/TLR, Pelle/IRAK, Cactus/IκB, Dorsal/NF-κB", size="tiny", color=P.muted())
