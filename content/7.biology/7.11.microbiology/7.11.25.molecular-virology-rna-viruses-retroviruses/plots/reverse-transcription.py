# Reverse transcription of a retroviral genome: how two template exchanges duplicate u3 and u5 and build
# identical long terminal repeats at both ends of the DNA product.
# 1 initiation from the tRNA primer at the primer-binding site; 2 the first jump, R to r;
# 3 (+) strand synthesis primed from the RNase H-resistant polypurine tract; 4 the second jump through the
# complementary primer-binding sequences, then strand-displacement synthesis to the linear duplex.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16.6, 11.0)
LW = 2.2


def seg(x0, x1, y, tok, text=None, h=0.42, size="tiny"):
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, h, tok, text=text, radius=0.05, size=size, zorder=9)


def rna(x0, x1, y, tok="rna", lw=LW, dashed=False):
    ax.plot([x0, x1], [y, y], color=P.edge(tok), lw=lw, ls="--" if dashed else "-",
            solid_capstyle="round", zorder=6)


def dna(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=P.edge("negative"), lw=LW, solid_capstyle="round", zorder=7)


def step(n, y, text):
    bio.label(ax, (0.55, y), str(n), size="normal", bold=True)
    bio.label(ax, (1.1, y), text, size="tiny", color=P.muted(), ha="left")


def trna(at):
    bio.protein(ax, at, 0.5, 0.36, "trna", text="tRNA", size="tiny", zorder=12)


X0, X1 = 3.4, 14.6

# --- 1  initiation -----------------------------------------------------------------------------------------
y = 10.0
step(1, y + 0.75, "the tRNA primer sits at the primer-binding site; (−) strand DNA stops after ~100 nt,\nand RNase H removes the RNA it has copied")
rna(X0, X1, y)
for x0, x1, t in ((X0, X0 + 0.7, "r"), (X0 + 0.7, X0 + 1.5, "u5"), (X0 + 1.5, X0 + 2.2, "pbs"),
                  (X1 - 2.2, X1 - 1.5, "ppt"), (X1 - 1.5, X1 - 0.7, "u3"), (X1 - 0.7, X1, "r")):
    seg(x0, x1, y, "highlight", t)
bio.label(ax, (X0 - 0.3, y), "5′", size="tiny")
bio.label(ax, (X1 + 0.3, y), "3′", size="tiny")
trna((X0 + 2.6, y + 0.5))
dna(X0, X0 + 2.0, y + 0.5)
bio.label(ax, (X0 + 1.4, y - 0.5), "(−) strong-stop DNA", size="tiny", color=P.edge("negative"))

# --- 2  first jump -----------------------------------------------------------------------------------------
y = 7.9
step(2, y + 0.75, "first jump: R in the new DNA pairs with r at the 3′ end of a genome,\nand synthesis continues the length of the template")
rna(X0 + 1.4, X1, y)
seg(X1 - 0.7, X1, y, "highlight", "r")
seg(X1 - 1.5, X1 - 0.7, y, "highlight", "u3")
seg(X1 - 2.2, X1 - 1.5, y, "highlight", "ppt")
dna(X1 - 0.7, X1, y + 0.5)
trna((X1 + 0.6, y + 0.5))
bio.arrow(ax, (X0 + 2.2, y + 0.9), (X1 - 0.9, y + 0.9), kind="process", color=P.muted(), bend=-0.08)
bio.label(ax, (11.6, y + 1.3), "the 5′ copy anneals to the 3′ end", size="tiny", color=P.muted())
dna(X1 - 4.5, X1 - 0.7, y + 0.5)
bio.arrow(ax, (X1 - 4.6, y + 0.5), (X1 - 6.0, y + 0.5), kind="process", color=P.edge("negative"))

# --- 3  (+) strand priming ---------------------------------------------------------------------------------
y = 5.8
step(3, y + 0.75, "the polypurine tract resists RNase H and primes (+) strand DNA, which copies\nthe first 18 nucleotides of the tRNA: (+) strong-stop DNA")
dna(X0, X1, y)
for x0, x1, t in ((X0, X0 + 0.7, "U3"), (X0 + 0.7, X0 + 1.5, "R"), (X0 + 1.5, X0 + 2.2, "U5"),
                  (X1 - 0.8, X1, "PBS")):
    seg(x0, x1, y, "positive", t)
rna(X1 - 2.0, X1 - 0.8, y + 0.42, "rna", lw=2.6)
bio.label(ax, (X1 - 1.4, y + 0.78), "ppt", size="tiny", color=P.edge("rna"))
dna(X1 - 3.4, X1 - 0.8, y + 0.42)
bio.arrow(ax, (X1 - 3.5, y + 0.42), (X1 - 4.8, y + 0.42), kind="process", color=P.edge("negative"))

# --- 4  second jump and the product --------------------------------------------------------------------------
y = 3.5
step(4, y + 0.95, "second jump: the complementary primer-binding sequences pair, and strand-displacement\nsynthesis completes both strands")
dna(X0, X1, y + 0.25)
dna(X0, X1, y - 0.25)
for x0, x1, t in ((X0, X0 + 0.7, "U3"), (X0 + 0.7, X0 + 1.5, "R"), (X0 + 1.5, X0 + 2.2, "U5"),
                  (X1 - 2.2, X1 - 1.5, "U3"), (X1 - 1.5, X1 - 0.7, "R"), (X1 - 0.7, X1, "U5")):
    seg(x0, x1, y, "positive", t, h=0.78)
for a, b in ((X0, X0 + 2.2), (X1 - 2.2, X1)):
    ax.plot([a, b], [y - 0.62, y - 0.62], color=P.edge("highlight"), lw=3.0, solid_capstyle="round", zorder=9)
    bio.label(ax, ((a + b) / 2, y - 0.95), "LTR", size="tiny", bold=True, color=P.edge("highlight"))
bio.label(ax, (8.6, y - 1.5), "identical at both ends, although u3 and u5 occur once each in the RNA",
          size="tiny", color=P.muted())

bio.label(ax, (8.3, 1.3), "The left LTR supplies the promoter and enhancer for host RNA polymerase II, the right one the\npoly(A) signal; integrase will remove two nucleotides from each 3′ end of this duplex (§25.6.2)",
          size="small", color=P.muted())
