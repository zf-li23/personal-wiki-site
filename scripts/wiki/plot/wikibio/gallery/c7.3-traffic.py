# The machinery of vesicle traffic (wikibio.traffic). A: a clathrin triskelion and a 60-triskelion
# "soccer ball" cage around its vesicle. B: budding of a clathrin-coated vesicle, from a flat coated patch
# to a constricted neck with a dynamin collar and a free coated vesicle. C: the three coats seen in
# section (COPII, COPI, clathrin with its adaptor layer). D: the GDP/GTP cycle of a Rab protein with GEF,
# GAP, GDI and an effector. E: a partially zippered trans-SNARE complex and the NSF hexamer with alpha-SNAPs.
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(20, 14)
P = bio.P

bio.panel(ax, "A", (0.2, 13.8))
T.triskelion(ax, (2.2, 11.4), 1.3, angle=10, labels=True)
T.cage(ax, (6.2, 11.4), 1.8, kind="clathrin", rotation=(18, 28, 0))
bio.label(ax, (6.2, 9.2), "Clathrin cage (60 triskelia)", size="small")

bio.panel(ax, "B", (9.0, 13.8))
for k, st in enumerate((0.0, 0.35, 0.65, 0.88)):
    x0 = 9.2 + k * 2.3
    a = T.bud(ax, (x0, 10.0), (x0 + 2.1, 10.0), at=1.05, stage=st, r=0.6, kind="clathrin", side=-1, cargo=3)
    if st > 0.8:
        T.dynamin(ax, a["neck_center"] + (0, -0.12), 2 * a["neck_halfwidth"] + 0.16, rings=2, axis=90)
c = (19.0, 8.3)
T.coated_vesicle(ax, c, 0.6, kind="clathrin", cargo=3)
bio.label(ax, (14.5, 11.2), "Coated pit  →  constricted neck (dynamin)  →  vesicle", size="small")
bio.label(ax, (9.2, 10.9), "Lumen / outside", size="tiny", ha="left", color=P.muted())
bio.label(ax, (9.4, 7.8), "Cytosol", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "C", (0.2, 7.6))
for k, kind in enumerate(("copii", "copi", "clathrin")):
    xy = (1.6 + k * 2.6, 5.6)
    T.coated_vesicle(ax, xy, 0.6, kind=kind, cargo=3)
    bio.label(ax, (xy[0], 4.45), {"copii": "COPII", "copi": "COPI", "clathrin": "Clathrin/AP"}[kind], size="small")

bio.panel(ax, "D", (8.6, 7.6))
T.gtpase_cycle(ax, (11.9, 3.6), w=3.4, name="Rab", gdi="GDI", effector="Effector")

bio.panel(ax, "E", (16.0, 7.6))
T.snare_complex(ax, 19.4, 5.2, 3.6, zipped=0.6, length=2.4, labels=True)
T.nsf(ax, (17.4, 1.2), 0.45)
bio.label(ax, (18.2, 1.2), "NSF hexamer + α-SNAP", size="tiny", ha="left")
