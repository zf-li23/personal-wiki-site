# Progressive alignment of the MCM family. 15 sequences (human MCM2-7, MCM6 of eight further eukaryotes, the
# single MCM of the archaeon Saccharolobus solfataricus) were aligned with FAMSA; the guide tree on the left
# is the UPGMA tree of the pairwise distances 1 - identity computed from that alignment, and the order in
# which the progressive method merges profiles follows it from the tips to the root. Right: 40 columns
# around the Walker A motif (GDPxxxKS, boxed), residues coloured where they agree with the column consensus
# in at least half of the sequences. MCM6 proteins share S instead of G in GDP(G/S); the guide tree groups
# the paralogs by similarity only and is not a reliable phylogeny (the archaeal MCM joins MCM5).
import wikibio as bio
from wikibio import sequence as seqmod

P = bio.P
NEWICK = ("((((MCM7_HUMAN:0.3313,MCM4_HUMAN:0.3313):0.0076,MCM3_HUMAN:0.3389):0.0041,((MCM_SACS2:0.3287,"
          "MCM5_HUMAN:0.3287):0.0111,MCM2_HUMAN:0.3398):0.0031):0.0041,((MCM6_DICDI:0.2686,(MCM6_ORYSI:0.1335,"
          "MCM6_ARATH:0.1335):0.1351):0.0073,((MCM6_YEAST:0.2220,MCM6_SCHPO:0.2220):0.0474,((MCM6_ANOGA:0.1122,"
          "MCM6_DROME:0.1122):0.0650,(MCM6_MOUSE:0.0207,MCM6_HUMAN:0.0207):0.1565):0.0921):0.0066):0.0711)")
ALN = {
    "MCM6_HUMAN": "LRGDINVCIVGDPSTAKSQFLKHVEEFSPRAVYTSGKASS", "MCM6_MOUSE": "LRGDINVCIVGDPSTAKSQFLKHVDEFSPRAVYTSGKASS",
    "MCM6_DROME": "LRGDINVCIVGDPSTAKSQFLKQVSDFSPRAIYTSGKASS", "MCM6_ANOGA": "LRGDINVCIVGDPSTAKSQFLKQVSDFSPRAVYTSGKASS",
    "MCM6_ARATH": "LRGDINVCIVGDPSCAKSQFLKYTAGIVPRSVYTSGKSSS", "MCM6_ORYSI": "LRGDINVCIVGDPSCAKSQFLKYTAGIVPRSVYTSGKSSS",
    "MCM6_DICDI": "LRGDINVCIVGDPSTSKSTFLKYLVSFLPRTVYTSGKASS", "MCM6_SCHPO": "LRGDLNICIVGDPSTSKSQFLKYVCNFLPRAIYTSGKASS",
    "MCM6_YEAST": "LRGDINICVVGDPSTSKSQFLKYVVGFAPRSVYTSGKASS", "MCM2_HUMAN": "VRGDINVLLCGDPGTAKSQFLKYIEKVSSRAIFTTGQGAS",
    "MCM3_HUMAN": "IRGDINILLIGDPSVAKSQLLRYVLCTAPRAIPTTGRGSS", "MCM4_HUMAN": "FRAEINILLCGDPGTSKSQLLQYVYNLVPRGQYTSGKGSS",
    "MCM5_HUMAN": "RRGDINLLMLGDPGTAKSQLLKFVEKCSPIGVYTSGKGSS", "MCM7_HUMAN": "IRGNINICLMGDPGVAKSQLLSYIDRLAPRSQYTTGRGSS",
    "MCM_SACS2": "IRGDIHILIIGDPGTAKSQMLQFISRVAPRAVYTTGKGST"}


def parse(s):
    """Minimal Newick parser: returns nested (children, length) / (name, length) tuples."""
    pos = 0

    def node():
        nonlocal pos
        if s[pos] == "(":
            pos += 1
            kids = [node()]
            while s[pos] == ",":
                pos += 1
                kids.append(node())
            pos += 1
            name = None
        else:
            j = pos
            while s[pos] not in ":,)":
                pos += 1
            name, kids = s[j:pos], None
        ln = 0.0
        if pos < len(s) and s[pos] == ":":
            j = pos + 1
            pos = j
            while pos < len(s) and s[pos] not in ",)":
                pos += 1
            ln = float(s[j:pos])
        return (name, kids, ln)
    return node()


tree = parse(NEWICK)
leaves = []


def collect(n):
    if n[1] is None:
        leaves.append(n[0])
    else:
        for k in n[1]:
            collect(k)


collect(tree)
fig, ax = bio.canvas(26.0, 10.6)
ch, cw = 0.5, 0.36
ytop, xa = 9.0, 11.6
row_y = {nm: ytop - ch * (r + 0.5) for r, nm in enumerate(leaves)}
scale = 7.6 / 0.42


def draw(n, x):
    name, kids, ln = n
    x1 = x + ln * scale
    if kids is None:
        y = row_y[name]
    else:
        ys = [draw(k, x1) for k in kids]
        ax.plot([x1, x1], [min(ys), max(ys)], color=P.ink(), lw=0.9)
        y = (min(ys) + max(ys)) / 2
    ax.plot([x, x1], [y, y], color=P.ink(), lw=0.9)
    if kids is None:
        tok = "protein" if name.startswith("MCM6") else ("negative" if "SACS2" in name else "dna")
        bio.label(ax, (x1 + 0.15, y), name.replace("_", " "), size="tiny", ha="left", color=P.edge(tok))
    return y


draw(tree, 0.4)
seqmod.alignment(ax, [ALN[nm] for nm in leaves], at=(xa, ytop), cell=(cw, ch), color_by="identity",
                 consensus=False, conservation=False, ruler=False, size="tiny", highlight=[(10, 17, "Walker A")])
bio.scale_bar(ax, (0.4, 0.6), 0.1 * scale, "0.1 (1 - identity)", size="tiny")
