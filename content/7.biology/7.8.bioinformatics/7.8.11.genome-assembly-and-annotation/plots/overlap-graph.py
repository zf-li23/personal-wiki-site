# Abstract overlap graph of five reads and its transitive reduction (string graph).
import wikigraph as G

pos = {f"r{i}": (1.1 * i, 0.0 if i % 2 else 0.9) for i in range(1, 6)}
full = [("r1", "r2"), ("r2", "r3"), ("r3", "r4"), ("r4", "r5"),
        ("r1", "r3"), ("r2", "r4"), ("r3", "r5")]
reduced = [("r1", "r2"), ("r2", "r3"), ("r3", "r4"), ("r4", "r5")]
transitive = [("r1", "r3"), ("r2", "r4"), ("r3", "r5")]

fig, (a, b) = G.panels(2, 6.2, 1.6, titles=["A  overlap graph", "B  after transitive reduction"])
for ax in (a, b):
    ax.set_xlim(0.4, 6.0)
G.draw(a, pos, full, directed=True, highlight={e: G.GREY for e in transitive}, dashed=transitive)
G.draw(b, pos, reduced, directed=True, highlight={e: G.BLUE for e in reduced})
G.caption(a, (3.3, -0.35), "dashed: implied by two shorter overlaps")
G.caption(b, (3.3, -0.35), "one non-branching path: a unitig")
