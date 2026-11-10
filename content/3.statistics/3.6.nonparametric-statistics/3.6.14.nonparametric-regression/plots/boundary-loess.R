# Boundary bias of kernel regression: Nadaraya-Watson versus local linear LOESS.
set.seed(42)
x <- seq(1900, 2025, length.out = 80)
true_trend <- 14 + 1.2 * (x - 1900) / (40 + (x - 1900))
y <- true_trend + sin(x / 2) * 0.15 + rnorm(length(x), sd = 0.08)
nw_fit <- ksmooth(x, y, kernel = "normal", bandwidth = 15, x.points = x)
loess_fit <- loess(y ~ x, span = 0.25, degree = 1)
plot(x, y, pch = 16, col = "grey55", xlab = "year", ylab = "annual mean temperature (C)",
     main = "LOESS rescues boundary bias")
lines(x, true_trend, lty = 3)
lines(nw_fit$x, nw_fit$y, col = "steelblue", lwd = 2)
lines(x, predict(loess_fit, newdata = data.frame(x = x)), col = "firebrick", lwd = 2)
legend("topleft", c("smooth trend", "Nadaraya-Watson", "local linear (LOESS)"), lty = c(3, 1, 1),
       col = c("black", "steelblue", "firebrick"), lwd = c(1, 2, 2), bty = "n")
