"""Regenerative capacity across six animals (summary of the experimental literature reviewed in the text).

Rows: Hydra, a planarian, the axolotl, the zebrafish, the mouse and the human (PhyloPic silhouettes). Columns:
whole body from a small fragment, appendage (limb or fin), heart, spinal cord, liver, lens or retina.
Green: complete regeneration; yellow: partial or restricted (mouse heart only in the first postnatal week, digit
tips only, liver by compensatory growth of the remaining lobes, lens only in larvae); red: no regeneration
(repair by scarring); gray: the structure does not exist in that animal.
"""

from matplotlib.patches import FancyBboxPatch
import wikibio as bio

P = bio.P
LW = bio.core.LINE
fig, ax = bio.canvas(26.0, 13.5)
cols = ("whole body", "limb or fin", "heart", "spinal cord", "liver", "lens or retina")
Y, N, S, X = "positive", "negative", "highlight", "neutral"
rows = (
    ("Hydra", (Y, X, X, X, X, X), {}),
    ("planarian", (Y, X, X, X, X, Y), {0: "1/279 of body"}),
    ("axolotl", (N, Y, Y, Y, S, S), {5: "lens: larvae; retina: yes"}),
    ("zebrafish", (N, Y, Y, Y, Y, Y), {1: "fin"}),
    ("mouse", (N, S, S, N, S, N), {1: "digit tip", 2: "first week only", 4: "compensatory"}),
    ("human", (N, S, N, N, S, N), {1: "fingertip (children)", 4: "compensatory"}),
)
x0, y0, cw, rh = 6.0, 11.2, 3.2, 1.65
for j, c in enumerate(cols):
    bio.label(ax, (x0 + cw * (j + 0.5), y0 + 1.1), c, size="small", bold=True)
for i, (name, vals, notes) in enumerate(rows):
    y = y0 - rh * i
    bio.label(ax, (3.5, y), name, size="small", ha="left", italic=name in ("Hydra",))
    for j, v in enumerate(vals):
        ax.add_patch(FancyBboxPatch((x0 + cw * j + 0.12, y - 0.6), cw - 0.24, 1.2,
                                    boxstyle="round,pad=0,rounding_size=0.18", fc=P.fill(v) if v != X else P.light(v),
                                    ec=P.edge(v), lw=LW * 0.7, zorder=5))
        if j in notes:
            bio.label(ax, (x0 + cw * (j + 0.5), y), notes[j], size="tiny", color=P.on_fill(), zorder=8)
icons = ("phylopic/hydra", "phylopic/planarian", "phylopic/axolotl", "phylopic/zebrafish", "phylopic/mouse",
         "phylopic/human")
bio.icon(ax, "phylopic/hydra", at=(1.8, y0), height=1.3, color="animal")
bio.icon(ax, "phylopic/planarian", at=(1.8, y0 - rh), width=2.0, color="animal")
bio.icon(ax, "phylopic/axolotl", at=(1.8, y0 - 2 * rh), width=2.2, color="animal")
bio.icon(ax, "phylopic/zebrafish", at=(1.8, y0 - 3 * rh), width=2.2, color="animal")
bio.icon(ax, "phylopic/mouse", at=(1.8, y0 - 4 * rh), width=2.0, color="animal")
bio.icon(ax, "phylopic/human", at=(1.8, y0 - 5 * rh), height=1.4, color="animal")
leg = ((Y, "complete"), (S, "partial or restricted"), (N, "none (scar)"), (X, "absent"))
for k, (t, s) in enumerate(leg):
    xx = 6.2 + 4.9 * k
    ax.add_patch(FancyBboxPatch((xx, 0.55), 0.6, 0.5, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=P.fill(t) if t != X else P.light(t), ec=P.edge(t), lw=LW * 0.7))
    bio.label(ax, (xx + 0.8, 0.8), s, size="tiny", ha="left")
