"""Heart looping as the buckling of a tube that grows between fixed poles (Formula 28.5.1). A: the tube is held
at its arterial and venous poles; as it lengthens beyond the distance between them, it bends out of the straight
line in the first clamped-clamped mode, with an amplitude of (2/pi) sqrt(L dL) for an excess length dL. B: the
amplitude against the excess growth: without bias the bifurcation is a symmetric pitchfork (left or right
equally likely, dashed); a small left-right asymmetry (h > 0, from asymmetric cell ingression at the poles, under
Nodal-Pitx2 control) unfolds it so that the tube always bends to the right, as in an imperfect pitchfork."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 4.0), gridspec_kw={"width_ratios": [1, 1.2]})
fig.subplots_adjust(left=0.06, right=0.97, bottom=0.15, top=0.88, wspace=0.3)
L0 = 1.0
s = np.linspace(0, 1, 200)
for k, (dL, tk) in enumerate(((0.0, "neutral"), (0.03, "receptor"), (0.08, "drug"), (0.15, "muscle"))):
    A = 2 / np.pi * np.sqrt(L0 * dL)
    w = A / 2 * (1 - np.cos(2 * np.pi * s))
    a.plot(-w, s, color=charts.line(tk), lw=6, solid_capstyle="round", alpha=0.85, label=f"excess length {dL:.2f} L")
a.plot([-0.4, 0.15], [1, 1], color=P_.ink(), lw=2)
a.plot([-0.4, 0.15], [0, 0], color=P_.ink(), lw=2)
a.text(0.17, 1.0, "arterial pole", va="center", fontsize=FT["tiny"], color=P_.ink())
a.text(0.17, 0.0, "venous pole", va="center", fontsize=FT["tiny"], color=P_.ink())
a.text(-0.36, 0.5, "embryo's\nright", ha="left", va="center", fontsize=FT["tiny"], color=P_.muted())
a.set_xlim(-0.45, 1.0)
a.set_ylim(-0.1, 1.1)
a.set_aspect("equal")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
a.set_xticks([])
a.set_yticks([])
for sp in a.spines.values():
    sp.set_visible(False)
charts.title(a, "A  Buckling between fixed poles")
mu = np.linspace(-0.5, 1.5, 400)
amp = np.sqrt(np.clip(mu, 0, None))
b.plot(mu, amp, color=P_.muted(), lw=1.4, ls="--")
b.plot(mu, -amp, color=P_.muted(), lw=1.4, ls="--", label="no bias: right or left")
b.plot(mu[mu < 0], 0 * mu[mu < 0], color=P_.muted(), lw=1.4, ls="--")
for h, tk in ((0.03, "receptor"), (0.12, "muscle")):
    roots = []
    for m in mu:
        r = np.roots([-1, 0, m, h])
        r = r[np.isreal(r)].real
        roots.append(r[r > 0].max())
    b.plot(mu, roots, color=charts.line(tk), lw=1.8, label=f"bias h = {h}")
b.axhline(0, color=P_.muted(), lw=0.5)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "growth beyond the critical length (scaled)", "rightward deflection (scaled)")
charts.title(b, "B  A biased pitchfork chooses the right")
