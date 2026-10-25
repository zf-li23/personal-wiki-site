"""Amphipathic helices. A: helical wheel (100 degrees per residue, viewed from the N-terminus) of the
first 18 residues of magainin 2 with the hydrophobic moment vector (Eisenberg consensus scale).
B: hydrophobic moment per residue as a function of the assumed angle between residues; the peak
near 100 degrees shows that the sequence is periodic like an alpha helix. C: heptad wheel of the
GCN4 leucine zipper (GCN4-p1), two parallel helices related by a twofold axis."""

import math

import numpy as np
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import charts

P = bio.P
EISENBERG = {"A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29, "Q": -0.85, "E": -0.74, "G": 0.48,
             "H": -0.40, "I": 1.38, "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12, "S": -0.18,
             "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08}
MAGAININ = "GIGKFLHSAKKFGKAFVGEIMNS"
GCN4 = "RMKQLEDKVEELLSKNYHLENEVARLKKLVGER"


def aa_fill(c):
    for name, (col, members) in P.AMINO_ACID_CLASS.items():
        if c in members:
            return col
    return P.fill("neutral")


def moment(seq, delta_deg):
    h = np.array([EISENBERG[c] for c in seq])
    k = np.arange(len(seq))
    z = np.sum(h * np.exp(1j * np.radians(delta_deg) * k))
    return abs(z) / len(seq), math.degrees(math.atan2(z.imag, z.real))


fig, ax = bio.canvas(22.4, 9.0)

# --- A: helical wheel -------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.9))
seq = MAGAININ[:18]
c = np.array([4.0, 4.6])
R = 2.75
pos = []
for k, aa in enumerate(seq):
    th = math.radians(90 - 100 * k)            # clockwise seen from the N-terminus
    pos.append(c + R * np.array([math.cos(th), math.sin(th)]))
for k in range(len(seq) - 1):
    a, b = pos[k], pos[k + 1]
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.muted(), lw=0.6, alpha=0.6 if k else 1.0, zorder=3)
for k, aa in enumerate(seq):
    ax.add_patch(Circle(pos[k], 0.38, facecolor=aa_fill(aa), edgecolor=P.muted(), lw=0.7, zorder=6))
    bio.label(ax, pos[k], aa, size="small", bold=True, color=P.on_fill(), zorder=7)
    off = (pos[k] - c) / R * 0.62
    bio.label(ax, pos[k] + off, str(k + 1), size="tiny", color=P.muted(), zorder=7)
mu, _ = moment(seq, 100.0)
vsum = sum(EISENBERG[aa] * (pos[k] - c) / R for k, aa in enumerate(seq)) / len(seq)   # same vector, wheel frame
tip = c + vsum / np.linalg.norm(vsum) * 1.9
bio.arrow(ax, tuple(c), tuple(tip), kind="process", color=P.edge("highlight"), lw=2.0)
ax.add_patch(Circle(c, 0.08, color=P.ink(), zorder=8))
bio.label(ax, tuple(c + np.array([0, -0.55])), f"μH = {mu:.2f}", size="tiny", color=P.edge("highlight"), bold=True)
bio.label(ax, (4.0, 0.95), "Magainin 2 (residues 1-18), viewed from N-terminus", size="small")
# legend for the residue classes
names = {"hydrophobic": "hydrophobic", "polar": "polar", "positive": "basic", "negative": "acidic"}
for i, (key, (col, _)) in enumerate(P.AMINO_ACID_CLASS.items()):
    x = 0.6 + i * 1.95
    ax.add_patch(Circle((x, 0.3), 0.16, facecolor=col, edgecolor=P.muted(), lw=0.6))
    bio.label(ax, (x + 0.25, 0.3), names[key], size="tiny", ha="left")

