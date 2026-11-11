"""Causal inference for audiovisual localization (model of Koerding et al. 2007).

Prior over position: N(0, 15^2) deg; sigma_v = 2 deg, sigma_a = 8 deg; prior probability of a common
cause p = 0.5. For each true pair (s_v = 0, s_a = disparity) 20000 noisy observations x_v, x_a are
drawn; the posterior probability of a common cause and the model-averaged auditory estimate
s_a_hat = P(C=1|x) s_hat_C1 + (1 - P(C=1|x)) s_hat_C2 are computed with the closed forms.
A: mean posterior probability of a common cause against the disparity. B: mean shift of the auditory estimate
(relative to the auditory-only estimate, toward vision) with the model-averaged estimate (solid), with forced fusion (dashed) and with
no integration (dotted).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
sv, sa, s0, pc = 2.0, 8.0, 15.0, 0.5
dis = np.arange(0, 41, 2.0)
n = 20000


def like1(xv, xa):
    V = sv ** 2 * sa ** 2 + sv ** 2 * s0 ** 2 + sa ** 2 * s0 ** 2
    return np.exp(-0.5 * ((xv - xa) ** 2 * s0 ** 2 + xv ** 2 * sa ** 2 + xa ** 2 * sv ** 2) / V) / (2 * np.pi * np.sqrt(V))


def like2(xv, xa):
    return np.exp(-0.5 * (xv ** 2 / (sv ** 2 + s0 ** 2) + xa ** 2 / (sa ** 2 + s0 ** 2))) / (
        2 * np.pi * np.sqrt((sv ** 2 + s0 ** 2) * (sa ** 2 + s0 ** 2)))


post, bias, fused, alone = [], [], [], []
for d in dis:
    xv = rng.normal(0, sv, n)
    xa = rng.normal(d, sa, n)
    l1, l2 = like1(xv, xa), like2(xv, xa)
    p1 = pc * l1 / (pc * l1 + (1 - pc) * l2)
    s_c1 = (xv / sv ** 2 + xa / sa ** 2) / (1 / sv ** 2 + 1 / sa ** 2 + 1 / s0 ** 2)
    s_c2 = (xa / sa ** 2) / (1 / sa ** 2 + 1 / s0 ** 2)
    est = p1 * s_c1 + (1 - p1) * s_c2
    post.append(p1.mean())
    bias.append(s_c2.mean() - est.mean())
    fused.append(s_c2.mean() - s_c1.mean())
    alone.append(0.0)

fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1))
ax = axs[0]
ax.plot(dis, post, color=P.edge("dna"), lw=2)
ax.set_xlabel("Audiovisual disparity / deg")
ax.set_ylabel("Mean P(common cause | x)")
ax.set_ylim(0, 1)
ax.set_title("A  Evidence for a common cause", loc="left", fontsize=10)
ax = axs[1]
ax.plot(dis, bias, color=P.edge("rna"), lw=2.2, label="causal inference")
ax.plot(dis, fused, color=P.edge("dna"), lw=1.5, ls="--", label="forced fusion")
ax.plot(dis, alone, color=P.muted(), lw=1.5, ls=":", label="no integration")
ax.set_xlabel("Audiovisual disparity / deg")
ax.set_ylabel("Shift of auditory estimate toward vision / deg")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Ventriloquism fades with disparity", loc="left", fontsize=10)
fig.tight_layout()
