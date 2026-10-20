# Two regression lines of a bivariate normal distribution, and the regression effect in simulated heights.
library(MASS)
set.seed(0)

rho <- 0.5
Sigma <- matrix(c(1, rho, rho, 1), 2)
xy <- mvrnorm(200, mu = c(0, 0), Sigma = Sigma)

op <- par(mfrow = c(1, 2))

# left: density contours, sample, and the two regression lines
g <- seq(-3, 3, length.out = 200)
Sinv <- solve(Sigma)
q <- outer(g, g, function(x, y) Sinv[1, 1] * x^2 + 2 * Sinv[1, 2] * x * y + Sinv[2, 2] * y^2)
contour(g, g, q, levels = c(0.5, 1.5, 3, 5, 8), drawlabels = FALSE, col = "gray", asp = 1,
        xlab = "x", ylab = "y", main = "Standard bivariate normal, rho = 0.5")
points(xy, pch = 19, cex = 0.5, col = adjustcolor("steelblue", 0.6))
abline(0, rho, col = "firebrick", lwd = 2)          # E(Y | X = x) = 0.5 x
abline(0, 1 / rho, col = "forestgreen", lwd = 2)    # E(X | Y = y) = 0.5 y, i.e. y = 2 x
abline(0, 1, lty = 2)                               # major axis
legend("topleft", bty = "n", cex = 0.75, lwd = c(2, 2, 1), lty = c(1, 1, 2),
       col = c("firebrick", "forestgreen", "black"),
       legend = c("E(Y | X = x) = 0.5 x", "E(X | Y = y) = 0.5 y, i.e. y = 2 x", "major axis y = x"))

# right: regression toward the mean in simulated parent and child heights
n <- 900
mu <- 68; s <- 1.8; r <- 0.65
z <- mvrnorm(n, mu = c(0, 0), Sigma = matrix(c(1, r, r, 1), 2))
parent <- mu + s * z[, 1]
child <- mu + s * z[, 2]
plot(parent, child, pch = 19, cex = 0.4, col = adjustcolor("steelblue", 0.35),
     xlab = "mid-parent height (inches)", ylab = "child height (inches)",
     main = "Regression toward the mean (simulated heights)")
grp <- cut(parent, breaks = seq(63.5, 73.5, by = 1), right = FALSE)
med <- tapply(child, grp, function(v) if (length(v) >= 10) median(v) else NA)
points(64:73, med, pch = 15, col = "firebrick")
abline(a = mu * (1 - r), b = r, col = "firebrick", lwd = 1.5)   # E(child | parent)
abline(0, 1, lty = 2)
legend("topleft", bty = "n", cex = 0.75, pch = c(15, NA), lty = c(NA, 2),
       col = c("firebrick", "black"), legend = c("median child height per parent group", "child = parent"))
par(op)
