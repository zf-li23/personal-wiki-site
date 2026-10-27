"""The nuclear envelope in section (schematic).
(A) Cytoplasm above, nucleoplasm below: the outer nuclear membrane with ribosomes, continuous with an ER tube;
the perinuclear space continuous with the ER lumen; the inner nuclear membrane lined by the lamina and
peripheral heterochromatin; two nuclear pore complexes in pores where the membranes join; a LINC complex.
(B) One NPC enlarged in side view with its parts. (C) NPC face view showing the eightfold symmetry."""

import wikibio as bio
from wikibio import nuclear as N

P = bio.P
fig, ax = bio.canvas(22.2, 8.0)

# A: envelope section
bio.panel(ax, "A", (0.1, 7.90))
env = N.envelope(ax, 0.4, 11.6, 3.7, gap=0.55, pores=[4.4, 9.2], pore_width=1.5, er=1.6, er_height=2.0, tint=(3.3, 3.1))
N.linc(ax, 6.9, env, reach=1.5)
bio.callout(ax, (1.6, 5.20), (2.7, 6.70), "ER (rough)")
bio.callout(ax, (2.6, 4.25), (2.9, 5.50), "Outer nuclear membrane")
bio.callout(ax, (2.9, 3.70), (3.4, 1.20), "Perinuclear space")
bio.callout(ax, (6.0, 3.35), (5.6, 1.70), "Inner nuclear membrane")
bio.callout(ax, (8.0, 3.10), (7.4, 1.20), "Lamina")
bio.callout(ax, (10.6, 2.75), (10.2, 0.80), "Heterochromatin")
bio.callout(ax, (6.95, 5.40), (7.9, 6.70), "Nesprin (KASH)")
bio.callout(ax, (6.9, 3.10), (6.4, 2.20), "SUN")
bio.callout(ax, (6.5, 5.70), (5.6, 6.70), "Actin")
bio.callout(ax, (9.75, 4.3), (10.3, 6.70), "Nuclear pore complex")
bio.callout(ax, (3.6, 4.40), (4.0, 6.20), "Ribosome")

# B: one NPC enlarged
bio.panel(ax, "B", (12.2, 7.90))
y0 = 3.7
env2 = N.envelope(ax, 12.6, 17.6, y0, gap=0.7, pores=[15.1], pore_width=2.4, ribosomes=False, tint=(3.3, 3.1), labels=False,
                  heterochromatin=False, lamina_depth=0.0, draw_pores=False)
p = N.pore(ax, 15.1, y0, gap=0.7, width=2.4)
bio.callout(ax, p["filaments"][-1], (17.0, 6.40), "Cytoplasmic filaments")
bio.callout(ax, (14.33, y0 + 0.62), (13.0, 5.80), "Cytoplasmic ring")
bio.callout(ax, (14.05, y0), (13.0, 5.00), "Inner ring")
bio.callout(ax, (14.33, y0 - 0.62), (13.0, 2.40), "Nuclear ring")
bio.callout(ax, p["basket"], (13.0, 1.60), "Nuclear basket")
bio.callout(ax, (15.1, y0 + 0.1), (17.2, 5.20), "FG mesh")
bio.callout(ax, (16.27, y0 + 0.2), (17.25, 4.50), "Pore membrane")
bio.label(ax, (17.5, 6.80), "Cytoplasm", size="small", bold=True, ha="right", color=P.muted())
bio.label(ax, (17.5, 0.95), "Nucleoplasm", size="small", bold=True, ha="right", color=P.muted())

# C: face view
bio.panel(ax, "C", (19.2, 7.90))
N.pore_top(ax, (20.75, 4.90), 1.0)
bio.label(ax, (20.75, 3.05), "Face view", size="small")
bio.label(ax, (20.75, 2.60), "(eightfold symmetry)", size="tiny", color=P.muted())
bio.scale_bar(ax, (20.15, 1.70), 1.2, "about 50 nm", size="tiny")
