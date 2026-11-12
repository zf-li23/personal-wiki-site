# The appendicular ovipositor of a female insect (schematic lateral view of the abdominal tip, anterior to
# the left), coloured by segment of origin: from segment 8 (blue) the first valvifer (gonocoxite 8) and the
# first, ventral valvulae (gonapophyses 8); from segment 9 (green) the second valvifer (gonocoxite 9), the
# second, inner valvulae (gonapophyses 9) and the third, dorsal valvulae (gonoplacs). The valvulae slide on
# one another along a tongue-and-groove joint (olistheter). In grasshoppers the dorsal and ventral valves
# are short digging blades and the inner valves are small; in katydids all three pairs form a long sabre;
# in aculeate Hymenoptera the ovipositor became the sting. Segments 10-11 bear the cerci.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 10)
S8, S9, OTHER = "channel", "enzyme", "neutral"
segs = [(1.0, 3.2, OTHER, "7"), (3.2, 5.6, S8, "8"), (5.6, 8.0, S9, "9"), (8.0, 9.6, OTHER, "10")]
for a, b, tok, n in segs:
    bio.shape(ax, [(a, 6.6), (b, 6.7), (b, 8.4), (a, 8.5)], tok if tok == OTHER else tok, lw=0.9, zorder=4, alpha=1.0)
    bio.label(ax, ((a + b) / 2, 7.55), "T" + n, size="small")
bio.shape(ax, [(1.0, 3.6), (3.2, 3.6), (3.2, 4.6), (1.0, 4.6)], OTHER, lw=0.9, zorder=4)
bio.label(ax, (2.1, 4.1), "S7", size="small")
bio.shape(ax, [(9.6, 6.9), (11.0, 7.0), (11.2, 8.0), (9.6, 8.2)], OTHER, lw=0.9, zorder=4)
bio.label(ax, (10.3, 7.55), "Epiproct", size="tiny")
ax.plot([10.5, 12.4], [7.3, 8.3], color=P.edge("neutral"), lw=2.4, zorder=5, solid_capstyle="round")
# valvifers
bio.shape(ax, [(3.4, 4.0), (5.4, 4.2), (5.2, 5.6), (3.6, 5.4)], S8, lw=0.9, zorder=5)
bio.shape(ax, [(5.8, 4.6), (7.8, 5.0), (7.8, 6.4), (5.8, 6.2)], S9, lw=0.9, zorder=5)
# valvulae: ventral (8), inner (9), dorsal (9)
bio.shape(ax, [(5.2, 4.3), (15.5, 4.6), (17.5, 5.0), (15.5, 4.9), (5.2, 4.8)], S8, lw=0.9, zorder=6)
bio.shape(ax, [(7.6, 5.0), (15.5, 5.1), (17.3, 5.25), (15.5, 5.35), (7.6, 5.4)], S9, lw=0.9, zorder=7)
bio.shape(ax, [(7.8, 5.6), (15.5, 5.55), (17.5, 5.5), (15.5, 6.0), (7.8, 6.2)], S9, lw=0.9, zorder=6, alpha=1.0)
ax.plot([16.8, 17.3], [5.22, 5.28], color=P.ink(), lw=0.6, zorder=8)
C = bio.callout
C(ax, (4.4, 4.8), (2.0, 2.4), "1st valvifer (gonocoxite 8)")
C(ax, (11.0, 4.55), (9.0, 2.4), "1st (ventral) valvula, gonapophysis 8")
C(ax, (6.8, 5.6), (5.0, 9.4), "2nd valvifer (gonocoxite 9)")
C(ax, (13.0, 5.25), (18.0, 3.4), "2nd (inner) valvula, gonapophysis 9")
C(ax, (12.0, 5.9), (13.0, 9.0), "3rd (dorsal) valvula, gonoplac")
C(ax, (11.8, 8.0), (16.0, 8.6), "Cercus")
bio.label(ax, (21.5, 7.6), "segment 8", size="small", ha="left")
bio.label(ax, (21.5, 6.9), "segment 9", size="small", ha="left")
bio.shape(ax, [(20.9, 7.45), (21.3, 7.45), (21.3, 7.75), (20.9, 7.75)], S8, lw=0.8, zorder=9)
bio.shape(ax, [(20.9, 6.75), (21.3, 6.75), (21.3, 7.05), (20.9, 7.05)], S9, lw=0.8, zorder=9)
bio.label(ax, (14.0, 1.2), "T = tergum, S = sternum", size="tiny", color=P.muted(), ha="left")
