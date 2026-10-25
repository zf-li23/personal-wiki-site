# pUC19 and blue-white screening. A: map of pUC19 (2686 bp): the pMB1-derived origin (high copy number), the
# bla gene (ampicillin resistance) and the lacZ-alpha fragment with the multiple cloning site (MCS) inside it,
# under the lac promoter. B: the logic of selection and screening on ampicillin + X-gal + IPTG plates in a
# lacZ-delta-M15 host: cells without plasmid die; cells with re-ligated vector make the alpha peptide, which
# complements the host omega fragment, and form blue colonies; an insert in the MCS disrupts lacZ-alpha and
# gives white colonies.
import numpy as np
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(21.0, 9.4)
bio.panel(ax, "A", (0.1, 9.3))
G.plasmid(ax, (5.2, 4.5), 2.8, 2686, name="pUC19", ticks=500, features=[
    {"name": "lacZα", "start": 146, "end": 469, "strand": -1, "token": "dna", "italic": True},
    {"name": "MCS", "start": 396, "end": 454, "strand": 0, "token": "neutral", "track": 1},
    {"name": "lac promoter", "start": 514, "end": 544, "strand": -1, "token": "positive"},
    {"name": "ori", "start": 867, "end": 1455, "strand": -1, "token": "highlight"},
    {"name": "bla (AmpR)", "inside": False, "start": 1626, "end": 2486, "strand": -1, "token": "receptor"},
], sites=[("EcoRI", 396), ("KpnI", 408), ("BamHI", 417), ("XbaI", 423), ("SalI", 429), ("PstI", 435), ("HindIII", 447)])

bio.panel(ax, "B", (11.0, 9.3))
bio.label(ax, (11.5, 8.95), "Plate: ampicillin + X-gal + IPTG, host lacZΔM15", size="normal", bold=True, ha="left")
rows = [
    ("no plasmid", None, "killed by ampicillin", "no colony"),
    ("vector re-ligated", "dna", "LacZα + ΔM15 → active β-galactosidase", "blue colony"),
    ("vector + insert", "positive", "insert in MCS disrupts lacZα", "white colony: recombinant"),
]
for k, (name, tok, why, result) in enumerate(rows):
    y = 7.4 - 2.25 * k
    bio.label(ax, (11.5, y + 0.45), name, size="small", bold=True, ha="left")
    if tok:
        c, R = np.array([12.4, y - 0.35]), 0.6
        th = np.linspace(0, 2 * np.pi, 160)
        ax.plot(c[0] + R * np.cos(th), c[1] + R * np.sin(th), color=P.edge("neutral"), lw=2.0, zorder=9)
        arc = np.linspace(np.radians(40), np.radians(140), 60)
        ax.plot(c[0] + R * np.cos(arc), c[1] + R * np.sin(arc), color=P.edge("dna"), lw=5, zorder=10,
                solid_capstyle="butt")
        if tok == "positive":
            mid = np.linspace(np.radians(75), np.radians(105), 30)
            ax.plot(c[0] + R * np.cos(mid), c[1] + R * np.sin(mid), color=P.edge("positive"), lw=7, zorder=11,
                    solid_capstyle="butt")
    else:
        bio.label(ax, (12.4, y - 0.35), "—", size="normal", color=P.muted())
    bio.label(ax, (13.4, y - 0.2), why, size="small", ha="left")
    col = {"blue colony": "dna", "white colony: recombinant": "neutral"}.get(result)
    cx = 19.4
    if col:
        ax.add_patch(bio.core.Circle((cx, y - 0.2), 0.42, facecolor=P.fill(col) if col == "dna" else P.surface(),
                                     edgecolor=P.edge(col), lw=1.3, zorder=10))
    bio.label(ax, (cx, y - 0.95), result, size="tiny", color=P.muted())
bio.label(ax, (11.5, 0.85), "blue arc: lacZα; green: insert", size="tiny", ha="left", color=P.muted())
bio.label(ax, (11.5, 0.45), "X-gal is cleaved by β-galactosidase to a blue dye; IPTG inactivates LacI",
          size="tiny", ha="left", color=P.muted())
