"""The mitotic spindle and the forces in it (schematic) and the kinematics of anaphase (model curves).

(A) A metaphase spindle of an animal cell. Three classes of microtubules have their minus ends at or near the
poles: kinetochore microtubules (bundled into K-fibers) end on kinetochores; interpolar (non-kinetochore)
microtubules overlap antiparallel at the equator; astral microtubules radiate to the cortex. Forces:
kinesin-5 cross-links antiparallel microtubules and slides them apart (pushes the poles outward); kinesin-14
pulls them together; cortical dynein pulls astral microtubules and the poles toward the cortex;
chromokinesins (kinesin-4/10) on the chromosome arms push the arms away from the poles (polar ejection
force); depolymerization at kinetochores and at the poles (poleward flux) pulls the chromosomes poleward,
resisted by cohesin at the centromere, which puts the sister kinetochores under tension.
(B) Anaphase in a mammalian cell (idealized curves): the distance from the kinetochores to their pole falls at
about 1 um per minute (anaphase A, driven mainly by depolymerization of kinetochore microtubules at the
kinetochore and by flux), while the poles move apart from about 12 to about 22 um (anaphase B, driven by
kinesin-5 sliding at the midzone and cortical dynein), starting slightly later.
"""

import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio import cytoskel as C

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 11.5)
bio.panel(ax, "A", (0.2, 11.3))
c = (8.8, 5.8)
ax.add_patch(__import__("matplotlib.patches", fromlist=["Ellipse"]).Ellipse(
    c, 17.0, 10.0, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.4, zorder=1))
sp = C.spindle(ax, c, half_length=5.0, height=4.2, chromosomes=3, astral=7, interpolar=3, kmts=3, chrom_length=0.9,
               lw=1.3)
poles = sp["poles"]
# labels for the three classes
bio.callout(ax, (c[0] - 2.6, c[1] + 1.05), (3.2, 10.0), "kinetochore microtubules\n(K-fiber)", size="tiny")
bio.callout(ax, (c[0] - 1.5, c[1] + 2.3), (8.0, 10.5), "interpolar microtubules", size="tiny")
bio.callout(ax, (poles[1][0] + 2.2, c[1] + 1.4), (15.2, 10.0), "astral microtubules", size="tiny")
bio.callout(ax, poles[0] + np.array([-0.1, -0.25]), (1.8, 1.7), "centrosome (spindle pole)", size="tiny")
bio.callout(ax, sp["kinetochores"][4], (11.6, 9.4), "sister kinetochores\nunder tension", size="tiny")
# force arrows
yk = c[1] - 2.45
bio.arrow(ax, (c[0] - 0.2, yk), (c[0] - 1.5, yk), kind="process", color=P.edge("enzyme"), lw=1.6)
bio.arrow(ax, (c[0] + 0.2, yk), (c[0] + 1.5, yk), kind="process", color=P.edge("enzyme"), lw=1.6)
bio.label(ax, (c[0], yk - 0.45), "kinesin-5 slides interpolar\nmicrotubules apart", size="tiny", color=P.edge("enzyme"),
          bold=True, va="top")
for s, pole in ((-1, poles[0]), (1, poles[1])):
    bio.arrow(ax, (pole[0] + s * 1.6, pole[1] - 1.9), (pole[0] + s * 2.4, pole[1] - 2.5), kind="process",
              color=P.edge("protein"), lw=1.6)
bio.label(ax, (poles[1][0] + 1.2, poles[1][1] - 3.0), "cortical dynein pulls\nastral microtubules", size="tiny",
          color=P.edge("protein"), bold=True)
# polar ejection on an arm
arm = sp["chromosomes"][2]
bio.arrow(ax, (arm[0] - 0.55, arm[1] + 0.55), (arm[0] - 0.05, arm[1] + 0.55), kind="process", color=P.edge("drug"), lw=1.4)
bio.label(ax, (arm[0] - 2.6, arm[1] + 0.85), "polar ejection\n(chromokinesins)", size="tiny", color=P.edge("drug"), bold=True)
# poleward pull at kinetochore
k0 = sp["kinetochores"][0]
bio.arrow(ax, (k0[0] + 0.35, k0[1] - 0.45), (k0[0] + 1.3, k0[1] - 0.45), kind="process", color=P.edge("negative"), lw=1.4)
bio.label(ax, (k0[0] + 2.8, k0[1] - 0.95), "depolymerization and\nflux pull poleward", size="tiny",
          color=P.edge("negative"), bold=True)

# ----- B
bio.panel(ax, "B", (18.4, 11.3))
b = charts.axes_at(ax, (19.8, 2.0, 6.8, 8.0))
t = np.linspace(-2, 12, 600)
sA = np.clip(t / 5.5, 0, 1)
kp = 6.0 - 5.2 * sA
sB = np.clip((t - 1.0) / 6.0, 0, 1)
pp = 12.0 + 10.0 * (3 * sB ** 2 - 2 * sB ** 3)
b.plot(t, kp, color=charts.line("negative"), lw=1.9)
b.plot(t, pp, color=charts.line("enzyme"), lw=1.9)
b.axvline(0, color=P.muted(), ls=":", lw=0.9)
b.text(0.2, 23.3, "anaphase onset", fontsize=FT["tiny"], color=P.muted())
b.text(6.2, 3.0, "kinetochore to pole\n(anaphase A)", fontsize=FT["tiny"], color=charts.line("negative"))
b.text(2.0, 18.0, "pole to pole\n(anaphase B)", fontsize=FT["tiny"], color=charts.line("enzyme"))
b.set_xlim(-2, 12)
b.set_ylim(0, 25)
charts.style_axes(b, "time / min", "distance / µm")
