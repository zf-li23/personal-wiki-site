# The bacterial (E. coli) replication fork, moving to the right. DnaB helicase encircles the lagging-strand
# template and unwinds 5'->3'; gyrase ahead of the fork removes the positive supercoils. DNA polymerase III
# (with its beta sliding clamp) extends the leading strand continuously towards the fork and the lagging
# strand discontinuously away from it, in Okazaki fragments started from RNA primers laid down by primase
# (DnaG); SSB coats the exposed single strand. Behind, DNA polymerase I removes each primer by nick
# translation and DNA ligase seals the remaining nick. Parental strands dark blue, new DNA light blue, RNA
# primers orange. (Simplification: the lagging-strand template loop, "trombone", is drawn flat.)
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

fig, ax = bio.canvas(20, 9.6)
P = bio.P
yc, half, arm = 4.7, 0.24, 2.2
xf, xr = 14.0, 12.4          # fork vertex and end of the arm ramp
dx = 0.2


def ramp(x):
    t = np.clip((xf - np.asarray(x, float)) / (xf - xr), 0, 1)
    return arm * (0.5 - 0.5 * np.cos(np.pi * t))


xs = np.arange(0.8, 19.6, dx)
top = MB.track(xs, yc + half + ramp(xs))
bot = MB.track(xs, yc - half - ramp(xs))
seq = MB.sequence(len(xs), "fork")
comp = MB.complement(seq)
fx = np.linspace(0.8, 19.6, 900)


def span(a, b):
    return (xs >= a) & (xs < b)


parental = xs >= xf
lead = xs < 12.4
frag_dna = [(0.8, 3.6), (3.6, 6.4), (6.9, 9.6), (11.0, 11.45)]
frag_rna = [(6.4, 6.8), (9.6, 10.1), (11.45, 11.9)]
lag_paired = np.zeros(len(xs), bool)
for a, b in frag_dna + frag_rna:
    lag_paired |= span(a, b)
newprimer = span(12.9, 13.25)                  # primer being made by primase at the helicase
lag_paired |= newprimer

# --- base pairs and unpaired bases --------------------------------------------------------------------------
MB.ladder(ax, top[parental], bot[parental], [seq[i] for i in np.where(parental)[0]])
new_top = top - (0, 2 * half)
new_bot = bot + (0, 2 * half)
MB.ladder(ax, top[lag_paired], new_top[lag_paired], [seq[i] for i in np.where(lag_paired)[0]])
MB.ladder(ax, bot[lead], new_bot[lead], [comp[i] for i in np.where(lead)[0]])
single_top = ~parental & ~lag_paired
single_bot = ~parental & ~lead
nt = np.c_[np.zeros(len(xs)), -np.ones(len(xs))]
MB.stubs(ax, top[single_top], (0, -1), [seq[i] for i in np.where(single_top)[0]])
MB.stubs(ax, bot[single_bot], (0, 1), [comp[i] for i in np.where(single_bot)[0]])

# --- backbones -----------------------------------------------------------------------------------------------
MB.backbone(ax, MB.track(fx, yc + half + ramp(fx)), "dna", zorder=11)
MB.backbone(ax, MB.track(fx, yc - half - ramp(fx)), "dna", zorder=11)
yl, yt = yc - half - arm + 2 * half, yc + half + arm - 2 * half


def new_strand(a, b, token="dna", lagging=True, shade="fill"):
    x = np.linspace(a, b, 60)
    y = yc + half + ramp(x) - 2 * half if lagging else yc - half - ramp(x) + 2 * half
    MB.backbone(ax, MB.track(x, y), token, shade=shade)


new_strand(0.8, 12.35, lagging=False)
for a, b in frag_dna:
    new_strand(a + 0.04, b - 0.04)
for a, b in frag_rna + [(12.9, 13.25)]:
    new_strand(a + 0.03, b - 0.03, "rna", shade="edge")

