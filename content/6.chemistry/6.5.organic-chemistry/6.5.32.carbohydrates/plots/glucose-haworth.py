"""D-Glucose in water: the open-chain aldehyde (Fischer projection) and the two pyranose
hemiacetals formed when the C5 hydroxyl adds to C1 (Haworth projections). Converting a Fischer
projection into a Haworth projection: a group on the right of the Fischer projection points down
in the Haworth projection, a group on the left points up; for a D-sugar the CH2OH on C5 points up.
The new stereocentre C1 (the anomeric carbon, red) carries its OH down (alpha, trans to the C5
CH2OH) or up (beta, cis). Equilibrium composition at 25 C: about 36% alpha, 64% beta, and of
the order of 0.003% open chain (the furanoses are below 1%)."""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

RED = "#dc2626"
# Fischer pattern of D-glucose, C2..C5: side of the OH
FISCHER = ["R", "L", "R", "R"]


def fischer(ax, x, y):
    ink = plt.rcParams["text.color"]
    ax.text(x, y, "CHO", ha="center", va="center", fontsize=11, color=RED)
    for i, side in enumerate(FISCHER):
        yy = y - 0.62 * (i + 1)
        ax.plot([x, x], [yy + 0.47, yy - 0.15 if i < 3 else yy - 0.47], color=ink, lw=1.3)
        ax.plot([x - 0.55, x + 0.55], [yy, yy], color=ink, lw=1.3)
        left, right = ("H", "OH") if side == "R" else ("HO", "H")
        ax.text(x - 0.62, yy, left, ha="right", va="center", fontsize=10)
        ax.text(x + 0.62, yy, right, ha="left", va="center", fontsize=10)
        ax.text(x + 0.12, yy + 0.2, str(i + 2), fontsize=7, color="0.5")
    ax.text(x, y - 0.62 * 5, "CH$_2$OH", ha="center", va="center", fontsize=11)
    ax.text(x - 0.55, y - 0.02, "1", fontsize=7, color="0.5", ha="right")


def haworth(ax, x, y, anomer):
    """Pyranose ring: O at the back right, C1 right, C2 front right, C3 front left, C4 left, C5 back left."""
    ink = plt.rcParams["text.color"]
    P = {"O": (0.85, 0.55), "C1": (1.6, 0.0), "C2": (1.05, -0.6), "C3": (-0.55, -0.6), "C4": (-1.1, 0.0), "C5": (-0.15, 0.55)}
    P = {k: (x + a, y + b) for k, (a, b) in P.items()}
    order = ["O", "C1", "C2", "C3", "C4", "C5", "O"]
    for a, b in zip(order, order[1:]):
        (x0, y0), (x1, y1) = P[a], P[b]
        if a == "O":
            x0 += 0.17 * (x1 - x0) / abs(x1 - x0 + 1e-9) * 0.9
        if b == "O":
            x1 -= 0.17 * (x1 - x0) / abs(x1 - x0 + 1e-9) * 0.9
        front = {a, b} <= {"C1", "C2", "C3", "C4"}
        if front and {a, b} == {"C2", "C3"}:
            ax.add_patch(Polygon([(x0, y0 - 0.05), (x1, y1 - 0.05), (x1, y1 + 0.05), (x0, y0 + 0.05)], color=ink))
        elif front:
            dy = 0.05
            ax.add_patch(Polygon([(x0, y0 - 0.012), (x1, y1 - dy), (x1, y1 + dy), (x0, y0 + 0.012)] if a in ("C1", "C4") else
                                 [(x0, y0 - dy), (x1, y1 - 0.012), (x1, y1 + 0.012), (x0, y0 + dy)], color=ink))
        else:
            ax.plot([x0, x1], [y0, y1], color=ink, lw=1.3)
    ax.text(*P["O"], "O", ha="center", va="center", fontsize=11)
    up_c1, down_c1 = ("OH", "H") if anomer == "beta" else ("H", "OH")
    subs = {"C1": (up_c1, down_c1), "C2": ("H", "OH"), "C3": ("OH", "H"), "C4": ("H", "OH"), "C5": ("CH$_2$OH", "H")}
    for c, (up, down) in subs.items():
        cx, cy = P[c]
        for sign, g in ((1, up), (-1, down)):
            col = RED if c == "C1" and g == "OH" else ink
            inner = (c in ("C2", "C3") and sign > 0) or (c == "C5" and sign < 0)
            L = 0.32 if inner else 0.5
            ax.plot([cx, cx], [cy, cy + L * sign], color=col, lw=1.3)
            ha = "center"
            if c == "C4" and g in ("OH", "HO"):
                g, ha = "HO", "right"
            ax.text(cx + (0.12 if ha == "right" else 0), cy + (L + 0.17) * sign, g, ha=ha if ha != "right" else "right", va="center", fontsize=10, color=col)
        dx, dy = (0.1, -0.3) if c in ("C2", "C3") else (0.1, 0.12)
        ax.text(cx + dx, cy + dy, c[1], fontsize=7, color="0.5")


fig, ax = plt.subplots(figsize=(12, 4.6))
haworth(ax, 0.0, 0.0, "alpha")
ax.text(0.25, -1.75, r"$\alpha$-D-glucopyranose" + "\n" + r"about 36%, $[\alpha]_{\mathrm{D}} = +112.2^\circ$", ha="center", va="center", fontsize=10)
ink = plt.rcParams["text.color"]
for xa in (2.7, 8.3):
    ax.annotate("", xy=(xa + 1.1, 0.12), xytext=(xa, 0.12), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.2))
    ax.annotate("", xy=(xa, -0.12), xytext=(xa + 1.1, -0.12), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.2))
fischer(ax, 6.05, 1.55)
ax.text(6.05, -2.25, "open-chain D-glucose\nabout 0.003%", ha="center", va="center", fontsize=10)
haworth(ax, 11.4, 0.0, "beta")
ax.text(11.65, -1.75, r"$\beta$-D-glucopyranose" + "\n" + r"about 64%, $[\alpha]_{\mathrm{D}} = +18.7^\circ$", ha="center", va="center", fontsize=10)
ax.set_xlim(-2.0, 13.6)
ax.set_ylim(-2.7, 2.0)
ax.set_aspect("equal")
ax.axis("off")
