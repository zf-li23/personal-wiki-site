# Two properties of concept learning. A: abstraction of the same-different concept depends on the number of
# training stimuli (illustrative curves of the pattern reported by Katz and Wright 2006 for pigeons). Birds were
# trained to report whether two pictures were the same or different with a training set of 8 to 1024 pictures;
# accuracy on the training pairs was high for every set size, but accuracy with novel pictures (transfer) rose
# from chance with 8 pictures to the level of training with the largest sets. Curve: transfer = 0.5 + 0.35 /
# (1 + exp(-1.4 (log2 N - 6))). B: generalization gradients and peak shift (after Hanson 1959), with Spence's
# (1937) model: training on S+ (550 nm) builds excitation, a Gaussian around S+ (s.d. 12 nm); discrimination
# training with S- (560 nm) adds inhibition, a smaller Gaussian around S- (s.d. 10 nm, weight 0.85). The net
# gradient after discrimination training peaks not at S+ but away from S- (peak shift).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 9.4)

pa = quant.Plot(ax, (2.0, 1.8, 7.6, 6.4), (2.5, 10.5), (0.4, 1.0), xlabel="Training set size (pictures)",
                ylabel="Proportion correct", xticks=[(3, "8"), (4, "16"), (6, "64"), (8, "256"), (10, "1024")],
                yticks=[0.5, 0.75, 1.0])
bio.panel(ax, "A", (0.2, 9.2))
x = np.linspace(3, 10, 200)
pa.hline(0.5, text="chance", side="left")
pa.line(x, np.full_like(x, 0.86), "dna", lw=2.0, text="training pairs", at=0.15, dy=0.22)
tr = 0.5 + 0.35 / (1 + np.exp(-1.4 * (x - 6)))
pa.line(x, tr, "rna", lw=2.0, text="novel pairs (transfer)", at=0.62, dx=0.25, dy=-0.25)
xs = np.arange(3, 11)
pa.points(xs, 0.5 + 0.35 / (1 + np.exp(-1.4 * (xs - 6))), "rna", r=0.1)

pb = quant.Plot(ax, (12.6, 1.8, 8.4, 6.4), (500, 600), (0, 1.05), xlabel="Wavelength / nm", ylabel="Responding (relative)",
                xticks=[500, 520, 540, 560, 580, 600], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.8, 9.2))
w = np.linspace(500, 600, 400)
exc = np.exp(-0.5 * ((w - 550) / 12) ** 2)
inh = 0.85 * np.exp(-0.5 * ((w - 560) / 10) ** 2)
net = np.clip(exc - inh, 0, None)
pb.line(w, exc, "dna", lw=2.0, dashed=True, text="S+ only", at=0.66, dx=0.15)
pb.line(w, net / net.max(), "rna", lw=2.0, text="after S+ 550 nm, S- 560 nm", at=0.42, dx=-0.15, dy=0.0, ha="right")
pb.vline(550, text="S+")
pb.vline(560, text="S-")
pk = w[np.argmax(net)]
pb.text(pk - 1.5, 0.97, f"peak {pk:.0f} nm", ha="right", token="rna")
