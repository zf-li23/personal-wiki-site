# Isotonic regression (PAVA) and Nadaraya-Watson kernel regression for a simulated series of
# annual mean temperatures.
set.seed(42)
x <- seq(1900, 2025, length.out = 80)
true_trend <- 14 + 1.2 * (x - 1900) / (40 + (x - 1900))
y <- true_trend + sin(x / 2) * 0.15 + rnorm(length(x), sd = 0.08)
iso <- isoreg(x, y)
nw <- ksmooth(x, y, kernel = "normal", bandwidth = 15, x.points = x)
plot(x, y, pch = 16, col = "grey55", xlab = "year", ylab = "annual mean temperature (C)")
lines(x, iso$yf, type = "s", col = "firebrick", lwd = 2)
lines(nw$x, nw$y, col = "steelblue", lwd = 2)
lines(x, true_trend, lty = 3)
legend("topleft", c("isotonic (PAVA)", "Nadaraya-Watson", "trend"), lty = c(1, 1, 3),
       col = c("firebrick", "steelblue", "black"), lwd = c(2, 2, 1), bty = "n")
