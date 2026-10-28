"""The eumelanin-pheomelanin switch in dog melanocytes (activity-flow style, SBGN arrow semantics).

alpha-MSH activates MC1R (gene E); agouti signaling protein (gene A) inhibits MC1R; beta-defensin 103 (gene K,
allele K^B) binds MC1R and prevents the inhibition by agouti. Active MC1R drives eumelanin (TYRP1, gene B:
black vs brown); inactive MC1R gives pheomelanin. Melanophilin (gene D) is needed for full deposition of both
pigments. Epistasis: ee removes the receptor (masks K, A, B); K^B masks A."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 10.0)
B = dict(w=3.6, h=1.1, size="small")
nodes = {
    "msh": ((2.6, 7.8), "α-MSH", "neutral"),
    "asip": ((2.6, 5.0), "Agouti protein\n(gene A)", "receptor"),
    "cbd": ((2.6, 2.2), "β-defensin 103\n(gene K, Kᴮ)", "enzyme"),
    "mc1r": ((9.0, 5.0), "MC1R\n(gene E)", "highlight"),
    "eu": ((15.4, 7.0), "Eumelanin", "neutral"),
    "pheo": ((15.4, 3.0), "Pheomelanin\n(yellow, red)", "highlight"),
    "tyrp": ((21.2, 8.4), "TYRP1 (gene B):\nblack, bb brown", "dna"),
    "mlph": ((21.2, 5.0), "Melanophilin (gene D):\ndeposition, dd dilute", "trna"),
}
for k, (xy, t, tok) in nodes.items():
    bio.box(ax, xy, B["w"] if k not in ("tyrp", "mlph") else 4.4, B["h"], token=tok, text=t, size=B["size"])
X = lambda k: nodes[k][0]
bio.arrow(ax, (X("msh")[0] + 1.85, X("msh")[1] - 0.2), (X("mc1r")[0] - 1.85, X("mc1r")[1] + 0.35), kind="activation")
bio.arrow(ax, (X("asip")[0] + 1.85, X("asip")[1]), (X("mc1r")[0] - 1.85, X("mc1r")[1]), kind="inhibition")
bio.arrow(ax, (X("cbd")[0], X("cbd")[1] + 0.6), (X("asip")[0], X("asip")[1] - 0.6), kind="inhibition")
bio.label(ax, (X("cbd")[0] + 0.25, 3.6), "blocks agouti\nat the receptor", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (X("mc1r")[0] + 1.85, X("mc1r")[1] + 0.3), (X("eu")[0] - 1.85, X("eu")[1] - 0.2), kind="activation")
bio.label(ax, (12.2, 6.6), "receptor on", size="tiny", color=P.muted())
bio.arrow(ax, (X("mc1r")[0] + 1.85, X("mc1r")[1] - 0.3), (X("pheo")[0] - 1.85, X("pheo")[1] + 0.2), kind="process",
          dashed=True)
bio.label(ax, (12.2, 3.4), "receptor off\n(default)", size="tiny", color=P.muted())
bio.arrow(ax, (X("tyrp")[0] - 2.25, X("tyrp")[1] - 0.2), (X("eu")[0] + 1.85, X("eu")[1] + 0.3), kind="modulation")
bio.arrow(ax, (X("mlph")[0] - 2.25, X("mlph")[1] + 0.2), (X("eu")[0] + 1.85, X("eu")[1] - 0.3), kind="necessary")
bio.arrow(ax, (X("mlph")[0] - 2.25, X("mlph")[1] - 0.2), (X("pheo")[0] + 1.85, X("pheo")[1] + 0.3), kind="necessary")
bio.label(ax, (12.0, 0.9), "ee: no receptor, masks K, A and B (yellow)      Kᴮ: receptor kept on, masks A (solid color)",
          size="small", color=P.ink())
