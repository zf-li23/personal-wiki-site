import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

fig, ax = plt.subplots(figsize=(10, 6.2))
ax.set_xlim(-0.2, 15.6)
ax.set_ylim(-0.9, 9.7)
ax.set_aspect("equal")
ax.axis("off")

BOX = "C0"
WIRE = "0.45"
CTRL = "C1"


def box(x0, y0, x1, y1, label, fs=10):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec=BOX, lw=1.6))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2, label, ha="center", va="center", fontsize=fs, weight="bold")


def mux(xc, yc, h, labels):
    """Vertical 2:1 or 3:1 multiplexer; labels from top to bottom."""
    w = 0.5
    ax.add_patch(Polygon([(xc - w / 2, yc + h / 2), (xc + w / 2, yc + h / 2 - 0.2),
                          (xc + w / 2, yc - h / 2 + 0.2), (xc - w / 2, yc - h / 2)],
                         closed=True, fill=False, ec=BOX, lw=1.6))
    n = len(labels)
    ys = [yc + h / 2 - (i + 0.5) * h / n for i in range(n)]
    for y, lab in zip(ys, labels):
        ax.text(xc - 0.12, y, lab, ha="center", va="center", fontsize=8)
    return ys


def wire(points, arrow=True, color=WIRE, ls="-"):
    xs, ys = zip(*points)
    ax.plot(xs[:-1] + (xs[-1],), ys, color=color, lw=1.2, ls=ls)
    if arrow:
        ax.annotate("", xy=points[-1], xytext=points[-2],
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.2, shrinkA=0, shrinkB=0))


def dot(x, y):
    ax.plot([x], [y], "o", color=WIRE, ms=3.5)


# components
pcm = mux(0.75, 5.0, 1.4, ["1", "0"])           # PCSel: 1 = ALU, 0 = PC + 4
box(1.4, 4.5, 2.4, 5.5, "PC")
box(3.1, 6.6, 4.0, 7.3, "+4")
box(3.0, 3.3, 4.2, 4.8, "IMEM")
box(5.3, 3.6, 7.0, 6.4, "")
ax.text(6.15, 6.1, "RegFile", ha="center", va="center", fontsize=10, weight="bold")
for y, lab in [(5.8, "DataD"), (5.3, "AddrD"), (4.8, "AddrA"), (4.2, "AddrB")]:
    ax.text(5.38, y, lab, ha="left", va="center", fontsize=7.5)
for y, lab in [(5.3, "DataA"), (4.2, "DataB")]:
    ax.text(6.95, y, lab, ha="right", va="center", fontsize=7.5)
box(5.6, 1.3, 7.0, 2.3, "ImmGen", fs=9)
box(7.6, 2.5, 8.7, 3.3, "Branch\nComp", fs=8)
am = mux(9.2, 5.6, 1.2, ["1", "0"])             # ASel: 1 = PC, 0 = rs1
bm = mux(9.2, 3.8, 1.2, ["1", "0"])             # BSel: 1 = imm, 0 = rs2
ax.add_patch(Polygon([(9.9, 6.3), (11.0, 5.4), (11.0, 3.9), (9.9, 3.0), (9.9, 4.3), (10.2, 4.65), (9.9, 5.0)],
                     closed=True, fill=False, ec=BOX, lw=1.6))
ax.text(10.55, 4.65, "ALU", ha="center", va="center", fontsize=10, weight="bold")
box(11.9, 2.4, 13.3, 4.2, "")
ax.text(12.6, 3.9, "DMEM", ha="center", va="center", fontsize=10, weight="bold")
ax.text(11.97, 3.4, "Addr", ha="left", va="center", fontsize=7.5)
ax.text(11.97, 2.7, "DataW", ha="left", va="center", fontsize=7.5)
ax.text(13.25, 3.4, "DataR", ha="right", va="center", fontsize=7.5)
wbm = mux(14.3, 4.6, 1.8, ["2", "1", "0"])      # WBSel: 2 = PC + 4, 1 = ALU, 0 = DMEM

