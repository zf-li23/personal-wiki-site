"""The citric acid cycle as an amphibolic hub.

Blue (outward): intermediates drawn off for biosynthesis. Green (inward): anaplerotic reactions that refill
the cycle (pyruvate carboxylase, PEP carboxykinase, PEP carboxylase of plants and bacteria, malic enzyme),
and other catabolic inputs (amino acids, odd-chain fatty acids). Grey: the cycle itself.
"""

import numpy as np

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(24.0, 17.0, scale=0.4)
OUT, IN = P.edge("channel"), P.edge("positive")
pw = M.Pathway(ax, size="small")
c, r = (12.0, 8.5), 4.0
cyc = [("cit", "Citrate"), ("icit", "Isocitrate"), ("akg", "α-Ketoglutarate"), ("scoa", "Succinyl-CoA"),
       ("suc", "Succinate"), ("fum", "Fumarate"), ("mal", "Malate"), ("oaa", "Oxaloacetate")]
pos = M.ring(c, r, 8, start=112.5, clockwise=True)
for (id, t), p in zip(cyc, pos):
    pw.node(id, p, t)
for k in range(8):
    a, b = cyc[k][0], cyc[(k + 1) % 8][0]
    pw.step(a, b, bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c), color=P.muted())
pw.node("acoa", (12.0, 15.6), "Acetyl-CoA", token="highlight", bold=True)
bio.arrow(ax, pw.anchor("acoa", "b") + (0, -0.05), (9.3, 11.6), kind="process", color=P.muted(), bend=0.15)


def out(src, xy, text, token="metabolite"):
    pw.node(text, xy, text, token=token)
    pw.step(src, text, color=OUT)


def inn(xy, dst, text, enzyme=None, token="metabolite"):
    pw.node(text, xy, text, token=token)
    pw.step(text, dst, color=IN, enzyme=enzyme, enzyme_size="tiny")


out("cit", (5.0, 15.6), "Fatty acids, sterols")
out("akg", (21.2, 9.4), "Glutamate → Gln, Pro, Arg; purines")
out("scoa", (20.8, 5.6), "Porphyrins, heme")
out("oaa", (3.2, 13.4), "Aspartate → Asn, Thr, Met, Lys;\npyrimidines")
out("oaa", (2.4, 11.4), "PEP → glucose")
inn((2.2, 9.3), "oaa", "Pyruvate")
inn((2.2, 7.6), "oaa", "PEP")
inn((2.2, 5.4), "mal", "Pyruvate ")
inn((17.6, 1.4), "scoa", "Ile, Met, Thr, Val;\nodd-chain fatty acids")
inn((20.6, 13.0), "akg", "Glu ")
bio.label(ax, (5.3, 10.05), "pyruvate carboxylase", size="tiny", bold=True, color=IN)
bio.label(ax, (5.3, 8.15), "PEP carboxykinase,\nPEP carboxylase", size="tiny", bold=True, color=IN)
bio.label(ax, (5.3, 5.55), "malic enzyme", size="tiny", bold=True, color=IN)
bio.label(ax, (c[0], c[1] + 0.3), "Citric acid\ncycle", size="normal", bold=True, color=P.muted())
bio.label(ax, (0.4, 16.4), "biosynthesis (out)", size="small", bold=True, ha="left", color=OUT)
bio.label(ax, (0.4, 15.8), "anaplerosis (in)", size="small", bold=True, ha="left", color=IN)
