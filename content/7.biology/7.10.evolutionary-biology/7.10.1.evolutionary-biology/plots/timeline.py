"""A timeline of evolutionary thought, 1650-2010: the main works and discoveries in four eras
(before Darwin; Darwin and the eclipse of natural selection; the evolutionary synthesis; the
molecular and genomic era). Dates are those of publication."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 10.4)



def X(year):
    """Piecewise-linear time axis: 1640-1850 compressed, 1850-2020 expanded."""
    if year <= 1850:
        return 1.0 + (year - 1640) / 210 * 9.0
    return 10.0 + (year - 1850) / 170 * 19.0


AXIS = 5.2
ERAS = [(1640, 1859, "Before Darwin", "neutral"), (1859, 1918, "Darwin and the eclipse of selection", "highlight"),
        (1918, 1953, "Evolutionary synthesis", "positive"), (1953, 2020, "Molecular and genomic era", "dna")]
for a, b, name, tok in ERAS:
    bio.shape(ax, [(X(a), AXIS - 0.22), (X(b), AXIS - 0.22), (X(b), AXIS + 0.22), (X(a), AXIS + 0.22)], tok, lw=0.6)
    bio.label(ax, ((X(a) + X(b)) / 2, AXIS), name, size="tiny", bold=True, color=P.on_fill())

for year in (1650, 1700, 1750, 1800, 1850, 1875, 1900, 1925, 1950, 1975, 2000):
    ax.plot([X(year), X(year)], [AXIS - 0.36, AXIS - 0.22], color=P.muted(), lw=0.7)
    bio.label(ax, (X(year), AXIS - 0.6), str(year), size="tiny", color=P.muted())

# (year, text, level above the axis, alignment of the label)
EVENTS = [
    (1650, "Ussher dates the\nCreation to 4004 BC", -1, "center"),
    (1735, "Linnaeus,\nSystema Naturae", 1, "center"),
    (1788, "Hutton: steady\ngeological cycles", -1, "right"),
    (1809, "Lamarck, Philosophie\nzoologique", 2, "center"),
    (1812, "Cuvier: extinction,\ncatastrophes", -2, "center"),
    (1830, "Lyell, Principles\nof Geology", -1, "left"),
    (1859, "Darwin, On the\nOrigin of Species", 3, "center"),
    (1866, "Mendel's paper\non pea hybrids", 2, "left"),
    (1900, "Mendel rediscovered;\nmutationism", 1, "right"),
    (1918, "Fisher:\nMendelian variance", 2, "center"),
    (1931, "Wright, Fisher,\nHaldane: theory", 3, "left"),
    (1937, "Dobzhansky, Genetics and\nthe Origin of Species", 2, "left"),
    (1953, "Structure\nof DNA", 1, "center"),
    (1966, "Electrophoresis 1966;\nneutral theory 1968", 3, "center"),
    (1977, "Woese and Fox:\nrRNA tree", 1, "left"),
    (2001, "Draft human\ngenome", 2, "center"),
]
for year, text, level, ha in EVENTS:
    x = X(year)
    side = AXIS + 0.22 if level > 0 else AXIS - 0.22
    y = side + 1.2 * level + (0 if level > 0 else -0.5)
    ax.plot([x, x], [side, y + (-0.05 if level > 0 else 0.05)], color=P.muted(), lw=0.7)
    ax.plot([x], [side], "o", ms=3, color=P.ink())
    bio.label(ax, (x + {"left": -0.08, "right": 0.08}.get(ha, 0), y + (0.02 if level > 0 else -0.02)), text, size="tiny",
              va="bottom" if level > 0 else "top", ha=ha)

# the reception in China and the Soviet Union, below the axis
CHINA = [(1898, "Yan Fu, Tianyan lun\n(after Huxley)"), (1920, "Ma Junwu: complete\nChinese Origin"),
         (1948, "Lysenko: genetics\nbanned in the USSR"), (1956, "Qingdao symposium:\ngenetics restored in China")]
for k, (year, text) in enumerate(CHINA):
    x = X(year)
    y = AXIS - 1.3 - 1.25 * (k % 2) - 0.5
    ax.plot([x, x], [AXIS - 0.22, y + 0.05], color=P.muted(), lw=0.7, ls=(0, (2, 2)))
    bio.label(ax, (x, y), text, size="tiny", va="top", color=P.muted())
bio.label(ax, (X(1862), AXIS - 3.5), "Reception in China\nand the Soviet Union", size="tiny", ha="left",
          color=P.muted(), italic=True)
