"""A piece of the Gene Ontology (biological process), from 'cellular response to glucocorticoid
stimulus' up to the root; arrows are is_a relations from child to parent (some parents of the lower
terms are omitted). Each term shows the number of airway genes annotated to it after propagation by
the true-path rule (n, out of 11707 tested genes with a biological-process annotation) and the number
of them among the 402 genes induced by dexamethasone (k: padj < 0.05, log2 FC > 1). Colour: one-sided
hypergeometric p-value of the overlap. Every gene counted at a term is counted again at all its
ancestors, so the tests along a path are strongly dependent. Annotations: GO Consortium, goa_human
(UniProtKB, excluding NOT and ND), ontology go-basic, 2026 releases."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19, 12.4)
# id: (label, n, k, p, x, y)
T = {
    "0008150": ("biological_process", 11707, 402, 1.0, 9.5, 11.5),
    "0050896": ("response to stimulus", 4662, 200, 2.6e-5, 6.0, 9.9),
    "0009987": ("cellular process", 10254, 348, 0.76, 14.5, 9.9),
    "0042221": ("response to chemical", 2032, 87, 1.4e-2, 3.6, 8.1),
    "0009719": ("response to endogenous\nstimulus", 819, 50, 4.6e-5, 8.4, 8.1),
    "0051716": ("cellular response to\nstimulus", 3877, 162, 1.3e-3, 14.5, 8.1),
    "0033993": ("response to lipid", 531, 32, 1.4e-3, 2.4, 6.2),
    "0009725": ("response to hormone", 544, 39, 1.0e-5, 7.2, 6.2),
    "0070887": ("cellular response to\nchemical stimulus", 1262, 61, 3.5e-3, 13.0, 6.2),
    "0048545": ("response to steroid\nhormone", 183, 12, 2.4e-2, 4.8, 4.4),
    "0031960": ("response to\ncorticosteroid", 91, 10, 1.1e-3, 4.8, 2.7),
    "0051384": ("response to\nglucocorticoid", 76, 10, 2.6e-4, 4.8, 1.0),
    "0071385": ("cellular response to\nglucocorticoid stimulus", 33, 7, 1.1e-4, 11.0, 1.0),
}
E = [("0050896", "0008150"), ("0009987", "0008150"), ("0042221", "0050896"), ("0009719", "0050896"),
     ("0051716", "0050896"), ("0051716", "0009987"), ("0033993", "0042221"), ("0009725", "0042221"),
     ("0009725", "0009719"), ("0070887", "0042221"), ("0070887", "0051716"), ("0048545", "0033993"),
     ("0048545", "0009725"), ("0031960", "0048545"), ("0051384", "0031960"), ("0071385", "0051384")]
W, H = 3.6, 1.25


def token(p):
    return "negative" if p < 1e-3 else "highlight" if p < 0.05 else "neutral"


for t, (lab, n, k, p, x, y) in T.items():
    bio.box(ax, (x, y), W, H, token(p))
    bio.label(ax, (x, y + 0.2), lab, size="tiny", color=P.on_fill())
    bio.label(ax, (x, y - 0.42 if "\n" in lab else y - 0.32), f"k/n = {k}/{n}", size="tiny", color=P.on_fill(), bold=True)


def edge_point(x, y, tx, ty):
    # point on the box border of (x, y) in the direction of (tx, ty)
    dx, dy = tx - x, ty - y
    s = min((W / 2) / abs(dx) if dx else 1e9, (H / 2) / abs(dy) if dy else 1e9)
    return x + dx * s, y + dy * s


for c, p in E:
    x1, y1 = T[c][4:6]
    x2, y2 = T[p][4:6]
    bio.arrow(ax, edge_point(x1, y1, x2, y2), edge_point(x2, y2, x1, y1), kind="process", lw=1.0, head=0.18)

for i, (tok, txt) in enumerate([("negative", "p < 0.001"), ("highlight", "0.001 <= p < 0.05"), ("neutral", "p >= 0.05")]):
    bio.box(ax, (15.3, 3.4 - 0.75 * i), 0.5, 0.45, tok, radius=0.06)
    bio.label(ax, (15.75, 3.4 - 0.75 * i), txt, size="small", ha="left")
