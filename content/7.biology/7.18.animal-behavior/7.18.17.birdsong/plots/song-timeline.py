"""Timelines of song learning in two well-studied species (ages in days after hatching; typical values).
White-crowned sparrow (Marler 1970): sensory phase about day 10-50, singing begins the next spring (about day
150), crystallized song by about day 200; the phases are separated by a silent interval. Zebra finch (Immelmann
1969; Doupe and Kuhl 1999): memorization about day 20-65, subsong from about day 35, so the phases overlap,
crystallization at about day 90. Bars below: outcomes of the classic manipulations."""
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 11)
p = quant.Plot(ax, (5.2, 1.6, 17.6, 7.6), xlim=(0, 260), ylim=(0, 4), xlabel="Age / days after hatching",
               xticks=[0, 50, 100, 150, 200, 250], frame="l")


def bar(y, a, b, tok, text, h=0.5):
    X0, Y0 = p.xy(a, y - h / 2)
    X1, Y1 = p.xy(b, y + h / 2)
    bio.box(ax, ((X0 + X1) / 2, (Y0 + Y1) / 2), X1 - X0, Y1 - Y0, tok, text=text, size="tiny", radius=0.08)


for y, name, icon in [(3.3, "White-crowned sparrow", "sparrow"), (1.4, "Zebra finch", "zebra-finch")]:
    X, Y = p.xy(0, y)
    bio.label(ax, (X - 0.3, Y + 0.25), name, size="small", ha="right", bold=True)
    if icon == "sparrow":
        bio.icon(ax, "phylopic/sparrow", at=(X - 1.6, Y - 0.55), height=0.8, color="neutral")
    else:
        bio.icon(ax, "phylopic/zebra-finch", at=(X - 1.6, Y - 0.55), height=0.8, color="neutral")
# sparrow: sensory row above, motor row below
bar(3.65, 10, 50, "receptor", "sensory phase")
bar(3.0, 150, 185, "highlight", "subsong, plastic song")
bar(3.0, 185, 258, "positive", "crystallized song")
bar(1.75, 20, 65, "receptor", "sensory phase")
bar(1.1, 35, 90, "highlight", "subsong, plastic song")
bar(1.1, 90, 258, "positive", "crystallized song")
X0, Y0 = p.xy(52, 3.0)
X1, _ = p.xy(148, 3.0)
ax.plot([X0, X1], [Y0, Y0], color=P.muted(), lw=0.9, ls=(0, (3, 2)), zorder=6)
bio.label(ax, ((X0 + X1) / 2, Y0 + 0.3), "silent: memory stored", size="tiny", color=P.muted())
bio.label(ax, (p.X(150), p.Y(3.95)), "sensorimotor phase", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (p.X(68), p.Y(1.42)), "phases overlap", size="tiny", color=P.muted(), ha="left")
# legend of manipulations
bio.label(ax, (5.2, 10.5), "Isolated: abnormal 'isolate' song with species features.   Deafened before singing: "
          "no song structure.   Deafened after crystallization: song largely kept.", size="tiny", ha="left")
ax.set_ylim(0.3, 11)
