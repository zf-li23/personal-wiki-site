# The CTCF binding motif as counts, logo and weights. JASPAR matrix MA0139.1 (913 sites from CTCF ChIP-seq
# peaks in human cells). A: sequence logo; the height of each stack is the information content
# R = 2 - (H + e_n) in bits, letters are scaled by their frequencies (total 17.2 bits). B: the position
# weight matrix log2[(n_bj + 0.8 q_b) / (N + 0.8) / q_b] with the human background q = (0.295, 0.205,
# 0.205, 0.295) for A, C, G, T, in bits; the consensus base of each column has the largest weight, and
# bases never observed (C at positions 10 and 13, G at position 5) receive large negative weights that
# the pseudocount keeps finite.
import numpy as np
import wikibio as bio
from wikibio import charts as C, sequence as S

P = bio.P
CTCF = np.array([[87, 291, 76, 459], [167, 145, 414, 187], [281, 49, 449, 134], [56, 800, 21, 36],
                 [8, 903, 0, 2], [744, 13, 65, 91], [40, 528, 334, 11], [107, 433, 48, 324],
                 [851, 11, 32, 18], [5, 0, 903, 3], [333, 3, 566, 9], [54, 12, 504, 341], [12, 0, 890, 8],
                 [56, 8, 775, 71], [104, 733, 5, 67], [372, 13, 507, 17], [82, 482, 307, 37],
                 [117, 322, 73, 396], [402, 181, 266, 59]], float)
q = np.array([0.295, 0.205, 0.205, 0.295])
N = CTCF.sum(1, keepdims=True)
Wm = np.log2((CTCF + 0.8 * q) / (N + 0.8) / q)
L = len(CTCF)
fig, ax = bio.canvas(24.0, 11.0)
S.logo(ax, CTCF, at=(2.0, 6.4), col_width=1.0, height=3.6, title="A   Logo (information content)")
b = C.axes_at(ax, (2.0, 0.9, L * 1.0, 3.6))
im = b.imshow(Wm.T, aspect="auto", cmap="RdBu_r", vmin=-8, vmax=8, extent=(0.5, L + 0.5, 3.5, -0.5))
for j in range(L):
    for k in range(4):
        v = Wm[j, k]
        b.text(j + 1, k, f"{v:.1f}", ha="center", va="center", fontsize=bio.core.FONT["tiny"] * 0.85,
               color="#1f2430" if abs(v) < 5 else "#ffffff")
b.set_yticks(range(4))
b.set_yticklabels(list("ACGT"))
b.set_xticks(range(1, L + 1))
C.style_axes(b, "position", None, box=True)
bio.label(ax, (2.0 + L / 2, 5.0), "B   Position weight matrix (bits)", size="small", bold=True)
cb = C.axes_at(ax, (22.0, 0.9, 0.35, 3.6))
fig.colorbar(im, cax=cb)
C.style_axes(cb, None, None, box=True)
