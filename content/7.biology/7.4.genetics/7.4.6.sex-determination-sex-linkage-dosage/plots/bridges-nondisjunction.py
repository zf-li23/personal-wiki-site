"""Bridges' proof of the chromosome theory. A: X-chromosome nondisjunction in meiosis I of a white-eyed
female gives XX and O eggs (red: maternal homologue, blue: paternal homologue, both carrying w). B: the
exceptional eggs fertilized by sperm of a red-eyed male: XXY white-eyed females and XO red-eyed (sterile)
males survive; XXX and OY zygotes die. C: in an XXY female, the two X chromosomes usually disjoin from
each other (X and XY eggs), but sometimes X and Y pair and the two X chromosomes go to the same pole
(XX and Y eggs): secondary nondisjunction."""
import wikibio as bio
from wikibio import cytogenetics as C

fig, ax = bio.canvas(26.0, 8.0)
bio.panel(ax, "A", (0.2, 7.8))
bio.label(ax, (3.9, 7.45), "Primary nondisjunction in an XX female", size="small")
C.meiosis_lineage(ax, (1.3, 3.8), [("receptor", "dna")], nondisjunction=("I", 0), names=[("X^{w}", "X^{w}")])
bio.panel(ax, "B", (9.0, 7.8))
bio.label(ax, (12.1, 7.45), "Exceptional eggs x normal sperm", size="small")
out = {(0, 0): ("$X^{w}X^{w}X^{+}$\ndies", "negative"), (0, 1): ("$X^{w}X^{w}Y$\nwhite female", "highlight"),
       (1, 0): ("$X^{+}O$\nred male, sterile", "highlight"), (1, 1): ("OY\ndies", "negative")}
C.gamete_table(ax, (11.0, 5.6), ["$X^{w}X^{w}$", "O"], ["$X^{+}$", "Y"], lambda i, j: out[(i, j)], cell=(2.2, 1.1),
               row_title="Egg", col_title="Sperm")
bio.panel(ax, "C", (17.0, 7.8))
bio.label(ax, (21.4, 7.45), "Segregation in an XXY female", size="small")
P = bio.P
rows = [("X and X pair, Y moves at random (more frequent)", "eggs  $X^{w}$  and  $X^{w}Y$", "neutral"),
        ("X and Y pair, the unpaired X joins the paired X (less frequent)", "eggs  $X^{w}X^{w}$  and  Y", "highlight")]
for i, (title, eggs, tok) in enumerate(rows):
    y = 6.2 - i * 2.6
    bio.label(ax, (17.6, y), title, size="small", ha="left")
    bio.box(ax, (21.4, y - 1.0), 6.6, 0.75, token=tok)
    bio.label(ax, (21.4, y - 1.0), eggs, size="small", color=P.on_fill())
bio.label(ax, (21.3, 0.9), "XX and Y eggs give XXY white females and XY red males\namong the progeny of a red-eyed male",
          size="tiny", color=P.muted())
