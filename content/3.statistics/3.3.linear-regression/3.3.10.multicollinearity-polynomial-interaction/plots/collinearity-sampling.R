# Sampling distribution of (b1, b2) for uncorrelated and for highly correlated explanatory variables.
library(MASS)
set.seed(0)
n <- 30
reps <- 2000
sigma <- 1

op <- par(mfrow = c(1, 2), oma = c(0, 0, 2, 0))
for (rho in c(0, 0.95)) {
  x <- mvrnorm(n, mu = c(0, 0), Sigma = matrix(c(1, rho, rho, 1), 2))
  X <- cbind(1, x)
  est <- t(replicate(reps, {
    y <- 2 + x[, 1] + x[, 2] + rnorm(n, 0, sigma)
    lm.fit(X, y)$coefficients[2:3]
  }))
  se <- sigma * sqrt(diag(solve(crossprod(X)))[2:3])
  plot(est, pch = 20, cex = 0.4, col = adjustcolor("steelblue", 0.4),
       xlim = c(-1.5, 3.5), ylim = c(-1.5, 3.5), xlab = "b1", ylab = "b2",
       main = sprintf("corr(X1, X2) = %g:  sd(b1) = %.2f, sd(b2) = %.2f", rho, se[1], se[2]),
       cex.main = 0.9)
  points(1, 1, pch = 3, cex = 2.5, lwd = 2, col = "firebrick")
}
mtext("Same true coefficients (1, 1), same n = 30: collinearity inflates the variances", outer = TRUE)
par(op)
