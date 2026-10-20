# An outlier near the center of X shifts the line; an outlier at an extreme X tilts it.
set.seed(0)
x <- seq(1, 96, by = 5)
y <- 30 + 50 * x + 200 * rnorm(length(x))
cases <- list(
  list(title = "outlier at X = 50 (near the mean of X)", xo = 50, yo = 30 + 50 * 50 + 10000, loc = "topright"),
  list(title = "outlier at X = 100 (extreme X)", xo = 100, yo = 30 + 50 * 100 - 10000, loc = "topleft")
)

fit <- lm(y ~ x)
op <- par(mfrow = c(1, 2))
for (cs in cases) {
  xa <- c(x, cs$xo)
  ya <- c(y, cs$yo)
  fit_a <- lm(ya ~ xa)
  plot(xa, ya, type = "n", xlim = c(-2, 102), xlab = "X", ylab = "Y", main = cs$title, cex.main = 0.9)
  points(x, y, pch = 19, col = "steelblue", cex = 0.8)
  points(cs$xo, cs$yo, pch = 15, col = "firebrick", cex = 1.3)
  abline(fit_a, col = "firebrick", lwd = 1.5)
  abline(fit, col = "steelblue", lwd = 1.5, lty = 2)
  legend(cs$loc, bty = "n", cex = 0.8, lwd = 1.5, lty = c(1, 2), col = c("firebrick", "steelblue"),
         legend = c(sprintf("with outlier: b1 = %.1f", coef(fit_a)[2]),
                    sprintf("without outlier: b1 = %.1f", coef(fit)[2])))
}
par(op)
