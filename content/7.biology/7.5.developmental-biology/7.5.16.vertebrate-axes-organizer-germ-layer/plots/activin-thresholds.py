# Threshold responses of Xenopus animal-cap cells to Activin (Formula 16.3.1). A cell with R_T = 5000 receptors binds
# Activin with dissociation constant K_D; the number of occupied receptors is R_T c / (c + K_D). Occupancy of about 100
# receptors switches on brachyury (mesoderm, muscle), about 300 switches on goosecoid (dorsal mesoderm, organizer)
# (Dyson and Gurdon, 1998); below the first threshold cells stay epidermal. A: occupancy against Activin
# concentration with the two thresholds; the fates form three bands, and a three-fold step in concentration moves a
# cell from one to the next. B: mutual repression between Goosecoid and Brachyury (Formula 16.3.2, simulated on a row
# of cells exposed to a graded Activin input) turns the graded occupancy into two domains with a sharp border.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
RT, KD = 5000.0, 1.0
c = np.logspace(-3, 0, 300)
occ = RT * c / (c + KD)
t1, t2 = 100.0, 300.0
c1, c2 = KD * t1 / (RT - t1), KD * t2 / (RT - t2)

fig, ax = bio.canvas(22.0, 8.4)
pa = C.axes_at(ax, (1.8, 1.5, 8.6, 5.6))
pa.axvspan(c[0], c1, color=P.fill("channel"), alpha=0.25, lw=0)
pa.axvspan(c1, c2, color=P.fill("muscle"), alpha=0.25, lw=0)
pa.axvspan(c2, c[-1], color=P.fill("positive"), alpha=0.25, lw=0)
pa.loglog(c, occ, color=P.ink(), lw=2.0)
for t, name in [(t1, "brachyury on"), (t2, "goosecoid on")]:
    pa.axhline(t, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    pa.text(1.1e-3, t * 1.12, name, fontsize=bio.core.FONT["tiny"], color=P.muted(), style="italic")
for x, txt in [(np.sqrt(c[0] * c1), "epidermis"), (np.sqrt(c1 * c2), "mesoderm"), (np.sqrt(c2 * c[-1]), "dorsal\nmesoderm")]:
    pa.text(x, 2.5e3, txt, fontsize=bio.core.FONT["tiny"], ha="center", va="top", color=P.ink())
pa.set_xlim(c[0], c[-1])
pa.set_ylim(4, 6e3)
C.style_axes(pa, "Activin / K_D", "occupied receptors per cell")
bio.panel(ax, "A", (0.3, 8.2))

# B: mutual repression on a row of cells
n = 60
x = np.linspace(0, 1, n)
act = 0.004 * np.exp(5.5 * x)  # graded Activin, in units of K_D
o = RT * act / (act + KD)
s1 = o / t1
s2 = o / t2


def hill(u, m=4):
    return u ** m / (1 + u ** m)


B = np.zeros(n); G = np.zeros(n)
for _ in range(4000):
    dB = hill(s1) / (1 + (G / 0.3) ** 4) - B
    dG = hill(s2) / (1 + (B / 2.0) ** 2) - G
    B += 0.02 * dB
    G += 0.02 * dG
pb = C.axes_at(ax, (13.0, 1.5, 8.0, 5.6))
pb.plot(x, np.minimum(o / t2, 3) / 3, color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="occupancy (scaled)")
pb.plot(x, B, color=C.line("muscle"), lw=2.0, label="Brachyury")
pb.plot(x, G, color=C.line("positive"), lw=2.0, label="Goosecoid")
pb.set_xlim(0, 1)
pb.set_ylim(0, 1.1)
C.style_axes(pb, "position (low → high Activin)", "level")
pb.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (11.6, 8.2))
