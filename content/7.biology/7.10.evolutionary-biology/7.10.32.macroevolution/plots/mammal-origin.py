"""The origin of mammals from early synapsids (Section 32.1.2): a cladogram of some of the fossil taxa in
the lineage leading to crown Mammalia, after Futuyma and Kirkpatrick (2017), Fig. 20.1. Each fossil
genus is a side branch of the stem lineage; numbered bars mark where characters evolved: 1, a temporal
fenestra behind the eye; 2, enlarged fenestra and large canines; 3, enlarged dentary, cheek teeth with
several cusps in a row, a bony secondary palate; 4, cheek teeth with an inner cusp, a contact between
dentary and squamosal; 5, a double jaw joint (articular-quadrate and dentary-squamosal); 6, a lower
jaw of the dentary alone, with the articular and quadrate free in the middle ear as hammer and anvil."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ink, muted = P.ink(), P.muted()
fig, ax = plt.subplots(figsize=(10.4, 4.4))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.97)
TAXA = [("Haptodus", "early synapsid"), ("Biarmosuchus", "therapsid"), ("Procynosuchus", "early cynodont"),
        ("Thrinaxodon", "cynodont"), ("Probainognathus", "advanced cynodont"), ("Morganucodon", "mammaliaform"),
        ("Hadrocodium", "mammaliaform")]
n = len(TAXA)
x_end = n + 1.4
ax.plot([0, x_end], [0, 0], color=ink, lw=1.6)
for k, (name, grp) in enumerate(TAXA):
    x = k + 0.8
    ax.plot([x, x + 0.9], [0, 1.0 + 0.0], color=ink, lw=1.3)
    ax.plot([x + 0.9], [1.0], "o", ms=6, color=P.edge("rna"))
    ax.text(x + 0.9, 1.15, name, rotation=35, ha="left", va="bottom", fontsize=FT["small"], color=ink, style="italic")
ax.plot([x_end, x_end + 0.6], [0, 0], color=charts.line("dna"), lw=2.6)
ax.annotate("", xy=(x_end + 0.85, 0), xytext=(x_end + 0.55, 0), arrowprops=dict(arrowstyle="-|>", color=charts.line("dna"), lw=1.3))
ax.text(x_end + 0.95, 0, "crown Mammalia\n(monotremes, marsupials,\nplacentals)", va="center", ha="left", fontsize=FT["small"], color=ink)
TRAITS = [(0.4, "temporal fenestra"), (1.4, "enlarged fenestra, large canines"),
          (2.4, "enlarged dentary, multicusped cheek teeth, secondary palate"),
          (4.4, "inner cusp on cheek teeth, dentary-squamosal contact"),
          (5.4, "double jaw joint"), (7.4, "jaw of dentary only; hammer and anvil in the middle ear")]
for k, (x, txt) in enumerate(TRAITS):
    ax.plot([x, x], [-0.18, 0.18], color=P.edge("highlight"), lw=3.2, solid_capstyle="butt")
    ax.text(x, -0.26, str(k + 1), ha="center", va="top", fontsize=FT["tiny"], color=ink, weight="bold")
    ax.text(0.2, -0.75 - 0.32 * k, f"{k + 1}  {txt}", ha="left", va="center", fontsize=FT["tiny"], color=ink)
ax.set_xlim(-0.3, x_end + 3.8)
ax.set_ylim(-2.8, 3.2)
ax.axis("off")
