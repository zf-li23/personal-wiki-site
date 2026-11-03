"""Transitional fossils between lobe-finned fishes and tetrapods, placed on their phylogeny and on a
time axis. Fossil taxa (dots) are side branches of the lineage leading to living tetrapods (the
stem lineage): none is a direct ancestor, but each shows an intermediate combination of characters.
Living sarcopterygians (coelacanths, lungfishes) and the crown tetrapods continue to the present.
Bars on the stem mark where the characters named evolved. Ages are approximate (Ma, Late Devonian
to Early Carboniferous); the relationships follow Futuyma and Kirkpatrick (2017), Fig. 17.16."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = plt.subplots(figsize=(10.5, 4.6))
fig.subplots_adjust(left=0.03, right=0.97, bottom=0.14, top=0.97)

stem_y = 0.0
ink, muted = P.ink(), P.muted()
# (name, node age, tip age, y, living?)
SIDE = [
    ("Coelacanths", 415, 330, 7.0, True),
    ("Lungfishes", 410, 330, 6.0, True),
    ("Eusthenopteron", 392, 385, 5.0, False),
    ("Panderichthys", 386, 380, 4.0, False),
    ("Tiktaalik", 380, 375, 3.0, False),
    ("Acanthostega", 372, 365, 2.0, False),
    ("Ichthyostega", 369, 365, 1.0, False),
]
ax.plot([422, 352], [stem_y, stem_y], color=ink, lw=1.6)
ax.plot([352, 330], [stem_y, stem_y], color=charts.line("dna"), lw=2.6)
for name, node, tip, y, living in SIDE:
    ax.plot([node, node], [stem_y, y], color=ink, lw=1.3)
    ax.plot([node, tip], [y, y], color=ink if not living else charts.line("dna"), lw=1.3 if not living else 2.6)
    if living:
        ax.annotate("", xy=(327, y), xytext=(331, y), arrowprops=dict(arrowstyle="-|>", color=charts.line("dna"), lw=1.2))
        ax.text(325, y, name + " (living)", va="center", ha="left", fontsize=FT["small"], color=ink)
    else:
        ax.plot([tip], [y], "o", ms=6, color=P.edge("rna"))
        ax.text(tip - 1.2, y + 0.08, name, va="bottom", ha="left", fontsize=FT["small"], color=ink, style="italic")
        ax.text(tip - 1.2, y - 0.08, f"~{tip} Ma", va="top", ha="left", fontsize=FT["tiny"], color=muted)
ax.annotate("", xy=(327, stem_y), xytext=(331, stem_y), arrowprops=dict(arrowstyle="-|>", color=charts.line("dna"), lw=1.2))
ax.text(325, stem_y, "Crown tetrapods\n(amphibians, amniotes)", va="center", ha="left", fontsize=FT["small"], color=ink)

TRAITS = [(419, "lobed paired fins with limb-like bones"), (389, "flat skull, long snout"),
          (383, "no gill-cover bones, mobile neck, flexible elbow and wrist"),
          (376, "limbs with digits (more than five)"), (360, "five or fewer digits")]
for k, (x, text) in enumerate(TRAITS):
    ax.plot([x, x], [stem_y - 0.25, stem_y + 0.25], color=P.edge("highlight"), lw=3.0, solid_capstyle="butt")
    ax.text(x, stem_y - 0.35, str(k + 1), ha="center", va="top", fontsize=FT["tiny"], color=ink, weight="bold")
    ax.text(352 - 0.0, -0.6 - 0.4 * k, f"{k + 1}  {text}", ha="left", va="center", fontsize=FT["tiny"], color=ink)

ax.set_xlim(424, 300)
ax.set_ylim(-3.0, 7.6)
for s in ("left", "right", "top"):
    ax.spines[s].set_visible(False)
ax.set_yticks([])
ax.set_xticks([420, 400, 380, 360, 340, 320])
ax.axvspan(419.6, 358.9, ymin=0, ymax=0.018, color=P.fill("highlight"))
ax.axvspan(358.9, 300, ymin=0, ymax=0.018, color=P.fill("neutral"))
ax.text(389, -2.62, "Devonian", ha="center", fontsize=FT["tiny"], color=muted)
ax.text(330, -2.62, "Carboniferous", ha="center", fontsize=FT["tiny"], color=muted)
charts.style_axes(ax, "time (Ma)")
ax.spines["left"].set_visible(False)
