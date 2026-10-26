# Separating and distinguishing the three nuclear RNA polymerases.
# A: idealized DEAE-Sephadex elution profile (after Roeder and Rutter 1969). Protein absorbance is a sum of broad
# peaks, polymerase activity three narrow Gaussian peaks (I, II, III) eluting at increasing ammonium sulfate
# concentration along a linear gradient. Arbitrary units; the shapes are illustrative, not data.
# B: alpha-amanitin sensitivity modeled as single-site inhibition v/v0 = 1 / (1 + [I]/IC50) with the
# half-inhibitory concentrations of the mammalian enzymes (Pol II 0.02, Pol III 20 ug/mL, Pol I resistant).
# The shaded bands mark the concentrations used to assign transcripts in Example 12.1.2.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19.0, 7.8)

# ---- A: elution profile
a = C.axes_at(ax, (1.4, 1.3, 7.0, 5.2))
f = np.linspace(0, 80, 600)  # fraction number


def g(x, m, s, h):
    return h * np.exp(-0.5 * ((x - m) / s) ** 2)


protein = g(f, 8, 4, 1.0) + g(f, 30, 9, 0.45) + g(f, 55, 12, 0.35) + 0.04
activity = g(f, 22, 2.6, 0.75) + g(f, 38, 2.8, 1.0) + g(f, 52, 3.0, 0.55)
salt = np.clip((f - 12) / 60, 0, 1) * 0.6

a.plot(f, protein, color=C.line("neutral"), lw=1.6, label="protein ($A_{280}$)")
a.plot(f, activity, color=C.line("enzyme"), lw=2.0, label="polymerase activity")
a.set_xlim(0, 80)
a.set_ylim(0, 1.25)
a.set_yticks([])
C.style_axes(a, "fraction number", "signal (arbitrary units)")
for m, h, name in [(22, 0.75, "I"), (38, 1.0, "II"), (52, 0.55, "III")]:
    a.text(m, h + 0.05, name, ha="center", va="bottom", fontsize=bio.core.FONT["small"], color=C.line("enzyme"),
           weight="bold")
s = a.twinx()
s.plot(f, salt, color=P.muted(), lw=1.0, ls=(0, (4, 3)))
s.set_ylim(0, 0.75)
s.set_yticks([0, 0.3, 0.6])
C.style_axes(s, None, "[(NH$_4$)$_2$SO$_4$] / M", box=True)
s.spines["left"].set_visible(False)
s.spines["top"].set_visible(False)
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
s.text(76, 0.62, "salt", ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "A", (0.1, 7.7))
bio.label(ax, (0.6, 7.35), "Ion-exchange chromatography (idealized)", size="normal", bold=True, ha="left")

# ---- B: alpha-amanitin dose response
b = C.axes_at(ax, (11.2, 1.3, 7.2, 5.2))
c = np.logspace(-4, 3, 400)  # ug/mL
b.axvspan(0.5, 2.0, color=P.fill("highlight"), alpha=0.35, lw=0)
b.axvspan(100, 400, color=P.fill("highlight"), alpha=0.35, lw=0)
for ic50, tok, name in [(None, "dna", "Pol I"), (0.02, "enzyme", "Pol II"), (20.0, "rna", "Pol III")]:
    v = np.ones_like(c) if ic50 is None else 1 / (1 + c / ic50)
    b.plot(c, 100 * v, color=C.line(tok), lw=2.0, label=name)
    if ic50:
        b.plot([ic50], [50], "o", ms=4, mfc=P.fill(tok), mec=C.line(tok))
b.axhline(50, color=P.muted(), lw=0.7, ls=(0, (2, 2)))
b.set_xscale("log")
b.set_xlim(1e-4, 1e3)
b.set_ylim(0, 116)
b.set_xticks([1e-4, 1e-2, 1, 1e2], ["$10^{-4}$", "$10^{-2}$", "1", "$10^{2}$"])
C.style_axes(b, "[α-amanitin] / (µg mL$^{-1}$)", "activity / % of control")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
b.text(1.0, 108, "1 µg/mL", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.text(200, 108, "200 µg/mL", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "B", (9.9, 7.7))
bio.label(ax, (10.4, 7.35), "Sensitivity to α-amanitin", size="normal", bold=True, ha="left")
