# Two Gurken signals and the localization of the axis mRNAs during oogenesis. A (stage 6-7): the oocyte nucleus lies
# at the posterior; Gurken (yellow) signals to the terminal follicle cells, which adopt a posterior fate and signal
# back, reorganizing the oocyte microtubules. B (stage 9-10): the nucleus has moved to an anterior-dorsal corner,
# where Gurken now signals to the overlying follicle cells and makes them dorsal; bicoid mRNA (pink) is anchored at
# the anterior cortex by dynein-dependent transport, oskar mRNA (green) at the posterior pole by kinesin-1, and the
# nurse cells pour their cytoplasm into the oocyte through ring canals.
import wikibio as bio
from wikibio import bodyaxes as BA

fig, ax = bio.canvas(24.0, 15.2)
P = bio.P

bio.panel(ax, "A", (0.2, 15.0))
bio.label(ax, (1.0, 14.6), "Stage 6-7: first Gurken signal", size="normal", bold=True, ha="left")
a = BA.EggChamber(ax, (6.6, 11.3), 8.0, 3.8, nucleus="posterior", boundary=0.6, border_cells=False)
a.cortex(-30, 30, "highlight", width=0.3)
A = a.anchors
bio.arrow(ax, (A["nucleus"][0] + 0.1, A["nucleus"][1] + 0.35), (A["follicle_posterior"][0] - 0.05, A["follicle_posterior"][1] + 0.9),
          kind="activation", bend=-0.3)
bio.label(ax, (11.3, 13.0), "Gurken → Torpedo (EGFR):\nterminal follicle cells\nbecome posterior", size="small", ha="left")
bio.arrow(ax, (A["follicle_posterior"][0] - 0.05, A["follicle_posterior"][1] - 0.9), (A["nucleus"][0] - 0.6, A["nucleus"][1] - 0.45),
          kind="activation", bend=-0.3, dashed=True)
bio.label(ax, (11.3, 9.6), "signal back to the oocyte:\nmicrotubules reorganize", size="small", ha="left")
bio.callout(ax, A["nurse"], (1.0, 9.0), "Nurse cells")
bio.callout(ax, A["nucleus"], (9.7, 14.4), "Oocyte nucleus")

bio.panel(ax, "B", (0.2, 7.6))
bio.label(ax, (1.0, 7.2), "Stage 9-10: second Gurken signal and mRNA localization", size="normal", bold=True, ha="left")
b = BA.EggChamber(ax, (7.4, 3.6), 10.0, 4.4, nucleus="dorsal")
b.microtubules()
b.anterior_cap("receptor", width=0.35)
b.cortex(-28, 28, "positive", width=0.3)
b.cortex(118, 142, "highlight", width=0.3)
B = b.anchors
bio.arrow(ax, (B["nucleus"][0] + 0.3, B["nucleus"][1] + 0.2), (B["follicle_dorsal"][0] + 0.4, B["follicle_dorsal"][1] + 0.1),
          kind="activation", bend=-0.4)
bio.callout(ax, B["follicle_dorsal"], (10.0, 7.0), "Dorsal follicle cells")
bio.callout(ax, B["ring_canal"], (2.6, 0.5), "Ring canals")
bio.callout(ax, B["border_cells"], (1.0, 6.4), "Border cells")
bio.callout(ax, B["posterior"], (13.6, 2.0), "Posterior pole")

# key
x0, y0 = 15.6, 6.6
items = [("receptor", "bicoid", "mRNA, anterior (dynein)"), ("positive", "oskar", "mRNA, posterior (kinesin-1);\nnanos is trapped here later"),
         ("highlight", "gurken", "mRNA and protein, next to\nthe oocyte nucleus")]
for k, (tok, g, txt) in enumerate(items):
    y = y0 - k * 1.5
    ax.add_patch(bio.core.FancyBboxPatch((x0, y - 0.18), 0.6, 0.36, boxstyle="round,pad=0,rounding_size=0.08",
                                         facecolor=P.edge(tok), edgecolor="none", zorder=12))
    bio.label(ax, (x0 + 0.9, y + 0.12), g, size="small", italic=True, ha="left", bold=True)
    bio.label(ax, (x0 + 2.6, y), txt, size="tiny", ha="left", color=P.muted())
ax.plot([x0, x0 + 0.6], [y0 - 4.5, y0 - 4.5], color=P.mix(P.edge("neutral"), P.surface(), 0.25), lw=0.9)
bio.label(ax, (x0 + 0.9, y0 - 4.5), "microtubules: minus ends at the anterior and lateral\ncortex, plus ends biased to the posterior",
          size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0, 0.5), "anterior left, dorsal up", size="tiny", color=P.muted(), ha="left")
