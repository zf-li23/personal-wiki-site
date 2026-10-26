# Control of Pol II after initiation (idealized models, not measured profiles).
# A, top: Pol II density along a paused gene of 6 kb: a promoter-proximal peak (pause at +50, width 25 bp)
# holding J/k_r polymerases and a uniform gene-body density J/v; with v = 33 nt/s, pause lifetime 5 min and a
# 300 bp window the pausing index is v/(k_r w) = 33 (Example 13.5.2). A, bottom: fractions of polymerase carrying
# Ser5-P and Ser2-P on the CTD, modeled as exp(-x/1.2 kb) and 1 - exp(-x/2 kb) with distance x from the start.
# B: proofreading by transcript cleavage, Eq. (13.2): eps/eps0 = k_ext/(k_c + k_ext), rates in units of the normal
# elongation rate; extension from a mismatch 1e-2 or 1e-3 times normal. Shaded: intrinsic cleavage and with TFIIS.
import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(19.0, 9.6)

# ---- A
x = np.linspace(-500, 6000, 2000)
v, kr, w = 33.0, 1 / 300.0, 300.0
J = 0.05  # polymerases per second (arbitrary)
body = np.where(x > 0, J / v, 0.0) * (x < 5800)
peak = (J / kr) * np.exp(-0.5 * ((x - 50) / 25) ** 2) / (25 * np.sqrt(2 * np.pi))
dens = (body + peak) * 1e3  # per kb
top = C.axes_at(ax, (1.5, 4.9, 7.6, 2.6))
dens = np.maximum(dens, 0.05)
top.fill_between(x, 0.05, dens, color=P.fill("enzyme"), alpha=0.6, lw=0)
top.plot(x, dens, color=C.line("enzyme"), lw=1.4)
top.set_xlim(-500, 6000)
top.set_yscale("log")
top.set_ylim(0.3, dens.max() * 3)
top.set_xticks([])
C.style_axes(top, None, "Pol II / kb (log)")
pi = (J / kr) / (J * w / v)
top.text(400, dens.max() * 1.2, f"pause peak (+20 to +60)\npausing index = {pi:.0f}", fontsize=bio.core.FONT["tiny"],
         color=P.ink(), va="top")
top.text(3000, 2.6, "gene body: J/v", fontsize=bio.core.FONT["tiny"], color=P.muted())

bot = C.axes_at(ax, (1.5, 1.6, 7.6, 2.6))
xx = np.clip(x, 0, None)
s5 = np.where(x > 0, np.exp(-xx / 1200), 0)
s2 = np.where(x > 0, 1 - np.exp(-xx / 2000), 0)
bot.plot(x, s5, color=C.line("drug"), lw=2.0, label="Ser5-P (CDK7)")
bot.plot(x, s2, color=C.line("receptor"), lw=2.0, label="Ser2-P (CDK9, Ctk1)")
bot.set_xlim(-500, 6000)
bot.set_ylim(0, 1.08)
bot.set_xticks([0, 2000, 4000, 6000], ["TSS", "2 kb", "4 kb", "6 kb"])
C.style_axes(bot, "position along the gene", "fraction of Pol II")
bot.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center right")
G.construct(ax, 1.5 + 7.6 * 500 / 6500 - 0.06, 8.1, [{"kind": "promoter"}, {"kind": "cds", "text": "gene", "token": "dna", "width": 6.2}],
            unit=0.45, gap=0.0)
bio.panel(ax, "A", (0.1, 9.5))
bio.label(ax, (0.6, 9.15), "Pausing and the CTD cycle", size="normal", bold=True, ha="left")

# ---- B
b = C.axes_at(ax, (11.4, 1.6, 7.0, 5.9))
kc = np.logspace(-4, 0, 300)
b.axvspan(3e-4, 2e-3, color=P.fill("neutral"), alpha=0.35, lw=0)
b.axvspan(3e-2, 2e-1, color=P.fill("positive"), alpha=0.35, lw=0)
for kext, tok in [(1e-2, "dna"), (1e-3, "rna")]:
    b.plot(kc, kext / (kc + kext), color=C.line(tok), lw=2.0, label=f"$k_{{ext}}$ = {kext:g} × elongation rate")
b.set_xscale("log")
b.set_yscale("log")
b.set_xlim(1e-4, 1)
b.set_ylim(5e-4, 1.5)
C.style_axes(b, "cleavage rate $k_c$ / elongation rate", "remaining errors $\\varepsilon/\\varepsilon_0$")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
b.text(7.7e-4, 1.15, "intrinsic", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.text(7.7e-2, 1.15, "with TFIIS", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "B", (10.1, 9.5))
bio.label(ax, (10.6, 9.15), "Proofreading by cleavage", size="normal", bold=True, ha="left")
