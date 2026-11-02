# Run-order drift confounded with group: cancers first versus random order.
set.seed(0)
n_cancer <- 100; n_control <- 100; n <- n_cancer + n_control
ord <- 1:n
drift <- 6.0 - 2.5 * (ord / n)^2       # quality drifts downward, no true group difference
signal <- drift + rnorm(n, 0, 0.8)
g_first <- rep(c(1, 0), c(n_cancer, n_control))   # cancers run first
g_random <- sample(g_first)                       # randomized run order

par(mfrow = c(1, 2))
for (k in 1:2) {
  g <- if (k == 1) g_first else g_random
  tt <- t.test(signal[g == 1], signal[g == 0], var.equal = TRUE)
  ttl <- if (k == 1) "Cancers run first, controls later" else "Randomized run order"
  plot(ord, signal, type = "n", xlab = "run order (sample number)", ylab = "measured intensity",
       main = sprintf("%s\nmean difference = %.2f, p = %.1e", ttl,
                      mean(signal[g == 1]) - mean(signal[g == 0]), tt$p.value), cex.main = 0.85)
  lines(ord, drift, lty = 2, col = "gray")
  points(ord[g == 1], signal[g == 1], pch = 19, cex = 0.6, col = "firebrick")
  points(ord[g == 0], signal[g == 0], pch = 15, cex = 0.6, col = "steelblue")
  if (k == 1) legend("bottomleft", c("cancer", "control"), pch = c(19, 15),
                     col = c("firebrick", "steelblue"), bty = "n")
}
