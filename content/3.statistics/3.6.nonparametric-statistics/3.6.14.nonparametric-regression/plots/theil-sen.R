# Theil-Sen and least squares lines for 30 points, of which the 3 with the largest x are
# replaced by gross errors.
theil_sen <- function(x, y) {
  ij <- combn(length(x), 2)
  dx <- x[ij[2, ]] - x[ij[1, ]]
  s <- (y[ij[2, ]] - y[ij[1, ]])[dx != 0] / dx[dx != 0]
  b <- median(s)
  c(intercept = median(y - b * x), slope = b)
}
set.seed(1)
n <- 30
x <- sort(runif(n, 0, 10))
y <- 2 + 0.8 * x + rnorm(n)
y_bad <- y
y_bad[(n - 2):n] <- rnorm(3, 0.5, 0.5)
op <- par(mfrow = c(1, 2))
for (yy in list(y, y_bad)) {
  plot(x, yy, pch = 16, col = "grey50", ylim = range(c(y, y_bad)), ylab = "y")
  abline(2, 0.8, lty = 3)
  abline(lm(yy ~ x), col = "steelblue", lwd = 2)
  abline(theil_sen(x, yy), col = "darkorange", lwd = 2)
  legend("topleft", c("true", "least squares", "Theil-Sen"), lty = c(3, 1, 1),
         col = c("black", "steelblue", "darkorange"), bty = "n")
}
par(op)
