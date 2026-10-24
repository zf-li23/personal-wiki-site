"""Re and Si faces of the carbonyl carbon of butan-2-one. CIP order at the trigonal carbon:
O > CH2CH3 > CH3. Seen from the front, O -> Et -> Me runs clockwise (Re face); seen from the
back (mirror image of the drawing), it runs anticlockwise (Si face)."""

import numpy as np
import matplotlib.pyplot as plt


def face(ax, x0, flip, title):
    ink = plt.rcParams["text.color"]
    s = -1 if flip else 1
    pts = {"O": (0, 1.1), "CH$_2$CH$_3$": (s * 0.95, -0.55), "CH$_3$": (-s * 0.95, -0.55)}
    for name, (x, y) in pts.items():
        ax.plot([x0, x0 + 0.72 * x], [0, 0.72 * y], color=ink, lw=1.8)
        ax.text(x0 + 1.05 * x * (1.25 if "CH" in name else 1), 1.05 * y, name, ha="center", va="center", fontsize=11)
    ax.plot([x0 - 0.06, x0 - 0.06], [0.1, 0.78], color=ink, lw=1.8)  # second line of C=O
    ax.plot([x0], [0], "o", color=ink, ms=3)
    th = np.linspace(np.radians(80), np.radians(-200), 80) if not flip else np.linspace(np.radians(100), np.radians(380), 80)
    r = 0.42
    ax.plot(x0 + r * np.cos(th), r * np.sin(th), color="#2563eb", lw=1.4)
    end = np.array([x0 + r * np.cos(th[-1]), r * np.sin(th[-1])])
    prev = np.array([x0 + r * np.cos(th[-4]), r * np.sin(th[-4])])
    ax.annotate("", xy=end, xytext=prev, arrowprops=dict(arrowstyle="-|>", color="#2563eb"))
    ax.text(x0, -1.5, title, ha="center", fontsize=10)


fig, ax = plt.subplots(figsize=(8, 3.4))
face(ax, 0, False, "front: 1 $\\to$ 2 $\\to$ 3 clockwise = Re face")
face(ax, 4.2, True, "back: anticlockwise = Si face")
ax.set_aspect("equal")
ax.set_xlim(-2, 6.2)
ax.set_ylim(-1.9, 1.6)
ax.axis("off")
