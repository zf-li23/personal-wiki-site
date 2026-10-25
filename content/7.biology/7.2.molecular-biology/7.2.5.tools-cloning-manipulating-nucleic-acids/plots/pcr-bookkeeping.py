# PCR bookkeeping. A: the strands after cycles 1-3, computed by copying every strand with the primer that
# anneals to it. Grey: the two original strands; blue: "long" products, which start at a primer but run to the
# end of their template; orange: target-length strands bounded by both primers. Duplexes of exactly target
# length first appear after cycle 3 (2 of 8); after n cycles there are 2^n - 2n of them. B: amplification
# from 1e3, 1e6 (2^20) and 1e9 starting duplexes with a primer-limited model: in each cycle a fraction
# E0 p/(p + N) of the N duplexes is copied (primer annealing, concentration p, competes with re-annealing of
# product strands), using up primer; p0 = 1 uL x 10 uM = 6e12 primer molecules. All curves level off near
# 1e12 duplexes, as the sudden-stop estimate 2^20 x 2^21 (dashed) suggests.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(21.0, 10.4)

# ---- A: strands -----------------------------------------------------------------------------------------
L0, L1, F, R = -4.0, 14.0, 0.0, 10.0  # template ends; forward primer 5' end at F, reverse primer 5' end at R
strands = [(+1, L0, L1, "orig"), (-1, L0, L1, "orig")]
per_cycle = []
for cyc in range(3):
    new = []
    for o, a, b, kind in strands:
        if o == +1 and a <= F <= R <= b:  # reverse primer anneals at R, copies leftwards to a
            k = "short" if a >= F else "long"
            new.append((-1, max(a, F) if kind != "orig" else a, R, k))
        if o == -1 and a <= F <= R <= b:
            k = "short" if b <= R else "long"
            new.append((+1, F, min(b, R) if kind != "orig" else b, k))
    per_cycle.append(list(zip(strands, new)))
    strands = strands + new

col = {"orig": "neutral", "long": "dna", "short": "drug"}
bio.panel(ax, "A", (0.1, 10.3))
bio.label(ax, (0.6, 9.95), "Strands after each cycle", size="normal", bold=True, ha="left")
scale, x0 = 0.2, 0.9
ytop = 9.1
for c, pairs in enumerate(per_cycle):
    xc = x0 + c * 4.3
    bio.label(ax, (xc + (L1 - L0) * scale / 2, ytop), f"after cycle {c + 1}: {len(pairs)} duplexes", size="small", bold=True)
    for k, (t, n) in enumerate(sorted(pairs, key=lambda p: (p[0][3] != "orig", p[0][3] == "short"))):
        y = ytop - 0.6 - k * 0.6
        for (o, a, b, kind) in (t, n):
            yy = y + (0.08 if o == +1 else -0.08)
            ax.plot([xc + (a - L0) * scale, xc + (b - L0) * scale], [yy, yy], color=P.edge(col[kind]), lw=2.0,
                    solid_capstyle="butt")
    xF, xR = xc + (F - L0) * scale, xc + (R - L0) * scale
    yl = ytop - 0.6 - (len(pairs) - 1) * 0.6 - 0.35
    ax.plot([xF, xF], [ytop - 0.3, yl], color=P.muted(), lw=0.6, ls=(0, (2, 2)))
    ax.plot([xR, xR], [ytop - 0.3, yl], color=P.muted(), lw=0.6, ls=(0, (2, 2)))
for k, (kind, txt) in enumerate([("orig", "original strand"), ("long", "long product (one defined end)"),
                                 ("short", "target length (both ends defined)")]):
    ax.plot([0.8 + 4.2 * k, 1.5 + 4.2 * k], [0.45, 0.45], color=P.edge(col[kind]), lw=2.4)
    bio.label(ax, (1.65 + 4.2 * k, 0.45), txt, size="tiny", ha="left")
bio.label(ax, (6.9, 1.1), "target-length duplexes after n cycles: 2ⁿ − 2n  (0, 0, 2, 8, 22, …)", size="small")

# ---- B: plateau -------------------------------------------------------------------------------------------
a = C.axes_at(ax, (15.4, 1.5, 5.2, 7.6))
E0, p0, n = 0.95, 6e12, 40
for N0, tok in [(1e3, "protein"), (2 ** 20, "enzyme"), (1e9, "receptor")]:
    N, p, xs = [N0], p0, []
    for _ in range(n):
        new = E0 * N[-1] * p / (p + N[-1])
        p -= new
        N.append(N[-1] + new)
    a.semilogy(range(n + 1), N, color=C.line(tok), lw=1.8, label=f"$N_0$ = {N0:.0e}".replace("e+0", "e").replace("1e", "10^") if False else None)
    a.text(n + 0.5, N[-1], "", fontsize=6)
a.semilogy([0, 21, 21], [2 ** 20, 2 ** 41, 2 ** 41], color=P.muted(), lw=1.0, ls=(0, (4, 3)))
a.plot([21, n], [2 ** 41, 2 ** 41], color=P.muted(), lw=1.0, ls=(0, (4, 3)))
a.axhline(p0, color=C.line("negative"), lw=0.9, ls=(0, (1, 2)))
a.text(1, p0 * 1.6, "primer: 6×10¹² molecules", fontsize=bio.core.FONT["tiny"], color=C.line("negative"))
for N0, y in [(1e3, 1e3), (2 ** 20, 2 ** 20), (1e9, 1e9)]:
    a.text(0.6, y * 2.2, {1e3: "10³", 2 ** 20: "2²⁰ ≈ 10⁶", 1e9: "10⁹"}[N0], fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(0, n)
a.set_ylim(1e2, 1e14)
a.set_yticks([1e2, 1e4, 1e6, 1e8, 1e10, 1e12, 1e14])
C.style_axes(a, "cycle", "duplexes")
bio.panel(ax, "B", (14.0, 10.3))
bio.label(ax, (14.5, 9.95), "Primer-limited plateau", size="normal", bold=True, ha="left")
