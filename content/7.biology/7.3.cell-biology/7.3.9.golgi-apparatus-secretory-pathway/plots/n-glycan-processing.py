# Processing of an N-linked glycan from the ER through the Golgi stack (SNFG symbols; reducing end at the
# bottom, attached to Asn). ER: Man8GlcNAc2 after glucose trimming and ER mannosidase I. cis Golgi: Golgi
# mannosidase I trims to Man5GlcNAc2 (lysosomal hydrolases are instead tagged with mannose 6-phosphate here).
# medial Golgi: GlcNAc transferase I adds GlcNAc to the alpha1-3 arm; mannosidase II removes two mannoses;
# GlcNAc transferase II adds GlcNAc to the alpha1-6 arm, and core fucosylation adds Fuc. trans Golgi and
# TGN: galactosyl- and sialyltransferases complete a complex biantennary glycan. Endoglycosidase H cleaves
# the glycan until mannosidase II has acted; resistance to Endo H therefore marks arrival in the medial Golgi.
import wikibio as bio
from wikibio import glycan as G

fig, ax = bio.canvas(24, 11)
P = bio.P
cols = [("ER", "er", 1.6), ("cis Golgi", "golgi", 5.4), ("medial Golgi", "golgi", 9.6), ("medial Golgi", "golgi", 13.4),
        ("medial Golgi", "golgi", 17.2), ("trans Golgi / TGN", "golgi", 21.4)]
STR = [
    "Man(a1-2)Man(a1-6)[Man(a1-3)]Man(a1-6)[Man(a1-2)Man(a1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
    "Man(a1-6)[Man(a1-3)]Man(a1-6)[Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
    "Man(a1-6)[Man(a1-3)]Man(a1-6)[GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
    "Man(a1-6)[GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)GlcNAc(b1-",
    "GlcNAc(b1-2)Man(a1-6)[GlcNAc(b1-2)Man(a1-3)]Man(b1-4)GlcNAc(b1-4)[Fuc(a1-6)]GlcNAc(b1-",
    G.N_GLYCANS["complex"],
]
NAMES = ["Man8GlcNAc2", "Man5GlcNAc2", "GlcNAcMan5", "GlcNAcMan3", "GlcNAc2Man3Fuc", "complex, sialylated"]
ENZ = ["Golgi Man I", "GlcNAc-T I", "Man II", "GlcNAc-T II,\nFuc-T", "Gal-T, Sia-T"]
bands = [(0.2, 3.3, "er", "ER"), (3.5, 7.3, "golgi", "cis"), (7.5, 19.2, "golgi", "medial"), (19.4, 23.8, "golgi", "trans / TGN")]
for x0, x1, tok, name in bands:
    ax.add_patch(bio.core.FancyBboxPatch((x0, 0.9), x1 - x0, 9.6, boxstyle="round,pad=0,rounding_size=0.3",
                                         facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.0, zorder=0))
    bio.label(ax, ((x0 + x1) / 2, 10.1), name, size="normal", bold=True, color=P.edge(tok))
for k, ((_, _, x), s) in enumerate(zip(cols, STR)):
    G.draw(ax, s, at=(x, 2.2), direction="up", step=0.95, row=0.8, size=0.4, labels=None, aglycone="Asn", stub=0.45)
    bio.label(ax, (x, 1.25), NAMES[k], size="tiny")
for k, e in enumerate(ENZ):
    xa, xb = cols[k][2] + 1.25, cols[k + 1][2] - 1.25
    if k == 4:
        xb = cols[k + 1][2] - 1.9
    bio.arrow(ax, (xa, 5.0), (xb, 5.0), kind="process")
    bio.label(ax, ((xa + xb) / 2, 5.55), e, size="tiny", va="bottom")
# Endo H sensitivity bar
ax.plot([0.6, 12.0], [0.55, 0.55], color=P.edge("negative"), lw=3)
ax.plot([12.4, 23.6], [0.55, 0.55], color=P.edge("positive"), lw=3)
bio.label(ax, (6.3, 0.22), "Endo H sensitive", size="tiny")
bio.label(ax, (18.0, 0.22), "Endo H resistant", size="tiny")
G.legend(ax, (8.6, 9.3), ["Man", "GlcNAc", "Gal", "Fuc", "Neu5Ac"], cols=5, dx=2.0, size=0.34, label_size="tiny")
