# Benjamini-Hochberg versus Bonferroni on simulated z-tests: 1000 hypotheses, 100 with a true effect.
set.seed(0)
m <- 1000
m1 <- 100
alpha <- 0.05
z <- rnorm(m)
z[1:m1] <- z[1:m1] + 3.0
p <- 2 * pnorm(-abs(z))

# Step-up rule: reject the k smallest p-values, k = max{i : p_(i) <= i alpha / m}.
ord <- order(p)
ps <- p[ord]
ranks <- 1:m
below <- which(ps <= ranks / m * alpha)
k <- if (length(below) > 0) max(below) else 0
# The same rejections from the adjusted p-values.
stopifnot(sum(p.adjust(p, method = "BH") <= alpha) == k)
n_bonf <- sum(p.adjust(p, method = "bonferroni") <= alpha)
false_bh <- sum(ord[seq_len(k)] > m1)  # hypotheses 1..m1 carry the true effect

show <- 1:150
par(mfrow = c(1, 2))
for (logscale in c(FALSE, TRUE)) {
  plot(show, ps[show], pch = 19, cex = 0.5, col = "steelblue", log = if (logscale) "y" else "",
       ylim = if (logscale) range(ps[show]) else c(0, 0.02), xlab = "rank i", ylab = "p-value",
       main = if (logscale) "log scale" else sprintf("BH rejects %d (%d false); Bonferroni rejects %d", k, false_bh, n_bonf),
       cex.main = 0.9)
  lines(show, show / m * alpha, col = "darkorange", lwd = 1.5)
  abline(h = alpha / m, lty = 2, col = "firebrick")
  abline(v = k + 0.5, lty = 3, col = "gray")
  if (!logscale) {
    legend("topleft", bty = "n", cex = 0.8, legend = c("sorted p-values", "BH line i alpha / m", "Bonferroni alpha / m"),
           col = c("steelblue", "darkorange", "firebrick"), pch = c(19, NA, NA), lty = c(NA, 1, 2))
  }
}