# PC and next-PC logic
wire([(1.0, 5.0), (1.4, 5.0)])
wire([(2.4, 5.0), (2.7, 5.0), (2.7, 4.05), (3.0, 4.05)])
dot(2.7, 5.0)
wire([(2.7, 5.0), (2.7, 6.95), (3.1, 6.95)])
wire([(2.7, 6.95), (2.7, 7.8), (8.6, 7.8), (8.6, am[0]), (8.95, am[0])])
dot(2.7, 6.95)
wire([(4.0, 6.95), (4.4, 6.95), (4.4, 8.6), (13.7, 8.6), (13.7, wbm[0]), (14.05, wbm[0])])
wire([(4.4, 8.6), (0.1, 8.6), (0.1, pcm[1]), (0.5, pcm[1])])
dot(4.4, 8.6)
ax.text(5.0, 8.75, "PC + 4", fontsize=8, color=WIRE)

# instruction fields
wire([(4.2, 4.05), (4.7, 4.05)], arrow=False)
ax.plot([4.7, 4.7], [1.8, 5.3], color=WIRE, lw=1.2)
for y, lab in [(5.3, "inst[11:7]"), (4.8, "inst[19:15]"), (4.2, "inst[24:20]")]:
    wire([(4.7, y), (5.3, y)])
    ax.text(4.75, y + 0.1, lab, fontsize=6.5, va="bottom")
wire([(4.7, 1.8), (5.6, 1.8)])
ax.text(4.75, 1.9, "inst[31:7]", fontsize=6.5, va="bottom")
wire([(4.7, 1.8), (4.7, 0.7)])
ax.text(4.75, 1.0, "inst[31:0]", fontsize=6.5)

# register file outputs
wire([(7.0, 5.3), (7.3, 5.3), (7.3, am[1]), (8.95, am[1])])
dot(7.3, 5.3)
wire([(7.3, 5.3), (7.3, 3.1), (7.6, 3.1)])
wire([(7.0, 4.2), (7.45, 4.2), (7.45, bm[1]), (8.95, bm[1])])
dot(7.45, 4.2)
wire([(7.45, 2.7), (7.6, 2.7)])
wire([(7.45, 4.2), (7.45, 2.0), (11.6, 2.0), (11.6, 2.7), (11.9, 2.7)])
wire([(7.0, 1.8), (8.85, 1.8), (8.85, bm[0]), (8.95, bm[0])])

# ALU and memory
wire([(9.45, 5.6), (9.9, 5.6)])
wire([(9.45, 3.8), (9.9, 3.8)])
wire([(11.0, 4.65), (11.5, 4.65), (11.5, 3.4), (11.9, 3.4)])
dot(11.5, 4.65)
wire([(11.5, 4.65), (14.05, wbm[1])])
wire([(11.5, 4.65), (11.5, 8.2), (0.3, 8.2), (0.3, pcm[0]), (0.5, pcm[0])])
ax.text(5.0, 8.32, "ALU result", fontsize=8, color=WIRE)
wire([(13.3, 3.4), (13.7, 3.4), (13.7, wbm[2]), (14.05, wbm[2])])
wire([(14.55, 4.6), (15.1, 4.6), (15.1, 9.2), (5.0, 9.2), (5.0, 5.8), (5.3, 5.8)])
ax.text(9.5, 9.32, "write-back data", fontsize=8, color=WIRE)

# controller
box(1.0, -0.8, 15.3, 0.1, "Control unit", fs=10)
for x, y, lab, up in [(0.75, 4.3, "PCSel", True), (6.3, 1.3, "ImmSel", True), (5.45, 3.6, "RegWEn", True),
                      (7.85, 2.5, "BrUn", True), (8.15, 2.5, "BrEq", False), (8.45, 2.5, "BrLt", False),
                      (9.2, 3.2, "BSel", True), (10.4, 3.3, "ALUSel", True),
                      (12.6, 2.4, "MemRW", True), (14.3, 3.7, "WBSel", True)]:
    if up:
        wire([(x, 0.1), (x, y)], color=CTRL, ls="--")
    else:
        wire([(x, y), (x, 0.1)], color=CTRL, ls="--")
    ax.text(x + 0.05, 0.2, lab, ha="left", va="bottom", fontsize=6.5, color=CTRL, rotation=90)
wire([(9.65, 0.1), (9.65, 5.1), (9.3, 5.1)], color=CTRL, ls="--")
ax.text(9.7, 0.2, "ASel", ha="left", va="bottom", fontsize=6.5, color=CTRL, rotation=90)

fig.tight_layout()
