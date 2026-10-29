"""The founder cells of the C. elegans embryo. Each division of the P lineage is asymmetric and produces one
somatic founder cell (AB, MS and E from EMS, C, D) and one P cell; P4 forms the germ line. Bars beneath
the founders show their main products (germ-layer colours: ectoderm blue, mesoderm red, endoderm yellow,
germ line purple); the numbers are the cells each founder contributes to the hatched larva, out of 558
(another 113 cells generated in the embryo die by programmed cell death)."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(21, 10.4)
tok = {"ec": E.tok("ectoderm"), "me": E.tok("mesoderm"), "en": E.tok("endoderm"), "gl": E.tok("germline"), "mix": "neutral"}
nodes = {"P0": (10.5, 9.4), "AB": (5.0, 7.6), "P1": (14.0, 7.6), "ABa": (3.0, 5.8), "ABp": (7.0, 5.8), "EMS": (11.4, 5.8),
         "P2": (16.8, 5.8), "MS": (10.2, 4.0), "E": (12.6, 4.0), "C": (15.4, 4.0), "P3": (18.2, 4.0), "D": (17.2, 2.2),
         "P4": (19.4, 2.2)}
edges = [("P0", "AB"), ("P0", "P1"), ("AB", "ABa"), ("AB", "ABp"), ("P1", "EMS"), ("P1", "P2"), ("EMS", "MS"), ("EMS", "E"),
         ("P2", "C"), ("P2", "P3"), ("P3", "D"), ("P3", "P4")]
for a, b in edges:
    (xa, ya), (xb, yb) = nodes[a], nodes[b]
    ax.plot([xa, xa, xb, xb], [ya - 0.35, ya - 0.75, ya - 0.75, yb + 0.35], color=P.ink(), lw=1.1, zorder=3, solid_joinstyle="miter")
col = {"P0": "mix", "AB": "ec", "P1": "mix", "ABa": "ec", "ABp": "ec", "EMS": "mix", "P2": "mix", "MS": "me", "E": "en", "C": "mix",
       "P3": "mix", "D": "me", "P4": "gl"}
for k, (x, y) in nodes.items():
    bio.box(ax, (x, y), 1.3, 0.62, tok[col[k]], k, size="small")
fates = {"ABa": ("neurons, hypodermis,\nanterior pharynx", "ec", "389 (AB)"), "ABp": ("neurons, hypodermis,\nspecialized cells", "ec", ""),
         "MS": ("body muscle, posterior\npharynx, glands", "me", "80"), "E": ("intestine\n(20 cells)", "en", "20"),
         "C": ("hypodermis,\nbody muscle", "mix", "47"), "D": ("body muscle", "me", "20"), "P4": ("germ line", "gl", "2")}
for k, (text, t, n) in fates.items():
    x, y = nodes[k]
    yy = 2.95 if k in ("ABa", "ABp") else (1.2 if k in ("D", "P4") else 2.95)
    if k in ("D", "P4"):
        yy = 1.15
    if k in ("MS", "E", "C"):
        yy = 2.6
    ax.plot([x - 0.6, x + 0.6], [yy + 0.55, yy + 0.55], color=P.edge(tok[t]), lw=4, solid_capstyle="butt")
    bio.label(ax, (x, yy), text, size="tiny", va="top" if False else "center")
    if n:
        bio.label(ax, (x, yy - 0.75), n, size="tiny", color=P.muted())
bio.label(ax, (0.4, 9.9), "Founder cells of the C. elegans embryo", size="small", bold=True, ha="left")
bio.arrow(ax, (20.5, 9.0), (20.5, 6.6), kind="process", head=0.2, color=P.muted())
bio.label(ax, (20.7, 7.8), "time", size="tiny", color=P.muted(), ha="left", rotation=90)
