# Contours of a bivariate normal density with their principal axes, and the chi-square coverage of the ellipses.
library(MASS)

set.seed(0)
mu <- c(1.0, 2.0)
Sigma <- matrix(c(2.0, 1.2, 1.2, 1.5), 2, 2)
X <- mvrnorm(400, mu, Sigma)
e <- eigen(Sigma, symmetric = TRUE)
lam <- e$values
P <- e$vectors
tt <- seq(0, 2 * pi, length.out = 400)
circle <- rbind(cos(tt), sin(tt))

par(mfrow = c(1, 2))
plot(X, pch = 19, cex = 0.4, col = "gray60", asp = 1, xlab = "x1", ylab = "x2",
     main = "Contours (x - mu)^T Sigma^(-1) (x - mu) = c^2")
levels <- c(0.5, 0.9, 0.99)
cols <- c("steelblue", "darkorange", "firebrick")
for (i in seq_along(levels)) {
  c0 <- sqrt(qchisq(levels[i], df = 2))
  ell <- mu + P %*% diag(c0 * sqrt(lam)) %*% circle
  lines(ell[1, ], ell[2, ], col = cols[i], lwd = 2)
}
c0 <- sqrt(qchisq(0.9, df = 2))
for (k in 1:2) {
  v <- c0 * sqrt(lam[k]) * P[, k]
  arrows(mu[1], mu[2], mu[1] + v[1], mu[2] + v[2], col = "forestgreen", lwd = 2, length = 0.1)
}
points(mu[1], mu[2], pch = 3, cex = 1.5)
legend("topleft", bty = "n", cex = 0.8, legend = paste0(levels * 100, "% contour"),
       col = cols, lwd = 2)

# Fraction of the sample inside each ellipse versus its nominal probability.
d2 <- mahalanobis(X, center = mu, cov = Sigma)
nominal <- seq(0.01, 0.99, by = 0.01)
frac <- sapply(nominal, function(a) mean(d2 <= qchisq(a, df = 2)))
plot(nominal, frac, type = "l", lwd = 2, col = "steelblue", asp = 1,
     xlab = "nominal probability 1 - alpha", ylab = "fraction of the 400 points",
     main = "Probability content of the ellipses")
abline(0, 1, lty = 2, col = "gray50")
