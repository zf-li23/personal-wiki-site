"""Three learning paradigms and the brain structures proposed to specialize in them (after Doya 1999).

Each column: the circuit, the teaching signal and the rule.
Cortex: unsupervised (Hebbian, self-supervised prediction), dw ~ pre x post (with normalization).
Cerebellum: supervised, climbing-fibre error from the inferior olive, dw ~ -pre x error (LTD at parallel
fibre synapses when climbing fibre active).
Basal ganglia: reinforcement, dopamine reward prediction error delta, dw ~ delta x eligibility trace.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(18, 8.2)
cols = [
    (3.0, "Cerebral cortex", "Unsupervised", "neuron", "Input statistics,\nprediction errors",
     "$\\Delta w \\propto$ pre $\\times$ post\n(Hebbian, normalized)", "Representations,\nmodels of the world"),
    (9.0, "Cerebellum", "Supervised", "enzyme", "Climbing fibre:\nerror from inferior olive",
     "$\\Delta w \\propto -$pre $\\times$ error\n(parallel-fibre LTD)", "Internal models,\nprecise timing"),
    (15.0, "Basal ganglia", "Reinforcement", "highlight", "Dopamine: reward\nprediction error $\\delta$",
     "$\\Delta w \\propto \\delta \\times$ eligibility\n(three-factor rule)", "Action selection,\nhabits, values"),
]
for x, name, kind, tok, teach, rule, out in cols:
    bio.box(ax, (x, 7.2), 5.0, 0.9, token=tok, text=name, size="title")
    bio.label(ax, (x, 6.35), kind + " learning", size="normal", bold=True)
    bio.box(ax, (x, 5.15), 4.6, 1.2, token="neutral", text=teach, size="small")
    bio.label(ax, (x - 2.45, 5.95), "teaching signal", size="tiny", color=P.muted(), ha="left")
    bio.arrow(ax, (x, 4.5), (x, 3.85), kind="activation")
    bio.box(ax, (x, 3.2), 4.6, 1.2, token="neutral", text=rule, size="small")
    bio.label(ax, (x - 2.45, 4.0), "plasticity rule", size="tiny", color=P.muted(), ha="left")
    bio.arrow(ax, (x, 2.55), (x, 1.9), kind="process")
    bio.label(ax, (x, 1.3), out, size="small")
bio.arrow(ax, (5.6, 7.2), (6.4, 7.2), kind="link")
bio.arrow(ax, (11.6, 7.2), (12.4, 7.2), kind="link")
bio.label(ax, (9.0, 0.35), "All three interact through cortico-cerebellar and cortico-basal ganglia-thalamic loops", size="small", color=P.muted())
