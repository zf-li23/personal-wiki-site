"""Targets of neurotoxins on a schematic membrane (outside above). Inhibition bars: blockers;
open arrows: activators (toxins that open channels or prolong their opening)."""
import wikibio as bio
from wikibio import neuro

P = bio.P
fig, ax = bio.canvas(30, 12)
y = 4.2
neuro.patch(ax, 0.2, 29.8, y, depth=1.8)
mh = neuro.MEMBRANE_HALF
top = y + mh + 0.2

targets = [
    (4.0, "na", "Na$_\\mathrm{V}$ channel"),
    (9.5, "k", "K$_\\mathrm{V}$ channel"),
    (13.5, "k", "Ca$^{2+}$-activated\nK$^+$ (BK, SK)"),
    (17.5, "ca", "Ca$_\\mathrm{V}$2.2 (N-type)"),
    (21.3, "receptor", "Nicotinic ACh\nreceptor (muscle)"),
    (25.0, "receptor", "Glutamate receptor\n(kainate, AMPA)"),
]
for x, ion, name in targets:
    if ion == "receptor":
        neuro.channel(ax, x, y, None, token="receptor", text=name, text_dy=0.5)
    else:
        neuro.channel(ax, x, y, ion, text=name, text_dy=0.5)
neuro.pump(ax, 28.2, y, text="Na$^+$/K$^+$-ATPase", ions=False)

# (text x, text y, lines, target x, kind)
groups = [
    (1.9, 10.6, ["Block the pore:", "tetrodotoxin, saxitoxin,", "μ-conotoxin"], 3.8, "inhibition"),
    (6.2, 10.6, ["Open or prolong opening:", "batrachotoxin, grayanotoxin,", "brevetoxin, ciguatoxin,",
                 "α- and β-scorpion toxins,", "δ-conotoxin"], 4.2, "activation"),
    (9.9, 7.6, ["κ-conotoxin, hanatoxin,", "ShK, charybdotoxin"], 9.5, "inhibition"),
    (13.6, 10.6, ["Charybdotoxin,", "iberiotoxin (BK)", "apamin (SK)"], 13.5, "inhibition"),
    (17.5, 7.6, ["ω-conotoxin"], 17.5, "inhibition"),
    (21.3, 10.6, ["α-bungarotoxin,", "α-cobratoxin,", "α-conotoxin"], 21.3, "inhibition"),
    (25.0, 7.6, ["Domoic acid", "(agonist)"], 25.0, "activation"),
    (28.2, 10.6, ["Palytoxin", "(pump to channel)"], 28.2, "activation"),
]
for tx, ty, lines, x, kind in groups:
    for i, ln in enumerate(lines):
        bio.label(ax, (tx, ty - 0.48 * i), ln, size="small", bold=(i == 0 and ln.endswith(":")))
    y0 = ty - 0.48 * (len(lines) - 1) - 0.35
    bio.arrow(ax, (tx, y0), (x, top + 0.05), kind=kind, bg=bio.P.fill("extracellular"))
ax.set_ylim(1.7, 11.5)
