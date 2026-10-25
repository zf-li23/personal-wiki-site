# The bacterial sigma-70 promoter and the polymerase domains that read it.
# A: a promoter map from -60 to +20 (coding strand): UP element, -35 hexamer, 17 bp spacer, extended -10 (TGn),
# -10 hexamer, discriminator and the start site +1, with the domains of RNA polymerase holoenzyme that contact
# each element (alpha CTDs on flexible linkers, sigma regions 4.2, 3.0, 2.4 and 1.2) and the region melted in
# the open complex (-11 to +2).
# B: a sequence logo of the -35 and -10 hexamers built from the percentage of the consensus base at each
# position (Lewin, Genes 12e: -35 T82 T84 G78 A65 C54 A45; -10 T80 A95 T45 A60 A50 T96); the remaining
# probability is shared equally by the other three bases, so the logo shows conservation, not the full
# base distribution.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB
from wikibio import sequence as S

P = bio.P
fig, ax = bio.canvas(19.0, 10.8)


def X(pos):
    # promoter coordinate -> canvas x (no position 0: +1 follows -1 directly)
    p = pos if pos < 0 else pos - 1
    return 1.6 + (p + 61) * 0.205


# --- A: promoter map -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.65))
y = 6.6
ax.plot([X(-62), X(21)], [y, y], color=P.ink(), lw=2.2, solid_capstyle="round", zorder=4)
elements = [(-60, -41, "UP element", "positive"), (-35, -30, "−35", "highlight"), (-15, -13, "TGn", "neutral"),
            (-12, -7, "−10", "highlight"), (-6, -1, "disc.", "neutral")]
for a, b, name, tok in elements:
    x0, x1 = X(a) - 0.1, X(b) + 0.1
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, 0.62, token=tok, text=name, size="tiny", radius=0.08, zorder=6)
# spacer bracket
xa, xb = X(-29) + 0.05, X(-13) - 0.15
ax.plot([xa, xa, xb, xb], [y - 0.55, y - 0.7, y - 0.7, y - 0.55], color=P.muted(), lw=0.8)
bio.label(ax, ((xa + xb) / 2, y - 0.98), "17 ± 1 bp spacer", size="tiny", color=P.muted())
# melted region
xa, xb = X(-11) - 0.1, X(2) + 0.1
ax.plot([xa, xa, xb, xb], [y - 0.55, y - 1.4, y - 1.4, y - 0.55], color=P.edge("negative"), lw=0.9)
bio.label(ax, ((xa + xb) / 2, y - 1.68), "melted in RPo (−11 to +2)", size="tiny", color=P.edge("negative"))
# start site: bent arrow
xs = X(1)
ax.plot([xs, xs, xs + 1.0], [y + 0.05, y + 0.75, y + 0.75], color=P.ink(), lw=1.4, solid_joinstyle="round")
bio.arrow(ax, (xs + 0.8, y + 0.75), (xs + 1.25, y + 0.75), kind="process")
bio.label(ax, (xs + 0.62, y + 1.08), "+1", size="small")
# coordinate ticks
for pos in (-60, -50, -40, -30, -20, -10, 1, 10, 20):
    bio.label(ax, (X(pos), y - 2.25), f"{pos:+d}".replace("-", "−") if pos != 1 else "+1", size="tiny", color=P.muted())
ax.plot([X(-62), X(21)], [y - 2.0, y - 2.0], color=P.muted(), lw=0.5)
for pos in (-60, -50, -40, -30, -20, -10, 1, 10, 20):
    ax.plot([X(pos), X(pos)], [y - 2.0, y - 1.92], color=P.muted(), lw=0.6)

# holoenzyme: core as a soft body behind, sigma domains and alpha CTDs in front
core = bio.core.blob(((X(-37) + X(20)) / 2, y + 2.05), (X(20) - X(-37)) / 2, 1.15, wobble=0.05, seed=7, k=9)
bio.shape(ax, core, token="enzyme", zorder=5)
bio.label(ax, (X(10), y + 2.45), "Core α₂ββ′ω", size="small", bold=True)
doms = [(-33, "σ4.2", 1.05), (-14, "σ3.0", 0.85), (-9, "σ2.4", 1.0), (-3, "σ1.2", 0.85)]
for pos, name, w in doms:
    bio.protein(ax, (X(pos), y + 1.05), w, 0.72, "protein", text=name, size="tiny")
for pos in (-53, -45):
    bio.protein(ax, (X(pos), y + 0.98), 1.05, 0.7, "positive", text="αCTD", size="tiny")
    # flexible linker to the alpha NTD in the core
    t = np.linspace(0, 1, 60)
    x0, y0, x1, y1 = X(pos) + 0.25, y + 1.33, X(-33) + 0.2, y + 2.55
    xx = x0 + (x1 - x0) * t
    yy = y0 + (y1 - y0) * t + 0.12 * np.sin(t * np.pi * 5)
    ax.plot(xx, yy, color=P.edge("positive"), lw=1.0, zorder=5)
bio.label(ax, (X(-49), y + 2.1), "linkers", size="tiny", color=P.muted())

# --- B: logos ----------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 3.05))
alphabet = "ACGT"


def matrix(consensus, percents):
    m = []
    for base, pc in zip(consensus, percents):
        f = pc / 100
        row = [(1 - f) / 3] * 4
        row[alphabet.index(base)] = f
        m.append(row)
    return np.array(m)


m35 = matrix("TTGACA", [82, 84, 78, 65, 54, 45])
m10 = matrix("TATAAT", [80, 95, 45, 60, 50, 96])
cw, hh = 0.62, 2.0
x35, x10, yb = 3.2, 10.6, 0.55
S.logo(ax, m35, at=(x35, yb), col_width=cw, height=hh, kind="probabilities", small_sample=False, start=-35,
       numbers=False)
S.logo(ax, m10, at=(x10, yb), col_width=cw, height=hh, kind="probabilities", small_sample=False, start=-12,
       numbers=False)
for k, pos in enumerate([-35, -34, -33, -32, -31, -30]):
    bio.label(ax, (x35 + (k + 0.5) * cw, yb - 0.25), f"{pos}".replace("-", "−"), size="tiny", color=P.muted())
for k, pos in enumerate([-12, -11, -10, -9, -8, -7]):
    bio.label(ax, (x10 + (k + 0.5) * cw, yb - 0.25), f"{pos}".replace("-", "−"), size="tiny", color=P.muted())
bio.label(ax, (x35 + 3 * cw, yb + hh + 0.3), "−35 element (TTGACA)", size="small", bold=True)
bio.label(ax, (x10 + 3 * cw, yb + hh + 0.3), "−10 element (TATAAT)", size="small", bold=True)
xm0, xm1 = x35 + 6 * cw + 0.3, x10 - 0.9
ax.plot([xm0, xm1], [yb + 0.5, yb + 0.5], color=P.muted(), lw=0.9, ls=(0, (3, 2)))
bio.label(ax, ((xm0 + xm1) / 2, yb + 0.8), "spacer 17 ± 1 bp", size="tiny", color=P.muted())
