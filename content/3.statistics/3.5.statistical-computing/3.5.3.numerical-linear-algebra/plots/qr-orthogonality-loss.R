# Loss of orthogonality ||I - Q^T Q|| of classical Gram-Schmidt, modified Gram-Schmidt and Householder QR.
set.seed(0)
m <- 50; n <- 12
eps <- .Machine$double.eps

cgs <- function(A) {
  Q <- matrix(0, nrow(A), ncol(A))
  for (j in 1:ncol(A)) {
    v <- A[, j]
    if (j > 1) for (i in 1:(j - 1)) v <- v - sum(Q[, i] * A[, j]) * Q[, i]  # original column
    Q[, j] <- v / sqrt(sum(v^2))
  }
  Q
}
mgs <- function(A) {
  V <- A; Q <- matrix(0, nrow(A), ncol(A))
  for (i in 1:ncol(A)) {
    Q[, i] <- V[, i] / sqrt(sum(V[, i]^2))
    if (i < ncol(A)) for (j in (i + 1):ncol(A)) V[, j] <- V[, j] - sum(Q[, i] * V[, j]) * Q[, i]  # updated column
  }
  Q
}
test_matrix <- function(kappa) {
  U <- qr.Q(qr(matrix(rnorm(m * n), m)))
  V <- qr.Q(qr(matrix(rnorm(n * n), n)))
  U %*% diag(10^seq(0, -log10(kappa), length.out = n)) %*% t(V)
}

kappas <- 10^seq(1, 15, length.out = 29)
loss <- sapply(kappas, function(k) {
  A <- test_matrix(k)
  sapply(list(CGS = cgs(A), MGS = mgs(A), Householder = qr.Q(qr(A))),
         function(Q) norm(diag(n) - crossprod(Q), "2"))
})

matplot(kappas, t(loss), log = "xy", type = "b", pch = c(1, 0, 2), lty = 1,
        col = c("red", "blue", "darkgreen"), ylim = c(1e-17, 1e2),
        xlab = "condition number kappa(A)", ylab = "||I - Q^T Q||_2",
        main = "Loss of orthogonality of the computed Q (50 x 12)")
lines(kappas, eps * kappas, lty = 2, col = "gray")
lines(kappas, pmin(eps * kappas^2, 10), lty = 3, col = "gray")
legend("topleft", c(rownames(loss), "eps * kappa", "eps * kappa^2"),
       col = c("red", "blue", "darkgreen", "gray", "gray"), lty = c(1, 1, 1, 2, 3))
