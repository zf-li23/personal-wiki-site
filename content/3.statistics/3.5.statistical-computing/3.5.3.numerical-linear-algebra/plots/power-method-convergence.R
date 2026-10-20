# Convergence of the power method for symmetric matrices with different eigenvalue ratios.
set.seed(0)
n <- 50
Q <- qr.Q(qr(matrix(rnorm(n * n), n)))
q0 <- rnorm(n); q0 <- q0 / sqrt(sum(q0^2))
K <- 80

power_errors <- function(ratio) {
  lam <- c(1, ratio, ratio * runif(n - 2))
  A <- Q %*% diag(lam) %*% t(Q)
  x1 <- Q[, 1]; q <- q0
  out <- matrix(NA, K, 2, dimnames = list(NULL, c("vector", "value")))
  for (k in 1:K) {
    z <- A %*% q
    q <- z / sqrt(sum(z^2))
    out[k, "value"] <- abs(drop(t(q) %*% A %*% q) - 1)   # Rayleigh quotient versus lambda_1 = 1
    out[k, "vector"] <- sqrt(sum((q - sign(sum(q * x1)) * x1)^2))
  }
  out
}

ratios <- c(0.5, 0.8, 0.95); cols <- c("blue", "orange", "red")
res <- lapply(ratios, power_errors)
par(mfrow = c(1, 2))
for (what in c("vector", "value")) {
  plot(NA, xlim = c(1, K), ylim = c(1e-17, 10), log = "y", xlab = "iteration k",
       ylab = if (what == "vector") "||q_k - x_1||" else "|q_k^T A q_k - lambda_1|",
       main = if (what == "vector") "Eigenvector error (dashed: ratio^k)" else "Eigenvalue error (dashed: ratio^(2k))")
  for (i in seq_along(ratios)) {
    e <- pmax(res[[i]][, what], 1e-17)
    lines(1:K, e, col = cols[i], lwd = 2)
    p <- if (what == "vector") 1 else 2
    lines(1:K, e[1] * ratios[i]^(p * (0:(K - 1))), col = cols[i], lty = 2)
  }
  legend("bottomleft", paste("|lambda2/lambda1| =", ratios), col = cols, lwd = 2)
}
