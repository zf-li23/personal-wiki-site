"""Structural and dynamical methods of molecular biophysics compared on logarithmic axes.

A: spatial detail against molecular mass. Each box spans the masses for which a method works well
and the resolution (or precision) it typically reaches, with the values of the comparison tables in
7.6.10, 7.6.13, 7.6.14 and 7.6.12: crystallography 0.5-3.5 A from peptides to viruses; solution NMR
(atomic precision of restrained ensembles) below about 50 kDa, with methyl-TROSY dynamics to about
1 MDa (dashed); single-particle cryo-EM 1.2-4 A above about 40 kDa; cryo-ET 1-3 nm in raw tomograms
and 3-10 A by subtomogram averaging above about 300 kDa; SAXS 10-30 A (overall shape) for any size;
smFRET (dashed: one distance, precision 1-5 A, not a map). B: the time windows over which each
method follows change: time-resolved crystallography from 100 fs (XFEL pump-probe) to mix-and-inject
seconds; NMR from ps (relaxation) to months (exchange); time-resolved SAXS from ps to s; smFRET from
ns (bursts) to minutes (surface traces); HDX from seconds to months; cryo-EM separates states by
classification but does not follow time (snapshots)."""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT

fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.4, 4.3), gridspec_kw={"width_ratios": [1.05, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.13, top=0.9, wspace=0.55)

# A: resolution versus mass. (name, mass range kDa, resolution range A, token, dashed, label position)
boxes = [
    ("X-ray crystallography", (1.0, 1e5), (0.5, 3.5), "protein", False, (1.3, 0.62)),
    ("solution NMR", (2.0, 50.0), (1.5, 3.0), "enzyme", False, (2.2, 1.6)),
    ("single-particle cryo-EM", (40.0, 1e5), (1.2, 4.0), "receptor", False, (300.0, 1.35)),
    ("cryo-ET + averaging", (300.0, 1e5), (3.0, 10.0), "channel", False, (1.2e3, 4.0)),
    ("cryo-ET tomograms", (300.0, 1e5), (10.0, 30.0), "dna", False, (1.2e3, 13.0)),
    ("SAXS (shape)", (5.0, 5e4), (10.0, 30.0), "atp", False, (6.0, 21.0)),
    ("smFRET (one distance)", (10.0, 1e4), (1.0, 5.0), "rna", True, (14.0, 6.6)),
]
for name, (m0, m1), (r0, r1), tok, dashed, (lx, ly) in boxes:
    ax.add_patch(Rectangle((m0, r0), m1 - m0, r1 - r0, facecolor=P.fill(tok) if not dashed else "none",
                           edgecolor=P.edge(tok), lw=1.0, alpha=0.45 if not dashed else 1.0,
                           ls="--" if dashed else "-", zorder=2))
    ax.text(lx, ly, name, fontsize=F["tiny"], color=P.ink(), zorder=5)
# NMR dynamics extension (methyl-TROSY)
ax.add_patch(Rectangle((50.0, 1.5), 1e3 - 50.0, 1.5, facecolor="none", edgecolor=charts.line("enzyme"),
                       lw=0.9, ls=":", zorder=2))
ax.text(60.0, 2.3, "NMR dynamics\n(methyl-TROSY)", fontsize=F["tiny"], color=P.muted(), zorder=5)
for m, lab in ((14.3, "lysozyme"), (64.0, "hemoglobin"), (2.5e3, "ribosome")):
    ax.axvline(m, color=P.muted(), lw=0.5, ls=":", zorder=1)
    ax.text(m * 1.08, 75.0, lab, rotation=90, fontsize=F["tiny"], color=P.muted(), va="bottom")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1.0, 1e5)
ax.set_ylim(80.0, 0.4)  # better resolution upward
ax.set_yticks([0.5, 1, 2, 5, 10, 20, 50])
ax.set_yticklabels(["0.5", "1", "2", "5", "10", "20", "50"])
charts.style_axes(ax, "molecular mass / kDa", "resolution or precision / Å")
charts.title(ax, "A  Spatial detail and size")

# B: time windows. (name, t0, t1, token, note)
bars = [
    ("X-ray (time-resolved)", 1e-13, 1e0, "protein", "XFEL pump–probe to mix-and-inject"),
    ("NMR", 1e-12, 1e7, "enzyme", "relaxation ps–ns, dispersion µs–ms, exchange s–months"),
    ("SAXS (time-resolved)", 1e-12, 1e1, "atp", "pump–probe, continuous and stopped flow"),
    ("smFRET", 1e-9, 1e3, "rna", "bursts ns–ms, surface traces ms–min"),
    ("HDX (NMR, MS)", 1e0, 1e7, "metabolite", "labeling times; most protected amides months"),
    ("cryo-EM, cryo-ET", None, None, "receptor", "states by classification; no time axis"),
]
for i, (name, t0, t1, tok, note) in enumerate(bars):
    y = len(bars) - i
    if t0 is not None:
        bx.add_patch(Rectangle((t0, y - 0.2), t1 - t0, 0.4, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                               lw=0.9, zorder=2))
    else:
        bx.text(1.0, y, "equilibrium snapshots", fontsize=F["tiny"], color=charts.line(tok), ha="center",
                va="center", style="italic")
    bx.text(1e-14, y + 0.36, note, fontsize=F["tiny"], color=P.muted(), va="center")
for t, lab in ((1e-12, "ps"), (1e-9, "ns"), (1e-6, "µs"), (1e-3, "ms"), (1.0, "s"), (3.6e3, "h"), (2.6e6, "month")):
    bx.axvline(t, color=P.mix(P.muted(), P.surface(), 0.5), lw=0.5, zorder=0)
    bx.text(t, len(bars) + 0.65, lab, fontsize=F["tiny"], color=P.muted(), ha="center")
bx.set_xscale("log")
bx.set_xlim(1e-14, 1e8)
bx.set_ylim(0.5, len(bars) + 0.9)
bx.set_yticks(range(len(bars), 0, -1))
bx.set_yticklabels([b[0] for b in bars])
bx.spines["left"].set_visible(False)
charts.style_axes(bx, "time scale followed / s")
bx.spines["left"].set_visible(False)
bx.tick_params(axis="y", length=0)
charts.title(bx, "B  Time windows")
