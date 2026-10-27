"""The cross-bridge cycle of myosin II (Lymn and Taylor 1971), schematic. The actin filament has its plus
end on the right; the thick filament (above) is pulled to the right relative to actin, i.e. myosin walks
towards the plus end. One cycle hydrolyses one ATP and moves the filaments about 5-10 nm.

1 Rigor: nucleotide-free head tightly bound, lever arm in the post-stroke position.
2 ATP binds: affinity for actin falls and the head detaches.
3 Hydrolysis: ATP -> ADP + Pi on the detached head re-cocks the lever (recovery stroke); the head binds
  weakly to a new actin subunit further towards the plus end.
4 Pi release: strong binding and the power stroke (lever swings towards the plus end), then ADP leaves
  and the head is back in rigor.
"""

import numpy as np

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(22.0, 12.0)
boxes = {1: (0.6, 6.4), 2: (11.6, 6.4), 3: (11.6, 0.4), 4: (0.6, 0.4)}
W, H = 9.8, 5.2
info = {
    1: ("1  Rigor", None, 0.0, 128, 3.6),
    2: ("2  ATP binds: head detaches", "ATP", 0.35, 128, 3.6),
    3: ("3  Hydrolysis: lever re-cocked, weak binding", "ADP·Pi", 0.12, 62, 4.6),
    4: ("4  Pi release: power stroke", "ADP", 0.0, 128, 4.6),
}
for k, (x0, y0) in boxes.items():
    title, nt, gap, lever, site = info[k]
    bio.label(ax, (x0 + 0.2, y0 + H - 0.3), title, size="small", bold=True, ha="left")
    fil = C.actin_filament(ax, (x0 + 0.6, y0 + 1.0), (x0 + W - 0.6, y0 + 1.0), r=0.14, states="D", ends=True)
    # target subunit highlighted
    tgt = np.array([x0 + site, y0 + 1.0])
    bio.label(ax, (tgt[0], y0 + 0.45), "binding site", size="tiny", color=P.muted()) if k == 3 else None
    end = C.myosin_head(ax, tgt + (0, 0.12), size=0.85, lever=lever, gap=gap, nucleotide=nt, lever_len=1.25)
    # thick filament backbone and the tail (S2) to it
    yb = y0 + 4.1
    ax.plot([x0 + 0.6, x0 + W - 0.6], [yb, yb], color=P.edge("myosin"), lw=5, solid_capstyle="round", zorder=8)
    ax.plot([end[0], end[0] + 1.0], [end[1], yb], color=P.edge("myosin"), lw=2.2, zorder=8)
    # reference line: where the tail joined the backbone in state 1
    ax.plot([x0 + 4.9] * 2, [yb - 0.35, yb + 0.35], color=P.muted(), lw=0.8, ls=(0, (2, 1.5)), zorder=9)
bio.label(ax, (5.5, 0.15), "dashed tick: tail position in state 1; the thick filament has moved →", size="tiny", color=P.muted())
# cycle arrows between boxes
bio.arrow(ax, (10.5, 9.2), (11.5, 9.2), kind="process")
bio.arrow(ax, (16.5, 6.3), (16.5, 5.7), kind="process")
bio.arrow(ax, (11.5, 3.0), (10.5, 3.0), kind="process")
bio.arrow(ax, (5.5, 5.7), (5.5, 6.3), kind="process")
bio.label(ax, (11.0, 9.75), "+ ATP", size="tiny")
bio.label(ax, (17.3, 6.0), "hydrolysis", size="tiny", ha="left")
bio.label(ax, (11.0, 3.55), "− Pi", size="tiny")
bio.label(ax, (5.9, 6.0), "− ADP", size="tiny", ha="left")
