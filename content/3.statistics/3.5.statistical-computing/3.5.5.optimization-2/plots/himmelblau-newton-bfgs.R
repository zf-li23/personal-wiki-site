# Newton's method and BFGS with backtracking on Himmelblau's function.
g <- function(x) (x[1]^2 + x[2] - 11)^2 + (x[1] + x[2]^2 - 7)^2
g.prime <- function(x) {
  matrix(c(4 * x[1]^3 + 4 * x[1] * x[2] - 42 * x[1] + 2 * x[2]^2 - 14,
           2 * x[1]^2 - 26 * x[2] - 22 + 4 * x[1] * x[2] + 4 * x[2]^3), ncol = 1)
}
g.2prime <- function(x) {
  matrix(c(12 * x[1]^2 + 4 * x[2] - 42, 4 * (x[1] + x[2]),
           4 * (x[1] + x[2]), 12 * x[2]^2 + 4 * x[1] - 26), nrow = 2, byrow = TRUE)
}

newton <- function(x, itr = 40) {
  path <- matrix(x, 1)
  for (i in 1:itr) {
    x <- x - solve(g.2prime(x), g.prime(x))
    path <- rbind(path, t(x))
  }
  path
}

bfgs <- function(x, itr = 40) {
  M <- diag(2)
  path <- matrix(x, 1)
  for (i in 1:itr) {
    d <- solve(M, g.prime(x))
    alpha <- 1
    xt <- x - alpha * d
    while (g(xt) > g(x)) {          # backtracking: halve until downhill
      alpha <- alpha / 2
      xt <- x - alpha * d
    }
    z <- xt - x
    y <- g.prime(xt) - g.prime(x)
    if (drop(t(y) %*% z) > 1e-12) {  # curvature condition
      Mz <- M %*% z
      M <- M - Mz %*% t(Mz) / drop(t(z) %*% Mz) + y %*% t(y) / drop(t(y) %*% z)
    }
    x <- xt
    path <- rbind(path, t(x))
  }
  path
}

x1 <- seq(-5, 5, length.out = 200); x2 <- seq(-5, 5, length.out = 200)
z <- outer(x1, x2, Vectorize(function(a, b) g(c(a, b))))
contour(x1, x2, log1p(z), nlevels = 25, col = hcl.colors(25), drawlabels = FALSE,
        xlab = "x", ylab = "y", main = "Himmelblau's function: contours of log(1 + g)")
paths <- list(newton(c(-2, -2)), bfgs(c(-2, -2)), bfgs(c(-4, 0)))
cols <- c("firebrick", "darkorange", "steelblue")
for (k in 1:3) lines(paths[[k]], type = "b", lty = 2, pch = 19, cex = 0.6, col = cols[k])
points(c(3, -2.805118, -3.779310, 3.584428), c(2, 3.131312, -3.283186, -1.848126), pch = 4, lwd = 2)
points(-0.270845, -0.923039, pch = 3, lwd = 2)
legend("topleft", bty = "n", cex = 0.8, col = cols, lty = 2, pch = 19,
       legend = c("Newton from (-2, -2)", "BFGS from (-2, -2)", "BFGS from (-4, 0)"))
sapply(paths, function(p) round(p[nrow(p), ], 6))