# --- B: hydrophobic moment spectrum ------------------------------------------------------------
bio.panel(ax, "B", (8.0, 8.9))
pax = charts.axes_at(ax, (9.3, 1.6, 4.6, 6.4))
deltas = np.arange(0, 181, 1.0)
spec = np.array([moment(MAGAININ, d)[0] for d in deltas])
pax.plot(deltas, spec, color=charts.line("highlight"), lw=1.6)
best = deltas[np.argmax(spec)]
pax.axvspan(95, 105, color=P.mix(P.fill("receptor"), P.surface(), 0.5), lw=0, zorder=0)
pax.axvspan(160, 180, color=P.mix(P.fill("highlight"), P.surface(), 0.5), lw=0, zorder=0)
pax.annotate(f"peak {best:.0f}°", (best, spec.max()), (best + 18, spec.max() + 0.02),
             fontsize=bio.core.FONT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
pax.text(100, 0.03, "α helix\n(100°)", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pax.text(170, 0.03, "β strand\n(~170°)", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pax.set_xlim(0, 180)
pax.set_ylim(0, spec.max() * 1.25)
pax.set_xticks([0, 60, 100, 140, 180])
charts.style_axes(pax, "angle between residues δ / °", "hydrophobic moment per residue")
charts.title(pax, "Magainin 2, all 23 residues")

# --- C: coiled-coil heptad wheel ---------------------------------------------------------------
bio.panel(ax, "C", (14.6, 8.9))
letters = "abcdefg"
heptad = {L: [] for L in letters}
for i, aa in enumerate(GCN4):
    heptad[letters[(i - 1) % 7]].append(aa)
step = -360.0 * 2 / 7                       # 3.5 residues per turn in a coiled coil
theta_a = -180.0 / 7                        # a and d symmetric about the interface
centers = (np.array([16.9, 4.7]), np.array([20.5, 4.7]))
rr = 1.25
for h, cc in enumerate(centers):
    ax.add_patch(Circle(cc, 0.55, facecolor=P.light("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=4))
    for k, L in enumerate(letters):
        th = math.radians(theta_a + k * step + (180.0 if h else 0.0))
        p = cc + rr * np.array([math.cos(th), math.sin(th)])
        core = L in "ad"
        tok = aa_fill("L") if core else (P.fill("highlight") if L in "eg" else P.fill("neutral"))
        ax.add_patch(Circle(p, 0.34, facecolor=tok, edgecolor=P.muted(), lw=0.7, zorder=6))
        bio.label(ax, tuple(p), L + ("′" if h else ""), size="small", bold=True, color=P.on_fill(), zorder=7)
        q = cc + (rr + 0.62 + (0.18 if L in "bcf" else 0.0)) * np.array([math.cos(th), math.sin(th)])
        txt = "".join(heptad[L])
        if L in "ad" or L in "eg":
            if (h == 0 and math.cos(th) > 0.2) or (h == 1 and math.cos(th) < -0.2):
                continue                       # interface labels are written below the wheels
        bio.label(ax, tuple(q), txt, size="tiny", color=P.muted(), zorder=7)
ax.plot([18.7, 18.7], [3.0, 6.4], color=P.muted(), lw=0.6, ls=(0, (2, 2)))
bio.label(ax, (18.7, 6.75), "twofold axis", size="tiny", color=P.muted())
yb = 2.0
for i, (L, text) in enumerate((("a", "a: " + " ".join(heptad["a"])), ("d", "d: " + " ".join(heptad["d"])),
                               ("e", "e: " + " ".join(heptad["e"])), ("g", "g: " + " ".join(heptad["g"])))):
    bio.label(ax, (16.0 + (i % 2) * 3.5, yb - (i // 2) * 0.45), text, size="tiny", ha="left")
bio.label(ax, (18.7, 0.95), "GCN4 leucine zipper: a, d core; g–e′ ion pairs", size="small")
bio.label(ax, (18.7, 8.3), "Coiled coil, viewed from N-termini", size="small", bold=True)
bio.label(ax, (4.0, 8.3), "Helical wheel", size="small", bold=True)
