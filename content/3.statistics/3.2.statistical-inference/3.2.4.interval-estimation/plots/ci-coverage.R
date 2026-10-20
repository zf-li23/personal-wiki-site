# One hundred simulated confidence intervals for a normal mean with k = 1.96 and k = 0.5.
set.seed(0)
mu <- 68
sigma <- sqrt(3.6)
n <- 100
reps <- 100
x <- matrix(rnorm(reps * n, mu, sigma), reps, n)
xbar <- rowMeans(x)
s <- apply(x, 1, sd)
idx <- seq_len(reps) - 1

op <- par(mfrow = c(1, 2))
for (k in c(1.96, 0.5)) {
  lo <- xbar - k * s / sqrt(n)
  hi <- xbar + k * s / sqrt(n)
  cover <- lo <= mu & mu <= hi
  plot(NA, xlim = c(67, 69), ylim = range(idx), xlab = "height (in)", ylab = "replication",
       main = sprintf("k = %g: %.0f%% of the intervals cover mu", k, 100 * mean(cover)))
  segments(lo, idx, hi, idx, col = ifelse(cover, "grey65", "firebrick"),
           lwd = ifelse(cover, 1.2, 1.8))
  points(xbar, idx, pch = 16, cex = 0.3, col = "grey35")
  abline(v = mu, col = "steelblue", lwd = 1.5)
}
par(op)
