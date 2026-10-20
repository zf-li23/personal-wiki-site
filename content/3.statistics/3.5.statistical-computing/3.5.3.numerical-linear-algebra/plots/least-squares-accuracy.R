# Relative error of least squares solutions by the normal equations, Householder QR and the SVD.
set.seed(0)
m <- 100; n <- 10
U <- qr.Q(qr(matrix(rnorm(m * n), m)))
V <- qr.Q(qr(matrix(rnorm(n * n), n)))
x_true <- rep(1, n)
eps <- .Machine$double.eps

kappas <- 10^seq(0, 12, length.out = 25)
err <- sapply(kappas, function(k) {
  A <- U %*% diag(10^seq(0, -log10(k), length.out = n)) %*% t(V)
  b <- A %*% x_true                      # consistent system: zero residual
  x_ne <- tryCatch({                     # normal equations via Cholesky
    R <- chol(crossprod(A))
    backsolve(R, forwardsolve(t(R), crossprod(A, b)))
  }, error = function(e) rep(NA, n))
  x_qr <- qr.coef(qr(A), b)              # Householder QR (LINPACK)
  s <- svd(A)
  x_svd <- s$v %*% (crossprod(s$u, b) / s$d)
  sapply(list(x_ne, x_qr, x_svd), function(x) sqrt(sum((x - x_true)^2) / n))
})

matplot(kappas, t(err), log = "xy", type = "b", pch = c(1, 0, 2), lty = 1,
        col = c("red", "blue", "darkgreen"), ylim = c(1e-17, 1e3),
        xlab = "condition number kappa(A)", ylab = "relative error of x",
        main = "Least squares with A = U diag(s) V^T (100 x 10), b = A x")
lines(kappas, eps * kappas, lty = 2, col = "gray")
lines(kappas, eps * kappas^2, lty = 3, col = "gray")
legend("topleft", c("normal equations (Cholesky)", "Householder QR", "SVD", "eps * kappa", "eps * kappa^2"),
       col = c("red", "blue", "darkgreen", "gray", "gray"), lty = c(1, 1, 1, 2, 3))
