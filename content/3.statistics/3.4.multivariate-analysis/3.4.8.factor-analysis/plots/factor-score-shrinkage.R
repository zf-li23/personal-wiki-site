# Bartlett (WLS) versus regression factor scores in a simulated two-factor model with known loadings.
set.seed(0)
p <- 6
m <- 2
n <- 400
L <- matrix(c(0.9, 0.0, 0.8, 0.1, 0.7, 0.0, 0.1, 0.6, 0.0, 0.5, 0.0, 0.4), ncol = 2, byrow = TRUE)
psi <- 1 - rowSums(L^2)
Ftrue <- matrix(rnorm(n * m), n, m)
X <- Ftrue %*% t(L) + matrix(rnorm(n * p), n, p) %*% diag(sqrt(psi))

Pinv <- diag(1 / psi)
Delta <- t(L) %*% Pinv %*% L
f_wls <- X %*% (Pinv %*% L %*% solve(Delta))      # Bartlett: (L^T Psi^-1 L)^-1 L^T Psi^-1 x
f_reg <- X %*% solve(L %*% t(L) + diag(psi), L)   # regression: L^T (L L^T + Psi)^-1 x

# With estimated loadings the same two scores come from factanal(X, 2, scores = "Bartlett" / "regression").

par(mfrow = c(1, 2))
for (j in 1:2) {
  mse_w <- mean((f_wls[, j] - Ftrue[, j])^2)
  mse_r <- mean((f_reg[, j] - Ftrue[, j])^2)
  plot(Ftrue[, j], f_wls[, j], pch = 19, cex = 0.4, col = adjustcolor("steelblue", 0.5),
       xlim = c(-3.5, 3.5), ylim = range(f_wls, f_reg),
       xlab = "true factor value", ylab = "estimated factor score",
       main = sprintf("factor %d  (delta = %.2f)", j, Delta[j, j]))
  points(Ftrue[, j], f_reg[, j], pch = 19, cex = 0.4, col = adjustcolor("firebrick", 0.5))
  abline(0, 1, lty = 2, col = "gray30")
  legend("topleft", bty = "n", cex = 0.8,
         legend = c(sprintf("Bartlett (WLS), MSE %.2f", mse_w), sprintf("regression, MSE %.2f", mse_r),
                    "45-degree line"),
         col = c("steelblue", "firebrick", "gray30"), pch = c(19, 19, NA), lty = c(NA, NA, 2))
}
