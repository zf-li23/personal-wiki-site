"""A reciprocal translocation heterozygote: cross-shaped pairing at pachytene and the gametes of the
three segregation patterns of the quadrivalent. Balance is checked by
cytogenetics.translocation_segregation (each segment exactly once in a gamete)."""
import wikibio as bio
from wikibio import cytogenetics as C

P = bio.P
fig, ax = bio.canvas(25, 9.4)
arms = (["A", "o", "B"], ["C", "D"], ["W", "o", "X"], ["Y", "Z"])
bio.panel(ax, "A", (0.2, 9.2))
bio.label(ax, (0.9, 8.9), "Pairing in a heterozygote", size="small", ha="left")
ch = C.translocation_cross(ax, (4.3, 4.6), arms, arm=2.9)
bio.panel(ax, "B", (8.8, 9.2))
bio.label(ax, (9.5, 8.9), "Segregation of the quadrivalent at anaphase I", size="small", ha="left")
pats = C.translocation_segregation(ch)
freq = {"Alternate": "common", "Adjacent-1": "common", "Adjacent-2": "rare"}
rule = {"Alternate": "N1 + N2 | T1 + T2", "Adjacent-1": "homologous centromeres to opposite poles",
        "Adjacent-2": "homologous centromeres to the same pole"}
y = 7.7
for p in pats:
    name = p["pattern"]
    bio.label(ax, (9.5, y), f"{name} ({freq[name]})", size="small", ha="left", bold=True)
    bio.label(ax, (9.5, y - 0.45), rule[name], size="tiny", ha="left", color=P.muted())
    for k, g in enumerate(p["gametes"]):
        x = 15.2 + k * 5.0
        c1, c2 = g["chromosomes"]
        C.lettered(ax, (x, y + 0.05), c1, unit=0.4, height=0.28)
        C.lettered(ax, (x, y - 0.4), c2, unit=0.4, height=0.28)
        ok = g["balanced"]
        bio.label(ax, (x + 2.3, y - 0.18), "balanced" if ok else "unbalanced", size="tiny", ha="left",
                  color=P.edge("positive" if ok else "negative"))
    y -= 2.25
bio.label(ax, (15.2, 8.6), "Gamete 1", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (20.2, 8.6), "Gamete 2", size="tiny", color=P.muted(), ha="left")
