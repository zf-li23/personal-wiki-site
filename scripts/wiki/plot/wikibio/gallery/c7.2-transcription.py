# A: the central dogma (information flows DNA -> RNA -> protein; reverse transcription by retroviruses and
# retrotransposons dashed). B: a transcription elongation complex. RNA polymerase holds a transcription bubble
# of about 13 unpaired nucleotides; the template strand is read 3'->5' and the RNA grows 5'->3' at the active
# site (Mg2+), where NTPs arrive; an RNA-DNA hybrid of about 8-9 bp sits upstream of the 3' end, and the
# RNA leaves through the exit channel while the DNA rewinds behind the enzyme.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

fig, ax = bio.canvas(18, 11.4)
P = bio.P

# --- A: central dogma -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.25))
MB.central_dogma(ax, (5.3, 9.55), gap=3.7)

# --- B: transcription bubble ------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 7.35))
y0, half, dx = 3.1, 0.24, 0.24
x0, x1 = 7.0, 11.8
xs = np.arange(0.9, 17.15, dx)
up = MB.bubble_profile(xs, x0, x1, 1.15, ramp=1.0)
dn = MB.bubble_profile(xs, x0, x1, 0.75, ramp=1.0)
fx = np.linspace(xs[0], xs[-1], 800)  # fine grid for the backbones
top = MB.track(xs, y0 + half + up)
bot = MB.track(xs, y0 - half - dn)
coding = MB.sequence(len(xs), "transcription")
template = MB.complement(coding)
closed = up < 0.05
hyb = (xs >= 8.6) & (xs <= 10.95)

MB.polymerase(ax, (9.45, 3.55), 6.9, 4.9, "enzyme", "RNA polymerase", alpha=0.85, text_at=(9.45, 5.45))

# DNA: base pairs where closed, unpaired bases in the bubble
MB.ladder(ax, top[closed], bot[closed], [coding[i] for i in np.where(closed)[0]], [template[i] for i in np.where(closed)[0]])
MB.stubs(ax, top[~closed], (0, -1), [coding[i] for i in np.where(~closed)[0]])
free = ~closed & ~hyb
MB.stubs(ax, bot[free], (0, 1), [template[i] for i in np.where(free)[0]])
MB.backbone(ax, MB.track(fx, y0 + half + MB.bubble_profile(fx, x0, x1, 1.15, ramp=1.0)), "dna", zorder=13)
MB.backbone(ax, MB.track(fx, y0 - half - MB.bubble_profile(fx, x0, x1, 0.75, ramp=1.0)), "dna2")

# RNA: hybrid with the template, then the exit path to the 5' end
rna_hyb = MB.track(xs[hyb], y0 - half - dn[hyb] + 2 * half)
rna_seq = "".join("U" if c == "T" else c for c in (coding[i] for i in np.where(hyb)[0]))
MB.ladder(ax, rna_hyb, bot[hyb], rna_seq, [template[i] for i in np.where(hyb)[0]], zorder=11)
exit_path = np.array([(2.9, 7.0), (4.4, 6.8), (5.9, 6.1), (7.0, 5.0), (7.75, 3.6), (8.15, rna_hyb[0, 1] + 0.12), (8.5, rna_hyb[0, 1])])
tail = MB.wavy(exit_path, amplitude=0.06)
rna = np.vstack([tail, rna_hyb])
MB.backbone(ax, rna, "rna", zorder=12)
# a few bases on the single-stranded RNA
pts, _ = MB.sample(tail[:-12], 0.3)
MB.stubs(ax, pts, (0.5, 1), MB.sequence(len(pts), "rna-tail", "ACGU"), length=0.14, zorder=11)
bio.label(ax, (2.55, 7.15), "5′", size="tiny", bold=True)
bio.label(ax, (rna_hyb[-1, 0] + 0.05, rna_hyb[-1, 1] + 0.3), "3′", size="tiny", bold=True)

# active site and incoming NTPs
site = rna_hyb[-1] + (0.24, -0.05)
bio.ion(ax, site, "mg", r=0.11, text=False)
for k, p in enumerate([(12.35, 1.55), (12.9, 1.1), (11.8, 0.95)]):
    bio.molecule(ax, p, token="atp", r=0.16)
bio.arrow(ax, (12.0, 1.55), site + (0.15, -0.15), kind="process", bend=-0.2, color=P.ink())
bio.label(ax, (13.25, 1.6), "NTPs", size="small", ha="left")
bio.callout(ax, tuple(site), (13.7, 2.45), "Active site (Mg²⁺)")

# polarity and orientation labels
MB.end_labels(ax, top, "5′", "3′")
MB.end_labels(ax, bot, "3′", "5′")
bio.label(ax, (0.9, y0 + 0.75), "Coding (non-template) strand", size="small", ha="left", color=P.edge("dna"))
bio.label(ax, (0.9, y0 - 0.75), "Template strand", size="small", ha="left", color=P.edge("dna2"))
bio.label(ax, (2.2, y0 - 1.35), "Upstream", size="small", color=P.muted())
bio.label(ax, (16.0, y0 - 1.35), "Downstream", size="small", color=P.muted())
bio.callout(ax, ((rna_hyb[0, 0] + rna_hyb[-1, 0]) / 2, rna_hyb[0, 1] - 0.27), (8.6, 0.55), "RNA–DNA hybrid (8–9 bp)")
bio.label(ax, (6.75, 4.75), "Rewinding", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (12.2, 4.75), "Unwinding", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (4.75, 6.25), "RNA exit", size="tiny", color=P.edge("rna"), ha="right")
bio.arrow(ax, (12.9, 6.55), (16.4, 6.55), kind="process")
bio.label(ax, (14.65, 6.85), "Direction of transcription", size="small", va="bottom")
