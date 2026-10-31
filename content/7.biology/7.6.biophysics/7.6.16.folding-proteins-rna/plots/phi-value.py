# Phi-value analysis of a two-state folder (synthetic data, 25 C, RT = 2.479 kJ/mol).
# Wild type: k_f(H2O) = 500 /s, k_u(H2O) = 0.05 /s, m_f = 7, m_u = 3 kJ/mol/M (as in the chevron of 7.1.6).
# Three mutants destabilize the native state by the same ddG = 5 kJ/mol but differ in where the lost
# interaction lies: phi = 0 (unstructured in the transition state: only k_u rises), phi = 0.5, phi = 1
# (fully formed in the transition state: only k_f falls).
# A: chevron plots, ln k_obs = ln(k_f exp(-m_f D/RT) + k_u exp(m_u D/RT)), with 4 % noise.
# B: Gibbs-energy diagrams U - TS - N for the wild type and the phi = 0 and phi = 1 mutants.
# C: a Leffler (Brønsted) plot for a hypothetical set of 14 mutations with phi ~ 0.3 (as in a diffuse nucleus):
#    change of ln k_f against change of ln K relative to the wild type; the slope is the average phi.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
RT = 2.479
kf0, ku0, mf, mu = 500.0, 0.05, 7.0, 3.0
ddG = 5.0
D = np.linspace(0, 8, 300)
Dpts = np.arange(0.25, 8.0, 0.5)


def chevron(kf, ku, D):
    return kf * np.exp(-mf * D / RT) + ku * np.exp(mu * D / RT)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2), gridspec_kw={"width_ratios": [1.15, 1, 1]})
cases = [("wild type", 0.0, None, "neutral"), ("φ = 0", ddG, 0.0, "dna"), ("φ = 0.5", ddG, 0.5, "enzyme"),
         ("φ = 1", ddG, 1.0, "rna")]
for lab, dd, phi, tok in cases:
    if phi is None:
        kf, ku = kf0, ku0
    else:
        kf = kf0 * np.exp(-phi * dd / RT)
        ku = ku0 * np.exp((1 - phi) * dd / RT)
    c = charts.line(tok)
    axs[0].plot(D, np.log(chevron(kf, ku, D)), color=c, lw=1.6, label=lab)
    y = chevron(kf, ku, Dpts) * np.exp(rng.normal(0, 0.04, Dpts.size))
    axs[0].plot(Dpts, np.log(y), "o", ms=3, color=c)
charts.style_axes(axs[0], "[urea] / M", "ln (k_obs / s⁻¹)")
axs[0].legend(fontsize=7.5, frameon=False, loc="upper center", ncol=2)
axs[0].set_ylim(-1.5, 9.5)
charts.title(axs[0], "A   Chevrons: same ΔΔG, different φ")

# B: Gibbs-energy diagrams with the unfolded state of each protein as reference (schematic barrier height)
ax = axs[1]
GU, GTS, GN = 0.0, 18.0, -RT * np.log(kf0 / ku0)


def profile(gts, gn):
    """Smooth curve through U (x = 1), TS (x = 3) and N (x = 5) with flat tangents at each level."""
    xs = np.linspace(0.4, 5.8, 400)
    knots = [(0.4, GU + 3), (1, GU), (3, gts), (5, gn), (5.8, gn + 3)]
    ys = np.empty_like(xs)
    for (x0, y0), (x1, y1) in zip(knots[:-1], knots[1:]):
        m = (xs >= x0) & (xs <= x1)
        t = (xs[m] - x0) / (x1 - x0)
        ys[m] = y0 + (y1 - y0) * (1 - np.cos(np.pi * t)) / 2
    return xs, ys


for lab, gts, gn, tok in (("wild type", GTS, GN, "neutral"), ("φ = 0", GTS, GN + ddG, "dna"),
                          ("φ = 1", GTS + ddG, GN + ddG, "rna")):
    xs, ys = profile(gts, gn)
    ax.plot(xs, ys, color=charts.line(tok), lw=1.6, label=lab)
for xx, txt in ((1, "U"), (3, "TS"), (5, "N")):
    ax.text(xx, -30, txt, ha="center", fontsize=9, color=P.ink())
ax.annotate("", xy=(5.55, GN + ddG), xytext=(5.55, GN), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(5.62, GN + ddG / 2, "ΔΔG", fontsize=7.5, color=P.muted(), va="center")
ax.annotate("", xy=(3.35, GTS + ddG), xytext=(3.35, GTS), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(3.42, GTS + ddG / 2, "ΔΔG‡ (φ = 1)", fontsize=7.5, color=P.muted(), va="center")
ax.set_xlim(0.3, 6.4)
ax.set_ylim(-32, GTS + 14)
ax.set_xticks([])
charts.style_axes(ax, "reaction coordinate", "G − G(U)  /  (kJ mol⁻¹)")
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.title(ax, "B   Where the mutation acts")

# C: Leffler plot, changes relative to the wild type (the line through the origin has slope phi)
n = 14
ddGs = rng.uniform(1.5, 9.0, n)
phis = np.clip(rng.normal(0.3, 0.08, n), 0, 1)
x = -ddGs / RT                                  # change in ln K
y = -phis * ddGs / RT + rng.normal(0, 0.05, n)  # change in ln k_f
axs[2].plot(x, y, "o", ms=4, color=charts.line("enzyme"))
slope = np.sum(x * y) / np.sum(x * x)
xx = np.linspace(x.min() - 0.3, 0, 10)
axs[2].plot(xx, slope * xx, color=P.muted(), lw=1.0, ls="--")
axs[2].plot([0], [0], "s", ms=5, color=charts.line("neutral"))
axs[2].text(-0.1, 0.06, "wild type", fontsize=7.5, ha="right", color=P.ink())
for ph in (0.0, 1.0):
    axs[2].plot(xx, ph * xx, color=P.muted(), lw=0.6, ls=":")
axs[2].text(xx[0] + 0.1, 0.05, "φ = 0", fontsize=7, color=P.muted())
axs[2].text(xx[0] + 0.2, xx[0] + 0.5, "φ = 1", fontsize=7, color=P.muted())
axs[2].text(-2.4, -0.25, f"fitted slope φ = {slope:.2f}", fontsize=8, color=P.ink())
charts.style_axes(axs[2], "Δ ln K  =  −ΔΔG/RT", "Δ ln k_f")
charts.title(axs[2], "C   Leffler plot of 14 mutants")
fig.tight_layout()
