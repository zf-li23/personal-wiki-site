# Order statistics of n = 5 iid U(0,1) variables: simulated histograms versus the exact Beta(k, n - k + 1) densities.
set.seed(0)
n <- 5
x <- seq(0, 1, length.out = 400)
samples <- t(apply(matrix(runif(20000 * n), ncol = n), 1, sort))   # row i = sorted sample i
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick", "purple")
breaks <- seq(0, 1, length.out = 61)

plot(NA, xlim = c(0, 1), ylim = c(0, 5.5), xlab = "x", ylab = "density",
     main = "order statistics of 5 uniform points (curves: exact, bars: simulation)", cex.main = 0.9)
for (k in 1:n) {
  h <- hist(samples[, k], breaks = breaks, plot = FALSE)
  plot(h, freq = FALSE, add = TRUE, col = adjustcolor(cols[k], 0.15), border = NA)
  lines(x, dbeta(x, k, n - k + 1), col = cols[k], lwd = 1.8)
}
legend("top", bty = "n", cex = 0.8, lty = 1, col = cols,
       legend = paste0("k = ", 1:n, ": Beta(", 1:n, ", ", n - (1:n) + 1, ")"))
