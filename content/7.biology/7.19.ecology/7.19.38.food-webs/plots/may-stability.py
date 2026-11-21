"""May's (1972) complexity-stability criterion.

Community matrices A = -I + M: self-regulation -1 on the diagonal, and each off-diagonal entry is
non-zero with probability C (connectance) and then drawn from N(0, sigma^2).
A: eigenvalues of one matrix with S = 250, C = 0.2 and sigma sqrt(SC) = 0.8; by the circular law they
fill a disk of radius sigma sqrt(SC) centered at -1 (circle), which lies in the left half-plane: the
equilibrium is stable.
B: fraction of 200 (S = 10), 120 (S = 40) or 30 (S = 150) random matrices that are stable
(all eigenvalues with negative real part), against sigma sqrt(SC), with C = 0.3. The transition
sharpens around 1 as S grows, as the circular law predicts.
"""

import numpy as np
from threadpoolctl import threadpool_limits

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
threadpool_limits(1)  # small eigenproblems: threads only add overhead
rng = np.random.default_rng(5)
fig, ax = bio.canvas(30.0, 12.0)


def community(S, Cn, sig):
    M = rng.normal(0, sig, (S, S)) * (rng.random((S, S)) < Cn)
    np.fill_diagonal(M, 0)
    return M - np.eye(S)


S, Cn = 250, 0.2
R = 0.8
ev = np.linalg.eigvals(community(S, Cn, R / np.sqrt(S * Cn)))
pa = C.axes_at(ax, (2.6, 1.6, 9.0, 9.0))
pa.scatter(ev.real, ev.imag, s=5, color=Q.line_color("dna"), lw=0)
th = np.linspace(0, 2 * np.pi, 300)
pa.plot(-1 + R * np.cos(th), R * np.sin(th), color=Q.line_color("negative"), lw=1.3)
pa.axvline(0, color=P.muted(), lw=0.9, ls="--")
pa.set_xlim(-2.2, 0.6)
pa.set_ylim(-1.4, 1.4)
pa.set_aspect("equal")
C.style_axes(pa, "Re(lambda)", "Im(lambda)")
pa.text(-1, 1.0, "radius sigma sqrt(SC)", fontsize=FS["tiny"], color=P.ink(), ha="center")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Eigenvalues: S = 250, C = 0.2", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (16.6, 1.9, 12.2, 8.4))
xs = np.linspace(0.4, 1.6, 11)
Cn = 0.3
for S, reps, tok in [(10, 200, "rna"), (40, 120, "positive"), (150, 30, "dna")]:
    fr = []
    for x in xs:
        sig = x / np.sqrt(S * Cn)
        st = [np.linalg.eigvals(community(S, Cn, sig)).real.max() < 0 for _ in range(reps)]
        fr.append(np.mean(st))
    pb.plot(xs, fr, "o-", ms=3, color=Q.line_color(tok), lw=1.4, label=f"S = {S}")
pb.axvline(1, color=P.muted(), lw=0.9, ls="--")
pb.set_xlim(0.4, 1.6)
pb.set_ylim(-0.03, 1.03)
C.style_axes(pb, "complexity sigma sqrt(SC)", "probability of stability")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (14.6, 11.6))
bio.label(ax, (16.6, 11.2), "Stability collapses at sigma sqrt(SC) = 1 (C = 0.3)", size="small", bold=True, ha="left")
