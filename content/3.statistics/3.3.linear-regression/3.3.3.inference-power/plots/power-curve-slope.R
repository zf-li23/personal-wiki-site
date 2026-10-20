# Power curves of the two-sided t-test of zero slope for two designs.
power <- function(beta1, n, sig2, ssx, alpha = 0.05) {
  df <- n - 2
  delta <- beta1 / sqrt(sig2 / ssx)
  cval <- qt(1 - alpha / 2, df)
  pt(cval, df, ncp = delta, lower.tail = FALSE) + pt(-cval, df, ncp = delta)
}

beta1 <- seq(-2, 2, length.out = 401)
designs <- list(c(25, 19800), c(45, 35800))   # (n, S_XX)
cols <- c("steelblue", "darkorange")
plot(NA, xlim = range(beta1), ylim = c(0, 1), xlab = "beta_1", ylab = "power",
     main = "Power for the slope in simple linear regression (sigma^2 = 2500, alpha = 0.05)",
     cex.main = 0.9)
for (k in seq_along(designs)) {
  n <- designs[[k]][1]; ssx <- designs[[k]][2]
  lines(beta1, power(beta1, n, 2500, ssx), col = cols[k], lwd = 2)
  p1 <- power(1, n, 2500, ssx)
  points(1, p1, pch = 19, col = cols[k])
  text(1.12, p1 - 0.08, sprintf("%.2f", p1), col = cols[k], adj = 0, cex = 0.8)
}
abline(h = 0.05, lty = 3, col = "gray")
abline(h = 0.95, lty = 2, col = "gray")
legend("bottomleft", bty = "n", lwd = 2, col = cols,
       legend = sapply(designs, function(d) sprintf("n = %g, S_XX = %g", d[1], d[2])))
