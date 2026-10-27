"""Once and only once: two windows for DNA replication separated by Cdk activity (schematic).

(A) Over one cycle (phases not to scale), the activity of S- and M-Cdks is low from late mitosis to late G1 and
high from the G1/S transition to anaphase; APC/C-Cdh1 is active in the low window and destroys geminin.
Origins can be licensed (MCM2-7 loaded) only in the low window, and fired only in the high window, when S-Cdk
and DDK (Cdc7-Dbf4) are active. (B) The steps at one origin. ORC, bound throughout the cycle, recruits Cdc6 and
Cdt1, which load two MCM2-7 hexamers as an inactive head-to-head double hexamer around duplex DNA (the
prereplicative complex). In S phase, DDK phosphorylates MCM and S-Cdk phosphorylates Sld2 and Sld3 (yeast;
RecQL4 and Treslin in vertebrates), which recruit Cdc45 and GINS: two CMG helicases form and move apart with
the replisomes. High Cdk activity prevents reloading: it phosphorylates ORC and Cdc6 (Cdc6 is exported or
degraded), while Cdt1 is bound by geminin and, at forks, destroyed by CRL4-Cdt2. Only when Cdk activity falls
at the end of mitosis can new MCM be loaded.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(26.0, 12.5)

# ----- A
bio.panel(ax, "A", (0.2, 12.3))
a = charts.axes_at(ax, (1.6, 7.0, 23.6, 4.4))
t = np.linspace(0, 24, 1200)


def sig(x, x0, w):
    return 1 / (1 + np.exp(-(x - x0) / w))


# stretched axis: M 0-2 (end of previous), G1 2-9, S 9-15, G2 15-18, M 18-22, G1 22-24
cdk = 0.9 * (1 - sig(t, 1.0, 0.12)) + 0.9 * sig(t, 8.6, 0.35) * (1 - sig(t, 19.8, 0.12))
cdh1 = 0.7 * sig(t, 1.4, 0.12) * (1 - sig(t, 8.0, 0.3)) + 0.7 * sig(t, 20.2, 0.12)
gem = 0.6 * sig(t, 8.2, 0.4) * (1 - sig(t, 19.6, 0.15)) + 0.6 * (1 - sig(t, 1.3, 0.12))
for x0, x1, tok, lab in ((0, 2, "negative", "M"), (2, 9, "positive", "G1"), (9, 15, "dna", "S"), (15, 18, "channel", "G2"),
                         (18, 22, "negative", "M"), (22, 24, "positive", "G1")):
    a.axvspan(x0, x1, color=P.fill(tok), alpha=0.16, lw=0)
    a.text((x0 + x1) / 2, 1.08, lab, ha="center", fontsize=FT["small"], weight="bold", color=P.ink())
a.plot(t, cdk, color=charts.line("negative"), lw=1.9)
a.plot(t, cdh1, color=charts.line("channel"), lw=1.7, ls="--")
a.plot(t, gem, color=charts.line("drug"), lw=1.4, ls=":")
a.text(12.0, 0.93, "S- and M-Cdk activity", color=charts.line("negative"), fontsize=FT["tiny"], ha="center", va="bottom")
a.text(5.5, 0.73, "APC/C–Cdh1", color=charts.line("channel"), fontsize=FT["tiny"], ha="center", va="bottom")
a.text(16.5, 0.63, "geminin", color=charts.line("drug"), fontsize=FT["tiny"], ha="center", va="bottom")
# windows
a.annotate("", xy=(8.8, -0.12), xytext=(1.2, -0.12), arrowprops=dict(arrowstyle="<->", color=charts.line("positive"), lw=1.1),
           annotation_clip=False)
a.text(5.0, -0.25, "licensing window: MCM loading, no firing", ha="center", va="top", fontsize=FT["tiny"],
       color=charts.line("positive"))
a.annotate("", xy=(19.8, -0.12), xytext=(9.0, -0.12), arrowprops=dict(arrowstyle="<->", color=charts.line("negative"), lw=1.1),
           annotation_clip=False)
a.text(14.4, -0.25, "firing window: origins fire, no reloading", ha="center", va="top", fontsize=FT["tiny"],
       color=charts.line("negative"))
a.set_xlim(0, 24)
a.set_ylim(0, 1.2)
a.set_xticks([])
a.set_yticks([])
charts.style_axes(a, None, "activity")

# ----- B: one origin
bio.panel(ax, "B", (0.2, 5.4))
Y = 2.4


def duplex(x0, x1, y=Y):
    bio.dna(ax, (x0, y), (x1, y), style="duplex", width=0.3, ends=False)


def mcm(c, w=0.55, h=0.85, tok="enzyme", text="MCM"):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=12))
    bio.label(ax, (c[0], c[1] - h / 2 - 0.28), text, size="tiny")


def blob(c, w, h, tok, text):
    bio.protein(ax, c, w, h, token=tok, text=text, size="tiny", zorder=13)


# 1: ORC + Cdc6 + Cdt1
duplex(0.6, 5.4)
blob((2.0, Y + 0.6), 1.3, 0.75, "protein", "ORC")
blob((3.2, Y + 0.62), 0.9, 0.6, "drug", "Cdc6")
blob((4.3, Y + 0.6), 0.9, 0.6, "positive", "Cdt1")
bio.label(ax, (3.0, Y + 1.55), "late M, G1: low Cdk", size="tiny", color=P.muted())
bio.label(ax, (3.0, Y - 1.2), "ORC recruits Cdc6, Cdt1", size="tiny")
bio.arrow(ax, (5.7, Y), (6.7, Y), kind="process")
# 2: double hexamer (pre-RC)
duplex(7.0, 11.6)
mcm((8.9, Y)); mcm((9.5, Y), tok="enzyme")
blob((10.8, Y + 0.6), 1.1, 0.65, "protein", "ORC")
bio.label(ax, (9.3, Y + 1.55), "licensed: pre-RC", size="tiny", bold=True, color=charts.line("positive"))
bio.label(ax, (9.3, Y - 1.2), "MCM double hexamer (inactive)", size="tiny")
bio.arrow(ax, (11.9, Y), (12.9, Y), kind="process")
bio.label(ax, (12.4, Y + 0.45), "S-Cdk\n+ DDK", size="tiny", bold=True)
# 3: firing -> a bubble with two CMG helicases
duplex(13.2, 14.3)
duplex(18.0, 19.0)
xs = np.linspace(14.3, 18.0, 60)
bump = 0.5 * np.sin(np.pi * (xs - 14.3) / 3.7) ** 0.6
ax.plot(xs, Y + 0.15 + bump, color=P.edge("dna"), lw=1.8, zorder=9)
ax.plot(xs, Y - 0.15 - bump, color=P.edge("dna2"), lw=1.8, zorder=9)
for x, d in ((14.75, -1), (17.55, 1)):
    yy = Y + d * 0.42
    ax.add_patch(FancyBboxPatch((x - 0.27, yy - 0.3), 0.54, 0.6, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.9, zorder=12))
    blob((x + 0.05 * d, yy + d * 0.62), 1.3, 0.42, "highlight", "Cdc45, GINS")
    bio.arrow(ax, (x + 0.3 * d, yy + d * 1.2), (x + 1.2 * d, yy + d * 1.2), kind="process")
bio.label(ax, (16.15, Y), "CMG", size="tiny", color=P.muted())
bio.label(ax, (16.1, Y - 1.85), "fired: two CMG helicases", size="tiny", bold=True, color=charts.line("negative"))
# 4: no reloading
bio.arrow(ax, (19.3, Y), (20.3, Y), kind="process")
duplex(20.6, 25.6)
blob((22.0, Y + 0.6), 1.1, 0.65, "protein", "ORC")
ax.add_patch(Circle((22.55, Y + 0.95), 0.18, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=14))
bio.label(ax, (22.55, Y + 0.95), "P", size="tiny", bold=True, color=P.on_fill(), zorder=15)
blob((23.6, Y + 0.95), 0.9, 0.55, "positive", "Cdt1")
blob((24.6, Y + 1.0), 1.1, 0.55, "drug", "geminin")
bio.label(ax, (23.1, Y - 1.0), "S, G2, early M: high Cdk\nORC, Cdc6 phosphorylated;\nCdt1 bound by geminin", size="tiny")
bio.label(ax, (23.1, Y + 1.85), "no new MCM loading", size="tiny", bold=True, color=charts.line("negative"))
