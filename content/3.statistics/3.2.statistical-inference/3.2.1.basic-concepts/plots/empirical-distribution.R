# Empirical distribution functions of standard normal samples of size 10 and 100, with the Kolmogorov distance D_n.
set.seed(0)
grid <- seq(-3.2, 3.2, length.out = 400)
op <- par(mfrow = c(1, 2))
for (n in c(10, 100)) {
  x <- rnorm(n)
  Fn <- ecdf(x)
  d <- unname(ks.test(x, "pnorm")$statistic)   # D_n = sup |F_n(x) - F(x)|
  plot(Fn, do.points = (n <= 20), verticals = FALSE, col = "steelblue", lwd = 1.4,
       xlim = c(-3.2, 3.2), xlab = "x", ylab = "probability",
       main = sprintf("n = %d,  D_n = %.3f", n, d))
  lines(grid, pnorm(grid), col = "firebrick", lwd = 1.4)
  if (n == 10) {
    legend("topleft", bty = "n", cex = 0.8, legend = c("EDF F_n(x)", "true CDF F(x)"),
           col = c("steelblue", "firebrick"), lwd = 1.4)
  }
}
par(op)
