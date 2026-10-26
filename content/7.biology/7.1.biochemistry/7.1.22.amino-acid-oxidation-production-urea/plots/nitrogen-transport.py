"""Inter-organ transport of amino nitrogen in mammals. Skeletal muscle exports amino groups as alanine (made
by transamination of glycolytic pyruvate) and glutamine; the liver removes the nitrogen as urea and returns
glucose made from the alanine carbon (glucose-alanine cycle). Other tissues, including the brain, make
glutamine from free ammonia (glutamine synthetase). The intestine uses glutamine as fuel and releases NH4+
and alanine into the portal blood. The kidney takes up glutamine and excretes NH4+ in the urine (increased
in acidosis), and excretes the urea made in the liver."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 11.6)
ink = P.ink()


def flow(a, b, text, tok="neutral", bend=0.0, at=0.5, dx=0.0, dy=0.25, ha="center", color=None):
    pts = bio.arrow(ax, a, b, kind="process", color=color or P.edge(tok), lw=1.8, head=0.24, bend=bend)
    m = pts[int(at * (len(pts) - 1))]
    bio.label(ax, (m[0] + dx, m[1] + dy), text, size="small", ha=ha, bold=True, color=color or P.edge(tok))


liver = (9.5, 6.0)
bio.icon(ax, "servier/liver", at=liver, height=2.6)
bio.label(ax, (liver[0] + 1.5, liver[1] - 1.4), "Liver:\nurea cycle,\ngluconeogenesis", size="small", bold=True, ha="left")
muscle = (2.6, 6.0)
bio.icon(ax, "servier/muscle", at=muscle, height=3.0)
bio.label(ax, (muscle[0], muscle[1] - 1.9), "Skeletal muscle", size="small", bold=True)
brain = (9.5, 10.2)
bio.icon(ax, "servier/brain", at=brain, height=1.8)
bio.label(ax, (brain[0] + 1.5, brain[1]), "Brain and other tissues", size="small", bold=True, ha="left")
gut = (9.5, 1.5)
bio.icon(ax, "servier/intestine", at=gut, height=2.0)
bio.label(ax, (gut[0] - 1.6, gut[1]), "Intestine", size="small", bold=True, ha="right")
kidney = (16.4, 6.0)
bio.icon(ax, "servier/kidney", at=kidney, height=2.4)
bio.label(ax, (kidney[0], kidney[1] - 1.7), "Kidney", size="small", bold=True)

# muscle <-> liver: glucose-alanine cycle
flow((4.2, 6.7), (8.0, 6.7), "Alanine", tok="positive", bend=-0.12)
flow((8.0, 5.3), (4.2, 5.3), "Glucose", tok="carbohydrate", bend=-0.12, dy=-0.3)
flow((4.0, 7.6), (8.2, 7.6), "Glutamine", tok="enzyme", bend=-0.25, dy=0.3)
# brain -> liver
flow((9.0, 9.2), (9.0, 7.5), "Gln", tok="enzyme", dx=-0.45, dy=0.0)
# gut -> liver (portal vein)
flow((9.9, 2.6), (9.9, 4.6), "NH₄⁺, Ala", tok="h", dx=0.4, dy=0.0, ha="left")
# liver -> kidney
flow((11.0, 6.6), (15.0, 6.6), "Urea", tok="positive", bend=-0.1)
flow((11.0, 7.8), (15.0, 7.4), "Glutamine", tok="enzyme", bend=-0.2, dy=0.3)
# kidney -> urine
bio.arrow(ax, (16.4, 4.0), (16.4, 2.8), kind="process", color=ink, lw=1.6, head=0.22)
bio.label(ax, (16.4, 2.4), "urine: urea, NH₄⁺", size="small", bold=True)
bio.label(ax, (16.6, 3.4), "glutaminase:\nNH₄⁺ (acidosis)", size="tiny", ha="left", color=P.muted())
bio.label(ax, (2.6, 9.0), "BCAA oxidation:\nN → Glu → Ala, Gln", size="tiny", color=P.muted())
