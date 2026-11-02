"""Mutant resistance in a tissue feedback loop (same illustrative BIG model as the previous figure).
A: net growth rate mu(G) of beta cells against glucose, monotonic (no glucotoxicity) and biphasic
(death rises again at high glucose): the biphasic curve has a stable zero at 5 mM and an unstable one at
12 mM; above it fewer beta cells mean more glucose (vicious cycle).
B: growth rate, at normal glucose, of a mutant that misreads glucose as lambda G (lambda > 1: for example
a glucokinase with lower half-saturation constant): with the monotonic curve every lambda > 1 has an
advantage; with the biphasic curve only 1 < lambda < 2.4 does.
C: a mutant clone starting at a fraction 1e-6 of the beta-cell mass. Monotonic tissue, lambda = 5: the
clone takes over within months (half the mass by day 36) and drives glucose to G0/lambda = 1 mM. Biphasic tissue: lambda = 5 is
eliminated; lambda = 1.5 still spreads, more slowly (half the mass by day 424), and lowers glucose towards 3.3 mM."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
G0, G1, mu0 = 5.0, 12.0, 0.1
c = 5.0 ** 3  # G^3 * (total insulin-secreting mass) = const at quasi-steady state, with B = 1 at G0


def mu_bi(G):
    return mu0 * (G / G0 - 1) * (1 - G / G1) * G1 / (G1 - G0)


def mu_mono(G):
    return mu0 * (G / G0 - 1)


fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.36)

ax = axs[0]
G = np.linspace(2, 20, 300)
ax.plot(G, mu_mono(G), color=charts.line("neutral"), lw=1.4, label="monotonic")
ax.plot(G, mu_bi(G), color=charts.line("protein"), lw=1.6, label="biphasic (glucotoxicity)")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.plot([G0], [0], "o", ms=6, color=charts.line("protein"))
ax.plot([G1], [0], "o", ms=6, mfc="none", mec=charts.line("protein"), mew=1.4)
ax.annotate("stable", (G0, 0), (G0 - 1.2, -0.07), fontsize=7, color=P.ink())
ax.annotate("unstable", (G1, 0), (G1 + 0.4, 0.03), fontsize=7, color=P.ink())
ax.set_ylim(-0.5, 0.3)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "glucose G (mM)", "beta-cell growth rate (1/day)")
charts.title(ax, "A  Rate plot")

ax = axs[1]
lam = np.linspace(0.3, 6, 300)
ax.plot(lam, mu_mono(lam * G0), color=charts.line("neutral"), lw=1.4, label="monotonic")
ax.plot(lam, mu_bi(lam * G0), color=charts.line("protein"), lw=1.6, label="biphasic")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvspan(1, G1 / G0, color=P.fill("negative"), alpha=0.25, lw=0)
ax.text(1.05, 0.22, "dangerous\nmutants", fontsize=7, color=P.ink())
ax.set_ylim(-0.8, 0.5)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "misreading factor lambda", "mutant growth rate at G0 (1/day)")
charts.title(ax, "B  Which mutants spread")


def clone(mu, lam, T=1000.0):
    def rhs(t, z):
        Bw, Bm = np.exp(z)
        Gq = (c / (Bw + Bm)) ** (1 / 3)
        return [mu(Gq), mu(lam * Gq)]

    t = np.linspace(0, T, 801)
    r = solve_ivp(rhs, (0, T), [0.0, np.log(1e-6)], t_eval=t, rtol=1e-8, atol=1e-10)
    Bw, Bm = np.exp(r.y)
    return t, (c / (Bw + Bm)) ** (1 / 3), Bm / (Bw + Bm)


ax = axs[2]
for mu, lamv, tok, lab in [(mu_mono, 5.0, "neutral", "monotonic, lambda = 5"),
                           (mu_bi, 5.0, "protein", "biphasic, lambda = 5"),
                           (mu_bi, 1.5, "negative", "biphasic, lambda = 1.5")]:
    t, Gt, frac = clone(mu, lamv)
    ax.plot(t, Gt, color=charts.line(tok), lw=1.5, label=lab)
ax.set_ylim(0, 6)
ax.legend(fontsize=7, frameon=False, loc="center right", bbox_to_anchor=(1.0, 0.36))
charts.style_axes(ax, "time (days)", "fasting glucose (mM)")
charts.title(ax, "C  Takeover by a mis-sensing clone")
