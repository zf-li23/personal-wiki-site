# Discrete worm-like chain in three dimensions (segment ds = 0.1 lp); end-to-end distances of
# chains of length L = 1, 5 and 50 lp compared with the Gaussian distribution.
set.seed(3)
ds <- 0.1
kappa <- 1 / ds
for (i in 1:50) kappa <- 1 / (1 / tanh(kappa) - exp(-ds))   # <cos theta> = exp(-ds/lp)

sample_cos <- function(n) {
  u <- runif(n)
  1 + log(u + (1 - u) * exp(-2 * kappa)) / kappa
}

cross <- function(a, b) cbind(a[, 2] * b[, 3] - a[, 3] * b[, 2],
                              a[, 3] * b[, 1] - a[, 1] * b[, 3],
                              a[, 1] * b[, 2] - a[, 2] * b[, 1])
unit <- function(a) a / sqrt(rowSums(a^2))

end_vectors <- function(M, nseg) {
  t <- unit(matrix(rnorm(3 * M), M, 3))
  r <- matrix(0, M, 3)
  for (k in 1:nseg) {
    r <- r + ds * t
    c <- sample_cos(M); s <- sqrt(pmax(1 - c^2, 0)); phi <- runif(M, 0, 2 * pi)
    a <- matrix(c(1, 0, 0), M, 3, byrow = TRUE)
    a[abs(t[, 1]) >= 0.9, ] <- matrix(c(0, 1, 0), sum(abs(t[, 1]) >= 0.9), 3, byrow = TRUE)
    e1 <- unit(cross(t, a)); e2 <- cross(t, e1)
    t <- c * t + s * (cos(phi) * e1 + sin(phi) * e2)
  }
  r
}

r2_wlc <- function(L) 2 * L - 2 * (1 - exp(-L))   # in units of lp^2
par(mfrow = c(1, 3))
for (L in c(1, 5, 50)) {
  R <- sqrt(rowSums(end_vectors(4000, round(L / ds))^2))
  x <- R / sqrt(r2_wlc(L))
  hist(x, breaks = 40, freq = FALSE, main = paste("L =", L, "lp"), xlab = "R / sqrt(<R^2>)")
  curve(4 * pi * x^2 * (3 / (2 * pi))^1.5 * exp(-1.5 * x^2), add = TRUE, col = "red")
  cat(L, mean(R^2), r2_wlc(L), "\n")   # simulated and predicted <R^2>
}
