# SBOL Visual 3: an IPTG-inducible GFP reporter (lac repressor / operator), a glyph key, and a pUC19 plasmid map
import wikibio as bio
from wikibio import genetics as G

# Figure 1: genetic construct and glyph key
fig, ax = bio.canvas(16, 7.6)
y = 4.3
parts = G.construct(ax, 0.9, y, [
    ("promoter", "$P_{\\mathrm{lacIq}}$"),
    ("rbs", "RBS"),
    {"kind": "cds", "text": "lacI", "token": "protein", "width": 2.2},
    ("terminator", "T1"),
    ("insulator", "Ins"),
    ("promoter", "$P_{\\mathrm{lac}}$"),
    ("operator", "lacO", ),
    ("rbs", "RBS"),
    {"kind": "cds", "text": "gfp", "token": "positive", "width": 2.4},
    ("terminator", "T2"),
], unit=0.62, gap=0.22)
lev = G.interaction(ax, parts[2], parts[6], kind="inhibition", height=1.45)
bio.label(ax, ((parts[2]["centre"] + parts[6]["centre"]) / 2, lev + 0.22), "LacI represses", size="small", va="bottom")
mid = (parts[2]["centre"] + parts[6]["centre"]) / 2
bio.molecule(ax, (mid + 1.2, lev + 1.05), "drug", "IPTG", r=0.32)
bio.arrow(ax, (mid + 1.2, lev + 0.72), (mid + 1.2, lev + 0.08), kind="inhibition")
bio.protein(ax, (parts[8]["centre"] + 0.2, y + 1.6), 0.9, 0.62, "positive", text="GFP")
bio.arrow(ax, (parts[8]["centre"], parts[8]["top"] + 0.08), (parts[8]["centre"] + 0.05, y + 1.22), kind="process")

# glyph key (forward strand, then a reverse-strand cassette)
kinds = [("promoter", "Promoter"), ("rbs", "RBS"), ("cds", "CDS"), ("terminator", "Terminator"), ("operator", "Operator"),
         ("insulator", "Insulator"), ("ori", "Origin"), ("primer", "Primer site"), ("recombination", "Recombination site"),
         ("spacer", "Spacer")]
for i, (k, name) in enumerate(kinds):
    x, yk = 0.9 + (i % 5) * 2.25, 2.2 - (i // 5) * 1.45
    g = G.construct(ax, x + (0.25 if k == "cds" else 0.55), yk, [{"kind": k, "width": 1.3 if k == "cds" else None}],
                    unit=0.55, ends=0.35)[0]
    bio.label(ax, (g["centre"], yk - 0.42), name, size="tiny", va="top")
G.construct(ax, 12.1, 1.5, [{"kind": "terminator", "reverse": True}, {"kind": "cds", "text": "cre", "token": "enzyme",
            "reverse": True, "width": 1.6}, {"kind": "rbs", "reverse": True}, {"kind": "promoter", "reverse": True}], unit=0.55)
bio.label(ax, (13.8, 2.35), "Reverse strand (right to left)", size="tiny", color=bio.P.muted())

# Figure 2: pUC19 plasmid map
fig2, ax2 = bio.canvas(11.6, 8.4)
G.plasmid(ax2, (5.6, 4.1), 2.9, 2686, name="pUC19", ticks=500, features=[
    {"name": "lacZα", "start": 146, "end": 469, "strand": -1, "token": "dna", "italic": True},
    {"name": "MCS", "start": 396, "end": 454, "strand": 0, "token": "neutral", "track": 1},
    {"name": "lac promoter", "start": 514, "end": 544, "strand": -1, "token": "positive"},
    {"name": "ori", "start": 867, "end": 1455, "strand": -1, "token": "highlight"},
    {"name": "AmpR", "start": 1626, "end": 2486, "strand": -1, "token": "receptor"},
    {"name": "AmpR promoter", "start": 2487, "end": 2591, "strand": -1, "token": "positive"},
], sites=[("EcoRI", 396), ("KpnI", 408), ("BamHI", 417), ("XbaI", 423), ("SalI", 429), ("PstI", 435), ("HindIII", 447)])
