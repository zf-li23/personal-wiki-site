# Normal Q-Q plots with a simultaneous band obtained from the DKW band for the CDF.
set.seed(7)
n <- 50; alpha <- 0.05
eps <- sqrt(log(2 / alpha) / (2 * n))
qqband <- function(s, main) {
  x <- sort(s); i <- 1:n
  z <- qnorm((i - 0.5) / n)        # plotting positions (i - 1/2)/n
  zl <- qnorm(pmax(i / n - eps, 1e-9)); zl[i / n - eps <= 0] <- -4
  zu <- qnorm(pmin((i - 1) / n + eps, 1 - 1e-9)); zu[(i - 1) / n + eps >= 1] <- 4
  plot(z, x, pch = 19, cex = 0.6, xlim = c(-3, 3), xlab = "theoretical normal quantile",
       ylab = "sample quantile", main = main)
  segments(zl, x, zu, x, col = adjustcolor("steelblue", 0.4), lwd = 3)
  abline(lm(x ~ z), col = "red")
}
par(mfrow = c(1, 2))
qqband(rnorm(n, 3, 2), "Normal sample")
qqband(rexp(n, 1 / 2), "Exponential sample")
