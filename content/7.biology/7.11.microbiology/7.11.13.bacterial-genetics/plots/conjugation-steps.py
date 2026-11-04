# The molecular steps of conjugation by an F-like plasmid between two Gram-negative cells (schematic).
# 1: the donor's sex pilus binds the recipient and retracts, pulling the cells together.
# 2: a mating pair forms; the type IV secretion system (T4SS) spans both envelopes. The relaxosome
#    (relaxase TraI with accessory proteins) nicks one strand at oriT; the relaxase stays covalently bound
#    to the 5' end, and the coupling protein hands the relaxase-DNA complex to the T4SS.
# 3: the relaxase leads the single strand into the recipient while the donor replaces it by rolling-circle
#    replication from the 3' end at the nick; the recipient makes the complementary strand discontinuously.
# 4: the relaxase rejoins the ends of the transferred strand (recircularization); both cells have a complete
#    double-stranded plasmid, and the recipient, now a donor, can transfer it in turn.
import numpy as np

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(27.0, 8.4)
W = 6.6
DON, REC = "bacterium", "neutral"


def ring(c, r, tok, lw=2.0, t0=0, t1=2 * np.pi, dashed=False, z=14):
    t = np.linspace(t0, t1, 160)
    ax.plot(c[0] + r * np.cos(t), c[1] + r * np.sin(t), color=P.edge(tok), lw=lw, zorder=z,
            ls=(0, (2.5, 1.6)) if dashed else "-", solid_capstyle="round")


def relaxase(xy, z=17):
    ax.add_patch(bio.core.Circle(xy, 0.2, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.0, zorder=z))


def pair(i, apart):
    x = i * W + W / 2
    yd, yr = (6.0, 2.3) if apart else (5.15, 2.85)
    M.bacillus(ax, (x, yd), 5.2, 2.0, token=DON, zorder=5)
    M.bacillus(ax, (x, yr), 5.2, 2.0, token=REC, zorder=5)
    bio.label(ax, (x - 2.25, yd + 0.55), "donor", size="tiny", ha="left", color=P.on_fill(), zorder=20)
    bio.label(ax, (x - 2.25, yr - 0.55), "recipient", size="tiny", ha="left", color=P.on_fill(), zorder=20)
    return x, yd, yr


def t4ss(x, y0, y1):
    ax.add_patch(bio.core.FancyBboxPatch((x - 0.32, y0), 0.64, y1 - y0, boxstyle="round,pad=0,rounding_size=0.12",
                                         facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=12))


titles = ["1  Pilus contact and retraction", "2  Mating pair; nicking at oriT", "3  Strand transfer and replication",
          "4  Recircularization"]
for i, t in enumerate(titles):
    bio.label(ax, (i * W + 0.3, 8.05), t, size="small", bold=True, ha="left")

# ---- 1 ----
x, yd, yr = pair(0, True)
ax.plot([x + 0.6, x + 0.9], [yd - 1.0, yr + 1.0], color=P.edge("dna"), lw=2.0, zorder=4)
bio.arrow(ax, (x + 1.5, yr + 1.2), (x + 1.5, yd - 1.15), kind="process", lw=1.0)
bio.label(ax, (x + 1.7, (yd + yr) / 2), "pilus\nretracts", size="tiny", ha="left")
bio.callout(ax, (x + 0.75, (yd + yr) / 2), (x - 1.6, (yd + yr) / 2), "sex pilus", size="tiny")
ring((x - 0.9, yd + 0.1), 0.42, "highlight", lw=2.2)
bio.label(ax, (x - 0.9, yd + 0.1), "F", size="tiny", bold=True, color=P.on_fill())
ring((x + 1.1, yd + 0.05), 0.55, "dna", lw=1.2)
bio.label(ax, (x + 1.1, yd + 0.05), "chr", size="tiny", color=P.on_fill())

# ---- 2 ----
x, yd, yr = pair(1, False)
t4ss(x, yr + 0.55, yd - 0.55)
c = (x - 0.2, yd + 0.25)
ring(c, 0.5, "highlight", lw=2.2)
nick = (c[0] + 0.5 * np.cos(-1.2), c[1] + 0.5 * np.sin(-1.2))
relaxase(nick)
bio.callout(ax, nick, (x + 0.55, yd + 0.45), "relaxase at oriT", size="tiny").set_color(P.on_fill())
bio.callout(ax, (x + 0.32, yr + 0.75), (x + 0.75, yr + 0.45), "T4SS", size="tiny").set_color(P.on_fill())

# ---- 3 ----
x, yd, yr = pair(2, False)
t4ss(x, yr + 0.55, yd - 0.55)
c = (x - 0.6, yd + 0.25)
ring(c, 0.5, "highlight", lw=1.4)                                   # retained circular strand
ring(c, 0.62, "positive", lw=1.8, t0=-1.0, t1=2.9)                  # new strand made by rolling circle
bio.label(ax, (c[0] + 1.9, c[1] + 0.55), "new strand\n(rolling circle)", size="tiny", color=P.edge("positive"))
# displaced single strand running through the T4SS into the recipient
p0 = np.array([c[0] + 0.5 * np.cos(-0.9), c[1] + 0.5 * np.sin(-0.9)])
p1 = np.array([x, yd - 0.75])
tt = np.linspace(0, 1, 30)[:, None]
q = (1 - tt) ** 2 * p0 + 2 * tt * (1 - tt) * np.array([x, c[1] - 0.3]) + tt ** 2 * p1
ax.plot(q[:, 0], q[:, 1], color=P.edge("highlight"), lw=1.8, zorder=15)
yy = np.linspace(yd - 0.75, yr + 0.2, 20)
ax.plot(np.full_like(yy, x), yy, color=P.edge("highlight"), lw=1.8, zorder=15)
relaxase((x, yr + 0.15))
bio.label(ax, (x - 0.3, yr + 0.15), "5′", size="tiny", ha="right", color=P.on_fill())
bio.callout(ax, (x, yr + 0.6), (x + 0.6, yr + 0.45), "single strand", size="tiny").set_color(P.on_fill())
for k in range(3):                                                  # complementary strand in the recipient
    ax.plot([x - 0.18, x - 0.18], [yr + 0.35 + 0.25 * k, yr + 0.5 + 0.25 * k], color=P.edge("positive"), lw=1.6,
            zorder=15)

# ---- 4 ----
x, yd, yr = pair(3, False)
for cc, z in (((x - 0.5, yd + 0.25), 14), ((x + 0.3, yr - 0.15), 14)):
    ring(cc, 0.5, "highlight", lw=2.2)
    ring(cc, 0.38, "positive", lw=1.4)
bio.label(ax, (x + 1.15, yd + 0.25), "F+", size="small", bold=True, color=P.on_fill(), zorder=20)
bio.label(ax, (x + 1.35, yr - 0.15), "F+", size="small", bold=True, color=P.on_fill(), zorder=20)
bio.label(ax, (x, 0.75), "both cells now donors", size="tiny", color=P.muted())

for i in range(3):
    bio.arrow(ax, ((i + 1) * W - 0.25, 4.1), ((i + 1) * W + 0.2, 4.1), kind="process", lw=1.0, head=0.16)
