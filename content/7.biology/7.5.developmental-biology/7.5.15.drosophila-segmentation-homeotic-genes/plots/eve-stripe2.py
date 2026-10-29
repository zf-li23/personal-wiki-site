# The even-skipped stripe 2 enhancer as a thermodynamic switch (Formula 15.3.1). A: the minimal stripe 2 element
# (about 480 bp) with its binding sites: five for Bicoid and one for Hunchback (activators, above the line), three
# each for Kruppel and Giant (repressors, below). B: input profiles along the egg (schematic) and the predicted
# probability of activation: the activators define a broad anterior region, anterior Giant cuts it from the front
# and Kruppel from the back, leaving one stripe. C: removing Giant moves the anterior border forward; removing
# Kruppel moves the posterior border back; removing Bicoid sites abolishes the stripe.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
x = np.linspace(0, 1, 400)
bcd = np.exp(-x / 0.2)
hb = 1 / (1 + np.exp((x - 0.48) / 0.02))
gt = np.exp(-((x - 0.25) / 0.06) ** 2)
kr = np.exp(-((x - 0.5) / 0.06) ** 2)
slp = 1 / (1 + np.exp((x - 0.15) / 0.02))  # anterior repressor (Sloppy-paired) in the head region


def theta(c, K):
    return c / (c + K)


def stripe(nb=5, nh=1, nk=3, ng=3, krf=1.0, gtf=1.0):
    # probability that at least two activator sites are occupied (sites independent)
    pb, ph = theta(bcd, 0.5), theta(hb, 0.4)
    q0 = (1 - pb) ** nb * (1 - ph) ** nh
    q1 = nb * pb * (1 - pb) ** max(nb - 1, 0) * (1 - ph) ** nh + nh * ph * (1 - ph) ** max(nh - 1, 0) * (1 - pb) ** nb
    act = 1 - q0 - q1
    quench = (1 - theta(krf * kr, 0.25)) ** nk * (1 - theta(gtf * gt, 0.25)) ** ng * (1 - theta(slp, 0.02))
    return act * quench


fig, ax = bio.canvas(23.0, 12.0)
bio.panel(ax, "A", (0.2, 11.8))
y0 = 9.6
ax.plot([1.2, 21.8], [y0, y0], color=P.edge("dna"), lw=3.0, solid_capstyle="round")
sites = [("B", 2.0, 1), ("K", 3.2, -1), ("B", 4.3, 1), ("G", 5.2, -1), ("H", 6.4, 1), ("K", 7.3, -1), ("B", 8.4, 1), ("G", 9.5, -1),
         ("B", 11.0, 1), ("K", 12.0, -1), ("G", 13.2, -1), ("B", 14.4, 1)]
stok = {"B": "receptor", "H": "channel", "K": "positive", "G": "drug"}
for s, xx, side in sites:
    yy = y0 + side * 0.55
    bio.box(ax, (xx, yy), 0.75, 0.55, token=stok[s], text=s, size="small")
    ax.plot([xx, xx], [y0, yy - side * 0.28], color=P.muted(), lw=0.7)
ax.add_patch(bio.core.FancyBboxPatch((16.4, y0 - 0.3), 3.6, 0.6, boxstyle="round,pad=0,rounding_size=0.1", facecolor=P.fill("dna2"),
                                     edgecolor=P.edge("dna2"), zorder=10))
bio.label(ax, (18.2, y0), "basal promoter → eve", size="tiny", italic=False)
bio.label(ax, (8.0, 11.2), "eve stripe 2 enhancer (about 480 bp, schematic order)", size="small", italic=False)
bio.label(ax, (21.0, 10.5), "B Bicoid  H Hunchback", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (21.0, 8.7), "K Krüppel  G Giant", size="tiny", color=P.muted(), ha="right")

bio.panel(ax, "B", (0.2, 7.6))
pa = C.axes_at(ax, (1.6, 1.4, 9.2, 5.6))
for c, t, n in [(bcd, "receptor", "Bcd"), (hb, "channel", "Hb"), (gt, "drug", "Gt"), (kr, "positive", "Kr"), (slp, "neutral", "Slp")]:
    pa.plot(x, c, color=C.line(t), lw=1.2, ls=(0, (3, 2)))
    i = int(np.argmax(c[20:]) + 20) if n in ("Gt", "Kr") else (20 if n == "Slp" else 60)
    pa.text(x[i], c[i] + 0.05, n, color=C.line(t), fontsize=bio.core.FONT["tiny"], ha="center")
pa.fill_between(x, stripe(), color=P.fill("na"), alpha=0.6, lw=0)
pa.plot(x, stripe(), color=C.line("na"), lw=2.0)
pa.set_xlim(0, 0.8)
pa.set_ylim(0, 1.1)
C.style_axes(pa, "x / L", "level; P(enhancer active)")
pb = C.axes_at(ax, (13.2, 1.4, 9.2, 5.6))
for kw, lab, t in [({}, "wild type", 0.0), ({"gtf": 0.0}, "no Giant", 0.45), ({"krf": 0.0}, "no Krüppel", 0.65),
                   ({"nb": 0}, "no Bicoid sites", 0.8)]:
    col = P.mix(C.line("na"), P.surface(), t)
    pb.plot(x, stripe(**kw), color=col, lw=2.0 if t == 0 else 1.5, label=lab, ls="-" if t == 0 else (0, (4, 2)))
pb.set_xlim(0, 0.8)
pb.set_ylim(0, 1.1)
C.style_axes(pb, "x / L", "P(enhancer active)")
pb.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (11.8, 7.6))
