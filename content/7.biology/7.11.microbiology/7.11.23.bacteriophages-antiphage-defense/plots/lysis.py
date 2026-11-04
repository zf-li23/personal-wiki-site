# How a phage lyses a Gram-negative host.
# A: the three steps of the lambda pathway, on cross-sections of the envelope: the holin accumulates in
#    the inner membrane while the endolysin waits in the cytoplasm; triggering opens large holes, the
#    proton-motive force collapses and the endolysin reaches the peptidoglycan; the spanin then fuses the
#    inner and outer membranes.
# B: the clock. Holin accumulates during late gene expression and triggers when the free holin reaches a
#    threshold; the antiholin, made from an upstream translational start, holds part of the holin inactive
#    and becomes hole-competent at the moment of triggering.
# C: the pinholin-SAR endolysin pathway of phage 21: the endolysin is exported and tethered to the
#    membrane in advance, and small pinholes that only depolarize the membrane release it.
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import microbio as M
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(34, 13.4)
MUT = P.muted()
HOL, END, SPN = "highlight", "drug", "negative"


def holin(x, y, token=HOL, w=0.2, h=0.62, zorder=14):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=P.fill(token), edgecolor=P.edge(token),
                           lw=0.6, zorder=zorder))


def endolysin(x, y, r=0.18, token=END, zorder=14):
    ax.add_patch(Circle((x, y), r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.7, zorder=zorder))


def strip(xa, w, y, title, seed):
    xb = xa + w
    L = M.envelope(ax, xa, xb, y, kind="gram-", top=y + 4.2, seed=seed, zorder=4)
    bio.label(ax, (xa + w / 2, y + 4.7), title, size="small", bold=True)
    return L, xa, xb


# ---------------------------------------------------------------- A: the three steps
bio.panel(ax, "A", (0.2, 13.1))
bio.label(ax, (0.9, 12.9), "The λ pathway: holin, endolysin, spanin", size="title", bold=True, ha="left")
steps = [("1  accumulation", "late genes are expressed;\nthe holin collects in the inner\nmembrane, the endolysin waits\nin the cytoplasm"),
         ("2  triggering", "the holin opens micron-scale\nholes, the proton-motive force\ncollapses and the endolysin\nreaches the peptidoglycan"),
         ("3  fusion", "with the wall degraded the\nspanin fuses the inner and\nouter membranes, and the\ncell lyses")]
for k, (ttl, txt) in enumerate(steps):
    L, xa, xb = strip(0.6 + k * 5.1, 4.4, 4.8, ttl, 3 + k)
    xs = np.linspace(xa + 0.5, xb - 0.5, 7)
    if k == 0:
        for x in xs[::2]:
            holin(x, L["im"])
        for x in xs[1::2]:
            endolysin(x + 0.1, L["im"] - 0.8)
    elif k == 1:
        for x in (xs[1], xs[4]):
            ax.add_patch(Rectangle((x - 0.42, L["im"] - 0.34), 0.84, 0.68, facecolor=P.fill("cytoplasm"),
                                   edgecolor="none", zorder=13))
            holin(x - 0.52, L["im"])
            holin(x + 0.52, L["im"])
        for x in xs[::2]:
            endolysin(x, (L["im_hi"] + L["pg_lo"]) / 2 + 0.25)
        bio.arrow(ax, (xs[1], L["im"] + 0.45), (xs[1], L["pg_lo"] - 0.3), kind="process", lw=0.9, head=0.16)
        bio.label(ax, (xb - 0.15, L["im"] - 0.95), "PMF collapses", size="tiny", color=MUT, ha="right", zorder=19)
    else:
        for x in (xs[1], xs[5]):
            ax.plot([x, x], [L["im"], L["om"]], color=P.edge(SPN), lw=2.4, zorder=14)
        ax.plot([xs[3] - 0.6, xs[3] + 0.6], [(L["im"] + L["om"]) / 2] * 2, color=P.edge(SPN), lw=2.8, zorder=15)
        bio.label(ax, (xs[3], (L["im"] + L["om"]) / 2 - 0.5), "membranes fused", size="tiny", color=MUT, zorder=19)
    bio.label(ax, (xa + 2.2, 2.4), txt, size="tiny", color=MUT)
