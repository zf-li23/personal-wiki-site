"""Boundary sharpening. (A) Dispersion relation of Turing's example for three diffusion ratios. (B) Dispersion
relation of the depletion model a_t = mu - h^2 a + D a'', h_t = c h^2 a - lam h (+ D_h h''). (C) Steady states of
the depletion model as level curves of the energy integral. (D) Spatial profiles of h for three amplitudes."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 4, figsize=(13.6, 3.5))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.86, wspace=0.36)


def growth(J, d1, d2, k):
    out = []
    for kk in k:
        M = J - np.diag([d1 * kk * kk, d2 * kk * kk])
        out.append(np.linalg.eigvals(M).real.max())
    return np.array(out)


a = axs[0]
J = np.array([[3 / 16, 1 / 4], [-1 / 4, -1 / 4]])
k = np.linspace(0, 2.0, 300)
for r, tok in ((0.1, "positive"), (0.25, "highlight"), (0.5, "negative")):
    a.plot(k, growth(J, r, 1.0, k), color=charts.line(tok), lw=1.6, label="eps/nu = %.2f" % r)
a.axhline(0, color=P_.muted(), lw=0.8)
a.set_ylim(-0.12, 0.08)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower left")
charts.style_axes(a, "wave number k", "growth rate")
charts.title(a, "A  Turing's example")

mu, lam, c, D = 1.0, 1.0, 2.0, 1.0
am = lam ** 2 / (c ** 2 * mu)
hm = c * mu / lam
Jd = np.array([[-hm ** 2, -2 * hm * am], [c * hm ** 2, 2 * c * hm * am - lam]])
b = axs[1]
k = np.linspace(0, 12, 400)
for dh, tok, lab in ((0.0, "drug", "D_h = 0"), (0.01, "dna", "D_h = 0.01")):
    b.plot(k, growth(Jd, D, dh, k), color=charts.line(tok), lw=1.6, label=lab)
b.axhline(0, color=P_.muted(), lw=0.8)
b.axvline(c * mu / (lam * np.sqrt(D)), color=P_.muted(), lw=0.8, ls="--")
b.text(2.2, -1.3, "k0", fontsize=FT["tiny"], color=P_.muted())
b.set_ylim(-1.6, 1.2)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower right")
charts.style_axes(b, "wave number k", "growth rate")
charts.title(b, "B  Depletion model")

cc = axs[2]
A = np.linspace(0.03, 1.4, 300)
Ap = np.linspace(-0.9, 0.9, 300)
AA, AP = np.meshgrid(A, Ap)
E = 0.5 * D * AP ** 2 + mu * AA - (lam ** 2 / c ** 2) * np.log(AA)
Em = mu * am - (lam ** 2 / c ** 2) * np.log(am)
cc.contour(AA, AP, E, levels=Em + np.array([0.002, 0.02, 0.08, 0.2, 0.4]), colors=[charts.line("protein")], linewidths=1.1)
cc.plot([am], [0], "o", color=P_.ink(), ms=3)
charts.style_axes(cc, "substrate a", "da/dx")
charts.title(cc, "C  Phase portrait")

d = axs[3]
for B, tok in ((0.02, "dna"), (0.12, "protein"), (0.5, "drug")):
    s = solve_ivp(lambda x, y: [y[1], (lam ** 2 / (c ** 2 * y[0]) - mu) / D], [0, 12], [am + B, 0.0], max_step=0.01, rtol=1e-9)
    d.plot(s.t, lam / (c * s.y[0]), color=charts.line(tok), lw=1.5, label="a(0) - a_m = %.2f" % B)
lg = d.legend(frameon=True, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right", facecolor=P_.surface(), edgecolor=P_.muted(), framealpha=1.0)
lg.set_zorder(10)
d.set_ylim(0, 9)
charts.style_axes(d, "position x", "self-enhancing species h")
charts.title(d, "D  Periodic profiles")
