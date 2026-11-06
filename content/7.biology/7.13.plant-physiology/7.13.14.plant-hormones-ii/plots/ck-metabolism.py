# Cytokinin biosynthesis, activation and inactivation (simplified).
# IPT (rate-limiting): DMAPP + ATP/ADP -> iP ribotides; CYP735A: -> tZ ribotides; LOG: ribotide -> free base.
# Inactivation: N-glucosylation (irreversible), O-glucosylation (reversible storage), CKX side-chain cleavage.
import wikibio as bio
from wikibio import metabolism as M

fig, ax = bio.canvas(21.5, 11)
P = bio.P
pw = M.Pathway(ax, size="small")
pw.node("atp", (3.3, 9.9), "DMAPP + ATP / ADP")
pw.node("iprtp", (3.3, 7.6), "iP ribotides\n(iPRTP / iPRDP / iPRMP)", h=0.75)
pw.node("ztp", (10.4, 7.6), "tZ ribotides\n(tZRTP / tZRDP / tZRMP)", h=0.75)
pw.node("ip", (3.3, 4.6), "iP (free base, active)", bold=True, token="positive")
pw.node("tz", (10.4, 4.6), "trans-Zeatin (active)", bold=True, token="positive")
pw.node("tzr", (16.0, 6.3), "tZ riboside\n(xylem transport form)", h=0.75)
pw.node("ogl", (16.6, 3.0), "O-glucoside (storage)", token="neutral")
pw.node("ngl", (10.4, 1.4), "N7-, N9-glucosides\n(inactive)", h=0.75, token="neutral")
pw.node("ade", (3.3, 1.4), "Adenine + side-chain\naldehyde (inactive)", h=0.75, token="neutral")
pw.node("trna", (18.9, 9.9), "tRNA (prenylated A37)")
pw.node("cz", (18.9, 8.0), "cis-Zeatin (minor)")

pw.step("atp", "iprtp", enzyme="IPT (rate-limiting)", enzyme_size="tiny", side=(None, "PPi"))
pw.step("iprtp", "ztp", enzyme="CYP735A (P450)", enzyme_size="tiny")
pw.step("iprtp", "ip", enzyme="LOG", enzyme_size="small")
pw.step("ztp", "tz", enzyme="LOG", enzyme_size="small")
pw.step("ztp", "tzr", enzyme="phosphatase", enzyme_size="tiny")
pw.step("tzr", "tz", reversible=True, enzyme="nucleosidase /\nkinase", enzyme_size="tiny")
pw.step("tz", "ogl", reversible=True, enzyme="ZOG / β-glucosidase", enzyme_size="tiny", enzyme_flip=True)
pw.step("tz", "ngl", enzyme="UGT76C", enzyme_size="tiny")
pw.step("ip", "ade", enzyme="CKX (FAD)", enzyme_size="tiny")
pw.step("tz", "ade", enzyme="CKX", enzyme_size="tiny", enzyme_flip=True)
pw.step("trna", "cz", enzyme="tRNA-IPT, degradation", enzyme_size="tiny")
