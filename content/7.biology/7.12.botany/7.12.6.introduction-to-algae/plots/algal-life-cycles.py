"""The three basic life cycles of algae. Blue sector: diploid (2n) phase; orange sector: haploid (n) phase.
A: zygotic meiosis (Chlamydomonas): the haploid cell is the plant, the zygote is the only diploid cell.
B: gametic meiosis (Fucus): the diploid thallus forms oogonia and antheridia in conceptacles of the
receptacles, and meiosis gives the eggs and sperm directly.
C: sporic meiosis with alternation of generations (kelp, Saccharina): meiosis in unilocular sporangia of the
diploid sporophyte gives zoospores, which grow into microscopic male and female gametophytes."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 13.4)
R = 3.6

def st(t, bold=False):
    return dict(text=t, size="small", bold=bold)

# A: Chlamydomonas
bio.panel(ax, "A", (0.2, 13.2))
bio.label(ax, (6.0, 12.6), "Zygotic meiosis", size="normal", bold=True)
bio.label(ax, (6.0, 11.95), "Chlamydomonas", size="small", italic=True, color=P.muted())
plant.alternation_of_generations(ax, (6.0, 5.6), R, [
    st("Vegetative cell (n)", True), st("Gametes (n)"), st("Zygote (2n)"), st("Resting zygote\n(thick wall)"),
    st("4 haploid cells")], meiosis=3, fertilization=1, gap=0.2,
    arrow_labels=["Mitosis", None, "Wall forms", None, "Growth"])

# B: Fucus
bio.panel(ax, "B", (12.2, 13.2))
bio.label(ax, (18.0, 12.6), "Gametic meiosis", size="normal", bold=True)
bio.label(ax, (18.0, 11.95), "Fucus", size="small", italic=True, color=P.muted())
plant.alternation_of_generations(ax, (18.0, 5.6), R, [
    st("Diploid thallus (2n)", True), st("Receptacle with\nconceptacles"), st("Oogonium,\nantheridium"),
    st("Eggs and sperm (n)"), st("Zygote (2n)")], meiosis=2, fertilization=3, gap=0.2,
    arrow_labels=[None, None, None, None, "Growth"])

# C: kelp
bio.panel(ax, "C", (24.2, 13.2))
bio.label(ax, (30.0, 12.6), "Sporic meiosis", size="normal", bold=True)
bio.label(ax, (30.0, 11.95), "Saccharina (kelp)", size="small", italic=True, color=P.muted())
plant.alternation_of_generations(ax, (30.0, 5.6), R, [
    st("Sporophyte (2n)", True), st("Unilocular\nsporangia"), st("Zoospores (n)"),
    st("Male and female\ngametophytes (n)", True), st("Egg and sperm"), st("Zygote (2n)")],
    meiosis=1, fertilization=4, gap=0.2,
    arrow_labels=[None, None, "Germination", None, None, "Growth"])
