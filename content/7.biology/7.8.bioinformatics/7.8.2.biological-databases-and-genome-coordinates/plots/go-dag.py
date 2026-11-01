# A fragment of the biological-process aspect of the Gene Ontology around terms annotated to MCM6, with a toy
# annotation set of 100 genes. Solid arrows: is_a; thick open blue arrows: part_of; dashed: paths
# through omitted intermediate terms. Each box gives direct / propagated gene counts and the information
# content -log2(n/N) after propagation by the true-path rule. DNA repair has two parents, so this is a DAG.
import math
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 15.0)
N = 100
terms = {  # name: (position, direct annotations)
    "biological_process": ((13.0, 13.6), 15),
    "metabolic process": ((7.0, 10.9), 30),
    "cellular response to\nDNA damage stimulus": ((19.5, 8.2), 10),
    "DNA metabolic process": ((7.0, 8.2), 5),
    "DNA replication": ((3.6, 5.3), 12),
    "DNA repair": ((12.2, 5.3), 20),
    "DNA replication initiation": ((3.6, 2.4), 8),
}
edges = [  # child, parent, kind
    ("metabolic process", "biological_process", "omit"),
    ("cellular response to\nDNA damage stimulus", "biological_process", "omit"),
    ("DNA metabolic process", "metabolic process", "omit"),
    ("DNA replication", "DNA metabolic process", "is_a"),
    ("DNA repair", "DNA metabolic process", "is_a"),
    ("DNA repair", "cellular response to\nDNA damage stimulus", "part_of"),
    ("DNA replication initiation", "DNA replication", "part_of"),
]
parents = {}
for c, p, _ in edges:
    parents.setdefault(c, []).append(p)


def ancestors(t):
    out = {t}
    for p in parents.get(t, []):
        out |= ancestors(p)
    return out


total = {t: 0 for t in terms}
for t, (_, d) in terms.items():
    for a in ancestors(t):
        total[a] += d
W, H = 5.6, 1.9
for t, ((x, y), d) in terms.items():
    n = total[t]
    ic = abs(-math.log2(n / N))
    tok = "highlight" if t in ("DNA replication initiation", "DNA replication") else "neutral"
    bio.box(ax, (x, y), W, H, token=tok, text=None)
    bio.label(ax, (x, y + 0.42), t, size="small", color=P.on_fill() if tok != "neutral" else P.ink())
    bio.label(ax, (x, y - 0.55), f"direct {d}, total {n},  IC {ic:.2f} bits", size="tiny",
              color=P.on_fill() if tok != "neutral" else P.ink())
for c, p, kind in edges:
    (xc, yc), _ = terms[c]
    (xp, yp), _ = terms[p]
    a = (xc, yc + H / 2)
    b = (xp, yp - H / 2)
    if kind == "omit":
        bio.arrow(ax, a, b, kind="process", dashed=True, lw=1.0, color=P.muted())
    elif kind == "is_a":
        bio.arrow(ax, a, b, kind="process", lw=1.3)
    else:
        bio.arrow(ax, a, b, kind="activation", lw=2.2, color=P.edge("dna"))
bio.label(ax, (21.0, 2.9), "is_a", size="small", ha="left")
bio.arrow(ax, (18.6, 2.9), (20.6, 2.9), kind="process", lw=1.3)
bio.label(ax, (21.0, 2.0), "part_of", size="small", ha="left")
bio.arrow(ax, (18.6, 2.0), (20.6, 2.0), kind="activation", lw=2.2, color=P.edge("dna"))
bio.label(ax, (21.0, 1.1), "via omitted terms", size="small", ha="left")
bio.arrow(ax, (18.6, 1.1), (20.6, 1.1), kind="process", dashed=True, lw=1.0, color=P.muted())
bio.label(ax, (3.6, 0.8), "MCM6 is annotated here", size="tiny", color=P.muted())
