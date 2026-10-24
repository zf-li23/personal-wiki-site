"""The D-aldoses from D-glyceraldehyde to the eight D-aldohexoses, as compact Fischer projections
(a horizontal stroke shows on which side the OH of each stereocentre lies; the hydrogens are
omitted). Each aldose gives two children by Kiliani-Fischer chain extension: the new stereocentre
is C2, with its OH on the right or on the left, and every older stereocentre keeps its place.
The OH of the highest-numbered stereocentre (the reference atom, red) is on the right in all of
them. A star marks the aldoses whose aldaric acid (both chain ends oxidized to COOH) is meso,
found from the pattern itself: the aldaric acid has a mirror plane exactly when the sequence of
sides reads the same from both ends."""

import matplotlib.pyplot as plt

NAMES = {
    "R": "glyceraldehyde",
    "RR": "erythrose", "LR": "threose",
    "RRR": "ribose", "LRR": "arabinose", "RLR": "xylose", "LLR": "lyxose",
    "RRRR": "allose", "LRRR": "altrose", "RLRR": "glucose", "LLRR": "mannose",
    "RRLR": "gulose", "LRLR": "idose", "RLLR": "galactose", "LLLR": "talose",
}
REF = "#dc2626"
STEP = 0.42  # vertical distance between carbons


def children(p):
    return ["R" + p, "L" + p]


def meso_aldaric(p):
    return p == p[::-1]


def fischer(ax, x, y, p):
    """Draw the aldose with side pattern p (C2 ... reference carbon) with its top (CHO) at (x, y)."""
    ink = plt.rcParams["text.color"]
    n = len(p)
    ax.text(x, y, "CHO", ha="center", va="center", fontsize=8.5)
    y0, y1 = y - 0.16, y - STEP * (n + 1) + 0.16
    ax.plot([x, x], [y0, y1], color=ink, lw=1.2)
    for i, side in enumerate(p):
        yy = y - STEP * (i + 1)
        colour = REF if i == n - 1 else ink
        dx = 0.32 if side == "R" else -0.32
        ax.plot([x, x + dx], [yy, yy], color=colour, lw=1.2)
        ax.text(x + dx * 1.75, yy, "OH", ha="center", va="center", fontsize=7.5, color=colour)
    ax.text(x, y - STEP * (n + 1), "CH$_2$OH", ha="center", va="center", fontsize=8.5)
    label = "D-" + NAMES[p] + (" *" if n > 1 and meso_aldaric(p) else "")
    ax.text(x, y - STEP * (n + 1) - 0.36, label, ha="center", va="center", fontsize=8.5, style="italic")
    return y - STEP * (n + 1) - 0.55  # bottom of the drawing


fig, ax = plt.subplots(figsize=(12, 8.4))
rows = [["R"]]
for _ in range(3):
    rows.append([c for p in rows[-1] for c in children(p)])
width = 16.0
ytop = [0.0, -2.3, -5.0, -8.1]
pos = {}
for r, row in enumerate(rows):
    for k, p in enumerate(row):
        x = (k + 0.5) * width / len(row) - width / 2
        bottom = fischer(ax, x, ytop[r], p)
        pos[p] = (x, ytop[r], bottom)
for r in range(1, 4):
    for p in rows[r]:
        parent = p[1:]
        xp, _, bp = pos[parent]
        x, yt, _ = pos[p]
        ax.plot([xp, x], [bp + 0.05, yt + 0.25], color="0.6", lw=0.8)
for r, label in enumerate(["C$_3$", "C$_4$", "C$_5$", "C$_6$"]):
    ax.text(-width / 2 - 0.4, ytop[r] - 0.5, label, ha="right", va="center", fontsize=10, color="0.45")
ax.text(width / 2, ytop[0] - 0.4, "* aldaric acid is meso\n(optically inactive)", ha="right", va="top", fontsize=9, color="0.4")
ax.set_xlim(-width / 2 - 1.2, width / 2 + 0.3)
ax.set_ylim(-10.9, 0.4)
ax.set_aspect("equal")
ax.axis("off")
