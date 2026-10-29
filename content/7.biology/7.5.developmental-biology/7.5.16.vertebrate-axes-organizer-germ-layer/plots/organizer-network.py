# Signals that pattern the Xenopus gastrula. Maternal VegT and Vg1 in the vegetal cells and dorsal beta-catenin
# (stabilized by Huluwa) together activate the Nodal-related genes (Xnr), most strongly on the dorsal side; high Nodal
# signalling with beta-catenin targets (Siamois, Twin) induces the organizer, which expresses transcription factors
# (Goosecoid, Lim1, Xnot) and secretes antagonists: Chordin, Noggin and Follistatin bind BMPs; Cerberus binds BMP,
# Nodal and Wnt; Dickkopf and Frzb block Wnt. Ventral BMP4 and Wnt8 promote ventral mesoderm and epidermis; their
# inhibition dorsally gives dorsal mesoderm and neural tissue.
import wikibio as bio

fig, ax = bio.canvas(22.0, 12.0)
P = bio.P


def node(xy, text, tok, w=3.0, italic=False):
    bio.box(ax, xy, w, 0.75, token=tok, text=text, size="small", italic=italic)


ax.add_patch(bio.core.FancyBboxPatch((0.4, 0.4), 10.0, 11.2, boxstyle="round,pad=0,rounding_size=0.3", facecolor=P.fill("cytoplasm"),
                                     edgecolor=P.edge("cytoplasm"), lw=1.0, zorder=1))
bio.label(ax, (0.8, 11.2), "Dorsal side", size="small", bold=True, ha="left")
ax.add_patch(bio.core.FancyBboxPatch((11.6, 0.4), 10.0, 11.2, boxstyle="round,pad=0,rounding_size=0.3", facecolor=P.fill("extracellular"),
                                     edgecolor=P.edge("extracellular"), lw=1.0, zorder=1))
bio.label(ax, (21.2, 11.2), "Ventral side", size="small", bold=True, ha="right")
node((2.6, 9.9), "Huluwa", "positive")
node((2.6, 8.4), "β-catenin", "protein")
node((7.6, 9.9), "VegT, Vg1", "highlight")
node((7.6, 8.4), "Nodal (Xnr)", "receptor")
node((2.6, 6.6), "Siamois, Twin", "dna2")
node((5.2, 4.9), "Organizer: Gsc, Lim1", "cl", w=4.4)
bio.arrow(ax, (2.6, 9.5), (2.6, 8.8), kind="activation", bg=P.fill("cytoplasm"))
bio.arrow(ax, (7.6, 9.5), (7.6, 8.8), kind="activation", bg=P.fill("cytoplasm"))
bio.arrow(ax, (4.1, 8.4), (6.05, 8.4), kind="activation", bg=P.fill("cytoplasm"))
bio.arrow(ax, (2.6, 8.0), (2.6, 7.0), kind="activation", bg=P.fill("cytoplasm"))
bio.arrow(ax, (2.9, 6.2), (4.4, 5.3), kind="activation", bg=P.fill("cytoplasm"))
bio.arrow(ax, (7.3, 8.0), (5.9, 5.3), kind="activation", bg=P.fill("cytoplasm"))
anta = [("Chordin, Noggin,\nFollistatin", 1.3), ("Cerberus", 2.5), ("Dkk1, Frzb", 3.6)]
ys = [2.6, 2.6, 2.6]
for k, (txt, _) in enumerate(anta):
    x = 2.0 + 3.2 * k
    bio.box(ax, (x, 2.3), 2.9, 1.0, token="metabolite", text=txt, size="tiny")
    bio.arrow(ax, (5.2, 4.5), (x, 2.85), kind="process", bg=P.fill("cytoplasm"))
node((16.6, 8.4), "BMP2, 4, 7", "drug")
node((16.6, 6.6), "Wnt8", "drug")
node((16.6, 4.4), "ventral mesoderm,\nepidermis", "neutral", w=3.6)
bio.arrow(ax, (16.6, 8.0), (16.6, 7.0), kind="link")
bio.arrow(ax, (16.6, 6.2), (16.6, 4.85), kind="activation", bg=P.fill("extracellular"))
bio.arrow(ax, (15.0, 8.2), (16.0, 4.85), kind="activation", bend=0.15, bg=P.fill("extracellular"))
bio.arrow(ax, (3.45, 2.85), (15.0, 8.4), kind="inhibition", bend=-0.1)
bio.arrow(ax, (6.6, 2.85), (15.0, 8.0), kind="inhibition", bend=-0.08)
bio.arrow(ax, (6.6, 2.85), (15.0, 6.6), kind="inhibition", bend=-0.05)
bio.arrow(ax, (9.4, 2.85), (15.0, 6.3), kind="inhibition", bend=-0.04)
bio.label(ax, (16.6, 1.6), "dorsally, where BMP and Wnt are blocked:\ndorsal mesoderm, neural plate, head", size="tiny", color=P.muted())
