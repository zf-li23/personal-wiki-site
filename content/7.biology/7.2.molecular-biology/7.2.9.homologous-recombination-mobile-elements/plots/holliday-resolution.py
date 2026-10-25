# The open (square-planar) Holliday junction and its two resolutions. Arms are coloured by the parental
# duplex they derive from: blue flanks A and B, pink flanks a and b. The continuous strands run between
# two arms of the same parent (A-B, a-b corners); the exchanged strands pass between a blue and a pink arm.
# Cutting the exchanged strands (1) restores A-B and a-b (noncrossover, patch); cutting the continuous
# strands (2) gives A-b and a-B (crossover, splice). Heteroduplex near the junction is drawn as a short
# segment of the other colour.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(22, 11)
cx, cy, arm, s = 5.2, 5.4, 3.6, 0.17
BL, PK = "dna", "receptor"
LW = bio.core.LINE * 2.2


def seg(p, q, tok, ls="-"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(tok), lw=LW, solid_capstyle="round", ls=ls, zorder=10)


def rungs(p0, p1, q0, q1, seed):
    a = MB.track(np.linspace(p0[0], p1[0], 16), np.linspace(p0[1], p1[1], 16))
    b = MB.track(np.linspace(q0[0], q1[0], 16), np.linspace(q0[1], q1[1], 16))
    MB.ladder(ax, a, b, MB.sequence(16, seed))


# arms: W = A (blue), N = B (blue), E = a (pink), S = b (pink)
r0 = 0.35
# W arm (y = cy +- s)
rungs((cx - arm, cy + s), (cx - r0, cy + s), (cx - arm, cy - s), (cx - r0, cy - s), "W")
rungs((cx + r0, cy + s), (cx + arm, cy + s), (cx + r0, cy - s), (cx + arm, cy - s), "E")
rungs((cx - s, cy + r0), (cx - s, cy + arm), (cx + s, cy + r0), (cx + s, cy + arm), "N")
rungs((cx - s, cy - arm), (cx - s, cy - r0), (cx + s, cy - arm), (cx + s, cy - r0), "S")
# continuous strands: NW (W top -> N left, blue), SE (E bottom -> S right, pink)
seg((cx - arm, cy + s), (cx - s, cy + s), BL); seg((cx - s, cy + s), (cx - s, cy + arm), BL)
seg((cx + arm, cy - s), (cx + s, cy - s), PK); seg((cx + s, cy - s), (cx + s, cy - arm), PK)
# exchanged strands: NE (N right blue -> E top pink), SW (S left pink -> W bottom blue)
seg((cx + s, cy + arm), (cx + s, cy + s), BL); seg((cx + s, cy + s), (cx + arm, cy + s), PK)
seg((cx - s, cy - arm), (cx - s, cy - s), PK); seg((cx - s, cy - s), (cx - arm, cy - s), BL)
for (x, y, t) in ((cx - arm - 0.45, cy, "A"), (cx, cy + arm + 0.45, "B"), (cx + arm + 0.45, cy, "a"), (cx, cy - arm - 0.45, "b")):
    bio.label(ax, (x, y), t, size="title", bold=True, italic=True)


def tri(x, y, ang, text):
    v = np.array([[0, 0.0], [-0.17, 0.3], [0.17, 0.3]])
    c, sn = np.cos(ang), np.sin(ang)
    v = v @ np.array([[c, sn], [-sn, c]]) + (x, y)
    ax.fill(v[:, 0], v[:, 1], color=P.edge("negative"), zorder=20, lw=0)
    bio.label(ax, (x + 0.55 * np.sin(-ang) * 0 + (0.5 if x > cx else -0.5), y + (0.5 if y > cy else -0.5)), text,
              size="small", bold=True, color=P.edge("negative"))


# cut 1 on exchanged strands (NE and SW corners), cut 2 on continuous strands (NW, SE)
tri(cx + 0.55, cy + 0.55, np.pi * 0.75, "1")
tri(cx - 0.55, cy - 0.55, -np.pi * 0.25, "1")
tri(cx - 0.55, cy + 0.55, -np.pi * 0.75, "2")
tri(cx + 0.55, cy - 0.55, np.pi * 0.25, "2")
bio.panel(ax, "A", (0.4, 10.4))
bio.label(ax, (1.0, 10.4), "Open Holliday junction", size="normal", bold=True, ha="left")
bio.label(ax, (cx + 2.0, cy + 2.2), "exchanged\nstrands", size="tiny", color=P.muted())
bio.label(ax, (cx - 2.0, cy + 2.2), "continuous\nstrands", size="tiny", color=P.muted())


def product(y, left, right, lt, rt, patch_tok, x0=12.4, x1=20.8, xp=(16.0, 17.2)):
    xm = 16.6
    for yy, (tl, tr) in ((y + s, (left, right)), (y - s, (left, right))):
        seg((x0, yy), (xm, yy), tl)
        seg((xm, yy), (x1, yy), tr)
    rungs((x0, y + s), (x1, y + s), (x0, y - s), (x1, y - s), f"p{y}")
    seg((xp[0], y + s), (xp[1], y + s), patch_tok)
    bio.label(ax, (x0 - 0.45, y), lt, size="title", bold=True, italic=True)
    bio.label(ax, (x1 + 0.45, y), rt, size="title", bold=True, italic=True)


bio.panel(ax, "B", (11.0, 10.4))
bio.label(ax, (11.6, 10.4), "Cut 1: noncrossover (patch)", size="normal", bold=True, ha="left")
product(8.9, BL, BL, "A", "B", PK)
product(7.5, PK, PK, "a", "b", BL)
bio.panel(ax, "C", (11.0, 5.0))
bio.label(ax, (11.6, 5.0), "Cut 2: crossover (splice)", size="normal", bold=True, ha="left")
product(3.5, BL, PK, "A", "b", PK, xp=(15.6, 16.6))
product(2.1, PK, BL, "a", "B", BL, xp=(15.6, 16.6))
bio.label(ax, (16.6, 0.9), "heteroduplex near the former junction", size="tiny", color=P.muted())
