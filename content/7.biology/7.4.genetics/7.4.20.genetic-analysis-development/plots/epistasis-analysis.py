"""Epistasis analysis: the informative double-mutant combinations. Left, a switch (regulatory) pathway in
which a loss-of-function mutation is combined with a gain-of-function mutation: the double mutant takes the
phenotype of the downstream gene. Right, a biosynthetic pathway with two loss-of-function mutations, where
the upstream block determines the phenotype."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17.0, 11.6)
ON, OFF = "positive", "neutral"


def chain(x, y, items, out_on, caption, note=None):
    """items: list of (text, state) with state in {'wt','lof','gof'}; draws A -> B -> output."""
    cx = x
    prev = None
    for text, state in items:
        tok = {"wt": "protein", "lof": "negative", "gof": "highlight"}[state]
        bio.box(ax, (cx, y), 1.5, 0.8, token=tok, text=text, size="normal")
        if prev is not None:
            bio.arrow(ax, (prev + 0.78, y), (cx - 0.78, y), kind="activation")
        if state == "lof":
            bio.label(ax, (cx, y - 0.75), "loss", size="tiny", color=P.edge("negative"), va="top")
        elif state == "gof":
            bio.label(ax, (cx, y - 0.75), "gain", size="tiny", color=P.edge("highlight"), va="top")
        prev = cx
        cx += 2.4
    bio.arrow(ax, (prev + 0.78, y), (cx - 0.5, y), kind="activation")
    bio.box(ax, (cx + 0.55, y), 1.9, 0.8, token=ON if out_on else OFF,
            text="output on" if out_on else "output off", size="small")
    bio.label(ax, (x - 1.5, y), caption, size="small", ha="right", bold=True)
    if note:
        bio.label(ax, (cx + 2.3, y), note, size="small", ha="left", color=P.muted())


bio.label(ax, (2.1, 11.1), "Switch (regulatory) pathway: A acts on B", size="title", ha="left", bold=True)
rows = [
    ("loss of A,\ngain of B", [("A", "lof"), ("B", "gof")], True, "B is epistatic: downstream"),
    ("gain of A,\nloss of B", [("A", "gof"), ("B", "lof")], False, "B is epistatic: downstream"),
    ("loss of A,\nloss of B", [("A", "lof"), ("B", "lof")], False, "no order can be inferred"),
    ("gain of A,\ngain of B", [("A", "gof"), ("B", "gof")], True, "no order can be inferred"),
]
for k, (cap, items, out, note) in enumerate(rows):
    chain(5.0, 9.8 - k * 1.85, items, out, cap, note)

bio.label(ax, (2.1, 2.1), "Biosynthetic pathway: enzyme A then enzyme B", size="title", ha="left", bold=True)
y = 1.25
bio.label(ax, (3.5, y), "loss of A,\nloss of B", size="small", ha="right", bold=True)
boxes = [("substrate", "metabolite"), ("intermediate 1", "metabolite"), ("product", "positive")]
xs = [5.2, 9.0, 12.8]
for k, ((text, tok), cx) in enumerate(zip(boxes, xs)):
    bio.box(ax, (cx, y), 2.6, 0.8, token=tok, text=text, size="small")
for k, (x0, x1, enz, blocked) in enumerate(((xs[0], xs[1], "A", True), (xs[1], xs[2], "B", True))):
    bio.arrow(ax, (x0 + 1.35, y), (x1 - 1.35, y), kind="process")
    mid = (x0 + x1) / 2
    bio.label(ax, (mid, y + 0.5), enz, size="small", italic=True)
    col = P.edge("negative") if k == 0 else P.muted()
    ax.plot([mid - 0.28, mid + 0.28], [y - 0.28, y + 0.28], color=col, lw=2.0, zorder=20)
    ax.plot([mid - 0.28, mid + 0.28], [y + 0.28, y - 0.28], color=col, lw=2.0, zorder=20)
    bio.label(ax, (mid, y - 0.55), "blocked:\nsubstrate accumulates" if k == 0 else "blocked:\nnever reached",
              size="tiny", color=col, va="top")
bio.label(ax, (14.6, y), "the double mutant shows\nthe upstream block", size="small", ha="left", color=P.muted())
