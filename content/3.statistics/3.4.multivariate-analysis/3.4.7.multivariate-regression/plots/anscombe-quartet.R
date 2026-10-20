# Anscombe's quartet (1973): the same least squares fit for four very different data sets.
# The data set ships with base R as `anscombe` (columns x1..x4, y1..y4).
ylim <- range(anscombe[, paste0("y", 1:4)])
par(mfrow = c(2, 2), mar = c(4, 4, 2.5, 1))
for (k in 1:4) {
  x <- anscombe[[paste0("x", k)]]
  y <- anscombe[[paste0("y", k)]]
  fit <- lm(y ~ x)
  b <- coef(fit)
  plot(x, y, pch = 19, col = "steelblue", xlim = c(2, 20), ylim = ylim, xlab = "x", ylab = "y",
       main = sprintf("data set %d:  y = %.2f + %.3f x,  R^2 = %.2f", k, b[1], b[2], summary(fit)$r.squared),
       cex.main = 0.9)
  abline(fit, col = "firebrick", lwd = 1.5)
  grid()
}
