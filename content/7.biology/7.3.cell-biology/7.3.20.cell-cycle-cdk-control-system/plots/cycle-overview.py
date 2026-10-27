"""The cell cycle and its control system (schematic).

(A) The four phases of a typical proliferating human cell in culture (about 24 h: G1 about 11 h, S about 8 h,
G2 about 4 h, M about 1 h), drawn clockwise, with the three regulatory transitions of the control system
(Start or the restriction point in late G1, the G2/M transition and the metaphase-to-anaphase transition)
as bars across the ring, the questions each transition asks, and the exit from G1 into the nondividing
state G0. (B) Relative activities of the cyclin-Cdk complexes and of the two forms of APC/C over one cycle
(schematic shapes after MBoC Figure 17-10 and 17-20, not measurements): G1-Cdk (cyclin D-Cdk4/6) follows
mitogen signaling; G1/S-Cdk (cyclin E-Cdk2) peaks at Start; S-Cdk (cyclin A-Cdk2/Cdk1) rises in S and
falls in early M; M-Cdk (cyclin B-Cdk1) accumulates in G2 but is held inactive until it is switched on
abruptly at G2/M and destroyed at anaphase; APC/C-Cdc20 is active from metaphase, APC/C-Cdh1 from late
anaphase to late G1.
"""

import math

import numpy as np

import wikibio as bio
from wikibio import cellbio, charts

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(25.0, 11.0)

# ----- A: the wheel
bio.panel(ax, "A", (0.2, 10.8))
c = (5.6, 5.3)
r = 3.0
phases = [("G1", 11 / 24, "positive"), ("S", 8 / 24, "dna"), ("G2", 4 / 24, "channel"), ("M", 1 / 24, "negative")]
seg = cellbio.cycle_wheel(ax, c, r, phases, width=1.1, start=90.0, gap=1.0)


def ang_frac(f):
    # angle of a point a fraction f of the way round from the start (clockwise)
    return 90.0 - 360.0 * f


start_a = ang_frac(10.0 / 24)       # late G1
g2m_a = ang_frac(23.0 / 24)         # end of G2
ma_a = ang_frac(23.6 / 24)          # inside M (metaphase to anaphase)
cellbio.checkpoint(ax, c, r, start_a, width=1.1, text="Start\n(restriction point)", text_xy=(8.2, 1.25), ha="left")
cellbio.checkpoint(ax, c, r, g2m_a, width=1.1, text="G2/M", text_xy=(2.5, 9.9), ha="center")
cellbio.checkpoint(ax, c, r, ma_a, width=1.1, text="metaphase-to-\nanaphase", text_xy=(8.7, 9.9), ha="center")

# the questions asked at each transition
qs = [((10.3, 9.3), "Are all chromosomes attached\nto the spindle?"),
      ((0.4, 8.6), "Is all DNA replicated?\nIs the DNA undamaged?"),
      ((8.2, 0.35), "Is the environment favorable?\nIs the cell big enough? DNA intact?")]
for xy, t in qs:
    bio.label(ax, xy, t, size="tiny", ha="left", color=P.muted())

# direction arrow inside the ring
th = np.linspace(math.radians(60), math.radians(-20), 40)
rr = r - 1.05
ax.plot(c[0] + rr * np.cos(th), c[1] + rr * np.sin(th), color=P.muted(), lw=1.0, zorder=9)
bio.arrow(ax, (c[0] + rr * math.cos(th[-3]), c[1] + rr * math.sin(th[-3])),
          (c[0] + rr * math.cos(th[-1]), c[1] + rr * math.sin(th[-1])), kind="process", color=P.muted(), head=0.18)
bio.label(ax, c, "interphase\n(G1 + S + G2)", size="small", color=P.muted())

# G0 side branch from early G1
g0_a = math.radians(ang_frac(4.0 / 24))
p0 = (c[0] + (r + 0.6) * math.cos(g0_a), c[1] + (r + 0.6) * math.sin(g0_a))
g0 = (10.6, 3.0)
bio.box(ax, g0, 1.5, 0.8, token="neutral", text="G0", size="normal")
bio.arrow(ax, p0, (g0[0] - 0.8, g0[1] + 0.25), kind="process", bend=-0.25, color=P.ink())
bio.arrow(ax, (g0[0] - 0.8, g0[1] - 0.25), (p0[0] - 0.15, p0[1] - 0.45), kind="process", bend=-0.25, color=P.ink(), dashed=True)
bio.label(ax, (g0[0], g0[1] - 0.85), "quiescent or\nterminally differentiated", size="tiny", color=P.muted())

