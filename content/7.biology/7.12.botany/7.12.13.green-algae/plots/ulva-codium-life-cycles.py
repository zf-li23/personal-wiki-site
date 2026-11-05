"""Two life cycles in the Ulvophyceae. Blue sector: diploid (2n); orange sector: haploid (n).
A: Ulva, isomorphic alternation of generations (sporic meiosis): the sporophyte forms quadriflagellate
zoospores by meiosis, which grow into a gametophyte of the same form; biflagellate gametes of two mating
types fuse, and the zygote grows directly into a new sporophyte.
B: Codium, gametic meiosis: the diploid siphonous thallus forms gametangia on the utricles; meiosis gives
large female and small male biflagellate gametes, the only haploid cells; the zygote germinates at once."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 13.6)
R = 3.7


def st(t, bold=False):
    return dict(text=t, size="small", bold=bold)


bio.panel(ax, "A", (0.2, 13.4))
bio.label(ax, (7.4, 12.8), "Isomorphic alternation of generations", size="normal", bold=True)
bio.label(ax, (7.4, 12.15), "Ulva", size="small", italic=True, color=P.muted())
plant.alternation_of_generations(ax, (7.4, 5.7), R, [
    st("Sporophyte (2n)\nblade, 2 cell layers", True), st("Zoosporangia"), st("Zoospores (n)\n4 flagella"),
    st("Gametophyte (n)\nsame form", True), st("Gametes (+ / −)\n2 flagella"), st("Zygote (2n)")],
    meiosis=1, fertilization=4, gap=0.2,
    arrow_labels=[None, None, "Settle,\ngerminate", "Gametangia", None, "No rest:\ngrowth"])

bio.panel(ax, "B", (15.2, 13.4))
bio.label(ax, (22.4, 12.8), "Gametic meiosis", size="normal", bold=True)
bio.label(ax, (22.4, 12.15), "Codium", size="small", italic=True, color=P.muted())
plant.alternation_of_generations(ax, (22.4, 5.7), R, [
    st("Diploid thallus (2n)\nsiphonous, utricles", True), st("Female and male\ngametangia"),
    st("Large ♀ and small ♂\ngametes (n)"), st("Zygote (2n)")],
    meiosis=1, fertilization=2, gap=0.2,
    arrow_labels=[None, None, None, "Germinates\nat once"])
