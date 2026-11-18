# Vollenweider's phosphorus loading model, dP/dt = L/z - (sigma + rho) P.
# A: loading diagram with sigma = 10/z (Vollenweider 1975): steady-state total phosphorus P = L / (10 + q_s),
#    where q_s = z/tau_w is the areal hydraulic load; lines of P = 10 and 20 mg m^-3 separate
#    oligotrophic, mesotrophic and eutrophic conditions. B: recovery after the loading is halved, for
#    lakes of 10 m mean depth with water residence times of 0.5, 3 and 15 years (sigma = 1/sqrt(tau_w)).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3))
qs = np.logspace(-1, 3, 200)
for Pc, lab, ls in ((10, "P* = 10 mg m$^{-3}$ (permissible)", "-"), (20, "P* = 20 mg m$^{-3}$ (dangerous)", "--")):
    a.plot(qs, Pc * (10 + qs) / 1000, color=P.ink(), lw=1.8, ls=ls, label=lab)
a.fill_between(qs, 1e-3, 10 * (10 + qs) / 1000, color=P.fill("dna"), alpha=0.25, lw=0)
a.fill_between(qs, 20 * (10 + qs) / 1000, 100, color=P.fill("chloroplast"), alpha=0.45, lw=0)
a.text(0.15, 0.03, "oligotrophic", fontsize=8, color=P.ink())
a.text(0.15, 1.2, "eutrophic", fontsize=8, color=P.ink())
a.text(0.15, 0.135, "mesotrophic", fontsize=8, color=P.ink())
a.annotate("", xy=(5, 0.2), xytext=(5, 0.8), arrowprops=dict(arrowstyle="-|>", color=P.edge("negative"), lw=1.4))
a.plot([5, 5], [0.8, 0.2], "o", color=P.edge("negative"), ms=5)
a.text(6, 0.85, "example lake: P* = 53", fontsize=7.5, color=P.edge("negative"))
a.text(6, 0.17, "loading cut by 75%: P* = 13", fontsize=7.5, color=P.edge("negative"))
a.set_xscale("log")
a.set_yscale("log")
a.set_xlim(0.1, 1000)
a.set_ylim(0.01, 30)
a.set_xlabel("Areal hydraulic load $q_s = z/\\tau_w$ / m yr$^{-1}$")
a.set_ylabel("Phosphorus loading $L$ / g m$^{-2}$ yr$^{-1}$")
a.legend(frameon=False, fontsize=7.5, loc="upper left")
a.set_title("A  Loading diagram", loc="left", fontweight="bold")

z, L0 = 10.0, 1.0
t = np.linspace(-2, 30, 600)
for tw, tok in ((0.5, "dna"), (3.0, "highlight"), (15.0, "negative")):
    k = 1 / tw + 1 / np.sqrt(tw)
    P0 = L0 / (z * k)
    Pt = np.where(t < 0, P0, P0 / 2 + (P0 / 2) * np.exp(-k * np.clip(t, 0, None)))
    b.plot(t, Pt / P0, color=P.edge(tok) if tok == "highlight" else P.fill(tok), lw=2,
           label=f"$\\tau_w$ = {tw:g} yr: response time {1 / k:.1f} yr")
b.axvline(0, color=P.muted(), lw=0.8, ls=":")
b.text(0.4, 1.02, "loading halved", fontsize=7.5, color=P.muted())
b.set_xlim(-2, 30)
b.set_ylim(0.4, 1.08)
b.set_xlabel("Years")
b.set_ylabel("Total phosphorus / initial value")
b.legend(frameon=False, fontsize=7.5, loc="upper right")
b.set_title("B  Response to reduced loading", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
