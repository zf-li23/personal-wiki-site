"""Natural frequencies for 10 000 people screened with low-dose CT, assuming a prevalence of 1.1 %,
sensitivity 93.8 % and specificity 73.4 % (first screening round of the National Lung Screening Trial).
Of the 2734 positive scans, only 103 come from people with lung cancer: the positive predictive value is
103 / 2734 = 3.8 %. Numbers are rounded to whole people.
"""
import wikibio as bio

P = bio.P
N, prev, se, sp = 10000, 0.011, 0.938, 0.734
D = round(N * prev)
TP = round(D * se)
FN = D - TP
ND = N - D
FP = round(ND * (1 - sp))
TN = ND - FP
fig, ax = bio.canvas(16, 8.4)
nodes = {
    "all": ((8, 7.4), f"{N:,} screened", "neutral"),
    "D": ((4, 5.0), f"{D} with cancer", "rna"),
    "ND": ((12, 5.0), f"{ND:,} without cancer", "dna"),
    "TP": ((2.1, 2.5), f"{TP} test +\n(true positive)", "rna"),
    "FN": ((5.9, 2.5), f"{FN} test -\n(false negative)", "rna"),
    "FP": ((10.1, 2.5), f"{FP:,} test +\n(false positive)", "dna"),
    "TN": ((13.9, 2.5), f"{TN:,} test -\n(true negative)", "dna"),
}
for key, (xy, text, tok) in nodes.items():
    bio.box(ax, xy, 3.3 if key in ("all", "D", "ND") else 3.2, 1.1 if key in ("all", "D", "ND") else 1.35, tok,
            text=text, size="small")
for a, b, lab in [("all", "D", f"prevalence {prev:.1%}"), ("all", "ND", f"{1 - prev:.1%}"),
                  ("D", "TP", f"Se {se:.1%}"), ("D", "FN", f"{1 - se:.1%}"),
                  ("ND", "FP", f"{1 - sp:.1%}"), ("ND", "TN", f"Sp {sp:.1%}")]:
    (x0, y0), (x1, y1) = nodes[a][0], nodes[b][0]
    bio.arrow(ax, (x0, y0 - 0.6), (x1, y1 + 0.72), kind="process", color=P.muted())
    bio.label(ax, ((x0 + x1) / 2 + (0.55 if x1 > x0 else -0.55), (y0 + y1) / 2 + 0.05), lab, size="tiny", color=P.muted(),
              ha="left" if x1 > x0 else "right")
bio.label(ax, (8, 0.7), f"positive tests: {TP} + {FP:,} = {TP + FP:,};   PPV = {TP} / {TP + FP:,} = {TP / (TP + FP):.1%};"
          f"   NPV = {TN:,} / {TN + FN:,} = {TN / (TN + FN):.2%}", size="small")
