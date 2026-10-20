# Chi-square plots of squared Mahalanobis distances: normal data versus heavy-tailed multivariate t data.
set.seed(0)
n <- 100
p <- 4
nu <- 4
Sigma <- 0.5 * diag(p) + 0.5
L <- t(chol(Sigma))  # lower triangular, Sigma = L L^T

normal <- matrix(rnorm(n * p), n, p) %*% t(L)
w <- rchisq(n, df = nu) / nu
heavy <- (matrix(rnorm(n * p), n, p) %*% t(L)) / sqrt(w)  # row i divided by sqrt(w_i)

q <- qchisq(((1:n) - 0.5) / n, df = p)

par(mfrow = c(1, 2))
for (case in list(list(x = normal, title = "multivariate normal"),
                  list(x = heavy, title = "multivariate t, 4 d.f."))) {
  d2 <- sort(mahalanobis(case$x, center = colMeans(case$x), cov = cov(case$x)))
  top <- max(q, d2) * 1.05
  plot(q, d2, pch = 19, cex = 0.7, col = "steelblue", xlim = c(0, max(q) * 1.05), ylim = c(0, top),
       xlab = "chi-square(4) quantile q_(j)", ylab = "ordered squared distance d^2_(j)",
       main = case$title)
  abline(0, 1, col = "firebrick", lwd = 1.2)
  grid()
}
