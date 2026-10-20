# Gradient descent on f(x) = (10 x1^2 + x2^2) / 2 with different step size rules, and conjugate gradient.
A <- diag(c(10, 1))
x0 <- c(2, 20)
f <- function(x) 0.5 * drop(t(x) %*% A %*% x)
grad <- function(x) drop(A %*% x)

fixed <- function(alpha, k) {
  x <- x0; path <- matrix(x, 1)
  for (i in 1:k) { x <- x - alpha * grad(x); path <- rbind(path, x) }
  path
}
backtracking <- function(k, beta = 0.8, c = 0.5) {
  x <- x0; path <- matrix(x, 1)
  for (i in 1:k) {
    gx <- grad(x); a <- 1
    while (f(x - a * gx) > f(x) - c * a * sum(gx^2)) a <- beta * a   # Armijo condition
    x <- x - a * gx; path <- rbind(path, x)
  }
  path
}
exact <- function(k) {
  x <- x0; path <- matrix(x, 1)
  for (i in 1:k) {
    r <- -grad(x)
    x <- x + sum(r^2) / drop(t(r) %*% A %*% r) * r
    path <- rbind(path, x)
  }
  path
}
conjugate_gradient <- function() {
  x <- x0; r <- -grad(x); d <- r; path <- matrix(x, 1)
  for (i in 1:2) {
    a <- sum(r^2) / drop(t(d) %*% A %*% d)
    x <- x + a * d
    r_new <- r - a * drop(A %*% d)
    d <- r_new + sum(r_new^2) / sum(r^2) * d
    r <- r_new; path <- rbind(path, x)
  }
  path
}

runs <- list("fixed step 0.35" = fixed(0.35, 6), "fixed step 0.01" = fixed(0.01, 100),
             "fixed step 0.1" = fixed(0.1, 40), "backtracking" = backtracking(40),
             "exact line search" = exact(40), "conjugate gradient" = conjugate_gradient())
g1 <- seq(-20, 20, length.out = 200)
F <- outer(g1, g1, function(a, b) 0.5 * (10 * a^2 + b^2))
op <- par(mfrow = c(2, 3), mar = c(3, 3, 3, 1))
for (nm in names(runs)) {
  p <- runs[[nm]]
  contour(g1, g1, F, levels = c(1, 10, 50, 200, 500, 1000, 2000), drawlabels = FALSE,
          col = "gray", asp = 1, main = sprintf("%s\nf = %.2e", nm, f(p[nrow(p), ])))
  lines(p, type = "o", pch = 19, cex = 0.5, col = "firebrick")
  points(0, 0, pch = 8, col = "steelblue")
}
par(op)
