# The free energy of supercoiling, G = K RT (dLk)^2 / N with K = 1100 (topoisomer distributions of
# relaxed circles, Depew & Wang 1975; Pulleyblank et al. 1975), N the length in bp and dLk = Lk - Lk0.
# A: the Boltzmann distribution of topoisomers produced when a closed circle is nicked and resealed
#    (or relaxed by a type I topoisomerase): P(Lk) ~ exp(-K (Lk - Lk0)^2 / N), with Lk0 = N / 10.5.
#    For 3990 bp, Lk0 = 380.0 is an integer and the most likely topoisomer has dLk = 0; for 3995 bp,
#    Lk0 = 380.48 and every topoisomer carries |dLk| >= 0.48 (Watson, Box 4-3).
# B: the free energy of supercoiling of a 5000-bp plasmid and the corresponding torque
#    tau = (1 / 2 pi) dG/dLk = K kB T sigma / (pi h), as functions of the superhelical density sigma.
import numpy as np
import wikibio as bio
from wikibio import charts as C

K, h = 1100.0, 10.5
RT = 8.314e-3 * 310.0           # kJ/mol
kT = 4.28                       # pN nm at 310 K
P = bio.P
fig, ax = bio.canvas(19, 8)

# --- A: topoisomer distributions ----------------------------------------------------------------
a = C.axes_at(ax, (1.5, 1.4, 6.8, 5.6))
for N, tok, off in ((3990, "dna", -0.17), (3995, "negative", 0.17)):
    lk0 = N / h
    lk = np.arange(376, 386)
    p = np.exp(-K * (lk - lk0) ** 2 / N)
    p /= p.sum()
    a.bar(lk + off, p, width=0.32, color=P.fill(tok), edgecolor=C.line(tok), lw=0.8,
          label=f"N = {N} bp, $\\mathrm{{Lk}}_0$ = {lk0:.2f}")
    a.axvline(lk0, color=C.line(tok), lw=0.9, ls=(0, (3, 2)))
a.set_xlim(375.5, 385.5)
a.set_ylim(0, 0.36)
a.set_xticks(range(376, 386, 2))
a.set_yticks([0, 0.1, 0.2, 0.3])
C.style_axes(a, "Linking number Lk", "Fraction of circles")
leg = a.legend(loc="upper right", frameon=False, fontsize=bio.core.FONT["tiny"])
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "A", (0.1, 7.7))
bio.label(ax, (1.5, 7.35), "Topoisomers after relaxation", size="normal", bold=True, ha="left")

# --- B: free energy and torque vs sigma -----------------------------------------------------------
b = C.axes_at(ax, (11.0, 1.4, 6.4, 5.6))
N = 5000
sig = np.linspace(-0.1, 0.1, 401)
dlk = sig * N / h
G = K * RT * dlk ** 2 / N
b.plot(sig, G, color=C.line("dna"), lw=1.8)
b.set_xlim(-0.1, 0.1)
b.set_ylim(0, 1300)
b.set_xticks([-0.1, -0.05, 0, 0.05, 0.1], ["−0.10", "−0.05", "0", "0.05", "0.10"])
b.set_yticks([0, 400, 800, 1200])
C.style_axes(b, "Superhelical density σ", "G (5 kb plasmid) / (kJ mol⁻¹)")
b.axvspan(-0.07, -0.05, color=P.fill("highlight"), alpha=0.35, lw=0)
b.text(-0.06, 1250, "purified\ncellular\nDNA", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center", va="top")
t = b.twinx()
t.plot(sig, K * kT * sig / (np.pi * h), color=C.line("negative"), lw=1.4, ls=(0, (4, 2)))
t.set_ylim(-15, 15)
t.set_yticks([-15, -10, -5, 0, 5, 10, 15], ["−15", "−10", "−5", "0", "5", "10", "15"])
C.style_axes(t, None, None)
t.spines["right"].set_visible(True)
t.spines["right"].set_color(P.muted())
t.set_ylabel("Torque τ / (pN nm)", color=P.ink(), fontsize=bio.core.FONT["small"])
t.axhline(-10.5, color=P.muted(), lw=0.8, ls=":")
t.text(0.098, -11.2, "B-DNA melts", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right", va="top")
bio.panel(ax, "B", (9.6, 7.7))
bio.label(ax, (11.0, 7.35), "Energy (solid) and torque (dashed)", size="normal", bold=True, ha="left")
