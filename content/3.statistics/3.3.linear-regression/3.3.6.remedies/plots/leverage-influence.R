# High leverage, outlier, influential point: fits with and without the marked observation.
set.seed(0)
x <- 1:9
y <- 5 + 9 * x + 6 * rnorm(length(x))
cases <- list(
  list(title = "A: high leverage, on the trend", xo = 20, yo = 5 + 9 * 20),
  list(title = "B: outlier, low leverage", xo = 5, yo = 10),
  list(title = "C: high leverage and outlier", xo = 20, yo = 50)
)

fit <- lm(y ~ x)
ylim <- range(c(y, sapply(cases, function(cs) cs$yo)))
op <- par(mfrow = c(1, 3))
for (k in seq_along(cases)) {
  cs <- cases[[k]]
  xa <- c(x, cs$xo)
  ya <- c(y, cs$yo)
  fit_a <- lm(ya ~ xa)
  m <- length(xa)
  h <- hatvalues(fit_a)[m]
  t <- rstudent(fit_a)[m]          # studentized deleted residual
  D <- cooks.distance(fit_a)[m]
  plot(x, y, pch = 19, col = "steelblue", xlim = c(0, 22), ylim = ylim, xlab = "X",
       ylab = if (k == 1) "Y" else "",
       main = sprintf("%s\nh = %.2f, t = %.1f, D = %.2f", cs$title, h, t, D), cex.main = 0.9)
  points(cs$xo, cs$yo, pch = 17, col = "firebrick", cex = 1.6)
  abline(fit_a, col = "firebrick", lwd = 1.5)
  abline(fit, col = "steelblue", lwd = 1.5, lty = 2)
  if (k == 1) legend("topleft", bty = "n", cex = 0.8, lwd = 1.5, lty = c(1, 2),
                     col = c("firebrick", "steelblue"), legend = c("all data", "without triangle"))
}
par(op)
