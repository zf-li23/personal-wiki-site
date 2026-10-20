"""ROC and precision-recall curves of two scoring classifiers on an imbalanced
test set (5% positives). The two classifiers have almost the same AUC, but B
gives a few percent of the negatives very high scores, which ruins the top of
its ranking: the precision-recall curve shows this, the ROC curve hardly does."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
n_pos, n_neg = 250, 4750
y = np.r_[np.ones(n_pos), np.zeros(n_neg)]

# A: Gaussian scores, shifted for positives
s_a = np.r_[rng.normal(2.0, 1.0, n_pos), rng.normal(0.0, 1.0, n_neg)]
# B: positives shifted further, but 4% of the negatives are confidently mis-scored
s_b = np.r_[rng.normal(2.3, 1.0, n_pos), rng.normal(0.0, 1.0, n_neg)]
bad = rng.random(n_neg) < 0.04
s_b[n_pos:][bad] += 3.0


def curves(y, s):
    order = np.argsort(-s, kind="stable")
    y = y[order]
    tp = np.cumsum(y)
    fp = np.cumsum(1 - y)
    tpr = np.r_[0, tp / tp[-1]]
    fpr = np.r_[0, fp / fp[-1]]
    precision = tp / (tp + fp)
    recall = tp / tp[-1]
    auc = np.trapezoid(tpr, fpr)
    ap = np.sum(precision[y == 1]) / tp[-1]        # average precision
    return fpr, tpr, recall, precision, auc, ap


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.4))
for name, s in [("A", s_a), ("B", s_b)]:
    fpr, tpr, rec, prec, auc, ap = curves(y, s)
    ax1.plot(fpr, tpr, label=f"classifier {name} (AUC = {auc:.3f})")
    ax2.plot(rec, prec, label=f"classifier {name} (AP = {ap:.3f})")
ax1.plot([0, 1], [0, 1], linestyle="--", color="gray", label="random guess")
ax2.axhline(n_pos / (n_pos + n_neg), linestyle="--", color="gray",
            label="random guess (prevalence 0.05)")
ax1.set(xlabel="false positive rate (FPR)", ylabel="true positive rate (TPR = recall)",
        title="ROC curves", xlim=(0, 1), ylim=(0, 1.01))
ax2.set(xlabel="recall", ylabel="precision", title="Precision-recall curves",
        xlim=(0, 1), ylim=(0, 1.01))
ax1.legend(loc="lower right")
ax2.legend(loc="upper right")
fig.tight_layout()