# ----- B: activities over one cycle
bio.panel(ax, "B", (13.0, 10.8))
a = charts.axes_at(ax, (14.4, 1.6, 10.0, 8.2))
t = np.linspace(0, 20, 1600)


def sig(x, x0, w):
    return 1 / (1 + np.exp(-(x - x0) / w))


# phase boundaries on a stretched (not to scale) time axis: G1 0-8, S 8-13, G2 13-16, M 16-20
G1S, SG2, G2M, END = 8.0, 13.0, 16.0, 20.0
META, ANA = 18.0, 18.5
g1cdk = 0.35 * sig(t, 2.0, 0.8) * (1 - 0.6 * sig(t, 14.5, 0.8))
g1scdk = 0.75 * sig(t, 7.0, 0.35) * (1 - sig(t, 9.8, 0.5))
scdk = 0.62 * sig(t, 8.5, 0.5) * (1 - sig(t, 17.0, 0.12))
mcdk = 1.0 * sig(t, G2M, 0.08) * (1 - sig(t, ANA, 0.12))
mcdk_inactive = 0.42 * sig(t, 14.0, 0.6) * (1 - sig(t, G2M, 0.07))
apc20 = 0.8 * sig(t, META, 0.08) * (1 - sig(t, 19.3, 0.15)) + 0.25 * sig(t, 16.8, 0.1) * (1 - sig(t, META, 0.08))
apch1 = 0.55 * (sig(t, 19.0, 0.12) + (1 - sig(t, 7.2, 0.3)) * (t < 15.0))
apch1 = np.clip(apch1, 0, 0.55)
for x0, x1, tok in ((0, G1S, "positive"), (G1S, SG2, "dna"), (SG2, G2M, "channel"), (G2M, END, "negative")):
    a.axvspan(x0, x1, color=P.fill(tok), alpha=0.18, lw=0)
curves = [(g1cdk, "positive", "-"), (g1scdk, "drug", "-"), (scdk, "dna", "-"), (mcdk, "negative", "-"),
          (mcdk_inactive, "negative", ":"), (apc20, "enzyme", "--"), (apch1, "channel", "--")]
for y, tok, ls in curves:
    a.plot(t, y, color=charts.line(tok), lw=1.8, ls=ls)
for (x, y, lab, tok) in ((3.0, 0.38, "G1-Cdk", "positive"), (6.4, 0.8, "G1/S-Cdk", "drug"),
                         (11.0, 0.66, "S-Cdk", "dna"), (14.6, 1.0, "M-Cdk", "negative"),
                         (13.6, 0.47, "inactive M-Cdk", "negative"),                          (3.2, 0.59, "APC/C–Cdh1", "channel")):
    a.text(x, y, lab, color=charts.line(tok), fontsize=FT["tiny"], ha="center", va="bottom")
a.annotate("APC/C–Cdc20", xy=(18.6, 0.66), xytext=(17.15, 0.42), color=charts.line("enzyme"), fontsize=FT["tiny"],
           ha="center", arrowprops=dict(arrowstyle="-", color=charts.line("enzyme"), lw=0.7))
for x, lab in ((4, "G1"), (10.5, "S"), (14.5, "G2"), (18, "M")):
    a.text(x, 1.13, lab, ha="center", fontsize=FT["small"], color=P.ink(), weight="bold")
for x, lab in ((7.75, "Start"), (16.0, "G2/M"), (18.0, "M/A")):
    a.axvline(x, color=P.edge("negative"), lw=0.9, ls="-", alpha=0.8)
    a.text(x, -0.07, lab, ha="center", va="top", fontsize=FT["tiny"], color=P.edge("negative"))
a.set_xlim(0, 20)
a.set_ylim(0, 1.2)
a.set_yticks([])
a.set_xticks([])
charts.style_axes(a, None, "relative activity")
bio.label(ax, (19.4, 0.55), "one cycle (phases not to scale)", size="small", color=P.muted())
