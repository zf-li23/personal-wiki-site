# MALDI-TOF identification of a colony (schematic and simulated spectra).
# A: cells from a colony are spotted on a steel target with matrix; a laser pulse desorbs and ionizes the
#    proteins (mostly singly charged), an electric field accelerates every ion through the same potential U,
#    and the ions drift through a field-free tube of length L. Since zeU = m v^2 / 2, the flight time is
#    t = L sqrt(m / (2 z e U)), so heavier ions arrive later; the detector records intensity against m/z.
#    Flight times printed for L = 1 m and U = 20 kV.
# B: spectra in the 2-20 kDa range, dominated by abundant ribosomal and other small basic proteins.
#    Simulated peak lists: the unknown shares most peaks with reference species 1 and few with species 2;
#    the match is the fraction of the unknown's peaks found in the reference within 600 ppm.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
fig = plt.figure(figsize=(12.5, 4.6))
axA = fig.add_axes([0.01, 0.05, 0.43, 0.88])
axA.set_xlim(0, 13)
axA.set_ylim(0, 8)
axA.set_aspect("equal")
axA.axis("off")
bio.panel(axA, "A", (0.1, 7.9))

# target plate with spots
axA.add_patch(Rectangle((0.6, 1.6), 0.35, 4.4, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.0))
for yy in np.linspace(2.0, 5.6, 5):
    axA.add_patch(Rectangle((0.95, yy - 0.18), 0.12, 0.36, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"), lw=0.6))
bio.label(axA, (0.78, 1.15), "target with\ncolony + matrix", size="tiny")
# laser
bio.arrow(axA, (3.2, 7.2), (1.15, 3.85), kind="process", color=P.edge("negative"), lw=1.6)
bio.label(axA, (3.35, 7.35), "laser pulse", size="tiny", ha="left", color=P.edge("negative"))
# acceleration grid
for xg in (1.9, 2.6):
    axA.plot([xg, xg], [2.2, 5.5], color=P.muted(), lw=1.0, ls=(0, (2, 1.5)))
bio.label(axA, (2.25, 1.75), "accelerate\n(potential $U$)", size="tiny")
# flight tube
axA.add_patch(FancyBboxPatch((2.9, 2.9), 8.2, 1.9, boxstyle="round,pad=0,rounding_size=0.3",
                             facecolor=P.fill("extracellular"), edgecolor=P.edge("extracellular"), lw=1.0))
bio.label(axA, (7.0, 5.15), "field-free flight tube, length $L$", size="tiny")
# ions: small fast, large slow
for x0, r, tok, lab in [(9.6, 0.13, "protein", "light ion: early"), (7.4, 0.22, "enzyme", ""), (5.0, 0.32, "rrna", "heavy ion: late")]:
    axA.add_patch(plt.Circle((x0, 3.85), r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    bio.arrow(axA, (x0 + r + 0.05, 3.85), (x0 + r + 0.75, 3.85), kind="process", lw=0.9)
    if lab:
        bio.label(axA, (x0, 3.2), lab, size="tiny", color=P.muted())
# detector
axA.add_patch(Rectangle((11.2, 2.6), 0.45, 2.5, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0))
bio.label(axA, (11.42, 2.2), "detector", size="tiny")
# formula and times
U, L, e, u = 2.0e4, 1.0, 1.602176634e-19, 1.66053906660e-27
times = [(m, L * np.sqrt(m * u / (2 * e * U)) * 1e6) for m in (4000, 10000, 16000)]
txt = "$t = L\\sqrt{m/(2zeU)}$\n" + "\n".join(f"$m/z$ = {m}: $t$ = {t:.1f} $\\mu$s" for m, t in times)
bio.label(axA, (7.0, 1.2), txt, size="tiny")

# ---- B: spectra -------------------------------------------------------------------------------
ref1 = np.sort(rng.uniform(2500, 15000, 22))
ref2 = np.sort(np.r_[rng.uniform(2500, 15000, 18), ref1[[2, 7, 12, 17]]])  # a few shared conserved proteins
keep = rng.random(ref1.size) < 0.85
unk = np.sort(np.r_[ref1[keep] * (1 + rng.normal(0, 150e-6, keep.sum())), rng.uniform(2500, 15000, 2)])
mz = np.linspace(2000, 16000, 6000)


def spectrum(peaks, seed):
    g = np.random.default_rng(seed)
    h = g.uniform(0.15, 1.0, peaks.size)
    y = np.zeros_like(mz)
    for p, a in zip(peaks, h):
        y += a * np.exp(-0.5 * ((mz - p) / (p * 4e-4)) ** 2)
    return y / y.max()


def score(q, ref, tol=600e-6):
    return np.mean([np.any(np.abs(ref - p) / p < tol) for p in q])


specs = [("unknown isolate", unk, "dna"), (f"reference species 1 (match {score(unk, ref1):.0%})", ref1, "positive"),
         (f"reference species 2 (match {score(unk, ref2):.0%})", ref2, "neutral")]
axB = fig.add_axes([0.53, 0.14, 0.45, 0.76])
for k, (name, pk, tok) in enumerate(specs):
    off = (2 - k) * 1.25
    axB.plot(mz, spectrum(pk, k + 10) + off, color=charts.line(tok), lw=0.9)
    axB.text(2100, off + 1.03, name, fontsize=7, color=P.ink())
axB.set_yticks([])
axB.set_xlim(2000, 16000)
charts.style_axes(axB, "$m/z$ (singly charged: mass / Da)", "relative intensity")
charts.title(axB, "B   Spectra matched against a database")
