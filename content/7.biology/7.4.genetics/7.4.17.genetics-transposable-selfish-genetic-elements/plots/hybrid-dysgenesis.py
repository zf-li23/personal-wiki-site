"""P-M hybrid dysgenesis in Drosophila: the outcome of the four crosses between P strains (carrying P
elements and maternally transmitted piRNAs against them) and M strains (no P elements). Only M females
crossed with P males give dysgenic, sterile offspring."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20, 8.2)
w, h = 4.2, 2.3
x0, y0 = 6.2, 6.2
bio.label(ax, (x0 + w, y0 + 1.4), "Male parent", size="small", color=P.muted())
bio.label(ax, (x0 - 2.7, y0 - h), "Female parent", size="small", color=P.muted(), rotation=90)
for j, s in enumerate(("M strain", "P strain")):
    bio.label(ax, (x0 + (j + 0.5) * w, y0 + 0.7), s, size="small")
    bio.icon(ax, "phylopic/drosophila", at=(x0 + (j + 0.5) * w + 1.55, y0 + 0.7), height=0.7,
             color="neutral" if j == 0 else "highlight")
for i, s in enumerate(("M strain", "P strain")):
    bio.label(ax, (x0 - 0.9, y0 - (i + 0.5) * h + 0.3), s, size="small")
    bio.icon(ax, "phylopic/drosophila", at=(x0 - 0.9, y0 - (i + 0.5) * h - 0.45), height=0.7,
             color="neutral" if i == 0 else "highlight")
cells = {(0, 0): ("normal", "no P elements", "positive"),
         (0, 1): ("dysgenic", "P transposes in germline:\nsterility, mutations, breaks", "negative"),
         (1, 0): ("normal", "maternal piRNAs present,\nno P from father", "positive"),
         (1, 1): ("normal", "P elements repressed by\nmaternal piRNAs", "positive")}
for (i, j), (a, b, tok) in cells.items():
    cx, cy = x0 + (j + 0.5) * w, y0 - (i + 0.5) * h
    bio.box(ax, (cx, cy), w - 0.25, h - 0.25, token=tok)
    bio.label(ax, (cx, cy + 0.5), a, size="normal", bold=True, color=P.on_fill(), zorder=12)
    bio.label(ax, (cx, cy - 0.35), b, size="tiny", color=P.on_fill(), zorder=12)
bio.label(ax, (15.4, 6.0), "Cytotype is maternal:", size="small", ha="left")
for k, t in enumerate(("P cytotype: piRNAs against P", "are deposited in the egg", "and silence P elements in", "the germline of the offspring.",
                       "", "M cytotype: no piRNAs;", "paternal P elements are", "unrestrained in the progeny.")):
    bio.label(ax, (15.4, 5.4 - 0.45 * k), t, size="tiny", ha="left", color=P.muted())
