# Promoters of the three nuclear RNA polymerases drawn to scale (positions relative to the start site +1).
# A: class II core promoter elements with their consensus sequences (IUPAC codes, nontemplate strand):
# BREu -38..-32, TATA -31..-24, BREd -23..-17, Inr -2..+4, MTE +18..+29, DPE +28..+32. No real promoter has all.
# B: class I (human rRNA) promoter: upstream control element -156..-107 and core element -45..+20.
# C: class III promoters: type 1 (5S rRNA; box A +50..+64, IE +67..+72, box C +80..+90), type 2 (tRNA; box A
# about +8..+19, box B about +52..+62) and type 3 (U6 snRNA; DSE about -245..-215, PSE -65..-48, TATA -31..-24).
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20.0, 17.0)


def axis_line(y, x0, x1, lo, hi, scale, ticks, label_ticks=True):
    """A DNA line from position lo to hi; returns a function mapping position to canvas x."""
    def X(p):
        return x0 + (p - lo) * scale
    ax.plot([X(lo), X(hi)], [y, y], color=P.ink(), lw=1.6, solid_capstyle="round", zorder=5)
    for t in ticks:
        ax.plot([X(t), X(t)], [y - 0.08, y - 0.2], color=P.muted(), lw=0.8)
        if label_ticks:
            bio.label(ax, (X(t), y - 0.42), f"{t:+d}".replace("-", "−") if t else "+1", size="tiny", color=P.muted())
    return X


def element(X, y, a, b, token, name, seq=None, h=0.46, row=0, dx=0.0):
    x0, x1 = X(a), X(b + 1)
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, h, token, None, radius=0.06, zorder=8)
    ty = y + h / 2 + 0.28 + 0.42 * row
    if row:
        ax.plot([(x0 + x1) / 2] * 2, [y + h / 2, ty - 0.18], color=P.muted(), lw=0.6)
    bio.label(ax, ((x0 + x1) / 2 + dx, ty), name, size="small", bold=True)
    if seq:
        bio.label(ax, ((x0 + x1) / 2, y - h / 2 - 0.85 - 0.38 * row), seq, size="tiny", color=P.muted())


def start(X, y, h=0.9, length=1.1):
    x = X(1)
    ax.plot([x, x, x + length], [y, y + h, y + h], color=P.ink(), lw=1.6, solid_joinstyle="round", zorder=9)
    bio.arrow(ax, (x + length - 0.3, y + h), (x + length + 0.05, y + h), kind="process", head=0.22)


# ---- A: class II core promoter
bio.panel(ax, "A", (0.1, 16.9))
bio.label(ax, (0.6, 16.55), "Class II core promoter (Pol II)", size="normal", bold=True, ha="left")
yA = 13.6
XA = axis_line(yA, 1.6, 0, -45, 40, 0.205, [-40, -30, -20, -10, 0, 10, 20, 30, 40], label_ticks=False)
for t in [-40, -30, -20, -10, 10, 20, 30, 40]:
    bio.label(ax, (XA(t), yA - 0.42), f"{t:+d}".replace("-", "−"), size="tiny", color=P.muted())
bio.label(ax, (XA(1), yA - 0.42), "+1", size="tiny", color=P.ink(), bold=True)
element(XA, yA, -38, -32, "antibody", "BREu", "SSRCGCC", row=1)
element(XA, yA, -31, -24, "highlight", "TATA", "TATAWAWR")
element(XA, yA, -23, -17, "antibody", "BREd", "RTDKKKK", row=1)
element(XA, yA, -2, 4, "positive", "Inr", "YYANWYY", dx=-0.75)
element(XA, yA, 18, 27, "receptor", "MTE", "CSARCSSAACGS", row=1)
element(XA, yA, 28, 32, "enzyme", "DPE", "RGWYV")
start(XA, yA + 0.25, h=1.55, length=1.4)
for a_, b_, txt in [(-38, -16, "TBP, TFIIB"), (-2, 33, "TFIID (TAF1, TAF2, TAF6, TAF9)")]:
    yy = yA + 2.15
    ax.plot([XA(a_), XA(a_), XA(b_), XA(b_)], [yy - 0.15, yy, yy, yy - 0.15], color=P.muted(), lw=0.8)
    bio.label(ax, ((XA(a_) + XA(b_)) / 2, yy + 0.3), txt, size="tiny", color=P.muted())
