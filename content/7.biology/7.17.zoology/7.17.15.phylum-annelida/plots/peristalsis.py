# Peristaltic crawling of an earthworm (kinematic model, illustrative parameters). Each of N segments keeps
# its volume V = pi r^2 l (incompressible coelomic fluid, closed by septa), so a segment that shortens becomes
# thicker. Lengths follow a retrograde wave, l_i(t) = l0 [1 + e sin(2 pi (f t - i / m))], i = 0 at the head,
# which travels backward (toward the tail) at m segments per cycle. Segments thicker than a threshold are
# anchored by their chaetae and do not slip; the worm's position is found at each step by keeping the mean
# position of the segments that stay anchored fixed. A: the worm at successive times (time downward);
# anchored segments green. B: head and tail position and the position of one wave crest. C: speed per cycle
# as a function of the relative change in length e: nearly proportional to e.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
N, l0, m, f = 16, 1.0, 6.0, 1.0
TH = 0.15                        # anchored when l < l0 (1 - TH e)


def simulate(e, cycles=3.0, steps=1200):
    t = np.arange(steps + 1) * (cycles / f / steps)
    i = np.arange(N)
    head = 0.0
    out_head, out_l, out_anchor = [], [], []
    prev_c, prev_a = None, None
    for tk in t:
        l = l0 * (1 + e * np.sin(2 * np.pi * (f * tk - i / m)))
        S = np.concatenate([[0], np.cumsum(l)[:-1]])
        rel = -S - l / 2                       # centres relative to the head
        anch = l < l0 * (1 - TH * e)
        if prev_c is not None:
            both = anch & prev_a
            if both.any():
                head = np.mean(prev_c[both] - rel[both])
        prev_c, prev_a = head + rel, anch
        out_head.append(head)
        out_l.append(l)
        out_anchor.append(anch)
    return t, np.array(out_head), np.array(out_l), np.array(out_anchor)


fig, ax = bio.canvas(30, 12.4)

# ---------------- A: snapshots ----------------
e0 = 0.35
t, hd, L, A = simulate(e0)
bio.panel(ax, "A", (0.2, 12.1))
bio.label(ax, (6.4, 11.8), "The worm at successive times (e = 0.35)", size="small", bold=True)
idx = np.linspace(0, 400, 9).astype(int)       # one cycle in 8 steps
scale, x_off = 0.62, 12.0
for row, k in enumerate(idx):
    y = 10.8 - row * 1.15
    l = L[k]
    r = np.sqrt(1 / (np.pi * l))                # V = 1
    S = np.concatenate([[0], np.cumsum(l)])
    for j in range(N):
        xa, xb = x_off + (hd[k] - S[j + 1]) * scale, x_off + (hd[k] - S[j]) * scale
        h = r[j] * 0.9
        tok = "positive" if A[k, j] else "neutral"
        bio.shape(ax, [[xa, y - h / 2], [xb, y - h / 2], [xb, y + h / 2], [xa, y + h / 2]], token=tok, lw=0.6, zorder=10)
    bio.label(ax, (x_off + hd[k] * scale + 0.35, y), f"t = {round(t[k] * f * 8)}/8 T", size="tiny",
              ha="left", color=P.muted())
ax.plot([x_off, x_off], [0.9, 11.4], color=P.muted(), lw=0.7, ls="--", zorder=5)
bio.label(ax, (x_off, 0.6), "head at t = 0", size="tiny", color=P.muted())
bio.label(ax, (1.2, 0.6), "tail", size="tiny", color=P.muted())
bio.arrow(ax, (3.0, 11.3), (1.4, 11.3), kind="process", lw=0.9)
bio.label(ax, (2.2, 11.6), "wave", size="tiny", color=P.muted())
bio.arrow(ax, (9.4, 11.3), (11.0, 11.3), kind="process", lw=0.9)
bio.label(ax, (10.2, 11.6), "worm", size="tiny", color=P.muted())

# ---------------- B: head, tail and wave crest ----------------
bio.panel(ax, "B", (15.0, 12.1))
pb = quant.Plot(ax, (16.6, 7.2, 5.6, 4.0), (0, 3), (-20, 12), xlabel="Time / cycles", ylabel="Position / $l_0$",
                xticks=[0, 1, 2, 3], yticks=[-20, -10, 0, 10])
tail = hd - L.sum(axis=1)
pb.line(t * f, hd, token="dna", lw=1.8, text="head", at=0.8)
pb.line(t * f, tail, token="dna", lw=1.2, dashed=True, text="tail", at=0.8)
# a wave crest (phase 1/4, the longest segment) moves backward at m segments per cycle
crest = []
for k in range(len(t)):
    j = int(round(m * (f * t[k] - 0.25))) % N
    S = np.concatenate([[0], np.cumsum(L[k])])
    crest.append(hd[k] - S[j] - L[k][j] / 2)
crest = np.array(crest)
jumps = np.where(np.diff(crest) > 3)[0]
start = 0
for jmp in list(jumps) + [len(t) - 1]:
    pb.line(t[start:jmp + 1] * f, crest[start:jmp + 1], token="negative", lw=1.0)
    start = jmp + 1
pb.text(0.3, -12.5, "wave crest", size="tiny", color=quant.line_color("negative"))

# ---------------- C: speed versus amplitude ----------------
bio.panel(ax, "C", (23.0, 12.1))
pc = quant.Plot(ax, (24.4, 7.2, 5.0, 4.0), (0, 0.5), (0, 2.5), xlabel="Relative length change  e",
                ylabel="Speed / ($l_0 f$)", xticks=[0, 0.25, 0.5], yticks=[0, 1, 2])
es = np.linspace(0.02, 0.5, 13)
U = []
for e in es:
    tt, h, LL, AA = simulate(e, cycles=2.0, steps=800)
    U.append((h[-1] - h[len(h) // 2]) / (tt[-1] - tt[len(tt) // 2]) / (l0 * f))
pc.points(es, U, token="dna", r=0.08)
pc.text(0.3, 0.6, "simulation", size="tiny", ha="left", color=quant.line_color("dna"))

# ---------------- explanatory strip ----------------
bio.label(ax, (22.8, 5.2), "Constant volume per segment:  $\\pi r^2 l = V$", size="small")
bio.label(ax, (22.8, 4.4), "circular muscle contracts: long and thin, moves forward", size="small", color=P.muted())
bio.label(ax, (22.8, 3.7), "longitudinal muscle contracts: short and thick, anchored by chaetae", size="small", color=P.muted())
bio.shape(ax, [[19.0, 2.1], [20.0, 2.1], [20.0, 2.45], [19.0, 2.45]], token="neutral", lw=0.7)
bio.shape(ax, [[24.0, 1.95], [24.6, 1.95], [24.6, 2.6], [24.0, 2.6]], token="positive", lw=0.7)
bio.label(ax, (19.5, 1.5), "moving", size="tiny", color=P.muted())
bio.label(ax, (24.3, 1.3), "anchored", size="tiny", color=P.muted())
