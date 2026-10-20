"""A 2d-tree on random points and the regions touched by one range query."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

rng = np.random.default_rng(0)
pts = rng.random((64, 2))
query = (0.22, 0.71, 0.30, 0.62)                   # x1, x2, y1, y2
stats = {"recursed": 0, "reported": 0}


def inside(box, r):
    return r[0] <= box[0] and box[1] <= r[1] and r[2] <= box[2] and box[3] <= r[3]


def meets(box, r):
    return box[0] <= r[1] and r[0] <= box[1] and box[2] <= r[3] and r[2] <= box[3]


def draw(ax, p, box, depth, active=True):
    """Draw the splitting lines of the subtree on p inside box.

    active: whether the query recursion actually visits this node.
    """
    if len(p) == 1:
        return
    d = depth % 2
    p = p[np.argsort(p[:, d])]
    mid = len(p) // 2
    s = p[mid, d]
    left, right = list(box), list(box)
    if d == 0:
        left[1] = right[0] = s
        ax.plot([s, s], box[2:], color="C0", lw=1.6 - 0.25 * min(depth, 5))
    else:
        left[3] = right[2] = s
        ax.plot(box[:2], [s, s], color="C1", lw=1.6 - 0.25 * min(depth, 5))
    for sub, b in ((p[:mid], left), (p[mid:], right)):
        recurse = active and meets(b, query) and not inside(b, query)
        if active and inside(b, query):            # reported in bulk, no recursion
            stats["reported"] += 1
            ax.add_patch(Rectangle((b[0], b[2]), b[1] - b[0], b[3] - b[2],
                                   color="C2", alpha=0.3, lw=0))
        elif recurse and len(sub) > 1:
            stats["recursed"] += 1
        draw(ax, sub, b, depth + 1, recurse)


fig, ax = plt.subplots(figsize=(6, 6))
draw(ax, pts, [0.0, 1.0, 0.0, 1.0], 0)
hit = ((query[0] <= pts[:, 0]) & (pts[:, 0] <= query[1])
       & (query[2] <= pts[:, 1]) & (pts[:, 1] <= query[3]))
ax.scatter(pts[~hit, 0], pts[~hit, 1], s=14, color="0.45", zorder=3)
ax.scatter(pts[hit, 0], pts[hit, 1], s=22, color="C3", zorder=3)
ax.add_patch(Rectangle((query[0], query[2]), query[1] - query[0], query[3] - query[2],
                       fill=False, color="C3", lw=2, ls="--", zorder=4))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("2d-tree: x-splits (blue), y-splits (orange);\n"
             f"query (dashed): {stats['reported']} subtrees reported whole, "
             f"{stats['recursed']} internal nodes recursed into")
fig.tight_layout()