bio.label(ax, (19.4, yA - 2.55), "W = A/T   R = A/G   Y = C/T   S = C/G   K = G/T   D = A/G/T   V = A/C/G   N = any",
          size="tiny", color=P.muted(), ha="right")

# ---- B: class I promoter
bio.panel(ax, "B", (0.1, 10.9))
bio.label(ax, (0.6, 10.55), "Class I promoter (Pol I, human rRNA)", size="normal", bold=True, ha="left")
yB = 8.6
XB = axis_line(yB, 1.6, 0, -170, 40, 0.083, [-150, -100, -50, 0], label_ticks=False)
for t in [-150, -100, -50]:
    bio.label(ax, (XB(t), yB - 0.42), f"{t:+d}".replace("-", "−"), size="tiny", color=P.muted())
bio.label(ax, (XB(1), yB - 0.42), "+1", size="tiny", color=P.ink(), bold=True)
element(XB, yB, -156, -107, "drug", "upstream control element")
element(XB, yB, -45, 20, "protein", "core element")
start(XB, yB + 0.25, h=1.0, length=0.9)
bio.label(ax, (XB(-76), yB + 0.95), "spacing matters", size="tiny", color=P.muted())

# ---- C: class III promoters
bio.panel(ax, "C", (0.1, 6.4))
bio.label(ax, (0.6, 6.05), "Class III promoters (Pol III)", size="normal", bold=True, ha="left")
rows = [
    (4.55, "type 1: 5S rRNA", -10, 125, [(50, 64, "metabolite", "A"), (67, 72, "carbohydrate", "IE"), (80, 90, "receptor", "C")], (1, 120)),
    (2.75, "type 2: tRNA", -10, 125, [(8, 19, "metabolite", "A"), (52, 62, "channel", "B")], (1, 73)),
]
for y, name, lo, hi, els, gene in rows:
    X = axis_line(y, 4.6, 0, lo, hi, 0.075, [], label_ticks=False)
    bio.label(ax, (4.3, y), name, size="small", ha="right")
    bio.box(ax, ((X(gene[0]) + X(gene[1])) / 2, y), X(gene[1]) - X(gene[0]), 0.2, "rna", None, radius=0.05, zorder=6)
    for a, b, tok, lab in els:
        element(X, y, a, b, tok, lab, h=0.42)
    start(X, y + 0.21, h=0.6, length=0.6)
    bio.label(ax, (X(gene[1]) + 0.1, y + 0.32), "TTTT", size="tiny", color=P.muted(), ha="left")

y = 0.95
X = axis_line(y, 13.4 - 250 * 0.0215 - 0.2, 0, -260, 115, 0.0215, [], label_ticks=False)
bio.label(ax, (X(-260) - 0.3, y), "type 3: U6 snRNA", size="small", ha="right")
bio.box(ax, ((X(1) + X(107)) / 2, y), X(107) - X(1), 0.2, "rna", None, radius=0.05, zorder=6)
element(X, y, -245, -215, "drug", "DSE", h=0.42)
element(X, y, -65, -48, "antibody", "PSE", h=0.42)
element(X, y, -31, -24, "highlight", "TATA", h=0.42, row=1)
start(X, y + 0.21, h=0.6, length=0.6)
bio.label(ax, (X(107) + 0.1, y + 0.32), "TTTT", size="tiny", color=P.muted(), ha="left")
for t in [-200, -100, 100]:
    ax.plot([X(t), X(t)], [y - 0.08, y - 0.2], color=P.muted(), lw=0.8)
    bio.label(ax, (X(t), y - 0.42), f"{t:+d}".replace("-", "−"), size="tiny", color=P.muted())
bio.label(ax, (19.6, 4.55), "internal\npromoters", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (19.6, 0.95), "upstream\npromoter", size="tiny", color=P.muted(), ha="right")
