"""Where the free energy of one glucose goes in aerobic respiration (malate-aspartate shuttle).

A: a waterfall from the standard Gibbs energy of complete oxidation (2840 kJ/mol) to ATP.
Stage 1, glycolysis, pyruvate dehydrogenase and the citric acid cycle: the electrons end up in
10 NADH (each worth 2F x 1.136 V = 219 kJ/mol when passed to O2) and 2 FADH2 of succinate
dehydrogenase (2F x 0.785 V = 151 kJ/mol), and 4 ATP or GTP are made by substrate-level
phosphorylation (about 50 kJ/mol each in the cell); about 145 kJ is released as heat.
Stage 2, the respiratory chain: 10 x 10 + 2 x 6 = 112 protons are pumped, each storing about
19 kJ/mol (Example 23.2.1), 2128 kJ in all. Stage 3, ATP synthase and transport: at 4 protons per
ATP (P/O 2.5 and 1.5) the gradient makes 28 ATP, and the total is 32 ATP, 1600 kJ, 56 %.
B: ATP per glucose and the corresponding efficiency (32 x 50 / 2840) against the protons used per
ATP, n/3 + 1, for the two shuttles; marked are the bovine c8 ring (3.67), the textbook value (4) and
the yeast c10 ring (4.33)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
tiny = bio.core.FONT["tiny"]
small = bio.core.FONT["small"]

F = 96.485
NADH = 2 * F * (0.816 + 0.320)
SUCC = 2 * F * (0.816 - 0.031)
ATP_CELL = 50.0
G0 = 2840.0
carriers = 10 * NADH + 2 * SUCC
sub_atp = 4 * ATP_CELL
grad = 112 * 19.0
atp_ox = 112 / 4 * ATP_CELL

fig, ax = bio.canvas(24.0, 9.6)

bio.panel(ax, "A", (0.1, 9.5))
a = charts.axes_at(ax, (1.6, 1.4, 12.2, 7.0))
stages = [
    ("Glucose\n+ 6 O$_2$", [(G0, "highlight", "")]),
    ("10 NADH + 2 FADH$_2$\n+ 4 ATP", [(sub_atp, "atp", "4 ATP"), (carriers, "enzyme", "NADH, FADH$_2$")]),
    ("proton gradient\n(112 H$^+$) + 4 ATP", [(sub_atp, "atp", ""), (grad, "channel", "112 H$^+$")]),
    ("32 ATP", [(sub_atp + atp_ox, "atp", "32 ATP")]),
]
tops = []
for i, (name, parts) in enumerate(stages):
    y = 0
    for h, tok, lab in parts:
        a.bar(i, h, bottom=y, width=0.58, color=P.fill(tok), edgecolor=charts.line(tok), lw=1.0)
        if lab:
            a.text(i, y + h / 2, lab, ha="center", va="center", fontsize=tiny, color=P.on_fill())
        y += h
    tops.append(y)
    a.text(i, y + 50, f"{y:.0f} kJ", ha="center", va="bottom", fontsize=tiny, color=P.ink(), weight="bold")
for i in range(1, len(tops)):
    loss = tops[i - 1] - tops[i]
    a.annotate("", (i - 0.32, tops[i]), (i - 0.32, tops[i - 1]),
               arrowprops=dict(arrowstyle="-|>", color=charts.line("negative"), lw=1.2))
    a.plot([i - 1 + 0.29, i - 0.32], [tops[i - 1]] * 2, color=P.muted(), lw=0.7, ls=":")
    a.text(i - 0.36, tops[i] - 30, f"heat\n{loss:.0f} kJ", ha="right", va="top",
           fontsize=tiny, color=charts.line("negative"))
a.set_xticks(range(len(stages)))
a.set_xticklabels([s[0] for s in stages])
a.set_xlim(-0.5, 3.5)
a.set_ylim(0, 3200)
charts.style_axes(a, None, r"free energy per glucose / kJ mol$^{-1}$")
charts.title(a, f"One glucose: {tops[-1] / G0:.0%} ends up in ATP")

bio.panel(ax, "B", (15.0, 9.5))
b = charts.axes_at(ax, (16.6, 1.4, 6.0, 7.0))
h = np.linspace(3.4, 4.8, 200)
for H, tok, lab in ((112, "enzyme", "malate–aspartate shuttle"), (104, "protein", "glycerol 3-phosphate shuttle")):
    b.plot(h, H / h + 4, color=charts.line(tok), lw=2.0, label=lab)
for x, lab in ((8 / 3 + 1, "bovine c$_8$"), (4.0, "textbook"), (10 / 3 + 1, "yeast c$_{10}$")):
    b.axvline(x, color=P.muted(), lw=0.7, ls=":")
    b.text(x + 0.02, 36.3, lab, fontsize=tiny, color=P.ink(), rotation=90, va="top")
b.set_xlim(3.4, 4.8)
b.set_ylim(24, 36.5)
b.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "H$^+$ per ATP ($n$/3 + 1)", "ATP per glucose")
r = b.twinx()
r.set_ylim(np.array(b.get_ylim()) * ATP_CELL / G0 * 100)
charts.style_axes(r, None, "efficiency / %", box=True)
r.spines["left"].set_visible(False)
r.spines["bottom"].set_visible(False)
r.spines["top"].set_visible(False)
charts.title(b, "Non-integer stoichiometry")
