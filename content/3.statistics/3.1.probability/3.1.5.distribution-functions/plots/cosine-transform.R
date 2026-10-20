# Density of Y = r cos X for X ~ U(0, 2 pi): two inverse branches give 1 / (pi sqrt(r^2 - y^2)), checked by simulation.
r <- 1
op <- par(mfrow = c(1, 2), mar = c(4, 4, 2.5, 1))

x <- seq(0, 2 * pi, length.out = 400)
plot(x, r * cos(x), type = "l", lwd = 2, col = "steelblue", xlab = "x", ylab = "",
     main = "Two preimages of each y in (-r, r)")
y0 <- 0.3
x1 <- acos(y0 / r)
abline(h = y0, lty = 2, col = "firebrick")
abline(h = 0, col = "gray")
segments(c(x1, 2 * pi - x1), 0, c(x1, 2 * pi - x1), y0, col = "firebrick")
points(c(x1, 2 * pi - x1), c(y0, y0), pch = 19, col = "firebrick")
text(c(x1, 2 * pi - x1) + 0.1, y0 + 0.08, c("h1(y)", "h2(y)"), adj = 0, cex = 0.8)

set.seed(0)
y_sim <- r * cos(runif(100000, 0, 2 * pi))
hist(y_sim, breaks = 60, freq = FALSE, ylim = c(0, 3), col = adjustcolor("darkorange", 0.5),
     border = NA, xlab = "y", main = "Density of Y = r cos X, r = 1")
y <- seq(-0.995, 0.995, length.out = 400)
lines(y, 1 / (pi * sqrt(r^2 - y^2)), lwd = 2, col = "steelblue")
legend("top", bty = "n", cex = 0.8, pch = c(15, NA), lty = c(NA, 1),
       col = c(adjustcolor("darkorange", 0.5), "steelblue"),
       legend = c("100000 simulated values", "1 / (pi sqrt(r^2 - y^2))"))
par(op)