for i, (name, tok) in enumerate((("holin", HOL), ("endolysin", END), ("spanin", SPN))):
    ax.add_patch(Rectangle((0.8 + i * 3.4, 0.6), 0.28, 0.48, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6))
    bio.label(ax, (1.25 + i * 3.4, 0.84), name, size="tiny", ha="left")

# ---------------------------------------------------------------- B: the clock
bio.panel(ax, "B", (16.4, 13.1))
bio.label(ax, (17.1, 12.9), "The holin clock", size="title", bold=True, ha="left")
pl = quant.Plot(ax, (17.9, 7.2, 5.6, 4.0), xlim=(0, 40), ylim=(0, 1.3), xlabel="time after infection / min",
                ylabel="holin in the membrane", xticks=[0, 10, 20, 30, 40], yticks=[0, 0.5, 1.0])
t = np.linspace(0, 40, 400)
thr = 0.6
trig = 8 + 30 * thr
free = np.clip((t - 8) / 30, 0, None)
held = np.clip((t - 8) / 30, 0, None) * 0.5
m = t <= trig
pl.line(t[m], free[m], "channel")
pl.line(t[m], held[m], "negative")
pl.line(t[t >= trig], np.full((t >= trig).sum(), 1.2), "channel", dashed=True)
pl.hline(thr, text="threshold: rafts form, holes open", side="left")
pl.vline(trig)
pl.text(13.5, 0.72, "free holin", size="tiny", token="channel", ha="left")
pl.text(17.0, 0.18, "held by antiholin", size="tiny", token="negative", ha="left")
pl.text(27.5, 1.04, "triggering: the hole-forming\nmolecules triple", size="tiny", ha="left", va="top")
bio.label(ax, (17.3, 5.6), "The holin gene has two translational starts.\n"
                           "The upstream one adds a positive residue that\n"
                           "keeps the first transmembrane helix out of the\n"
                           "bilayer: that product is the antiholin, and it\n"
                           "binds holin in an inactive heterodimer. At\n"
                           "triggering, depolarization lets its helix enter\n"
                           "the bilayer, so the inhibitor becomes an\n"
                           "activator and the switch is sharp.\n\n"
                           "A single missense change in the holin moves\n"
                           "the time of lysis by many minutes; a\n"
                           "protonophore triggers lysis at once.",
          size="tiny", ha="left", va="top", color=MUT)

# ---------------------------------------------------------------- C: pinholin and SAR endolysin
bio.panel(ax, "C", (24.6, 13.1))
bio.label(ax, (25.3, 12.9), "Pinholin and SAR endolysin (phage 21)", size="small", bold=True, ha="left")
for k, (ttl, txt) in enumerate([("1  waiting", "the endolysin is exported by\nSec and held inactive, tethered\nto the outside of the membrane"),
                                ("2  depolarization", "heptameric pinholes collapse the\nPMF; the SAR domain leaves the\nbilayer and the endolysin refolds\ninto its active form")]):
    L, xa, xb = strip(25.2 + k * 4.4, 3.9, 4.8, ttl, 8 + k)
    xs = np.linspace(xa + 0.5, xb - 0.5, 5)
    if k == 0:
        for x in xs[::2]:
            holin(x, L["im"], h=0.5)
        for x in xs[1::2]:
            endolysin(x, L["im_hi"] + 0.4, token="neutral")
            ax.plot([x, x], [L["im_hi"], L["im_hi"] + 0.22], color=P.edge("neutral"), lw=1.0, zorder=13)
    else:
        for x in (xs[1], xs[3]):
            ax.add_patch(Rectangle((x - 0.1, L["im"] - 0.3), 0.2, 0.6, facecolor=P.fill("cytoplasm"),
                                   edgecolor="none", zorder=13))
            holin(x - 0.2, L["im"], h=0.5)
            holin(x + 0.2, L["im"], h=0.5)
        for x in xs[::2]:
            endolysin(x, (L["im_hi"] + L["pg_lo"]) / 2 + 0.2)
    bio.label(ax, (xa + 1.95, 2.4), txt, size="tiny", color=MUT)
bio.label(ax, (25.2, 0.9), "Small phages with no room for a lysis cassette use single-gene lysis:\n"
                           "protein E of φX174 inhibits the translocase MraY, protein A2 of Qβ\n"
                           "inhibits MurA, and the growing cell lyses itself.", size="tiny", ha="left", color=MUT)
