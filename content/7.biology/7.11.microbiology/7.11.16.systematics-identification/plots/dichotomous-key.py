# A dichotomous key for common bacterial causes of urinary tract infection, starting from an isolate
# on a plate. Each couplet is one test with two outcomes; the leaves are presumptive identifications that
# are then confirmed (for example by MALDI-TOF or a test strip). Gram-positive cocci: catalase separates
# enterococci (negative) from staphylococci (positive), coagulase separates S. aureus from coagulase-negative
# staphylococci (S. saprophyticus in young women). Gram-negative rods: oxidase-positive Pseudomonas
# aeruginosa; among oxidase-negative rods (Enterobacterales), lactose fermenters (E. coli, Klebsiella) and
# non-fermenters (Proteus, urease-positive and swarming).
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 11.6)


def test(xy, text, w=4.4):
    bio.box(ax, xy, w, 1.0, "neutral", text, size="small")


def leaf(xy, name, note=None, w=4.6):
    bio.box(ax, xy, w, 1.05 if note is None else 1.4, "bacterium")
    if note is None:
        bio.label(ax, xy, name, size="small", italic=True, color=P.on_fill())
    else:
        bio.label(ax, (xy[0], xy[1] + 0.25), name, size="small", italic=True, color=P.on_fill())
        bio.label(ax, (xy[0], xy[1] - 0.3), note, size="tiny", color=P.on_fill())


def branch(a, b, text, side="left"):
    bio.arrow(ax, a, b, kind="process", lw=1.0)
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    off = -0.35 if side == "left" else 0.35
    bio.label(ax, (mx + off, my + 0.15), text, size="tiny", color=P.muted(), ha="right" if side == "left" else "left")


test((13, 10.6), "Isolate from urine: Gram stain", w=6.4)
test((6.5, 8.0), "Catalase")
test((19.5, 8.0), "Oxidase")
branch((11.5, 10.1), (7.5, 8.5), "Gram-positive cocci")
branch((14.5, 10.1), (18.5, 8.5), "Gram-negative rods", side="right")

test((9.4, 5.4), "Coagulase")
leaf((3.0, 5.4), "Enterococcus", r"e.g. $\it{E.\ faecalis}$", w=4.0)
branch((5.6, 7.5), (3.6, 6.1), "negative")
branch((7.4, 7.5), (8.9, 5.9), "positive", side="right")
leaf((6.6, 2.6), "Staphylococcus aureus", w=5.0)
leaf((12.4, 2.6), "Staphylococcus", r"coagulase-negative, e.g. $\it{S.\ saprophyticus}$", w=5.4)
branch((8.8, 4.9), (7.2, 3.1), "positive")
branch((10.0, 4.9), (11.8, 3.3), "negative", side="right")

leaf((23.1, 5.4), "Pseudomonas aeruginosa", w=5.0)
test((16.6, 5.4), "Lactose fermentation")
branch((20.4, 7.5), (22.4, 5.95), "positive", side="right")
branch((18.6, 7.5), (17.2, 5.9), "negative")
leaf((17.8, 2.6), "Proteus", "urease +, swarming", w=4.0)
leaf((23.0, 2.6), "Escherichia coli", r"or another coliform ($\it{Klebsiella}$)", w=5.2)
branch((16.9, 4.9), (17.6, 3.3), "negative")
branch((17.9, 4.9), (21.8, 3.2), "positive", side="right")
bio.label(ax, (13, 0.6), "Presumptive identifications (green) are confirmed by further tests before they are reported.",
          size="tiny", color=P.muted())
