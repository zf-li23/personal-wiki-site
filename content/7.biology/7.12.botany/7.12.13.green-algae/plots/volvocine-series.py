"""The volvocine series (schematic, not to scale): Chlamydomonas, Gonium, Pandorina, Eudorina, Pleodorina,
Volvox. Green: motile somatic (vegetative) cells; yellow: reproductive cells (gonidia). Each colony
cell is of the Chlamydomonas type with two flagella pointing outwards."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(36, 12.8)
Y = 6.6


def circ(c, r, n=60):
    t = np.linspace(0, 2 * np.pi, n)
    return np.c_[c[0] + r * np.cos(t), c[1] + r * np.sin(t)]


def cell(c, r, token="chloroplast", flag_dir=None, flen=1.0, z=8):
    bio.shape(ax, circ(c, r, 30), token=token, lw=0.7, zorder=z)
    if flag_dir is not None:
        d = np.asarray(flag_dir, float)
        d = d / np.hypot(*d)
        n = np.array([-d[1], d[0]])
        base = np.asarray(c) + d * r
        for sg in (-1, 1):
            t = np.linspace(0, 1, 12)[:, None]
            pts = base + d * (t * r * 1.6 * flen) + n * sg * (0.25 * r + t * r * 0.5 * flen)
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge("cell_wall"), lw=0.6, zorder=z - 1)


def gel(c, r, token="vacuole", z=3):
    bio.shape(ax, circ(c, r, 120), token=token, lw=0.9, zorder=z)


def caption(x, name, n, sex):
    bio.label(ax, (x, 2.2), name, size="normal", italic=True)
    bio.label(ax, (x, 1.45), n, size="small")
    bio.label(ax, (x, 0.8), sex, size="small", color=P.muted())


xs = [2.2, 7.4, 12.8, 18.4, 24.4, 31.4]
# 1 Chlamydomonas
cell((xs[0], Y), 0.7, flag_dir=(0, 1), flen=1.2)
caption(xs[0], "Chlamydomonas", "1 cell", "isogamy")
# 2 Gonium: 16 cells in a flat plate (top view), flagella out of plane shown as dots
gx, gy = xs[1], Y
bio.shape(ax, [[gx - 2.0, gy - 2.0], [gx + 2.0, gy - 2.0], [gx + 2.0, gy + 2.0], [gx - 2.0, gy + 2.0]], token="vacuole", lw=0.9, zorder=3)
for i in range(4):
    for j in range(4):
        cell((gx - 1.5 + i, gy - 1.5 + j), 0.36)
caption(xs[1], "Gonium", "4–32 cells (plate)", "isogamy")
# 3 Pandorina: 16 cells tightly packed
pc = (xs[2], Y)
gel(pc, 1.95)
ring = [(0, 0)] + [(0.78 * np.cos(a), 0.78 * np.sin(a)) for a in np.linspace(0, 2 * np.pi, 6, endpoint=False)] + \
       [(1.42 * np.cos(a), 1.42 * np.sin(a)) for a in np.linspace(0, 2 * np.pi, 10, endpoint=False) + 0.3]
for dx, dy in ring[:17]:
    d = (dx, dy) if (dx, dy) != (0, 0) else (0, 1)
    cell((pc[0] + dx, pc[1] + dy), 0.33, flag_dir=d if np.hypot(dx, dy) > 1.0 else None, flen=0.8)
caption(xs[2], "Pandorina", "~16 cells, compact", "anisogamy")
# 4 Eudorina: 32 cells at the periphery of a hollow sphere
ec = (xs[3], Y)
gel(ec, 2.3)
for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    d = np.array([np.cos(a), np.sin(a)])
    cell(np.asarray(ec) + d * 1.85, 0.34, flag_dir=d, flen=0.7)
for a in np.linspace(0, 2 * np.pi, 8, endpoint=False) + 0.2:
    d = np.array([np.cos(a), np.sin(a)])
    cell(np.asarray(ec) + d * 0.95, 0.3, z=5)
caption(xs[3], "Eudorina", "16–64 cells, hollow", "anisogamy (near oogamy)")
# 5 Pleodorina: small somatic cells anterior (top), large reproductive cells posterior
plc = (xs[4], Y)
gel(plc, 2.5)
for a in np.linspace(0, 2 * np.pi, 18, endpoint=False):
    d = np.array([np.cos(a), np.sin(a)])
    big = d[1] < -0.15
    cell(np.asarray(plc) + d * (1.95 if big else 2.1), 0.42 if big else 0.28, token="highlight" if big else "chloroplast",
         flag_dir=d, flen=0.6 if big else 0.9)
caption(xs[4], "Pleodorina", "32–128 cells", "anisogamy or oogamy")
bio.callout(ax, (plc[0] - 1.3, plc[1] + 1.7), (plc[0] - 2.6, Y + 3.9), "Somatic", size="small")
bio.callout(ax, (plc[0] + 1.0, plc[1] - 1.75), (plc[0] + 2.4, Y - 3.4), "Reproductive", size="small")
# 6 Volvox: thousands of small somatic cells, a few gonidia, daughter colonies inside
vc = np.array([xs[5], Y])
R = 3.3
gel(vc, R)
for a in np.linspace(0, 2 * np.pi, 64, endpoint=False):
    d = np.array([np.cos(a), np.sin(a)])
    cell(vc + d * (R - 0.16), 0.13, flag_dir=d, flen=1.0, z=8)
for a in (np.radians(-60), np.radians(-100), np.radians(-140)):
    d = np.array([np.cos(a), np.sin(a)])
    cell(vc + d * (R - 0.55), 0.36, token="highlight", z=9)
for dc, rr in (((-0.9, 0.7), 1.0), ((0.9, 0.2), 0.85)):
    c2 = vc + np.array(dc)
    gel(c2, rr, z=5)
    for a in np.linspace(0, 2 * np.pi, 22, endpoint=False):
        d = np.array([np.cos(a), np.sin(a)])
        cell(c2 + d * (rr - 0.1), 0.08, z=6)
caption(xs[5], "Volvox", "500 to >50 000 cells", "oogamy (sperm packets)")
bio.callout(ax, vc + np.array([np.cos(np.radians(-100)), np.sin(np.radians(-100))]) * (R - 0.55), (vc[0] + 2.6, Y - 4.0),
            "Gonidium", size="small")
bio.callout(ax, vc + np.array([-0.9, 1.4]), (vc[0] - 2.6, Y + 4.2), "Daughter colony", size="small")
bio.callout(ax, vc + np.array([R * 0.7, R * 0.7]), (vc[0] + 0.9, Y + 4.2), "Somatic cells", size="small")
# trend arrow
bio.arrow(ax, (0.8, 11.9), (35.0, 11.9), kind="process", color=P.muted())
bio.label(ax, (18.0, 12.3), "More cells; division of labour between somatic and reproductive cells; isogamy → oogamy",
          size="small", color=P.muted())
