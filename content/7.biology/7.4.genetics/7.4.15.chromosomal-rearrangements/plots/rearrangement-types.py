"""The four classes of chromosomal rearrangement drawn as lettered chromosomes (segments A-H, centromere
as a waist), and non-allelic homologous recombination between two copies of a low-copy repeat (R)."""
import wikibio as bio
from wikibio import cytogenetics as C

fig, ax = bio.canvas(25.5, 10.6)
P = bio.P
N = list("AB") + ["o"] + list("CDEFGH")
U = 0.5
bio.panel(ax, "A", (0.2, 10.4))
rows = [
    ("Normal", [N]),
    ("Deletion", [[g for g in N if g not in ("E", "F")]]),
    ("Tandem duplication", [N[:6] + ["E", "F"] + N[6:]]),
    ("Paracentric inversion", [C.invert(N, "D", "F")]),
    ("Pericentric inversion", [C.invert(N, "B", "D")]),
]
y = 9.4
for name, chroms in rows:
    bio.label(ax, (0.4, y), name, size="small", ha="left")
    C.lettered(ax, (4.6, y), chroms[0], token="dna", unit=U)
    y -= 0.95
# reciprocal translocation
bio.label(ax, (0.4, y), "Reciprocal translocation", size="small", ha="left")
ch = C.translocation_chromosomes((["A", "B", "o", "C", "D"], ["E", "F", "G", "H"], ["M", "o", "N", "O"], ["P", "Q", "R"]))
C.lettered(ax, (4.6, y + 0.22), ch["N1"], unit=U, height=0.3)
C.lettered(ax, (4.6, y - 0.22), ch["N2"], unit=U, height=0.3)
bio.arrow(ax, (9.9, y), (10.7, y), kind="process", head=0.16)
C.lettered(ax, (11.0, y + 0.22), ch["T1"], unit=U, height=0.3)
C.lettered(ax, (11.0, y - 0.22), ch["T2"], unit=U, height=0.3)
y -= 1.15
bio.label(ax, (0.4, y), "Robertsonian translocation", size="small", ha="left")
C.lettered(ax, (4.6, y + 0.22), C.with_token(["p", "o", "q", "q", "q"], "dna"), unit=U, height=0.3, text=False)
C.lettered(ax, (4.6, y - 0.22), C.with_token(["p", "o", "q", "q"], "enzyme"), unit=U, height=0.3, text=False)
bio.label(ax, (7.5, y + 0.22), "14", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (7.0, y - 0.22), "21", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (8.3, y), (9.1, y), kind="process", head=0.16)
fused = C.with_token(["q", "q"], "enzyme") + [("o", "dna")] + C.with_token(["q", "q", "q"], "dna")
C.lettered(ax, (9.4, y + 0.1), fused, unit=U, height=0.3, text=False)
bio.label(ax, (12.4, y + 0.1), "14q21q", size="tiny", color=P.muted(), ha="left")
C.lettered(ax, (9.4, y - 0.42), [("p", "enzyme"), ("o", "dna"), ("p", "dna")], unit=U * 0.6, height=0.2, text=False)
bio.label(ax, (10.4, y - 0.42), "small p-arm chromosome, lost", size="tiny", color=P.muted(), ha="left")

# B: NAHR
bio.panel(ax, "B", (15.0, 10.4))
bio.label(ax, (15.6, 9.9), "Non-allelic homologous recombination", size="small", ha="left")
Rt = "highlight"
a = [("A", "dna"), ("B", "dna"), ("R", Rt), ("C", "dna"), ("D", "dna"), ("R", Rt), ("E", "dna"), ("F", "dna")]
b = [(n, "receptor" if t == "dna" else t) for n, t in a]
xa, xb = 16.4, 16.4 + 3 * U
oa = C.lettered(ax, (xa, 8.8), a, unit=U)
ob = C.lettered(ax, (xb, 8.25), b, unit=U)
# crossover between the second R of a and the first R of b (misaligned pairing)
mx = oa["x"]["R"][1]
for s in (1, -1):
    ax.plot([mx - 0.25, mx + 0.25], [8.52 - s * 0.25, 8.52 + s * 0.25], color=P.edge("highlight"), lw=2.0, zorder=20)
bio.label(ax, (mx, 9.35), "misaligned repeats pair", size="tiny", color=P.muted())
p1, p2 = C.nahr_products(a, 5, b, 2)
bio.arrow(ax, (19.5, 7.7), (19.5, 7.0), kind="process", head=0.16)
o1 = C.lettered(ax, (16.4, 6.4), p1, unit=U)
bio.label(ax, (o1["x1"] + 0.3, 6.4), "duplication of R-C-D", size="small", ha="left", color=P.edge("positive"))
o2 = C.lettered(ax, (16.4, 5.6), p2, unit=U)
bio.label(ax, (o2["x1"] + 0.3, 5.6), "deletion of C-D-R", size="small", ha="left", color=P.edge("negative"))
bio.label(ax, (15.6, 4.4), "Direct repeats: deletion + reciprocal duplication", size="tiny", ha="left", color=P.muted())
bio.label(ax, (15.6, 3.9), "Inverted repeats: inversion of the segment between them", size="tiny", ha="left", color=P.muted())
bio.label(ax, (15.6, 3.4), "Repeats on non-homologous chromosomes: translocation", size="tiny", ha="left", color=P.muted())
ax.set_ylim(2.9, 10.6)
fig.set_size_inches(25.5 * 0.45, 7.7 * 0.45)
