"""The hematopoietic hierarchy and a model of a lineage choice. A: the classical tree, from the long-term
hematopoietic stem cell (HSC) through multipotent progenitors (MPP) to the common myeloid (CMP) and lymphoid
(CLP) progenitors, the megakaryocyte-erythrocyte (MEP) and granulocyte-macrophage (GMP) progenitors and the
mature cells, with key transcription factors (italic genes on the arrows) and cytokines (EPO, TPO, G-CSF, M-CSF,
IL-7). Single-cell studies show that commitment is more gradual and that some branches (megakaryocytes) can leave
directly from HSC-like cells. B, C: the GATA1-PU.1 switch (Formula 29.8.1), with self-activation a and mutual
repression b. Nullclines (GATA1: red; PU.1: blue), stable states (filled) and saddles (open). With strong
self-activation (a = 1, B) a third, central stable state coexists with the two committed states, a model of the
multipotent progenitor that co-expresses both factors at low levels (lineage priming); weaker self-activation
(a = 0.5, C) removes it, and the cell must choose erythroid-megakaryocytic (GATA1 high) or myeloid (PU.1 high)."""
import numpy as np
from scipy.optimize import fsolve
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(26, 11)
bio.panel(ax, "A", (0.2, 10.8))
N = {"HSC": (6.5, 9.8, "protein"), "MPP": (6.5, 8.3, "protein"), "CMP": (4.0, 6.6, "drug"), "CLP": (10.0, 6.6, "dna"),
     "MEP": (2.2, 4.8, "blood"), "GMP": (5.8, 4.8, "lipid_head"), "erythrocyte": (1.0, 2.6, "blood"), "megakaryocyte\n(platelets)": (3.4, 1.4, "receptor"),
     "granulocyte": (5.2, 2.6, "atp"), "monocyte,\nmacrophage": (7.6, 1.4, "antibody"), "B cell": (9.0, 3.4, "channel"),
     "T cell\n(thymus)": (10.8, 1.6, "dna2"), "NK cell": (12.2, 3.4, "enzyme")}
for k, (x, y, tk) in N.items():
    bio.box(ax, (x, y), 2.1 if len(k) > 5 else 1.4, 0.95 if "\n" in k else 0.7, tk, k, size="tiny")
E = [("HSC", "MPP", r"$\it{Runx1, Scl, Gata2}$"), ("MPP", "CMP", ""), ("MPP", "CLP", r"$\it{Ikaros}$, IL-7"), ("CMP", "MEP", r"$\it{Gata1}$"),
     ("CMP", "GMP", r"$\it{Pu.1}$, $\it{Cebpa}$"), ("MEP", "erythrocyte", "EPO, $\\it{Klf1}$"), ("MEP", "megakaryocyte\n(platelets)", "TPO"),
     ("GMP", "granulocyte", "G-CSF"), ("GMP", "monocyte,\nmacrophage", "M-CSF"), ("CLP", "B cell", r"$\it{Pax5}$"),
     ("CLP", "T cell\n(thymus)", "Notch"), ("CLP", "NK cell", "")]
for a_, b_, t in E:
    pa, pb = np.array(N[a_][:2]), np.array(N[b_][:2])
    bio.arrow(ax, tuple(pa), tuple(pb), kind="process", shrink=0.55, lw=1.0)
    if t:
        m = (pa + pb) / 2
        bio.label(ax, (m[0] + 0.15, m[1] + 0.1), t, size="tiny", ha="left", color=P.muted())


def F(z, a, b=1.0, th=0.5, n=4, k=1.0):
    x, y = z
    return np.array([a * x**n / (th**n + x**n) + b * th**n / (th**n + y**n) - k * x,
                     a * y**n / (th**n + y**n) + b * th**n / (th**n + x**n) - k * y])


for j, a in enumerate((1.0, 0.5)):
    sub = charts.axes_at(ax, (15.0 + 5.6 * j, 1.4, 4.6, 8.4))
    g = np.linspace(0, 2.1, 160)
    X, Y = np.meshgrid(g, g)
    U, V = F((X, Y), a)
    sub.contour(X, Y, U, levels=[0], colors=[charts.line("blood")], linewidths=1.6)
    sub.contour(X, Y, V, levels=[0], colors=[charts.line("dna")], linewidths=1.6)
    gs = np.linspace(0.05, 2.05, 13)
    Xs, Ys = np.meshgrid(gs, gs)
    Us, Vs = F((Xs, Ys), a)
    sub.quiver(Xs, Ys, Us, Vs, color=P.muted(), alpha=0.5, angles="xy", width=0.004)
    found = []
    for x0 in np.linspace(0, 2, 7):
        for y0 in np.linspace(0, 2, 7):
            s = fsolve(F, [x0, y0], args=(a,))
            if np.allclose(F(s, a), 0, atol=1e-8) and not any(np.allclose(s, q, atol=1e-3) for q in found):
                found.append(s)
    for s in found:
        h = 1e-6
        J = np.array([(F(s + [h, 0], a) - F(s - [h, 0], a)) / (2 * h), (F(s + [0, h], a) - F(s - [0, h], a)) / (2 * h)]).T
        stable = np.all(np.linalg.eigvals(J).real < 0)
        sub.plot(*s, "o", ms=7, color=P.ink(), mfc=P.ink() if stable else P.surface(), zorder=5)
    sub.set_xlim(0, 2.1)
    sub.set_ylim(0, 2.1)
    sub.set_aspect("equal")
    charts.style_axes(sub, "GATA1", "PU.1" if j == 0 else None)
    charts.title(sub, ("B  a = 1: three states", "C  a = 0.5: two states")[j])
