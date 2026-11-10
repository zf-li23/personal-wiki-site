# Clonal selection and the primary vs secondary antibody response: antigen selects the naive B cell whose
# receptor fits, the clone expands and differentiates into plasma cells and memory cells; a minimal
# kinetic model (antigen, IgM- and IgG-secreting B cells, memory cells, serum IgM and IgG) reproduces the
# lag, the IgM-to-IgG switch, and the faster, larger, IgG-dominated secondary response.
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import immuno, quant

P = bio.P
fig, ax = bio.canvas(25, 12.6)

# ---- A: clonal selection ------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.5))
naive = ["protein", "enzyme", "receptor", "channel", "carbohydrate"]
sel = 2
ys = 9.4
for k, tok in enumerate(naive):
    x = 1.3 + k * 1.55
    immuno.immune_cell(ax, (x, ys), r=0.55, token="neutral", receptor_token=tok, receptors=7, seed=k)
bio.label(ax, (4.4, 7.9), "Naive B cells: one receptor specificity each", size="tiny", va="top")
# the antigen binds the matching receptor
ag = (1.3 + sel * 1.55, 11.55)
bio.virus(ax, ag, 0.38, kind="enveloped")
bio.label(ax, (ag[0] + 0.6, ag[1]), "antigen", size="tiny", ha="left")
bio.arrow(ax, (ag[0], ag[1] - 0.52), (ag[0], ys + 0.95), kind="process", head=0.16)
# clonal expansion
bio.arrow(ax, (8.6, ys), (10.0, ys), kind="process")
bio.label(ax, (9.3, ys + 0.35), "selection", size="tiny", va="bottom")
bio.label(ax, (9.3, ys - 0.35), "+ T-cell help", size="tiny", va="top", color=P.muted())
for k, (dx, dy) in enumerate(((0, 0.55), (0.95, 0.55), (0.48, -0.3), (1.43, -0.3), (-0.47, -0.3), (0.48, 1.4))):
    immuno.immune_cell(ax, (10.95 + dx, ys + dy - 0.35), r=0.42, token="neutral", receptor_token=naive[sel],
                       receptors=6, seed=10 + k)
bio.label(ax, (11.4, 7.9), "Clonal expansion", size="tiny", va="top")
bio.arrow(ax, (12.9, ys + 0.5), (14.4, ys + 1.2), kind="process")
bio.arrow(ax, (12.9, ys - 0.5), (14.4, ys - 1.0), kind="process")
immuno.immune_cell(ax, (15.3, ys + 1.25), r=0.55, kind="plasma", token="neutral", seed=21)
for k, (dx, dy, a) in enumerate(((1.1, 0.5, -60), (1.4, -0.1, -90), (1.0, -0.55, -120))):
    bio.antibody(ax, (15.3 + dx, ys + 1.25 + dy), size=0.42, angle=a, token=naive[sel], light_token=naive[sel])
bio.label(ax, (17.1, ys + 1.25), "Plasma cells: secrete antibody\n(IgM first, then IgG)", size="tiny", ha="left")
immuno.immune_cell(ax, (15.3, ys - 1.1), r=0.5, kind="memory", token="neutral", receptor_token=naive[sel], receptors=6,
                   seed=22)
bio.label(ax, (16.2, ys - 1.1), "Memory B cells: long-lived, more numerous\nthan naive precursors, already switched",
          size="tiny", ha="left")

# ---- model (time in days; amounts in arbitrary units) -------------------------------------------------------
p = dict(dA=0.12, kc=0.05, Ka=0.05, r=1.2, c=0.02, d=0.25, ra=3.0, f=1.0, dm=0.001, pM=1.0, pG=1.0,
         kM=np.log(2) / 5, kG=np.log(2) / 21)  # serum half-lives: IgM 5 d, IgG 21 d


def rhs(t, y):
    A, BM, BG, Mem, M, G = y
    s = A / (A + p["Ka"])  # antigen-driven activation
    return [-p["dA"] * A - p["kc"] * (M + G) * A,                                   # antigen, cleared by antibody
            (p["r"] - p["c"]) * s * BM - p["d"] * (1 - s) * BM,                     # IgM-secreting B cells
            p["r"] * s * BG + p["c"] * s * BM - p["d"] * (1 - s) * BG + p["ra"] * s * Mem,  # class-switched (IgG)
            p["f"] * p["d"] * (1 - s) * (BM + BG) - p["ra"] * s * Mem - p["dm"] * Mem,  # memory: from contracting clone
            p["pM"] * BM - p["kM"] * M, p["pG"] * BG - p["kG"] * G]                 # serum IgM, IgG


boost = 60.0
s1 = solve_ivp(rhs, (0, boost), [1, 1e-4, 0, 0, 0, 0], max_step=0.1)
y2 = s1.y[:, -1].copy()
y2[0] += 1.0
s2 = solve_ivp(rhs, (boost, 120), y2, max_step=0.1)
t = np.r_[s1.t, s2.t]
Y = np.c_[s1.y, s2.y]
igm, igg = Y[4], Y[5]

# ---- B: titres ----------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 6.6))
pt = quant.Plot(ax, (2.6, 0.95, 21.6, 5.0), (0, 120), (0.1, 1e4), ylog=True, xlabel="Time / days",
                ylabel="Serum antibody (rel. units)", xticks=[0, 20, 40, 60, 80, 100, 120],
                yticks=[(0.1, "0.1"), (1, "1"), (10, "10"), (100, "10²"), (1000, "10³"), (1e4, "10⁴")], grid=True)
pt.line(t, np.maximum(igm, 1e-3), "receptor", lw=2.0, text="IgM", at=0.38, dx=0.1, dy=0.3, ha="left", va="bottom", size="small")
pt.line(t, np.maximum(igg, 1e-3), "dna", lw=2.0, text="IgG", at=0.9, dx=0.0, dy=-0.25, ha="left", va="top", size="small")
pt.line(t, np.maximum(igm + igg, 1e-3), "muted", lw=0.9, dashed=True)
for t0, text in ((0, "1st exposure"), (boost, "2nd exposure (same antigen)")):
    x0 = float(pt.X(t0))
    bio.arrow(ax, (x0, 6.85), (x0, 6.0), kind="process", head=0.18)
    bio.label(ax, (x0 + 0.15, 6.75), text, size="tiny", ha="left")
ipk1 = int(np.argmax(igg * (t < boost)))
ipk2 = int(np.argmax(igg * (t > boost)))
pt.text(t[ipk1] + 3, igg[ipk1] * 1.6, "primary: lag ~7 d, IgM first, then IgG", ha="left", va="bottom", size="tiny")
pt.text(t[ipk2] + 3, igg[ipk2] * 1.6,
        f"secondary: no lag, ~{igg[ipk2] / igg[ipk1]:.0f}× higher, IgG (memory, affinity-matured)", ha="left",
        va="bottom", size="tiny")
pt.hline(1.0, "muted", text="detection limit", x=101)
pt.text(9.5, 130, "total", ha="right", va="bottom", color=P.muted())
