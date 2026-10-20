# Gaussian kernel density estimates of an N(0, 1) sample for three bandwidths.
set.seed(0)
x <- rnorm(100)
grid <- seq(-4, 4, length.out = 801)
h_ref <- bw.nrd0(x)   # rule of thumb 0.9 * min(sd, IQR / 1.34) * n^(-1/5)

op <- par(mfrow = c(1, 3))
for (h in c(0.05, h_ref, 2.0)) {
  est <- density(x, bw = h, kernel = "gaussian", from = -4, to = 4, n = 801)
  plot(grid, dnorm(grid), type = "l", lty = 2, col = "grey50", lwd = 1.2,
       ylim = c(-0.05, 0.75), xlab = "x", ylab = "density", main = sprintf("h = %.2f", h))
  lines(est$x, est$y, col = "steelblue", lwd = 2)
  rug(x, col = "grey30")
}
legend("topright", bty = "n", cex = 0.8, legend = c("true density", "kernel estimate"),
       col = c("grey50", "steelblue"), lty = c(2, 1), lwd = c(1.2, 2))
par(op)
