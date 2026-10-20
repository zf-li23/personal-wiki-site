# 95% confidence ellipse for a bivariate mean with individual, Bonferroni and T^2 intervals.
library(MASS)

set.seed(0)
n <- 55
p <- 2
alpha <- 0.05
mu <- c(5.12, 4.72)
Sigma <- matrix(c(0.55, 0.62, 0.62, 0.85), 2, 2)
X <- mvrnorm(n, mu, Sigma)
xbar <- colMeans(X)
S <- cov(X)
se <- sqrt(diag(S) / n)

c_t <- qt(1 - alpha / 2, n - 1)
c_bonf <- qt(1 - alpha / (2 * p), n - 1)
c_T2 <- sqrt(p * (n - 1) / (n - p) * qf(1 - alpha, p, n - p))

# Ellipse n (xbar - mu)^T S^(-1) (xbar - mu) <= c_T2^2.
e <- eigen(S / n, symmetric = TRUE)
tt <- seq(0, 2 * pi, length.out = 400)
ell <- xbar + e$vectors %*% diag(c_T2 * sqrt(e$values)) %*% rbind(cos(tt), sin(tt))

par(mfrow = c(1, 2))
plot(X, pch = 19, cex = 0.6, col = "gray45", asp = 1,
     xlab = "Achievement-like rating", ylab = "Recognition-like rating",
     main = "Data and confidence ellipse")
lines(ell[1, ], ell[2, ], col = "firebrick", lwd = 2)
points(xbar[1], xbar[2], pch = 3, cex = 1.5)

pad <- 1.25 * c_T2 * se
plot(NA, xlim = xbar[1] + c(-1, 1) * pad[1], ylim = xbar[2] + c(-1, 1.5) * pad[2], asp = 1,
     xlab = "mu1", ylab = "mu2", main = "Intervals for the two component means")
lines(ell[1, ], ell[2, ], col = "firebrick", lwd = 2)
mult <- c(c_t, c_bonf, c_T2)
cols <- c("steelblue", "purple", "darkorange")
ltys <- c(2, 4, 3)
for (i in 1:3) {
  rect(xbar[1] - mult[i] * se[1], xbar[2] - mult[i] * se[2],
       xbar[1] + mult[i] * se[1], xbar[2] + mult[i] * se[2],
       border = cols[i], lty = ltys[i], lwd = 1.6)
}
points(xbar[1], xbar[2], pch = 3, cex = 1.5)
legend("topleft", bty = "n", cex = 0.75,
       legend = c("95% confidence ellipse",
                  sprintf("%s (c = %.2f)", c("individual t", "Bonferroni, m = 2", "T^2 intervals"), mult)),
       col = c("firebrick", cols), lty = c(1, ltys), lwd = c(2, 1.6, 1.6, 1.6))
