# Quantitative antigen-antibody binding (Eqs. 9.1-9.4 of the page).
# A: monovalent isotherm theta = c/(K_D + c) and the apparent isotherm of a bivalent antibody on a multivalent surface,
#    K_D,app = K_D / (1 + c_eff/K_D): avidity can make up for a 100-fold weaker site.
# B: Scatchard plot r/c against r for an antibody with n = 2 sites: straight lines for one affinity, concave for a mixture.
# C: precipitin behaviour of bivalent antibody and an antigen of valence n (Flory-Stockmayer connectivity index).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23.0, 7.2)

# --- A  isotherms ------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.05))
bio.label(ax, (3.9, 6.9), "Affinity and avidity", size="title", bold=True)
pa = quant.Plot(ax, (1.4, 1.2, 5.6, 4.9), xlim=(1e-13, 1e-4), ylim=(0, 1), xlog=True,
                xlabel="free antibody concentration / M", ylabel="bound fraction $\\theta$", ylabel_offset=1.0,
                xticks=[(1e-12, "$10^{-12}$"), (1e-10, "$10^{-10}$"), (1e-8, "$10^{-8}$"), (1e-6, "$10^{-6}$"), (1e-4, "$10^{-4}$")],
                yticks=[0, 0.5, 1])
c = np.logspace(-13, -4, 500)
CEFF = 1e-3


def kapp(kd, ceff=CEFF):
    return kd / (1 + ceff / kd)


curves = [("monovalent, $K_\\mathrm{D} = 10^{-7}$ M", 1e-7, "muted"),
          ("bivalent, same site", kapp(1e-7), "negative"),
          ("bivalent, $K_\\mathrm{D} = 10^{-5}$ M", kapp(1e-5), "channel")]
items = []
for txt, kd, tok in curves:
    pa.line(c, c / (kd + c), tok, lw=1.8, dashed=(tok == "muted"), zorder=20 if tok == "muted" else None)
    items.append((txt, tok, "--" if tok == "muted" else "-"))
pa.legend(items, (pa.X(3e-13), pa.Y(0.9)), step=0.42)
pa.hline(0.5, dashed=True)

# --- B  Scatchard -----------------------------------------------------------------------------------------
bio.panel(ax, "B", (8.0, 7.05))
bio.label(ax, (11.8, 6.9), "Scatchard plot ($n = 2$ sites)", size="title", bold=True)
pb = quant.Plot(ax, (9.2, 1.2, 5.4, 4.9), xlim=(0, 2), ylim=(0, 1.1e10),
                xlabel="bound sites per antibody $r$", ylabel="$r/c$ / M$^{-1}$", ylabel_offset=1.0,
                xticks=[0, 0.5, 1, 1.5, 2], yticks=[(0, "0"), (5e9, "$5\\times10^{9}$"), (1e10, "$10^{10}$")])
r = np.linspace(0, 2, 200)
n = 2
for K, tok in ((5e9, "channel"), (1e9, "enzyme")):
    pb.line(r, (n - r) * K, tok, lw=1.8)
# heterogeneous population: half the antibody with K = 5e9, half with K = 1e8 (per-site binding)
cc = np.logspace(-12, -4, 800)
K1, K2 = 5e9, 1e8
r_mix = n * 0.5 * (K1 * cc / (1 + K1 * cc) + K2 * cc / (1 + K2 * cc))
pb.line(r_mix, r_mix / cc, "negative", lw=1.8, dashed=True)
pb.legend([("$K = 5\\times10^{9}$ M$^{-1}$", "channel", "-"), ("$K = 10^{9}$ M$^{-1}$", "enzyme", "-"),
           ("mixture of two affinities", "negative", "--")], (pb.X(1.05), pb.Y(1.0e10)), step=0.42)

# --- C  precipitin zones --------------------------------------------------------------------------------------
bio.panel(ax, "C", (15.4, 7.05))
bio.label(ax, (20.0, 6.9), "Precipitin zones", size="title", bold=True)
pc = quant.Plot(ax, (17.0, 1.2, 5.2, 4.9), xlim=(0.02, 50), ylim=(0, 8), xlog=True,
                xlabel="antibody sites / antigen epitopes $\\rho$", ylabel="connectivity index",
                ylabel_offset=0.9, xticks=[(0.1, "0.1"), (1, "1"), (10, "10")], yticks=[0, 1, 2, 4, 6, 8])
rho = np.logspace(np.log10(0.02), np.log10(50), 600)
pA = np.where(rho < 1, 1.0, 1 / rho)
pB = np.where(rho < 1, rho, 1.0)
for nn, tok in ((3, "channel"), (5, "enzyme"), (9, "negative")):
    pc.line(rho, (nn - 1) * pA * pB, tok, lw=1.8)
pc.hline(1, dashed=True)
bio.label(ax, (pc.X(0.025), pc.Y(1.35)), "network forms\nabove 1", size="tiny", color=P.muted(), ha="left")
pc.legend([("$n = 3$", "channel", "-"), ("$n = 5$", "enzyme", "-"), ("$n = 9$", "negative", "-")], (pc.X(5), pc.Y(5.5)), step=0.42)
bio.label(ax, (pc.X(0.045), pc.Y(7.2)), "antigen\nexcess", size="tiny", color=P.muted())
bio.label(ax, (pc.X(1.0), pc.Y(7.5)), "equivalence", size="tiny", color=P.muted())
bio.label(ax, (pc.X(22), pc.Y(7.2)), "antibody\nexcess", size="tiny", color=P.muted())
