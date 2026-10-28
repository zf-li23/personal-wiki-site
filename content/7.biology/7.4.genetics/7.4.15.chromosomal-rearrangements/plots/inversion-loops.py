"""Crossing over inside the loop of an inversion heterozygote. The products are computed by
cytogenetics.crossover_products from the two gene orders (one crossover between the segments marked X;
the two chromatids not involved keep the parental orders)."""
import wikibio as bio
from wikibio import cytogenetics as C

P = bio.P
fig, ax = bio.canvas(26, 9.6)
N = list("AB") + ["o"] + list("CDEFG")
cases = [None, None]
cases[0] = ("A", "Paracentric inversion of D-E-F", ("D", "F"), ("D", "E"), 0.6)
cases[1] = ("B", "Pericentric inversion of B to E (includes the centromere)", ("B", "E"), ("C", "D"), 13.6)
for letter, title, (f, l), xo, x0 in cases:
    bio.panel(ax, letter, (x0 - 0.4, 9.5))
    bio.label(ax, (x0 + 0.5, 9.2), title, size="small", ha="left")
    r = C.inversion_loop(ax, (x0 + 1.4, 5.7), N, f, l, crossover=xo, unit=0.72)
    bio.label(ax, (r["right"] + 0.3, 5.7 + 0.2), "normal", size="tiny", ha="left", color=P.edge("dna"))
    bio.label(ax, (r["right"] + 0.3, 5.7 - 0.2), "inverted", size="tiny", ha="left", color=P.edge("receptor"))
    prods = [(C.with_token(N, "dna"), "parental (normal)", None),
             (C.with_token(r["inverted"], "receptor"), "parental (inverted)", None)]
    rec = C.crossover_products(C.with_token(N, "dna"), C.with_token(r["inverted"], "receptor"), *xo)
    for chrom in rec:
        d = C.describe(chrom, N)
        if d["kind"] == "dicentric":
            text = "dicentric: bridge at anaphase I"
        elif d["kind"] == "acentric":
            text = "acentric fragment: lost"
        else:
            text = f"duplication {'-'.join(d['extra'])}, deficiency {'-'.join(d['missing'])}"
        prods.append((chrom, text, "negative"))
    y = 3.3
    bio.label(ax, (x0 + 0.5, y + 0.55), "Products of meiosis", size="small", ha="left", color=P.muted())
    for chrom, text, tok in prods:
        o = C.lettered(ax, (x0 + 0.5, y), chrom, unit=0.42, height=0.3)
        bio.label(ax, (max(o["x1"], x0 + 5.0) + 0.3, y), text, size="tiny", ha="left",
                  color=P.edge(tok) if tok else P.ink())
        y -= 0.62
