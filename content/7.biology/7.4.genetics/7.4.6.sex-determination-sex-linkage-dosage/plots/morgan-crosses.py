"""Morgan's reciprocal crosses with the X-linked white gene of Drosophila. A: red-eyed female x white-eyed
male (cross A): all progeny red-eyed. B: white-eyed female x red-eyed male (cross D): red-eyed daughters and
white-eyed sons (criss-cross inheritance). Eggs down the left, sperm across the top."""
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(19.5, 5.3)


def pheno(loci):
    a, b = loci[0]
    sex = "female" if b.startswith("X") and a.startswith("X") else "male"
    red = "+" in a or "+" in b
    return f"{'red' if red else 'white'} {sex}"


cols = {"red female": "receptor", "red male": "drug", "white female": "neutral", "white male": "dna2"}
for k, (mom, dad, title) in enumerate((([("X^{+}", "X^{+}")], [("X^{w}", "Y")], "Cross A: red female x white male"),
                                       ([("X^{w}", "X^{w}")], [("X^{+}", "Y")], "Cross D: white female x red male"))):
    x0 = 2.2 + k * 9.8
    bio.panel(ax, "AB"[k], (x0 - 2.0, 5.1))
    bio.label(ax, (x0 + 2.6, 4.8), title, size="small")
    G.punnett(ax, (x0, 2.9), dad, mom, cell=1.25, phenotype=pheno, colors=cols, titles=("Sperm", "Eggs"))
