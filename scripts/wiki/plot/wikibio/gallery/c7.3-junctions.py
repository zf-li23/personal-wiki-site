# Cell junctions and the extracellular matrix (wikibio.junctions). A: a columnar epithelium with the
# junctional complex and basal junctions. B-E: close-ups of a tight junction, an adherens junction, a
# desmosome and a gap junction. F: a focal adhesion; G: a hemidesmosome on the basal lamina. H: integrin
# conformations. I: collagen from triple helix to quarter-staggered fibril and banded fibril. J: an
# aggrecan aggregate; K: laminin, fibronectin and elastin. L: the plant cell wall in face view and in
# section, and a plasmodesma.
import wikibio as bio
from wikibio import junctions as J

fig, ax = bio.canvas(30, 34)
P = bio.P

bio.panel(ax, "A", (0.2, 33.8))
a = J.epithelium(ax, 1.2, 11.0, 24.6, 7.2, n=3)
for key, txt, xy in (("tight", "Tight junction", (12.4, 31.2)), ("adherens", "Adherens belt", (12.4, 30.4)),
                     ("desmosome", "Desmosome", (12.4, 29.2)), ("gap", "Gap junction", (12.4, 26.9)),
                     ("hemidesmosome", "Hemidesmosome", (12.4, 24.2)), ("lamina", "Basal lamina", (12.4, 23.6))):
    bio.callout(ax, a[key], xy, txt)

for k, (fn, name) in enumerate(((J.tight_junction, "B  Tight junction"), (J.adherens_junction, "C  Adherens junction"),
                                (J.desmosome, "D  Desmosome"), (J.gap_junction, "E  Gap junction"))):
    x = 17.2 + (k % 2) * 6.6
    y0 = 27.6 if k < 2 else 20.4
    fn(ax, x, y0, y0 + 5.4)
    bio.label(ax, (x - 3.0, y0 + 5.9), name, size="small", bold=True, ha="left")

bio.panel(ax, "F", (0.2, 21.2))
f = J.focal_adhesion(ax, 1.0, 7.0, 17.6)
bio.callout(ax, f["talin"], (3.0, 20.4), "Talin")
bio.callout(ax, f["vinculin"], (5.0, 20.8), "Vinculin")
bio.callout(ax, f["fibronectin"], (0.8, 15.2), "Fibronectin")

bio.panel(ax, "G", (10.0, 21.2))
h = J.hemidesmosome(ax, 10.4, 15.4, 17.0)
bio.callout(ax, h["plaque"], (15.4, 18.6), "Plectin plaque")
bio.callout(ax, h["lamina"], (15.8, 15.2), "Basal lamina")

bio.panel(ax, "H", (0.2, 13.8))
for k, st in enumerate(("bent", "closed", "open")):
    xx = 1.6 + 2.2 * k
    J.integrin(ax, (xx, 12.2), state=st, ligand="fibronectin" if st == "open" else None)
    bio.label(ax, (xx, 9.4), st, size="small")
ax.plot([0.6, 7.6], [12.2, 12.2], color=P.edge("membrane"), lw=3)

bio.panel(ax, "I", (8.6, 13.8))
J.triple_helix(ax, (9.0, 13.0), (14.0, 13.0), width=0.32)
J.collagen_fibril(ax, (9.0, 10.4), 10.0, rows=5, D=0.9)
J.banded_fibril(ax, (9.0, 9.4), (19.0, 9.4), width=0.55, D=0.4)

bio.panel(ax, "J", (20.0, 13.8))
J.aggrecan_aggregate(ax, (20.4, 11.0), (29.4, 11.0), n=6)

bio.panel(ax, "K", (0.2, 8.2))
J.laminin(ax, (1.6, 6.6), 1.2)
J.fibronectin(ax, (3.2, 6.0), (6.4, 6.6))
J.elastin(ax, (9.0, 6.2), 2.2, 1.5, stretch=0.0)
J.elastin(ax, (13.6, 6.2), 2.2, 1.5, stretch=1.0)

bio.panel(ax, "L", (17.2, 8.2))
J.wall_face(ax, 17.6, 3.6, 4.0, 4.0)
J.wall_section(ax, 22.4, 29.6, 6.0)
J.plasmodesma(ax, (25.0, 1.6), wall=0.8)
J.basal_lamina(ax, 1.0, 9.0, 3.0, depth=1.0)
J.proteoglycan(ax, (10.6, 1.6), (14.6, 1.6), chains=10)
J.cellulose_synthase(ax, (16.2, 1.6), 0.4)
