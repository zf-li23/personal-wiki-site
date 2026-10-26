"""Origin of the ring atoms of purines and pyrimidines (isotope-tracer experiments of Buchanan and Greenberg).
Purine (left): N1 from the amino group of aspartate; C2 and C8 from formate carried as N10-formyltetrahydrofolate;
N3 and N9 from the amide nitrogen of glutamine; C4, C5 and N7 from glycine (the whole molecule); C6 from CO2
(bicarbonate). The ring is built on ribose 5-phosphate, attached at N9 throughout.
Pyrimidine (right): C2 from bicarbonate and N3 from the amide of glutamine, both through carbamoyl phosphate;
N1, C4, C5 and C6 from aspartate. The ring is closed first and attached to ribose 5-phosphate (at N1) as orotate."""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 9.6)
ink = P.ink()

SRC = {
    "Asp": ("channel", "Aspartate"),
    "Gln": ("receptor", "Glutamine (amide N)"),
    "Gly": ("positive", "Glycine"),
    "fTHF": ("highlight", "N¹⁰-Formyl-THF"),
    "CO2": ("drug", "HCO₃⁻ / CO₂"),
}
R_ATOM = 0.42


def atom(xy, text, src):
    tok = SRC[src][0]
    bio.box(ax, xy, 2 * R_ATOM, 2 * R_ATOM, token=tok, text=text, radius=R_ATOM, size="small", zorder=6)


def bond(a, b, double=False):
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = (b - a) / np.hypot(*(b - a))
    p, q = a + d * R_ATOM, b - d * R_ATOM
    ax.plot([p[0], q[0]], [p[1], q[1]], color=ink, lw=2.0, zorder=3, solid_capstyle="round")


def hexagon(center, r, start=90):
    return [(center[0] + r * np.cos(np.radians(start + 60 * k)), center[1] + r * np.sin(np.radians(start + 60 * k)))
            for k in range(6)]


# ---------- purine ----------
r = 1.35
hx = hexagon((6.4, 4.9), r)  # 0 top, 1 upper-left, 2 lower-left, 3 bottom, 4 lower-right, 5 upper-right
C6, N1, C2, N3, C4, C5 = hx
# imidazole ring on the C4-C5 edge (to the right)
mid = (np.array(C4) + np.array(C5)) / 2
side = np.hypot(*(np.array(C5) - np.array(C4)))
apothem = side / (2 * np.tan(np.radians(36)))
cen5 = mid + np.array([apothem, 0.0])
R5 = side / (2 * np.sin(np.radians(36)))
ang = [np.degrees(np.arctan2(*(np.array(p) - cen5)[::-1])) for p in (C5, C4)]
N7 = tuple(cen5 + R5 * np.array([np.cos(np.radians(ang[0] - 72)), np.sin(np.radians(ang[0] - 72))]))
C8 = tuple(cen5 + R5 * np.array([np.cos(np.radians(ang[0] - 144)), np.sin(np.radians(ang[0] - 144))]))
N9 = tuple(cen5 + R5 * np.array([np.cos(np.radians(ang[0] - 216)), np.sin(np.radians(ang[0] - 216))]))
for a, b in [(C6, N1), (N1, C2), (C2, N3), (N3, C4), (C4, C5), (C5, C6), (C5, N7), (N7, C8), (C8, N9), (N9, C4)]:
    bond(a, b)
for xy, t, s in [(N1, "N1", "Asp"), (C2, "C2", "fTHF"), (N3, "N3", "Gln"), (C4, "C4", "Gly"), (C5, "C5", "Gly"),
                 (C6, "C6", "CO2"), (N7, "N7", "Gly"), (C8, "C8", "fTHF"), (N9, "N9", "Gln")]:
    atom(xy, t, s)
# ribose 5-phosphate on N9
rib = (N9[0] + 0.2, N9[1] - 1.5)
ax.plot([N9[0], rib[0]], [N9[1] - R_ATOM, rib[1] + 0.35], color=ink, lw=2.0, zorder=3)
bio.box(ax, rib, 2.4, 0.7, token="carbohydrate", text="ribose 5-P", size="small")
# glycine bracket: C4-C5-N7 come in together
bio.label(ax, (6.4, 8.95), "Purine ring (as in IMP)", size="title", bold=True)

# sources with leader arrows
def source(xy, src, targets, ha="center"):
    tok, name = SRC[src]
    bio.box(ax, xy, 2.9, 0.72, token=tok, text=name, size="small")
    for t in targets:
        bio.arrow(ax, xy, t, kind="process", color=P.edge(tok), lw=1.4, shrink=0.52, head=0.18)


source((2.4, 7.4), "CO2", [C6])
source((2.0, 4.3), "Asp", [N1])
source((2.0, 2.6), "fTHF", [C2])
source((9.6, 8.3), "Gly", [N7, C5])
bio.label(ax, (11.25, 8.3), "C4, C5, N7\n(whole molecule)", size="tiny", color=P.muted(), ha="left")
source((12.2, 4.6), "fTHF", [C8])
source((6.0, 1.0), "Gln", [N3, N9])

# ---------- pyrimidine ----------
hy = hexagon((17.6, 4.9), r)  # 0 top, 1 upper-left, 2 lower-left, 3 bottom, 4 lower-right, 5 upper-right
pC4, pN3, pC2, pN1, pC6, pC5 = hy
for a, b in zip(hy, hy[1:] + hy[:1]):
    bond(a, b)
for xy, t, s in [(pC4, "C4", "Asp"), (pN3, "N3", "Gln"), (pC2, "C2", "CO2"), (pN1, "N1", "Asp"),
                 (pC6, "C6", "Asp"), (pC5, "C5", "Asp")]:
    atom(xy, t, s)
rib2 = (pN1[0], pN1[1] - 1.5)
ax.plot([pN1[0], rib2[0]], [pN1[1] - R_ATOM, rib2[1] + 0.35], color=ink, lw=2.0, zorder=3)
bio.box(ax, rib2, 3.6, 0.7, token="carbohydrate", text="ribose 5-P (added last)", size="small")
bio.label(ax, (17.6, 8.95), "Pyrimidine ring (as in UMP)", size="title", bold=True)
# aspartate: the N1-C6-C5-C4 unit
bio.box(ax, (20.6, 2.6), 2.2, 0.72, token="channel", text="Aspartate", size="small")
bio.label(ax, (20.6, 1.95), "N1, C4, C5, C6", size="tiny", color=P.muted())
for t in (pC5, pC6):
    bio.arrow(ax, (20.6, 2.96), t, kind="process", color=P.edge("channel"), lw=1.4, shrink=0.5, head=0.18)
bio.box(ax, (14.2, 7.7), 3.4, 0.72, token="neutral", text="Carbamoyl phosphate", size="small")
bio.label(ax, (14.2, 8.35), "(CPS II: Gln + HCO₃⁻ + 2 ATP)", size="tiny", color=P.muted())
for t in (pN3, pC2):
    bio.arrow(ax, (14.2, 7.34), t, kind="process", color=P.edge("neutral"), lw=1.4, shrink=0.5, head=0.18)

# legend
for i, k in enumerate(["Asp", "Gln", "Gly", "fTHF", "CO2"]):
    tok, name = SRC[k]
    x = 11.0 + 2.15 * i
    bio.box(ax, (x - 0.75, 0.55), 0.36, 0.36, token=tok, radius=0.18)
    bio.label(ax, (x - 0.5, 0.55), k if k != "fTHF" else "f-THF", size="tiny", ha="left")
