"""Ratio compression in isobaric labeling. A: observed against true log2 ratio of a peptide when a
fraction phi of the ions in the isolation window comes from co-isolated peptides whose channels are
1:1 (Eq. (9.6)); the identity line is phi = 0. B (simulation): 400 peptides of proteins changed
4-fold (log2 ratio 2) and 2000 unchanged ones, with interference fractions drawn from Beta(2, 5)
(mean 0.29) for MS2 reporter quantification and from Beta(1, 20) (mean 0.05) after synchronous
precursor selection with MS3; log-normal measurement noise with SD 0.15. The changed peptides are
pulled towards zero in MS2, much less in MS3."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def observed(R, phi):
    T, I = 1 - phi, phi
    return (T * R / (1 + R) + I / 2) / (T / (1 + R) + I / 2)


fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.88, wspace=0.3)
lr = np.linspace(-4, 4, 200)
for phi, tok in [(0.0, "neutral"), (0.1, "dna"), (0.3, "rna"), (0.5, "negative")]:
    a.plot(lr, np.log2(observed(2.0 ** lr, phi)), color=charts.line(tok), lw=1.5, label=f"phi = {phi}")
a.legend(frameon=False, fontsize=7.5, loc="upper left")
charts.style_axes(a, "true log2 ratio", "observed log2 ratio", grid=True)
charts.title(a, "A  Interference compresses ratios")

bins = np.linspace(-0.8, 2.6, 69)
for lab, ab, tok, y0 in [("MS2", (2, 5), "rna", 0), ("MS3", (1, 20), "dna", 0)]:
    phi_c = rng.beta(*ab, 400)
    phi_u = rng.beta(*ab, 2000)
    ch = np.log2(observed(4.0, phi_c)) + rng.normal(0, 0.15, 400)
    un = np.log2(observed(1.0, phi_u)) + rng.normal(0, 0.15, 2000)
    b.hist(np.r_[un, ch], bins, histtype="step", lw=1.4, color=charts.line(tok),
           label=f"{lab}: median of changed = {np.median(ch):.2f}")
b.axvline(2, color=P.muted(), ls="--", lw=0.8)
b.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(b, "observed log2 ratio", "peptides")
charts.title(b, "B  Unchanged (left) and 4-fold changed (right) peptides")
