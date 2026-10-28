"""When are two alleles separated? A locus (A/a) segregates at meiosis I if no crossover occurs between it and
the centromere (A), and at meiosis II if one does (B). Blue: paternal homologue; red: maternal."""
import wikibio as bio
from wikibio import genetics as G
from wikibio import cytogenetics as C

fig, ax = bio.canvas(19.0, 11.0)
B, R = "dna", "receptor"
L, cen, loc = 2.8, 0.25, 0.82
for k, (s0, title) in enumerate(((None, "No crossover between centromere and locus"),
                                 (0.55, "One crossover between centromere and locus"))):
    y = 8.0 - k * 5.3
    bio.panel(ax, "AB"[k], (0.2, y + 2.7))
    bio.label(ax, (5.6, y + 2.45), title, size="small")
    b = G.bivalent(ax, (2.2, y), length=L, centromere=cen, width=0.5, chiasma=s0, separation=0.7,
                   loci=[(loc, ("A", "a"))])
    if s0 is not None:
        bio.callout(ax, b["chiasma"], (3.9, b["chiasma"][1]), "chiasma")
    bio.label(ax, (2.2, y - L / 2 - 0.35), "bivalent", size="tiny", color=bio.P.muted(), va="top")
    # after meiosis I: homologue a (blue, one chromatid recombinant) and homologue b (red)
    if s0 is None:
        after = [([[(0, 1, B)], [(0, 1, B)]], ("A", "A")), ([[(0, 1, R)], [(0, 1, R)]], ("a", "a"))]
    else:
        after = [([[(0, 1, B)], [(0, s0, B), (s0, 1, R)]], ("A", "a")), ([[(0, s0, R), (s0, 1, B)], [(0, 1, R)]], ("A", "a"))]
    for j, (cols, al) in enumerate(after):
        cy = y + (1.15 if j == 0 else -1.15)
        C.round_cell(ax, (7.6, cy), 1.0)
        G.chromosome(ax, (7.6, cy), length=1.5, centromere=cen, width=0.42, colors=cols)
        bio.label(ax, (8.75, cy - 0.1), f"${al[0]}\\,{al[1]}$", size="normal", ha="left")
        bio.arrow(ax, (3.6, y + (0.4 if j == 0 else -0.4)), (6.5, cy), kind="process", lw=1.0, head=0.16)
        # meiosis II products
        for i in range(2):
            gy = cy + (0.55 if i == 0 else -0.55)
            C.round_cell(ax, (12.2, gy), 0.5)
            G.chromosome(ax, (12.2, gy), length=0.8, centromere=cen, width=0.4, sister=False, colors=[cols[i]])
            bio.label(ax, (12.9, gy), f"${al[i]}$", size="normal", ha="left")
            bio.arrow(ax, (8.7, cy + (0.35 if i == 0 else -0.35)), (11.6, gy), kind="process", lw=0.9, head=0.14)
    note = ("A and a separated at meiosis I\n(first-division segregation)" if k == 0 else
            "A and a separated at meiosis II\n(second-division segregation)")
    bio.label(ax, (16.3, y), note, size="small")
    bio.label(ax, (5.0, y + 1.85), "meiosis I", size="tiny", color=bio.P.muted())
    bio.label(ax, (10.1, y + 2.0), "meiosis II", size="tiny", color=bio.P.muted())
