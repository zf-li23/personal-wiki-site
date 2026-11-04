"""The nitrogen cycle of an ecosystem and the human doubling of nitrogen fixation.

A: the main pools and microbial transformations. N2 is fixed to ammonia by diazotrophs; ammonium is
assimilated into organic nitrogen and released again by ammonification (mineralization); nitrifiers
oxidize ammonium to nitrite and nitrate; nitrate is assimilated, reduced back to ammonium by DNRA, or
denitrified to N2O and N2; anammox converts ammonium and nitrite directly to N2. Leaks to the environment:
nitrate leaching to ground and surface water (eutrophication) and N2O emission (greenhouse gas,
stratospheric ozone loss).
B: global fixation of nitrogen into reactive forms around 2010, in Tg N per year: natural biological
fixation on land (58) and in the ocean (140; uncertain, range about 100-200) and by lightning (5), against
fixation by humans: the Haber-Bosch process (120), biological fixation by cultivated legumes and rice (60)
and NOx from combustion (30). Data from Fowler et al. (2013).
"""
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import ecology as E
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26.0, 12.5)

# A: cycle ------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 12.3))
n2 = E.node(ax, (7.0, 10.6), "N₂", token="neutral", size="small", w=1.6)
nh4 = E.node(ax, (12.6, 6.4), "NH₄⁺", token="enzyme", size="small", w=1.6)
org = E.node(ax, (13.6, 10.6), "organic N", token="plant", size="small")
no2 = E.node(ax, (10.6, 2.2), "NO₂⁻", token="atp", size="small", w=1.6)
no3 = E.node(ax, (4.2, 2.2), "NO₃⁻", token="lipid", size="small", w=1.6)
n2o = E.node(ax, (2.2, 6.4), "N₂O", token="receptor", size="small", w=1.6)
E.connect(ax, n2, nh4, bend=0.0)
bio.label(ax, (10.3, 7.3), "N₂ fixation", size="small", ha="right", color=P.muted())
E.connect(ax, nh4, org, bend=-0.3)
bio.label(ax, (14.5, 8.6), "assimilation", size="small", ha="left", color=P.muted())
E.connect(ax, org, nh4, bend=-0.3)
bio.label(ax, (12.3, 9.5), "ammonification", size="small", ha="right", color=P.muted())
E.connect(ax, nh4, no2)
bio.label(ax, (12.2, 4.0), "nitrification", size="small", ha="left", color=P.muted())
E.connect(ax, no2, no3, text="nitrification", text_side=1)
E.connect(ax, no3, n2o, text="denitrification", text_side=-1)
E.connect(ax, n2o, n2, bend=-0.2, text="denitrification", text_side=-1)
E.connect(ax, no2, n2, bend=0.0, color=P.edge("receptor"))
bio.label(ax, (9.4, 3.3), "anammox", size="small", ha="right", color=P.edge("receptor"))
E.connect(ax, no3, nh4, bend=0.1, dashed=True)
bio.label(ax, (6.2, 4.7), "DNRA", size="small", ha="right", color=P.muted())
bio.arrow(ax, (4.2, 1.6), (4.2, 0.5), kind="process", color=P.muted())
bio.label(ax, (4.5, 0.7), "leaching to water: eutrophication", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (1.8, 6.9), (1.0, 8.9), kind="process", color=P.muted())
bio.label(ax, (0.5, 9.4), "emission: greenhouse gas,\nstratospheric ozone loss", size="tiny", ha="left", color=P.muted())

# B: fixation fluxes --------------------------------------------------------------------------------
bio.panel(ax, "B", (15.0, 12.3))
items = [("lightning", 5, "neutral"), ("BNF, land", 58, "plant"), ("BNF, ocean", 140, "dna"),
         ("combustion NOx", 30, "negative"), ("crop BNF", 60, "negative"), ("Haber–Bosch", 120, "negative")]
pb = quant.Plot(ax, (19.0, 1.6, 6.2, 9.0), xlim=(0, 160), ylim=(-0.6, 6.6), xlabel="N fixed / (Tg N yr⁻¹)",
                xticks=[0, 40, 80, 120, 160], frame="l", grid=False)
for k, (name, v, tok) in enumerate(items):
    y = 5.6 - k - (0.4 if k >= 3 else 0)
    yy0, yy1 = pb.Y(y - 0.35), pb.Y(y + 0.35)
    ax.add_patch(FancyBboxPatch((pb.X(0), yy0), pb.X(v) - pb.X(0), yy1 - yy0, boxstyle="square,pad=0",
                                         facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=8))
    bio.label(ax, (pb.X(0) - 0.15, pb.Y(y)), name, size="tiny", ha="right")
    bio.label(ax, (pb.X(v) + 0.15, pb.Y(y)), f"{v}", size="tiny", ha="left")
bio.label(ax, (pb.X(80), pb.Y(6.3)), "natural: about 200", size="tiny", color=P.muted())
bio.label(ax, (pb.X(80), pb.Y(2.75)), "human: about 210", size="tiny", color=P.edge("negative"))
