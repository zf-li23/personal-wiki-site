# Principal axes of a correlated bivariate sample and the rotated (uncorrelated) principal component scores.
library(MASS)

set.seed(0)
n <- 150
Sigma <- matrix(c(3.0, 1.8, 1.8, 1.6), 2, 2)
x <- mvrnorm(n, c(2.0, 1.0), Sigma)
xbar <- colMeans(x)

pc <- prcomp(x)                 # eigen-decomposition of the sample covariance matrix
lam <- pc$sdev^2
E <- pc$rotation
sgn <- c(sign(E[1, 1]), sign(E[2, 2]))  # fix the arbitrary signs of the eigenvectors
E <- sweep(E, 2, sgn, "*")
y <- sweep(pc$x, 2, sgn, "*")   # scores (x - xbar) E

par(mfrow = c(1, 2))
plot(x, pch = 19, cex = 0.6, col = adjustcolor("steelblue", 0.7), asp = 1,
     xlab = "x_1", ylab = "x_2", main = "original coordinates")
tt <- seq(0, 2 * pi, length.out = 300)
for (c0 in 1:2) {
  ell <- xbar + c0 * E %*% (sqrt(lam) * rbind(cos(tt), sin(tt)))
  lines(ell[1, ], ell[2, ], col = "gray")
}
cols <- c("firebrick", "forestgreen")
for (k in 1:2) {
  v <- 2.2 * sqrt(lam[k]) * E[, k]
  arrows(xbar[1], xbar[2], xbar[1] + v[1], xbar[2] + v[2], col = cols[k], lwd = 2, length = 0.1)
  text(xbar[1] + 1.08 * v[1], xbar[2] + 1.08 * v[2], paste0("e_", k), col = cols[k])
}

plot(y, pch = 19, cex = 0.6, col = adjustcolor("darkorange", 0.7), asp = 1,
     xlab = sprintf("y_1 (sample variance %.2f)", lam[1]),
     ylab = sprintf("y_2 (sample variance %.2f)", lam[2]), main = "principal component scores")
abline(h = 0, col = cols[2])
abline(v = 0, col = cols[1])
