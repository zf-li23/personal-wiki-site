# Jacobi, Gauss-Seidel and SOR iterations for a 3 x 3 symmetric positive definite system.
A <- matrix(c(4, 3, 0,
              3, 4, -1,
              0, -1, 4), 3, byrow = TRUE)
b <- c(24, 30, -24)
x_true <- solve(A, b)   # (3, 4, -5)
n_iter <- 40

iterate <- function(omega = NULL, jacobi = FALSE) {
  x <- rep(1, 3); errs <- numeric(n_iter)
  for (t in 1:n_iter) {
    x_old <- x
    for (i in 1:3) {
      src <- if (jacobi) x_old else x                     # Jacobi uses only old values
      gs <- (b[i] - sum(A[i, -i] * src[-i])) / A[i, i]
      x[i] <- if (is.null(omega)) gs else (1 - omega) * x_old[i] + omega * gs
    }
    errs[t] <- max(abs(x - x_true))
  }
  errs
}

D <- diag(diag(A)); L <- A * lower.tri(A); U <- A * upper.tri(A)
rho <- function(B) max(Mod(eigen(B)$values))
B_sor <- function(w) solve(D + w * L, -(w * U + (w - 1) * D))
rhos <- c(rho(-solve(D, L + U)), rho(-solve(D + L, U)), rho(B_sor(1.25)))

par(mfrow = c(1, 2))
errs <- cbind(iterate(jacobi = TRUE), iterate(), iterate(omega = 1.25))
matplot(1:n_iter, errs, log = "y", type = "b", pch = 16, cex = 0.5, lty = 1,
        col = c("blue", "orange", "red"), ylim = c(1e-16, 10),
        xlab = "iteration t", ylab = "max |x(t) - x*|", main = "Jacobi, Gauss-Seidel and SOR")
legend("topright", sprintf(c("Jacobi, rho = %.3f", "Gauss-Seidel, rho = %.3f", "SOR 1.25, rho = %.3f"), rhos),
       col = c("blue", "orange", "red"), lty = 1)

omegas <- seq(0.05, 1.95, by = 0.01)
r <- sapply(omegas, function(w) rho(B_sor(w)))
plot(omegas, r, type = "l", col = "red", ylim = c(0, 1.05), xlab = "relaxation factor omega",
     ylab = "spectral radius", main = "Spectral radius of the SOR iteration matrix")
lines(omegas, abs(omegas - 1), lty = 2, col = "gray")
abline(v = 2 / (1 + sqrt(1 - rhos[1]^2)), lty = 3, col = "darkgreen")   # optimal omega
