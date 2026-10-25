# DNase I footprinting and gel-shift binding, simulated. A DNA fragment of 120 nt is labelled at one 5' end;
# DNase I cuts each phosphodiester with the same small probability, so the number of cuts per molecule is
# Poisson distributed (mean lambda) and the labelled fragment ends at the first cut from the label. A: lanes of
# a sequencing gel (band intensity = fraction of labelled fragments of each length) for naked DNA and for DNA
# with a protein covering positions 50-70 (no cuts there): the protected positions leave a gap, the footprint.
# B: the band intensity along the ladder for lambda = 0.5 (single-hit conditions) and lambda = 5: with heavy
# digestion nearly every labelled fragment is short and the distal part of the ladder, including the
# footprint, disappears. C: fraction of DNA shifted in a gel-shift assay against protein concentration,
# theta = [P] / ([P] + K_D) with K_D = 10 nM, read at half-shift when the DNA concentration is far below K_D.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
L = 120
pos = np.arange(1, L + 1)


def ladder(lam, protected=None):
    q = np.full(L, lam / L)  # cut probability per bond
    if protected is not None:
        q[protected[0]:protected[1]] = 0.0
    surv = np.cumprod(np.r_[1.0, 1 - q[:-1]])
    return surv * q  # probability the first cut is at bond i (labelled fragment of length i)


fig, ax = bio.canvas(21.0, 9.8)
# --- A: gel ---
gx, gy, gw, gh = 1.4, 1.0, 4.6, 7.2
ax.add_patch(bio.core.FancyBboxPatch((gx, gy), gw, gh, boxstyle="round,pad=0,rounding_size=0.1",
                                     facecolor=P.fill("extracellular"), edgecolor=P.edge("neutral"), lw=1.0, zorder=2))
lanes = [("DNA", None), ("DNA +\nprotein", (50, 70))]
for k, (name, prot) in enumerate(lanes):
    x = gx + 1.4 + k * 1.8
    I = ladder(0.5, prot)
    I = I / I.max()
    for i in range(2, L, 2):
        y = gy + 0.3 + (gh - 0.6) * (1 - i / L)
        ax.plot([x - 0.5, x + 0.5], [y, y], color=P.edge("dna"), lw=1.1, alpha=float(0.15 + 0.85 * I[i]), zorder=5,
                solid_capstyle="butt")
    bio.label(ax, (x, gy + gh + 0.4), name, size="tiny")
yf0 = gy + 0.3 + (gh - 0.6) * (1 - 70 / L)
yf1 = gy + 0.3 + (gh - 0.6) * (1 - 50 / L)
ax.plot([gx + gw + 0.1, gx + gw + 0.25, gx + gw + 0.25, gx + gw + 0.1], [yf0, yf0, yf1, yf1], color=P.ink(), lw=0.9)
bio.label(ax, (gx + gw + 0.35, (yf0 + yf1) / 2), "footprint", size="tiny", ha="left")
bio.label(ax, (gx - 0.15, gy + gh - 0.3), "short", size="tiny", ha="right", color=P.muted())
bio.label(ax, (gx - 0.15, gy + 0.3), "long", size="tiny", ha="right", color=P.muted())
bio.panel(ax, "A", (0.1, 9.65))
bio.label(ax, (0.6, 9.3), "Footprint", size="normal", bold=True, ha="left")

# --- B: intensity profiles ---
b = C.axes_at(ax, (8.6, 1.3, 5.4, 5.8))
for lam, tok in [(0.5, "dna"), (5.0, "negative")]:
    b.plot(pos, ladder(lam), color=C.line(tok), lw=1.6, label=f"λ = {lam:g} cuts per molecule")
    b.plot(pos, ladder(lam, (50, 70)), color=C.line(tok), lw=1.0, ls=(0, (3, 2)))
b.axvspan(50, 70, color=P.fill("protein"), alpha=0.35, lw=0)
b.text(60, b.get_ylim()[1] * 0.05 if False else 0.042, "protein", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_xlim(0, L)
b.set_ylim(0, 0.045)
C.style_axes(b, "fragment length / nt", "band intensity")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.9))
bio.panel(ax, "B", (7.3, 8.9))
bio.label(ax, (7.8, 8.55), "Single-hit conditions", size="normal", bold=True, ha="left")

# --- C: gel-shift binding curve ---
c = C.axes_at(ax, (16.0, 1.3, 4.6, 5.8))
Pc = np.logspace(-10, -6, 300)
KD = 1e-8
c.semilogx(Pc, Pc / (Pc + KD), color=C.line("protein"), lw=2.0)
rng = np.random.default_rng(1)
pts = np.array([1e-9, 3e-9, 1e-8, 3e-8, 1e-7, 3e-7])
c.semilogx(pts, pts / (pts + KD) + 0.03 * rng.standard_normal(len(pts)), "o", ms=4.5, mfc=P.fill("protein"),
           mec=C.line("protein"))
c.axvline(KD, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
c.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
c.set_xticks([1e-10, 1e-9, 1e-8, 1e-7, 1e-6], ["0.1", "1", "10", "100", "1000"])
c.set_ylim(-0.03, 1.05)
C.style_axes(c, "[protein] / nM", "fraction of DNA shifted")
bio.panel(ax, "C", (14.9, 8.9))
bio.label(ax, (15.4, 8.55), "Gel shift: half-shift at $K_D$", size="normal", bold=True, ha="left")
