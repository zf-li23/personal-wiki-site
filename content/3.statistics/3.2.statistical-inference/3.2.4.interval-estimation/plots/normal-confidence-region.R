# Confidence region for (mu, sigma^2) of a normal sample.
set.seed(0)
n <- 30
alpha <- 0.05
x <- rnorm(n)
xbar <- mean(x)
ss <- sum((x - xbar)^2)
g <- (1 - sqrt(1 - alpha)) / 2   # each of the two independent pieces has level sqrt(1 - alpha)
cc <- qnorm(1 - g)
s2_lo <- ss / qchisq(1 - g, n - 1)
s2_hi <- ss / qchisq(g, n - 1)

s2 <- seq(0, s2_hi * 1.25, length.out = 400)
half <- cc * sqrt(s2 / n)
plot(xbar - half, s2, type = "l", col = "steelblue", lwd = 1.5,
     xlim = range(xbar - half, xbar + half), ylim = c(0, s2_hi * 1.25),
     xlab = "mu", ylab = "sigma^2", main = sprintf("95%% confidence region, n = %d", n))
lines(xbar + half, s2, col = "steelblue", lwd = 1.5)
band <- seq(s2_lo, s2_hi, length.out = 200)
hb <- cc * sqrt(band / n)
polygon(c(xbar - hb, rev(xbar + hb)), c(band, rev(band)),
        col = adjustcolor("steelblue", 0.3), border = NA)
abline(h = c(s2_lo, s2_hi), lty = 2, col = "darkgreen")
points(0, 1, pch = 4, cex = 2, lwd = 2, col = "firebrick")
points(xbar, ss / (n - 1), pch = 19, cex = 0.7, col = "grey30")
legend("topleft", bty = "n", cex = 0.8,
       legend = c("(mu - x_bar)^2 = c^2 sigma^2 / n", "confidence region",
                  "true (mu, sigma^2) = (0, 1)", "(x_bar, s^2)"),
       col = c("steelblue", adjustcolor("steelblue", 0.3), "firebrick", "grey30"),
       lty = c(1, NA, NA, NA), pch = c(NA, 15, 4, 19), pt.cex = c(NA, 2, 1.5, 0.7))
