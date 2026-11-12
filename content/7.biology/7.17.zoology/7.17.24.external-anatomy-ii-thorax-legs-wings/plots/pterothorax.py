# A: a wing-bearing thoracic segment (mesothorax) in lateral view, anterior to the left (schematic). The
# notum bears the wing; the pleuron is divided by the pleural suture (externally the line of the internal
# pleural ridge) into the anterior episternum and posterior epimeron; at the top of the suture the
# pleural wing process is the fulcrum of the wing, at its foot the pleural coxal process articulates the
# coxa. The basalare (in front) and subalare (behind) are small sclerites in the membrane below the wing
# base on which the direct flight muscles insert. The trochantin lies in front of the coxa; the spiracle
# in the membrane between pro- and mesothorax. B: dorsal subdivisions of the notum: prescutum, scutum
# and scutellum form the alinotum carrying the wings; the postnotum (phragma-bearing) belongs to the
# acrotergite of the following segment.
import wikibio as bio
from matplotlib.patches import Ellipse

P = bio.P
fig, ax = bio.canvas(26, 12)
bio.panel(ax, "A", (0.2, 11.6))
bio.panel(ax, "B", (16.2, 11.6))
S = bio.shape
S(ax, [(2.0, 8.6), (10.5, 8.6), (11.2, 9.3), (9.5, 10.2), (3.0, 10.2), (1.6, 9.4)], "receptor", lw=1.0, zorder=4)   # notum
S(ax, [(10.5, 8.6), (12.6, 8.8), (12.8, 9.9), (11.2, 9.3)], "protein", lw=0.9, zorder=4)                           # postnotum
S(ax, [(2.2, 3.6), (6.3, 3.6), (6.6, 8.2), (2.3, 8.2)], "enzyme", lw=1.0, zorder=4)                                # episternum
S(ax, [(6.3, 3.6), (10.0, 3.6), (10.4, 8.2), (6.6, 8.2)], "positive", lw=1.0, zorder=4)                            # epimeron
ax.plot([6.6, 6.3], [8.2, 3.6], color=P.ink(), lw=2.2, zorder=6)                                                    # pleural suture
S(ax, [(6.35, 8.15), (6.85, 8.15), (6.7, 8.75), (6.5, 8.75)], "drug", lw=0.9, zorder=7)                           # pleural wing process
S(ax, [(4.4, 8.3), (5.4, 8.3), (5.3, 8.75), (4.5, 8.75)], "drug", lw=0.8, zorder=6)                               # basalare
S(ax, [(7.9, 8.3), (8.9, 8.3), (8.8, 8.75), (8.0, 8.75)], "drug", lw=0.8, zorder=6)                               # subalare
S(ax, [(2.0, 1.0), (10.4, 1.0), (10.0, 2.2), (2.3, 2.2)], "antibody", lw=1.0, zorder=4)                           # sternum
# coxa and trochantin
cx = Ellipse((6.0, 2.85), 2.2, 1.3, facecolor=P.fill("coxa"), edgecolor=P.edge("coxa"), lw=1.0, zorder=6)
ax.add_patch(cx)
S(ax, [(3.6, 3.0), (4.9, 3.5), (4.9, 3.0), (3.7, 2.7)], "bone", lw=0.8, zorder=6)
ax.add_patch(Ellipse((1.6, 7.0), 0.5, 0.8, facecolor=P.fill("neutral"), edgecolor=P.ink(), lw=0.9, zorder=7))      # spiracle
# wing stub
ax.plot([6.6, 8.0, 14.0], [8.9, 10.9, 11.4], color=P.edge("er"), lw=2.0, zorder=3)
bio.label(ax, (13.8, 11.0), "Wing", size="small", color=P.muted())
C = bio.callout
C(ax, (5.0, 9.6), (3.0, 11.3), "Notum (alinotum)")
C(ax, (12.0, 9.2), (13.6, 9.6), "Postnotum")
C(ax, (6.6, 8.6), (11.0, 7.4), "Pleural wing process")
C(ax, (4.9, 8.5), (0.6, 10.6), "Basalare")
C(ax, (8.4, 8.5), (11.0, 8.2), "Subalare")
C(ax, (4.2, 6.0), (0.6, 5.2), "Episternum")
C(ax, (8.4, 6.0), (11.6, 6.0), "Epimeron")
C(ax, (6.45, 5.5), (11.6, 5.0), "Pleural suture")
C(ax, (6.2, 3.6), (11.6, 4.0), "Pleural coxal process")
C(ax, (6.6, 2.6), (11.6, 3.0), "Coxa")
C(ax, (4.0, 2.95), (0.6, 3.5), "Trochantin")
C(ax, (8.0, 1.5), (11.6, 1.6), "Sternum")
C(ax, (1.6, 7.2), (0.6, 8.6), "Spiracle")
bio.label(ax, (6.2, 0.4), "anterior  ←", size="tiny", color=P.muted())
# B: dorsal notum
x0 = 20.5
S(ax, [(x0 - 1.8, 10.6), (x0 + 1.8, 10.6), (x0 + 1.6, 9.8), (x0 - 1.6, 9.8)], "receptor", lw=0.9, zorder=4)
S(ax, [(x0 - 1.6, 9.8), (x0 + 1.6, 9.8), (x0 + 2.0, 7.0), (x0 + 1.0, 6.2), (x0 - 1.0, 6.2), (x0 - 2.0, 7.0)], "channel", lw=0.9, zorder=4)
S(ax, [(x0 - 1.0, 6.2), (x0 + 1.0, 6.2), (x0 + 0.6, 5.0), (x0 - 0.6, 5.0)], "drug", lw=0.9, zorder=4)
S(ax, [(x0 - 1.7, 4.9), (x0 + 1.7, 4.9), (x0 + 1.5, 4.2), (x0 - 1.5, 4.2)], "protein", lw=0.9, zorder=4)
for s in (-1, 1):
    ax.plot([x0 + s * 2.0, x0 + s * 4.2], [8.6, 9.4], color=P.edge("er"), lw=2.0, zorder=3)
C(ax, (x0 + 1.2, 10.2), (x0 + 3.0, 11.2), "Prescutum")
C(ax, (x0 + 1.0, 8.0), (x0 + 3.2, 7.4), "Scutum")
C(ax, (x0 + 0.5, 5.6), (x0 + 3.2, 6.0), "Scutellum")
C(ax, (x0 + 1.2, 4.55), (x0 + 3.2, 4.4), "Postnotum")
bio.label(ax, (x0 - 3.2, 9.9), "anterior\n↑", size="tiny", color=P.muted())
