"""Four causal diagrams for identification: backdoor, adjusting for a collider, front door, controlled direct effect."""

import wikigraph as G

titles = ["(a) backdoor: adjust for $W$", "(b) backdoor through a collider $Z$",
          "(c) front door through $Z$", "(d) direct effect of $X$ on $Y$"]
fig, axes = G.panels(4, 2.4, 2.0, titles=titles)


def label(names):
    return {v: f"${v}$" for v in names}


# (a) drug X, recovery Y, weight W, unmeasured socioeconomic status Z
pos = {"Z": (0.0, 1.8), "W": (2.4, 1.8), "X": (0.0, 0.0), "Y": (2.4, 0.0)}
arcs = [("Z", "W"), ("Z", "X"), ("W", "Y"), ("X", "Y")]
G.draw(axes[0], pos, arcs, directed=True, vertex_labels=label(pos), dashed=[("Z", "W"), ("Z", "X")],
       vertex_color={"W": G.BLUE})

# (b) adjustment sets {E, Z}, {A, Z}, {E, Z, A}
pos = {"E": (0.0, 1.8), "A": (2.4, 1.8), "Z": (1.2, 1.2), "X": (0.4, 0.0), "Y": (2.0, 0.0)}
arcs = [("E", "X"), ("E", "Z"), ("A", "Z"), ("A", "Y"), ("Z", "X"), ("Z", "Y"), ("X", "Y")]
G.draw(axes[1], pos, arcs, directed=True, vertex_labels=label(pos), vertex_color={"Z": G.BLUE, "E": G.BLUE})

# (c) smoking X, tar Z, cancer Y, unobserved genotype U
pos = {"U": (1.2, 1.8), "X": (0.0, 0.0), "Z": (1.2, 0.0), "Y": (2.4, 0.0)}
arcs = [("U", "X"), ("U", "Y"), ("X", "Z"), ("Z", "Y")]
G.draw(axes[2], pos, arcs, directed=True, vertex_labels=label(pos), dashed=[("U", "X"), ("U", "Y")],
       vertex_color={"Z": G.BLUE})

# (d) gender X, qualification Z, income I, hiring Y
pos = {"I": (2.4, 1.8), "Z": (1.0, 1.3), "X": (0.0, 0.0), "Y": (2.4, 0.0)}
arcs = [("X", "Z"), ("X", "Y"), ("I", "Z"), ("I", "Y"), ("Z", "Y")]
G.draw(axes[3], pos, arcs, directed=True, vertex_labels=label(pos), highlight={("X", "Y"): G.RED})