# --- proteins ------------------------------------------------------------------------------------------------
MB.helicase(ax, (13.75, yc + half + ramp(13.75)), h=1.05, w=0.75, angle=-50)
bio.label(ax, (14.75, 6.35), "DnaB helicase", size="small", ha="left")
MB.enzyme(ax, (12.45, 5.45), 1.05, 0.55, "highlight", "Primase")
MB.ssb(ax, top[span(11.95, 12.85)] + (0, 0.02), every=1)
bio.callout(ax, (12.4, yt + 0.62), (11.6, 8.45), "SSB")
# polymerase III cores with their clamps
MB.clamp(ax, (12.35, yl + half - 0.02), h=1.05)
MB.polymerase(ax, (12.5, yl - 0.25), 1.35, 1.25, "enzyme", alpha=0.92, seed="pol3a", zorder=12)
bio.label(ax, (12.55, yl - 0.62), "Pol III", size="tiny", color=P.on_fill(), bold=True, zorder=13)
MB.clamp(ax, (11.0, yt - half + 0.02), h=1.05)
MB.polymerase(ax, (10.95, yt + 0.25), 1.35, 1.25, "enzyme", alpha=0.92, seed="pol3b", zorder=12)
bio.label(ax, (10.9, yt + 0.62), "Pol III", size="tiny", color=P.on_fill(), bold=True, zorder=13)
MB.enzyme(ax, (6.85, yt + 0.05), 0.95, 0.72, "protein", "Pol I", alpha=0.95)
MB.enzyme(ax, (3.6, yt + 0.05), 1.05, 0.66, "receptor", "Ligase", alpha=0.95)
MB.enzyme(ax, (17.0, yc + 0.02), 1.25, 1.25, "metabolite", "Gyrase", alpha=0.92)

# --- strand labels and directions ---------------------------------------------------------------------------
lab = dict(size="tiny", bold=True)
bio.label(ax, (0.45, yt + 2 * half), "5′", **lab)
bio.label(ax, (0.45, yt), "3′", **lab)
bio.label(ax, (0.45, yl - 2 * half), "3′", **lab)
bio.label(ax, (0.45, yl), "5′", **lab)
bio.label(ax, (19.9, yc + half), "3′", **lab)
bio.label(ax, (19.9, yc - half), "5′", **lab)
bio.label(ax, (7.5, yt - 0.42), "3′", size="tiny", bold=True)
bio.label(ax, (8.6, yt - 0.42), "Okazaki fragment", size="tiny", color=P.muted())
bio.label(ax, (9.95, yt - 0.42), "5′", size="tiny", bold=True)

for a, b in ((4.0, 6.0), (7.3, 9.3)):
    bio.arrow(ax, (b, yt + 1.2), (a, yt + 1.2), kind="process", color=P.edge("dna"))
bio.label(ax, (1.0, yt + 1.75), "Lagging strand: discontinuous, away from the fork", size="small", ha="left", color=P.edge("dna"))
bio.arrow(ax, (7.6, yl - 1.25), (11.2, yl - 1.25), kind="process", color=P.edge("dna"))
bio.label(ax, (1.0, yl - 1.25), "Leading strand: continuous, towards the fork", size="small", ha="left", color=P.edge("dna"))
bio.callout(ax, (9.85, yt + 0.0), (9.4, 8.45), "RNA primer")
bio.arrow(ax, (16.2, 8.6), (19.2, 8.6), kind="process")
bio.label(ax, (17.7, 8.9), "Fork movement", size="small", va="bottom")
bio.label(ax, (17.0, yc - 1.15), "relieves positive\nsupercoils", size="tiny", color=P.muted(), va="top")
# legend
ly = 0.45
for k, (col, text) in enumerate(((P.edge("dna"), "Parental DNA"), (P.fill("dna"), "New DNA"), (P.edge("rna"), "RNA primer"))):
    x = 6.0 + k * 3.4
    ax.plot([x, x + 0.6], [ly, ly], color=col, lw=bio.core.LINE * 2.2, solid_capstyle="round")
    bio.label(ax, (x + 0.8, ly), text, size="small", ha="left")
