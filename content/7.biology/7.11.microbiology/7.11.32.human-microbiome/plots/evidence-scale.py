"""A: why an association between microbiota composition and disease is weak evidence of causation, and what
has to be added. B: the strength of the evidence behind claims discussed in this chapter, on the three-level
scale used in the text (association / animal experiment / randomized trial in humans)."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 11)

# ---------------- A: causal diagram
bio.panel(ax, "A", (0.2, 10.8))
bio.box(ax, (3.4, 8.4), 4.0, 1.1, "bacterium", "microbiota", size="small")
bio.box(ax, (9.6, 8.4), 3.6, 1.1, "negative", "disease", size="small")
bio.arrow(ax, (5.5, 8.4), (7.7, 8.4), kind="process", head=0.2)
bio.label(ax, (6.6, 8.9), "claimed cause", size="tiny", color=P.muted())
bio.arrow(ax, (7.7, 7.9), (5.5, 7.9), kind="process", head=0.2, dashed=True)
bio.label(ax, (6.6, 7.3), "reverse causation:\ninflammation, transit time,\nappetite change", size="tiny", color=P.muted())
bio.box(ax, (6.5, 4.4), 5.4, 1.4, "neutral", "confounders: diet, drugs,\nage, geography, stool consistency", size="small")
bio.arrow(ax, (5.1, 5.1), (3.5, 7.8), kind="process", head=0.18)
bio.arrow(ax, (7.9, 5.1), (9.5, 7.8), kind="process", head=0.18)
bio.label(ax, (6.5, 2.9), "a difference between patients and controls\nis compatible with all three arrows",
          size="tiny", color=P.muted())

bio.panel(ax, "B", (14.4, 10.8))
rows = [
    ("recurrent CDI after antibiotics, cured by FMT", 3, False),
    ("probiotics in acute childhood diarrhea", 3, False),
    ("fiber → SCFAs → regulatory T cells", 2, False),
    ("gut community and adiposity (twin transfer)", 2, False),
    ("colonization resistance", 2, False),
    ("gut–brain axis in rodents", 2, False),
    ("IBD and reduced butyrate producers", 1, False),
    ("obesity and Bacillota : Bacteroidota ratio", 1, False),
    ("human behavior and gut composition", 1, False),
]
labels = {1: "association", 2: "animal experiment", 3: "randomized trial"}
toks = {1: "neutral", 2: "carbohydrate", 3: "positive"}
x0, w = 16.4, 2.5
y = 9.2
for text, level, italic in rows:
    for k in (1, 2, 3):
        tok = toks[level] if k <= level else None
        xs = x0 + (k - 1) * (w + 0.15)
        if tok:
            bio.shape(ax, [(xs, y - 0.3), (xs + w, y - 0.3), (xs + w, y + 0.3), (xs, y + 0.3)], token=tok, lw=0.8)
        else:
            bio.shape(ax, [(xs, y - 0.3), (xs + w, y - 0.3), (xs + w, y + 0.3), (xs, y + 0.3)],
                      token="neutral", lw=0.6, fill=False)
    bio.label(ax, (x0 - 0.3, y), text, size="tiny", ha="right", italic=italic)
    y -= 0.95
for k in (1, 2, 3):
    bio.label(ax, (x0 + (k - 1) * (w + 0.15) + w / 2, 9.9), labels[k], size="tiny", color=P.muted())
bio.label(ax, (x0 + 1.5 * w, 0.8), "filled bars: the levels of evidence that support the claim",
          size="tiny", color=P.muted())
